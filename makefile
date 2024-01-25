OUT=site
PAGES=$(OUT)/index.html $(OUT)/notes.html
STATIC=$(shell find data -type f) style.css

KATEX_PATH=/data/katex/
KATEX_OUT=$(OUT)$(KATEX_PATH)
KATEX_MEMBERS=katex/katex.min.css katex/katex.min.js katex/fonts

all: $(PAGES) $(STATIC)

$(STATIC): %:
	mkdir -p "$$(dirname "$(OUT)/$@")"
	cp -r "$@" "$(OUT)/$@"

notes.md:
	./update_notes.py

$(KATEX_OUT): %:
	mkdir -p katex_tmp
	curl -L "https://github.com/KaTeX/KaTeX/releases/latest/download/katex.tar.gz" > katex_tmp/katex.tar.gz
	cd katex_tmp && tar -xzf katex.tar.gz $(KATEX_MEMBERS)
	rm -rf "$(KATEX_OUT)" || echo "didn't exits"
	mkdir -p "$(KATEX_OUT)"
	cp -rf -- $(addprefix katex_tmp/,$(KATEX_MEMBERS)) "$(KATEX_OUT)"
	rm -rf katex_tmp

$(KATEX): $(OUT)$(KATEX_PATH)%:
	mkdir -p "$$(dirname "$@")"
	curl -L "https://cdn.jsdelivr.net/npm/katex/dist/$*" > "$@"

$(PAGES): $(OUT)/%.html: %.md $(VENV) $(KATEX_OUT)
	pandoc "$<" \
		--katex=$(KATEX_PATH) \
		--html-q-tags \
		--standalone \
		--css=style.css \
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
