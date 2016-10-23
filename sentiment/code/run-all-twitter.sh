

echo "-----------------------------------------------------------------------------------------------------------------------" >> full.txt
echo Twitter >> full.txt
python bigramFilter.py  ../dataset/data2/final_small_train.csv > bigram.txt 
python trigramFilter.py  ../dataset/data2/final_small_train.csv > trigram.txt 
python unigramFilter.py  ../dataset/data2/final_small_train.csv > unigram.txt 

cp featureExtractor1.py featureExtractor.py
echo SVM >> full.txt
python main.py svm ../dataset/data2/final_small_train.csv ../dataset/data2/final_small_test.csv >> full.txt

echo NB >> full.txt
python main.py nb_bernouli ../dataset/data2/final_small_train.csv ../dataset/data2/final_small_test.csv >> full.txt


echo "-----------------------------------------------------------------------------------------------------------------------" >> loss_polarity.txt
echo Twitter >> loss_polarity.txt
cp featureExtractor2.py featureExtractor.py
echo SVM >> loss_polarity.txt
python main.py svm ../dataset/data2/final_small_train.csv ../dataset/data2/final_small_test.csv >> loss_polarity.txt
 
echo NB >> loss_polarity.txt
python main.py nb_bernouli ../dataset/data2/final_small_train.csv ../dataset/data2/final_small_test.csv >> loss_polarity.txt
