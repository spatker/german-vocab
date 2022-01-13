#!/bin/bash

for i in {1..338}; do
    wget https://app.memrise.com/course/47049/5000-words-top-87-sorted-by-frequency/$i -O $i.html
done
