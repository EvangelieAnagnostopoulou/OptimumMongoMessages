#!/usr/bin/env python
import csv
import json
import bson
import sys, getopt, pprint
from pymongo import MongoClient
from collections import defaultdict
#CSV to JSON Conversion
mongo_client=MongoClient() 
mongo_conn = MongoClient('mongodb://83.212.113.64:27017')
mongo_db = mongo_conn.Optimum
Message= mongo_db["Message"]
#messages.drop()
header= ["persuasive_strategy", "context", "number_of_times_sent", "message_text", "target", "number_of_successes", "className"]
with open('/root/message.csv', 'rb') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=';,')
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        for each in reader:
            row={}
	    for field in header:
		row[field]=each[field]
            print row
	   # for k, v in row.iteritems():
           # convert2unicode(v)
            mongo_db.Message.insert(row)

