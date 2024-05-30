#!/usr/bin/bash

rm -r site
make -Bj6
ssh reu "rm -r public_html/*"
rsync -r site/* reu:public_html
