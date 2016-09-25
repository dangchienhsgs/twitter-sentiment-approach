data=$1

python code/extractDataset.py ./dataset/sandler-data/${data}_training_80.csv ./dataset/sandler-data/${data}_training_80_processed.csv ./dataset/sandler-data/${data}_training_80_tweets.csv


./ark-tweet-nlp/runTagger.sh ./dataset/sandler-data/${data}_training_80_tweets.csv  > dataset/sandler-data/${data}_training_80_tokenised.csv

python code/combine.py  dataset/sandler-data/${data}_training_80_processed.csv dataset/sandler-data/${data}_training_80_tokenised.csv  dataset/sandler-data/${data}_training_80_final.csv


python code/extractDataset.py ./dataset/sandler-data/${data}_testing_80.csv ./dataset/sandler-data/${data}_testing_80_processed.csv ./dataset/sandler-data/${data}_testing_80_tweets.csv


./ark-tweet-nlp/runTagger.sh ./dataset/sandler-data/${data}_testing_80_tweets.csv  > dataset/sandler-data/${data}_testing_80_tokenised.csv

python code/combine.py  dataset/sandler-data/${data}_testing_80_processed.csv dataset/sandler-data/${data}_testing_80_tokenised.csv  dataset/sandler-data/${data}_testing_80_final.csv

