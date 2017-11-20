TRUNCATE taxonomy

LOAD DATA LOCAL INFILE '/home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/uciel/taxonomy_table.txt' INTO TABLE taxonomy
  FIELDS TERMINATED BY '\t' ENCLOSED BY ''
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (file_name,specie_code,specie_name,kingdom,phylum,subphylum,class,order_tax,family,genus);

