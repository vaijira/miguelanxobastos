#!/bin/sh

## Get the path to the book
BOOK_PATH=$1

## Get the current path
CURRENT_PATH=$(pwd)

## Get to the right path
cd ${BOOK_PATH}

## Compile the book
Rscript -e 'bookdown::clean_book()'
Rscript -e 'bookdown::render_book("index.Rmd", output_format = "bookdown::bs4_book")'

## Get back to the previous path
cd ${CURRENT_PATH}
