#!/usr/bin/python
#~ from Bio import SeqIO

import argparse, MySQLdb, os, re, random, sys
import csv

cmdargs = str(sys.argv)
parser = argparse.ArgumentParser(description="Insert data to DB\n",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
parser.add_argument('-f', '--file',
                        dest = 'input_file',
                        action = 'store',
                        default = None,
                        help = "proteins file to insert into DB")
                        
      
options = parser.parse_args()
    



if options.input_file:
	protein_file = options.input_file.rstrip()

#~ print 'Usage: python parser_protein_information.py  -f /home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/uciel/protein_family_examples/YEAST.txt\n'

#~ print 'The file format has to be like this:\n\n'

#~ print 'YEAST_0001_00001        5246'
#~ print 'YEAST_0001_00002        8851'
#~ print 'YEAST_0001_00003        823'
#~ print 'YEAST_0001_00004        5066'
#~ print 'YEAST_0001_00005        1694'
#~ print 'YEAST_0001_00006        11838'
	

# Open database connection
db = MySQLdb.connect("localhost","cgenomics","abc.123","clusters" )
# prepare a cursor object using cursor() method
cursor = db.cursor()


with open(protein_file, 'rb') as f:
	reader = csv.reader(f)
	row1 = next(reader)
  
	m = re.search('(.*?)_(.*)', row1[0])
	table_name =  'protein_' + m.group(1)
	create_table = 'CREATE TABLE IF NOT EXISTS `' +  table_name  + '` (	 `protein_code` varchar(50) NOT NULL, 	 `family` int(11) NOT NULL 	 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
	cursor.execute(create_table)

	alter_table = 'ALTER TABLE `' +  table_name  + '` ADD UNIQUE KEY `protein_code` (`protein_code`)'
	cursor.execute(alter_table)

	 
	
with open(protein_file, 'rb') as f:
    for row in csv.reader(f,delimiter='\t',):
		protein_id = row[0].strip()
		family = row[1].strip()
		cursor.execute('''INSERT into '''+table_name+''' (protein_code, family)
			values (%s, %s)''',
			(protein_id, family, ))

    #~ # Commit your changes in the database
db.commit()
