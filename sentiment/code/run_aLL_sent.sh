

echo "-----------------------------------------------------------------------------------------------------------------------" >> full_sent.txt
echo Twitter >> full_sent.txt
python bigramFilter.py  ../dataset/data1/finalTrainingInput.txt > bigram.txt 
python trigramFilter.py  ../dataset/data1/finalTrainingInput.txt > trigram.txt 
python unigramFilter.py  ../dataset/data1/finalTrainingInput.txt > unigram.txt 

cp featureExtractor1.py featureExtractor.py
echo SVM >> full_sent.txt
python main.py svm ../dataset/data1/finalTrainingInput.txt ../dataset/data1/finalTestingInput.txt  >> full_sent.txt

echo NB >> full_sent.txt
python main.py nb_bernouli ../dataset/data1/finalTrainingInput.txt ../dataset/data1/finalTestingInput.txt  >> full_sent.txt


echo "-----------------------------------------------------------------------------------------------------------------------" >> loss_polarity_sent.txt
echo Twitter >> loss_polarity_sent.txt
cp featureExtractor2.py featureExtractor.py
echo SVM >> loss_polarity_sent.txt
python main.py svm ../dataset/data1/finalTrainingInput.txt ../dataset/data1/finalTestingInput.txt  >> loss_polarity_sent.txt
 
echo NB >> loss_polarity_sent.txt
python main.py nb_bernouli ../dataset/data1/finalTrainingInput.txt ../dataset/data1/finalTestingInput.txt  >> loss_polarity_sent.txt
