#python code/extractDataset.py dataset/predict/Apple.txt  dataset/predict/Apple_processed.txt dataset/predict/Apple_tweets.txt

# ./ark-tweet-nlp/runTagger.sh ./dataset/predict/Apple_tweets.txt > dataset/predict/Apple_tokenised.txt 

#python code/combine.py dataset/predict/Apple_processed.txt dataset/predict/Apple_tokenised.txt dataset/predict/Apple_final.txt



python code/extractDataset.py dataset/predict/Google.txt  dataset/predict/Google_processed.txt dataset/predict/Google_tweets.txt

 ./ark-tweet-nlp/runTagger.sh ./dataset/predict/Google_tweets.txt > dataset/predict/Google_tokenised.txt 

python code/combine.py dataset/predict/Google_processed.txt dataset/predict/Google_tokenised.txt dataset/predict/Google_final.txt


#python code/extractDataset.py dataset/predict/Microsoft.txt  dataset/predict/Microsoft_processed.txt dataset/predict/Microsoft_tweets.txt

# ./ark-tweet-nlp/runTagger.sh ./dataset/predict/Microsoft_tweets.txt > dataset/predict/Microsoft_tokenised.txt 

# python code/combine.py dataset/predict/Microsoft_processed.txt dataset/predict/Microsoft_tokenised.txt dataset/predict/Microsoft_final.txt



# python code/extractDataset.py dataset/predict/Twitter.txt  dataset/predict/Twitter_processed.txt dataset/predict/Twitter_tweets.txt

# ./ark-tweet-nlp/runTagger.sh ./dataset/predict/Twitter_tweets.txt > dataset/predict/Twitter_tokenised.txt 

# python code/combine.py dataset/predict/Twitter_processed.txt dataset/predict/Twitter_tokenised.txt dataset/predict/Twitter_final.txt


