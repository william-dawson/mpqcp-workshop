# Working on this site

Bilingual (en/ja) single-page site for the MPQCP workshop. Pelican + Jinja,
deployed to GitHub Pages by `.github/workflows/gh-pages.yml` on push to `main`.

## Core rule

Anything appearing in both languages lives in `data/`, never in the templates
or the Markdown. The English and Japanese pages of the previous site each
carried their own copy of the program, dates and committee, and drifted apart.

## Files

| Path | Holds |
| --- | --- |
| `data/workshop.yml` | Every fact: dates, venue, committee, program, fees, links |
| `data/strings.yml` | UI wording: headings, table labels, `Break`/`休憩`, per-language |
| `content/index-en.md`, `content/index-ja.md` | Only the "Focus" paragraph |
| `theme/templates/` | `base.html`, `page.html`, `partials/` |
| `theme/static/css/style.css` | Design tokens at the top, then styles |
| `pelicanconf.py` | Loads the YAML as `WORKSHOP`/`STRINGS`, sets the URL layout |

Output: `index.html` (en) and `ja/index.html`, links relative.

## Editing `data/workshop.yml`

A value is either a plain string, used for every language:

```yaml
    value: "January 19th - January 20th, 2027."
```

or a per-language mapping (missing languages fall back to `en`):

```yaml
    value:
      en: "January 19th - January 20th, 2027."
      ja: "2027年1月19日 (月)～20日 (火)。"
```

- HTML inside values is rendered as-is.
- `TBA` renders as a highlighted placeholder, localized to `未定`.
- `details` is the definition list; entries render in order. An entry with
  `people` renders as a list of "name (affiliation)".
- `program` is a list of days, each with `slots`. A slot has a `time` plus
  either `kind` (looked up in `strings.yml` → `session_kinds`) or
  `speaker`/`affiliation`/`title`. `keynote: true` marks a keynote row.

## Constraints

- **Japanese text goes on one physical line.** YAML folded blocks (`>-`) and
  Markdown soft line breaks both join lines with a space, which is wrong for
  Japanese.
- **Both Markdown files must keep `Slug: index`.** The shared slug is what makes
  Pelican treat them as translations; without it the language switcher shows
  only the current language.
- `Title:` in the Markdown is Pelican bookkeeping and is not displayed. The
  visible title comes from `name` + `acronym` in `data/workshop.yml`.
- `make serve` does not watch `data/`; restart it after editing YAML.
- `SITE_BASE_URL` in `pelicanconf.py` is only used for `<link rel="canonical">`.
  In-page links stay relative so the site works from any path.

## Yearly rollover

1. `edition`, `year`, `acronym`, `description`, `keywords` in `data/workshop.yml`.
2. Reset every `details` entry, all of `program`, and `registration.url` to `TBA`.
3. Update the ordinal and the year's theme in both `content/index-*.md`
   ("the eighth in a series…" / 「シリーズ第8回目」).
4. `make html`, check both pages, push.

## Adding a language

1. Add the code to `language_names` and add a matching block of UI strings in
   `data/strings.yml`.
2. Add that code wherever `data/workshop.yml` uses a mapping.
3. Create `content/index-<code>.md` with `Lang: <code>` and `Slug: index`.

The language menu and `/<code>/` URL are generated from that.

## Past editions

Only the current edition is published. Multi-year support is deliberately
deferred until a second edition exists. Intended shape when it does: one
`content/<year>/` folder per edition, newest at `/`, older at `/<year>/`, with a
redirect at the current year's own URL so year-specific links stay valid.

## Verifying a change

```sh
make html && python3 -c "import yaml; yaml.safe_load(open('data/workshop.yml'))"
```

Check `output/index.html` and `output/ja/index.html`: the language switcher
should list both languages, and the Japanese page should have no stray spaces
inside its sentences.
