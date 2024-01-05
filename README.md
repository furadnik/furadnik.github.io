# web
Code for my personal website.

## Compile

If you for some reason wanted to compile this thing, all you need is a recent version of Python and the Pandoc package.

Beware that a part of the web is the page with my notes, which dynamically downloads the git repo to a folder.
This might not work for you, depending on your git configuration.

You can build the pages from `.md` manually, or just run `make all` and let it build the whole web.
For more info, take a look at the `makefile`.
