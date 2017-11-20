TRUNCATE secondary_metabolism

LOAD DATA LOCAL INFILE '/home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/uciel/list_secondary_metabolism_clusters.txt' INTO TABLE secondary_metabolism
  FIELDS TERMINATED BY '\t' ENCLOSED BY ''
  LINES TERMINATED BY '\n'
  (cluster_code);

