TRUNCATE all_trees

LOAD DATA LOCAL INFILE '/home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/uciel/all_trees.txt' INTO TABLE all_trees
  FIELDS TERMINATED BY '\t' ENCLOSED BY ''
  LINES TERMINATED BY '\n'
  (family,tree);

