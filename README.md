# MPQCP workshop website

Home of the workshop website, starting with the 2027 edition. Built with
[Pelican](https://getpelican.com/) and published to GitHub Pages at
<https://william-dawson.github.io/mpqcp-workshop/> (English) and
<https://william-dawson.github.io/mpqcp-workshop/ja/> (Japanese).

## The one rule

**Content that appears in both languages lives in `data/`, not in HTML or
Markdown.** Dates, venue, committee, program, fees and links are written once
in `data/workshop.yml`, with per-language text only where the wording genuinely
differs. That is what keeps the two language versions from drifting apart,
which was the main maintenance problem with the previous site.

## Layout

```
data/workshop.yml           everything factual about the workshop
data/strings.yml            UI wording: headings, table labels, "Break"/"休憩"
content/index-en.md         the English "Focus" paragraph, and nothing else
content/index-ja.md         the Japanese "Focus" paragraph
theme/templates/            page structure (base, page, partials/)
theme/static/css/style.css  design tokens at the top, then the styles
pelicanconf.py              loading of the YAML above, and the URL layout
```

## Where to edit what

| I want to change... | Edit |
| --- | --- |
| Dates, venue, fees, deadlines, committee, organizers | `data/workshop.yml` → `details` |
| The program / schedule | `data/workshop.yml` → `program` |
| Registration form link, contact address | `data/workshop.yml` → `registration`, `contact` |
| The "Focus" paragraph | `content/index-en.md`, `content/index-ja.md` |
| Section headings, table headers, "Break"/"Lunch" labels | `data/strings.yml` |
| Colours, fonts, spacing | `theme/static/css/style.css` |
| Page structure | `theme/templates/` |

Values in `data/workshop.yml` may be written either as a plain string, shared by
every language:

```yaml
    value: "January 19th - January 20th, 2027."
```

or as a per-language mapping:

```yaml
    value:
      en: "January 19th - January 20th, 2027."
      ja: "2027年1月19日 (月)～20日 (火)。"
```

HTML is allowed inside these values, so links work as usual.

Keep Japanese text on a single physical line, both in the YAML files and in
`content/index-ja.md`: YAML folded blocks (`>-`) and Markdown soft line breaks both
join lines with a space, which is wrong for Japanese.

Anything left as `TBA` is rendered as a highlighted placeholder (`未定` on the
Japanese page), so unfinished items are visible on the page itself.

## Yearly update checklist

1. `edition`, `year`, `acronym`, `description` and `keywords` in
   `data/workshop.yml`.
2. Every entry under `details` (dates, venue, hotels, fee, deadline, support).
3. `program`: replace the placeholder days and slots with the real schedule.
4. `registration.url` and `contact.email`.
5. The ordinal and the year's theme in the two `content/index-*.md` files
   ("the eighth in a series…" / 「シリーズ第8回目」).
6. Check both pages render, then push to `main`.

The `Title:` line in the content files is internal bookkeeping for Pelican; the
title shown on the page and in the browser tab comes from `name` and `acronym`
in `data/workshop.yml`. The two files share `Slug: index`, which is what marks
them as translations of each other.

## Keeping past editions

This repository is meant to hold the workshop site from now on, but only the
current edition is published; keeping older ones online is deliberately left
until there is a second edition to keep. The intended shape when that happens:
move each year into its own `content/<year>/` folder, publish the newest at `/`
and the rest at `/<year>/`, and leave a redirect at the current year's own URL
so year-specific links stay valid. Nothing in the current setup blocks that —
the templates already read their data from one mapping per edition.

## Adding a language

1. Add the language code to `language_names` and a matching block of UI strings
   in `data/strings.yml`.
2. Add per-language text for that code wherever `data/workshop.yml` uses a
   mapping (anything missing falls back to English).
3. Create `content/index-<code>.md` with `Lang: <code>` and `Slug: index`.

The language menu and the `/<code>/` URL are generated automatically.

## Building locally

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make html     # build into output/
make serve    # preview at http://localhost:8000, rebuilding on edit
make clean
```

`make serve` watches `content/` and `theme/`, but Pelican only re-reads the
YAML files at startup; after editing one, restart it (or run `make html`).

## Deployment

Pushing to `main` triggers `.github/workflows/gh-pages.yml`, which runs
`make publish` and deploys `output/` to GitHub Pages.

All in-page links are relative, so the site works from a project subpath or a
domain root without configuration. `SITE_BASE_URL` in `pelicanconf.py` is used
only for `<link rel="canonical">`.
