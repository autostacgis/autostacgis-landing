# AutostacGIS landing page

Static site for **https://autostacgis.com**. Run `make dev` to preview on port 4174. `make check` checks local asset links. Push `main` to deploy using the included GitHub Pages action. There is no build framework to maintain.

## Domain setup

Enable GitHub Pages with GitHub Actions, set the custom domain to `autostacgis.com`, then enable HTTPS once the certificate is ready. The GitHub Pages custom domain is configured as `autostacgis.com`. `public/CNAME` records that choice in source; custom Actions deployments use the repository setting.

At your DNS provider, point the apex domain at GitHub Pages using the addresses in [GitHub's current domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Optionally set `www` as a CNAME to `autostacgis.github.io`. DNS and domain ownership stay with the domain registrar.

The page links to repository release pages for current downloads, rather than hardcoding a platform binary or release version. The app icon comes from `autostacgis-web/public/icon.svg`.

## Remaining Cloudflare DNS step

The site and Pages deployment are configured. At verification, Cloudflare nameservers answered for `autostacgis.com` but returned no A record. Import [dns/autostacgis.com.zone](dns/autostacgis.com.zone) in Cloudflare **DNS → Records → Import and Export → Import**, or add those four apex A records and the `www` CNAME manually. Keep the website records **DNS only** while GitHub issues its certificate. Once DNS resolves, enable **Enforce HTTPS** in the repository's Pages settings. The records come from [GitHub's domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
