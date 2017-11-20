#!/usr/bin/python
#~ from Bio import SeqIO

import argparse, MySQLdb, os, re, random, sys

cmdargs = str(sys.argv)
parser = argparse.ArgumentParser(description="Insert data to DB\n",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
parser.add_argument('-f', '--file',
                        dest = 'input_file',
                        action = 'store',
                        default = None,
                        help = "cluster_families.txt file to insert into DB")
                        
      
options = parser.parse_args()
    



if options.input_file:
	cluster_families_file = options.input_file.rstrip()

print 'Usage: python parser_cluster_families.py  -f /home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/uciel/cluster_families.txt\n'

print 'The file format of cluster_families has to be like this:\n\n'
	
print '# CF_000428'
print 'HYDPI   HYDPI_0001_00270;HYDPI_0001_00271;HYDPI_0001_00272;HYDPI_0001_00273;HYDPI_0001_00274;HYDPI_0001_00275;HYDPI_0001_00276;HYDPI_0001_00277;HYDPI_0001_00278;HYDPI_0001_00279;HYDPI_0001_00280;HYDPI_0001_00281;HYDPI_0001_00282;HYDPI_0001_00283;HYDPI_0001_00284;HYDPI_0001_00285;HYDPI_0001_00286;HYDPI_0001_00287'
print 'LACAM   LACAM_0032_05728;LACAM_0032_05729;LACAM_0032_05730;LACAM_0032_05731;LACAM_0032_05732;LACAM_0032_05733;LACAM_0032_05734;LACAM_0032_05735;LACAM_0032_05736;LACAM_0032_05737;LACAM_0032_05738;LACAM_0032_05739;LACAM_0032_05740;LACAM_0032_05741;LACAM_0032_05742'
print 'PLICR   PLICR_0001_00513;PLICR_0001_00514;PLICR_0001_00515;PLICR_0001_00516;PLICR_0001_00517;PLICR_0001_00518;PLICR_0001_00519;PLICR_0001_00520;PLICR_0001_00521;PLICR_0001_00522;PLICR_0001_00523;PLICR_0001_00524;PLICR_0001_00525;PLICR_0001_00526;PLICR_0001_00527;PLICR_0001_00528;PLICR_0001_00529;PLICR_0001_00530;PLICR_0001_00531'
print 'SUILU   SUILU_0025_03021;SUILU_0025_03022;SUILU_0025_03023;SUILU_0025_03024;SUILU_0025_03025;SUILU_0025_03026;SUILU_0025_03027;SUILU_0025_03028;SUILU_0025_03029;SUILU_0025_03030;SUILU_0025_03031;SUILU_0025_03032;SUILU_0025_03033;SUILU_0025_03034;SUILU_0025_03035;SUILU_0025_03036;SUILU_0025_03037;SUILU_0025_03038;SUILU_0025_03039;SUILU_0025_03040'
print '\n\n'

# Open database connection
db = MySQLdb.connect("localhost","cgenomics","abc.123","clusters" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

import csv
with open(cluster_families_file, 'rb') as f:
    for row in csv.reader(f,delimiter='\t',):
		if (row[0].startswith('#')):
			cluster_name = row[0].replace('#','').strip()
		else:
			specie = row[0].strip()
			proteins = row[1].split(';')
			for protein in proteins:
				print cluster_name,specie,protein
				cursor.execute('''INSERT into cluster_families (cluster_code, specie_code,protein_code)
                  values (%s, %s, %s)''',
                  (cluster_name, specie, protein.strip()))

    #~ # Commit your changes in the database
#~ db.commit()
