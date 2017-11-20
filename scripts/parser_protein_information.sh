#! /bin/sh

if [ $# -eq 0 ]; then
  echo "Please include path to the directory like: home/uchorostecki/users/tg/mmarcet/HGT3_proteomes/genome_walking4/conversion_files"
  exit 1
fi

files_directory=$1

for file in $(ls $files_directory ); do
	file_with_path=$files_directory$file
	echo "Running... ($file)\n"
	python parser_protein_information.py -f $file_with_path
done;
echo "Done!"



