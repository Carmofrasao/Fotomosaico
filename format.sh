#!/bin/bash

ls *.jpg > lista.txt
i=35
while read nome
do
convert –resize “160x120ˆ” $nome image$i.jpg
mogrify -crop "160x120+0+0" image$i.jpg
i=$((i+1))
done < lista.txt
rm lista.txt
