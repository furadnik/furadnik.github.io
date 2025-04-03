CITEPROC=--citeproc
CITE_CSL=index_csl.csl
OUT=site
PAGES=index.html notes.html pgp.html $(patsubst %.md,%.html,$(shell find projects -type f -name '*.md'))
STATIC=$(shell find data -type f) favicon.ico
OTHER=style.css
OUT_PAGES=$(addprefix $(OUT)/,$(PAGES))
OUT_STATIC=$(addprefix $(OUT)/,$(STATIC))
OUT_OTHER=$(addprefix $(OUT)/,$(OTHER))

KATEX_PATH=/data/katex
OUT_KATEX=$(OUT)$(KATEX_PATH)
KATEX_MEMBERS=katex/katex.min.css katex/katex.min.js katex/fonts

VENV=.venv
ACTIVATE=$(VENV)/bin/activate
PYTHON=$(VENV)/bin/python
HUE=$(VENV)/bin/hue

all: $(OUT_PAGES) $(OUT_STATIC) $(OUT_OTHER)

$(ACTIVATE): %:
	python -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

$(OUT_STATIC): $(OUT)/%:
	mkdir -p "$$(dirname "$@")"
	cp -r "$*" "$@"

$(OUT_KATEX): %:
	mkdir -p katex_tmp
	rm -rf "$(OUT_KATEX)" || echo "didn't exits"
	mkdir -p "$(OUT_KATEX)"
	cd katex_tmp && \
		curl -L "https://github.com/KaTeX/KaTeX/releases/latest/download/katex.tar.gz" | \
		tar -xzf - $(KATEX_MEMBERS)
	cp -rf -- $(addprefix katex_tmp/,$(KATEX_MEMBERS)) "$(OUT_KATEX)"
	rm -rf katex_tmp

$(OUT_PAGES): $(OUT)/%.html: %.md $(ACTIVATE) $(OUT_KATEX)
	mkdir -p "$$(dirname "$@")"
	cat "$<" | python -m preprocessors | pandoc - \
		$(CITEPROC) \
		--csl=$(CITE_CSL) \
		--katex=$(KATEX_PATH)/ \
		--lua-filter=authorship.lua \
		--html-q-tags \
		--standalone \
		--css=/style.css \
		--include-before-body=base_before.html \
		--include-after-body=base_after.html \
		--metadata title-prefix="Filip Úradník" \
		--metadata author-meta="Filip Úradník" \
		--output "$@"

# linky + accent?
# link hover
# nadpisy
# background
$(OUT)/style.css: $(ACTIVATE) style.css
	cat style.css \
		| sed 's/#00796b/$(shell $(HUE) .68 --min_contrast AAA)/' \
		| sed 's/#48a999/$(shell $(HUE) .78 .81 --min_contrast AAA)/' \
		| sed 's/#00251a/$(shell $(HUE) .18 --min_contrast AAA)/' \
		| sed 's/#fafbfc/$(shell $(HUE) 1 .001)/' \
		> $(OUT)/style.css

clean:
	rm -rf $(OUT) || echo "didn't exist"
	rm -rf notes.md || echo "didn't exist"
	rm -rf katex_tmp || echo "didn't exist"

upload: all
	web_upload 

# I want the notes updated always, because they rely on online content.
.PHONY: all copy_out $(OUT)/projects/index.html $(OUT)/notes.html
