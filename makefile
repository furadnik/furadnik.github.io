OUT=site
PAGES=index.html notes.html
STATIC=$(shell find data -type f) style.css favicon.ico
OUT_PAGES=$(addprefix $(OUT)/,$(PAGES))
OUT_STATIC=$(addprefix $(OUT)/,$(STATIC))

KATEX_PATH=/data/katex/
OUT_KATEX=$(OUT)$(KATEX_PATH)
KATEX_MEMBERS=katex/katex.min.css katex/katex.min.js katex/fonts

all: $(OUT_PAGES) $(OUT_STATIC)

$(OUT_STATIC): $(OUT)/%:
	mkdir -p "$$(dirname "$@")"
	cp -r "$*" "$@"

notes.md:
	./update_notes.py

$(OUT_KATEX): %:
	mkdir -p katex_tmp
	curl -L "https://github.com/KaTeX/KaTeX/releases/latest/download/katex.tar.gz" > katex_tmp/katex.tar.gz
	cd katex_tmp && tar -xzf katex.tar.gz $(KATEX_MEMBERS)
	rm -rf "$(OUT_KATEX)" || echo "didn't exits"
	mkdir -p "$(OUT_KATEX)"
	cp -rf -- $(addprefix katex_tmp/,$(KATEX_MEMBERS)) "$(OUT_KATEX)"
	rm -rf katex_tmp

$(KATEX): $(OUT)$(KATEX_PATH)%:
	mkdir -p "$$(dirname "$@")"
	curl -L "https://cdn.jsdelivr.net/npm/katex/dist/$*" > "$@"

$(OUT_PAGES): $(OUT)/%.html: %.md $(VENV) $(OUT_KATEX)
	pandoc "$<" \
		--katex=$(KATEX_PATH) \
		--html-q-tags \
		--standalone \
		--css=/style.css \
		--include-before-body=base_before.html \
		--include-after-body=base_after.html \
		--metadata title-prefix="Filip Úradník" \
		--metadata author-meta="Filip Úradník" \
		--output "$@"

clean:
	rm -rf $(OUT) || echo "didn't exist"
	rm -rf notes.md || echo "didn't exist"
	rm -rf katex_tmp || echo "didn't exist"

upload: all
	web_upload 

# I want the notes updated always, because they rely on online content.
.PHONY: notes.md all copy_out
