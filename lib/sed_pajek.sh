#!/bin/bash

for net in $(ls *.net)
	do
	sed -e 's#\<[0-9].[0-9] [0-9].[0-9] ellipse\>##g' -e 's#\(^.*\)\s\([A-Za-z0-9\.\_\-]*\)\s$#\1 "\2"#g' -i $net
	done

