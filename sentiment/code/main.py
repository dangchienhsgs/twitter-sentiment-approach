"""This code extracts the features and returns the features"""
from featureExtractor import *
from probablityModel import *
from classifier import *
from prepare import *
from svmutil import *

if __name__ == '__main__':

    """check arguments"""
    if len(sys.argv) != 4:
        print "Usage :: python main.py [method] ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput.txt"
        print "Method: svm, nb_gauss, nb_bernouli"
        sys.exit(0)

    acronymDict, stopWords, emoticonsDict = loadDictionary()

    priorScore = dict(map(lambda (k, v): (
        frozenset(reduce(lambda x, y: x + y, [[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),
        int(v)), [line.split('\t') for line in open("AFINN-111.txt")]))

    """create Unigram Model"""
    print "Creating Unigram Model......."
    uniModel = []
    f = open('./unigram.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            uniModel.append(line)
    uniModel.sort()

    print "Unigram Model Created"

    print "Creating Bigram Model......."
    biModel = []
    f = open('./bigram.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            biModel.append(line)
    biModel.sort()
    print "Bigram Model Created"

    print "Creating Trigram Model......."
    triModel = []
    f = open('./trigram.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            triModel.append(line)
    triModel.sort()
    print "Trigram Model Created"

    """ polarity dictionary combines prior score """
    polarityDictionary = probTraining(priorScore)

    """write the polarityDictionary"""
    """
    data=[]
    for key in polarityDictionary:
        data.append(key+'\t'+str(polarityDictionary[key][positive])+'\t'+str(polarityDictionary[key][negative])+'\t'+str(polarityDictionary[key][neutral]))
    f=open('polarityDictionary.txt','w')
    f.write('\n'.join(data))
    f.close()
    """

    """Create a feature vector of training set """
    print "Creating Feature Vectors....."

    encode = {'positive': 1.0, 'negative': 2.0, 'neutral': 3.0}
    trainingLabel = []
    f = open(sys.argv[2], 'r')
    featureVectorsTrain = []
    for i in f:
        if i:
            i = i.split('\t')
            tweet = i[1].split()
            token = i[2].split()
            label = i[3].strip()
            if tweet:
                vector = []
                trainingLabel.append(encode[label])
                vector, polarityDictionary = findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict,
                                                          acronymDict)
                uniVector = [0] * len(uniModel)
                for i in tweet:
                    word = i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind = uniModel.index(word)
                            uniVector[ind] = 1
                vector = vector + uniVector

                biVector = [0] * len(biModel)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                for i in range(len(tweet) - 1):
                    phrase = tweet[i] + ' ' + tweet[i + 1]
                    if word in biModel:
                        ind = biModel.index(phrase)
                        biVector[ind] = 1
                vector = vector + biVector

                triVector = [0] * len(triModel)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                for i in range(len(tweet) - 2):
                    phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + tweet[i + 2]
                    if word in triModel:
                        ind = triModel.index(phrase)
                        triVector[ind] = 1
                vector = vector + triVector

                # print vector
                featureVectorsTrain.append(vector)
    f.close()
    print "Feature Vectors Train Created....."

    """for each new tweet create a feature vector and feed it to above model to get label"""

    testingLabel = []
    data = []
    data1 = []
    f = open(sys.argv[3], 'r')
    featureVectorsTest = []
    for i in f:
        if i:
            i = i.split('\t')
            tweet = i[1].split()
            token = i[2].split()
            label = i[3].strip()
            if tweet:
                data.append(label)
                testingLabel.append(encode[label])
                vector = []
                vector, polarityDictionary = findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict,
                                                          acronymDict)

                uniVector = [0] * len(uniModel)
                for i in tweet:
                    word = i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind = uniModel.index(word)
                            uniVector[ind] = 1
                vector = vector + uniVector

                biVector = [0] * len(biModel)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                for i in range(len(tweet) - 1):
                    phrase = tweet[i] + ' ' + tweet[i + 1]
                    if word in biModel:
                        ind = biModel.index(phrase)
                        biVector[ind] = 1
                vector = vector + biVector

                triVector = [0] * len(triModel)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]

                for i in range(len(tweet) - 2):
                    phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + tweet[i + 2]
                    if word in triModel:
                        ind = triModel.index(phrase)
                        triVector[ind] = 1
                vector = vector + triVector
                featureVectorsTest.append(vector)
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."

    method = sys.argv[1]

    predictedLabel = []
    if method == "svm":
        predictedLabel = svm_classifier(trainingLabel, testingLabel, featureVectorsTrain, featureVectorsTest)
    elif method == "nb_gauss":
        predictedLabel = naivebayes_gaussian_classifier(trainingLabel, testingLabel, featureVectorsTrain,
                                                        featureVectorsTest)
    elif method == "nb_bernouli":
        predictedLabel = naivebayes_bernouli_classifier(trainingLabel, testingLabel, featureVectorsTrain,
                                                        featureVectorsTest)
    elif method == "svm_predict":
        predictedLabel = svm_classifier_predict(trainingLabel, featureVectorsTrain, featureVectorsTest)
        print predictedLabel

    else:
        print "Method {0} is not support".format(method)

    for i in range(len(predictedLabel)):
        givenLabel = predictedLabel[i]
        label = encode.keys()[encode.values().index(givenLabel)]
        data1.append(label)

    f = open('./taskB.gs', 'w')
    f.write('\n'.join(data))
    f.close()

    f = open('./taskB.pred', 'w')
    f.write('\n'.join(data1))
    f.close()
