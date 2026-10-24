# AutostacGIS landing page

Static site for **https://autostacgis.com**. Run `make dev` to preview on port 4174. `make check` checks local asset links. Push `main` to deploy using the included GitHub Pages action. There is no build framework to maintain.

## Domain setup

Enable GitHub Pages with GitHub Actions, set the custom domain to `autostacgis.com`, then enable HTTPS once the certificate is ready. `public/CNAME` is included in the deployment artifact.

At your DNS provider, point the apex domain at GitHub Pages using the addresses in [GitHub's current domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Optionally set `www` as a CNAME to `autostacgis.github.io`. DNS and domain ownership stay with the domain registrar.

The page links to repository release pages for current downloads, rather than hardcoding a platform binary or release version. The app icon comes from `autostacgis-web/public/icon.svg`.
