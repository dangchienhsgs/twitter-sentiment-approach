mkdir result

mkdir result/data1/

mkdir result/data1/svm
python main.py svm ../../data/final_small_train.csv ../../data/final_small_test.csv > result_svm_data1.txt 
cp taskB.gs taskB.pred result_svm_data1.txt result/data1/svm

#mkdir result/data1/gauss
#python main.py nb_gauss ../../data/final_small_train.csv ../../data/final_small_test.csv > result_gauss_data1.txt
#cp taskB.gs taskB.pred result_gauss_data1.txt result/data1/gauss

#mkdir result/data1/bernouli
#python main.py nb_bernouli ../../data/final_small_train.csv ../../data/final_small_test.csv > result_bernouli_data1.txt
#cp taskB.gs taskB.pred result_bernouli_data1.txt result/data1/bernouli


mkdir result/data2/

mkdir result/data2/svm
python main.py svm ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput.txt > result_svm_data2.txt 
cp taskB.gs taskB.pred result_svm_data2.txt result/data2/svm

#mkdir result/data2/gauss
#python main.py nb_gauss ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput.txt > result_gauss_data2.txt
#cp taskB.gs taskB.pred result_gauss_data2.txt result/data2/gauss

#mkdir result/data2/bernouli
#python main.py nb_bernouli ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput.txt > result_bernouli_data2.txt
#cp taskB.gs taskB.pred result_bernouli_data2.txt result/data2/bernouli


