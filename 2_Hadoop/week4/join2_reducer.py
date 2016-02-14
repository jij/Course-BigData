#!/usr/bin/env python
import sys

last_show = None
running_toal = 0
abc_found = False

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')

    curr_show = key_value[0]
    value_in = key_value[1]
    
    if curr_show != last_show:
        if abc_found == True:
            abc_found = False
            print( '%s\t%s' % (last_show, running_total) )  #print a string, tab, and string            
        running_total = 0
        last_show = curr_show

    if value_in.isdigit():
        running_total += int(value_in)
    
    if value_in == "ABC":
        abc_found = True
