PAGES=index.html notes.html
ALL_ENTRIES=$(PAGES) data style.css
OUT=site

all: $(PAGES)

notes.md:
	./update_notes.py

$(PAGES): %.html: %.md $(VENV)
	pandoc "$<" \
		--katex \
		--html-q-tags \
		--standalone \
		--css=style.css \
		--include-before-body=base_before.html \
		--include-after-body=base_after.html \
		--metadata title-prefix="Filip Úradník" \
		--metadata author-meta="Filip Úradník" \
		--output "$@"

copy_out: all
	rm -rf $(OUT)
	mkdir -p $(OUT)
	cp -r $(ALL_ENTRIES) $(OUT)

clean:
	rm -rf $(PAGES)
	rm -rf notes.md

upload: all
	web_upload 

# I want the notes updated always, because they rely on online content.
.PHONY: notes.md all copy_out
