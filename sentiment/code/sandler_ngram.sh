data=$1
python bigramFilter.py ../dataset/sandler-data/${data}_training_80_final.csv > bigram.txt
python trigramFilter.py ../dataset/sandler-data/${data}_training_80_final.csv > trigram.txt
python unigramFilter.py ../dataset/sandler-data/${data}_training_80_final.csv > unigram.txt

