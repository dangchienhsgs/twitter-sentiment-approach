# full
cp featureExtractor1.py featureExtractor.py

datas=( "google" "microsoft" "twitter" "apple")

for data in "${datas[@]}"
do
	echo "-----------------------------------------------------------------------------------------------------------------------" >> full.txt
	bash sandler_ngram.sh ${data}   

	
	echo ${data} svm >> full.txt
	python main.py svm ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> full.txt


	echo ${data} nb >> full.txt
	python main.py nb_bernouli ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> full.txt

done


cp featureExtractor2.py featureExtractor.py

datas=( "google" "microsoft" "twitter" "apple")

for data in "${datas[@]}"
do

	python bigramFilter.py  ../dataset/data2/final_small_train.csv > bigram.txt 
	python trigramFilter.py  ../dataset/data2/final_small_train.csv > trigram.txt 
	python unigramFilter.py  ../dataset/data2/final_small_train.csv > unigram.txt 

	echo sandler >> loss_polarity.txt
	echo "-----------------------------------------------------------------------------------------------------------------------" >> loss_polarity.txt
	bash sandler_ngram.sh ${data}   
	echo ${data} svm >> loss_polarity.txt
	python main.py svm ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> loss_polarity.txt


	echo ${data} nb >> loss_polarity.txt
	python main.py nb_bernouli ../dataset/sandler-data/${data}_training_80_final.csv ../dataset/sandler-data/${data}_testing_80_final.csv  >> loss_polarity.txt

done


