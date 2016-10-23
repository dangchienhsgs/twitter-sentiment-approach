# full_not_ngram
cp featureExtractor1.py featureExtractor.py

datas=( "google" "microsoft" "twitter" "apple")

for data in "${datas[@]}"
do
	echo "-----------------------------------------------------------------------------------------------------------------------" >> full_not_ngram.txt
	bash sandler_ngram.sh ${data}   

	
	echo ${data} svm >> full_not_ngram.txt
	python main-not-ngram.py svm ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> full_not_ngram.txt


	echo ${data} nb >> full_not_ngram.txt
	python main-not-ngram.py nb_bernouli ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> full_not_ngram.txt

done


cp featureExtractor2.py featureExtractor.py

datas=( "google" "microsoft" "twitter" "apple")

for data in "${datas[@]}"
do

	python bigramFilter.py  ../dataset/data2/final_small_train.csv > bigram.txt 
	python trigramFilter.py  ../dataset/data2/final_small_train.csv > trigram.txt 
	python unigramFilter.py  ../dataset/data2/final_small_train.csv > unigram.txt 

	echo sandler >> loss_polarity_not_ngram.txt
	echo "-----------------------------------------------------------------------------------------------------------------------" >> loss_polarity_not_ngram.txt
	bash sandler_ngram.sh ${data}   
	echo ${data} svm >> loss_polarity_not_ngram.txt
	python main-not-ngram.py svm ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> loss_polarity_not_ngram.txt


	echo ${data} nb >> loss_polarity_not_ngram.txt
	python main-not-ngram.py nb_bernouli ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> loss_polarity_not_ngram.txt

done


