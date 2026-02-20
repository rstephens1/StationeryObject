# Hugo Image Spec For StationeryObject

This is the canonical image spec for posts with 3-6 high-resolution close-ups.

## Storage Model

- Keep original high-resolution masters outside the site repo (archive drive/cloud backup).
- Commit only web-ready derivatives to the repo.
- Preferred post structure: page bundles.

Example:

```text
content/posts/hotel-baronette-stationery/index.md
content/posts/hotel-baronette-stationery/01-main.jpg
content/posts/hotel-baronette-stationery/02-grain.jpg
content/posts/hotel-baronette-stationery/03-watermark.jpg
```

Fallback location for shared assets:

```text
static/img/<slug>/01-main.jpg
```

## Front Matter Image Schema

Use an `images` array in post front matter. Order matters.

- `images[0]`: lead image for Home
- `images[0]`: archive thumbnail (Archive also uses the first image)

Example (TOML):

```toml
[[images]]
src = "01-main.jpg"
alt = "Letterhead on cream rag paper"
caption = "Main sheet, 1930s"

[[images]]
src = "02-grain.jpg"
alt = "Macro detail showing paper grain"
caption = "Fiber grain at macro distance"

[[images]]
src = "03-watermark.jpg"
alt = "Watermark under angled light"
caption = "Watermark detail"
```

You can also use absolute paths (`/img/...`) if image files are in `static/img`.

### Ingest Rule For Inline Copy

When source drafts are submitted with copy lines between image embeds, default mapping is:

- Copy immediately following an image belongs to the image above it.
- Store that copy in that image entry as `note`.
- If there is ambiguity, ask before publishing.

## Export Targets

For each image, export up to three sizes:

- `-xl`: long edge 2400-3200 px, high quality (detail view)
- `-md`: long edge 1400-1800 px (primary web use)
- `-sm`: long edge 800-1000 px (small cards/backup)

Suggested format:

- JPEG for photos/texture shots.
- Keep files below Cloudflare Pages per-file limits.

## Layout Behavior

- Home: reverse-chronological feed, newest post featured in center.
- Side columns: remaining posts alternate left/right.
- Archive: reverse-chronological rows with image on right.
- Archive image source: `images[0]`.

## Authoring Checklist Per Post

1. Crop and export derivatives.
2. Place images in page bundle folder (preferred).
3. Add `images` entries in front matter in display order.
4. Map inline draft copy to image `note` fields using the default ingest rule.
5. Set `summary` in front matter for feed/archive text.
6. Run `hugo` and visually verify Home, Archive, and the post page.
