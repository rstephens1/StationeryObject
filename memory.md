# Project Memory

## Stack
- Project: StationeryObject
- Domain: pending custom domain (Cloudflare Pages default during setup)
- DNS: Cloudflare
- Hosting: Cloudflare Pages
- Source control: GitHub
- Generator: Hugo
- Content roots: `/content/posts` for posts, `/content/about.md`, `/content/search.md`, `/content/archive.md`, `/content/submit.md`
- Assets: `/static/`

## Product Scope
- Home page shows a chronological post feed.
- RSS feed is available for posts.
- Navigation includes Home, Submissions, Archive, and About.
- Search is client-side against a Hugo-generated JSON index.
- Archive page lists posts grouped by month.

## Layout and behavior
- Base layout: `layouts/_default/baseof.html`
- Home feed: `layouts/index.html`
- Content page renderer: `layouts/_default/single.html`
- Search page renderer: `layouts/search/single.html`
- Archive page renderer: `layouts/archive/single.html`

## Cloudflare Pages
- Project name: `stationeryobject` (display name: StationeryObject)
- GitHub account for this repo: `rstephens1`
- Cloudflare account for this repo: `rstephens1@gmail.com`
- Suggested production branch: `main`
- Build command: `hugo --gc --minify`
- Build output directory: `public`
- CI deploy workflow: `.github/workflows/deploy-pages.yml`

## Update policy
- Keep this file updated as stack, deploy settings, and structure change.
- Update when layouts/content sections are added, removed, or renamed.
