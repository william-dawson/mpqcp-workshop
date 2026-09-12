# Build helpers for the MPQCP workshop site.
#
#   make html     build into output/ for local preview
#   make serve    build, then serve at http://localhost:8000 and rebuild on edit
#   make publish  build into output/ with deployment settings (used by CI)
#   make clean    remove output/

PELICAN ?= pelican
PELICANOPTS ?=

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py
PORT ?= 8000

.PHONY: help html clean serve publish

help:
	@sed -n '2,8p' Makefile

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

serve:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" -p $(PORT) $(PELICANOPTS)

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
