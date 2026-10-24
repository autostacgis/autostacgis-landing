from html.parser import HTMLParser
from pathlib import Path
class Check(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key, "")
            if value and not value.startswith(("https://", "#", "data:")):
                assert (Path("public") / value).is_file(), value
Check().feed(Path("public/index.html").read_text())
assert Path("public/CNAME").read_text().strip() == "autostacgis.com"
print("Landing page assets and domain checked")
