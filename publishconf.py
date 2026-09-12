"""Settings used when building the site for deployment (`make publish`).

Kept deliberately thin: the development and production builds should differ as
little as possible so that what is previewed locally is what gets published.
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

DELETE_OUTPUT_DIRECTORY = True

# Still relative: GitHub Pages serves the site from a subdirectory for project
# repositories and from the root for user/organization ones, and relative
# links work in both cases.
RELATIVE_URLS = True
