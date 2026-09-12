"""Pelican configuration for the MPQCP workshop site.

The site is a single bilingual page. Everything that must stay identical
between the languages (dates, venue, committee, program, links) lives in
data/workshop.yml; the wording of the UI lives in data/strings.yml. Both are
loaded here and exposed to the templates as WORKSHOP and STRINGS. The only
per-language prose is the body of content/index-<lang>.md.

The repository is the long-term home for the workshop, so when a later edition
is added the plan is to move each year into its own folder; nothing here
assumes there will only ever be one. See AGENTS.md.
"""

from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'


def load_yaml(name):
    with open(DATA_DIR / name, encoding='utf-8') as handle:
        return yaml.safe_load(handle)


# Uppercase settings are available in every template.
WORKSHOP = load_yaml('workshop.yml')
STRINGS = load_yaml('strings.yml')

AUTHOR = 'Computational Molecular Science Research Team'
SITENAME = '{} ({})'.format(WORKSHOP['name']['en'], WORKSHOP['acronym'])
SITEURL = ''

# Absolute URL of the deployed site, used for <link rel="canonical">. In-page
# links stay relative, so this is the only place the host name appears.
SITE_BASE_URL = 'https://william-dawson.github.io/mpqcp-workshop'

PATH = 'content'
TIMEZONE = 'Japan'
DEFAULT_LANG = 'en'

# Links are relative to each page, so the same output works on GitHub Pages
# (user or project site), on a local preview, and on any other host.
RELATIVE_URLS = True

# --- Content -----------------------------------------------------------------
# The site is made of translated pages, one per language; there are no articles.
PAGE_PATHS = ['']
ARTICLE_PATHS = []
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {'extra/nojekyll': {'path': '.nojekyll'}}

# The default language at /, every other language at /<lang>/.
PAGE_URL = ''
PAGE_SAVE_AS = 'index.html'
PAGE_LANG_URL = '{lang}/'
PAGE_LANG_SAVE_AS = '{lang}/index.html'

# Nothing else should be generated: no index, archives, feeds or taxonomies.
DIRECT_TEMPLATES = []
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

# --- Theme -------------------------------------------------------------------
THEME = 'theme'
THEME_STATIC_DIR = 'static'
PLUGINS = []

# `do` lets base.html build the language-switcher list.
JINJA_ENVIRONMENT = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'extensions': ['jinja2.ext.do'],
}
