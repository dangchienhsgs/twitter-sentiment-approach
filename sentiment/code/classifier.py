from svmutil import *
import random
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB


def svm_classifier(training_label, testing_label, train_vectors, test_vectors):
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model = svm_train(training_label, train_vectors)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model('.//code//sentimentAnalysisSVM.model', model)
    print "Model Saved. Proceed to test..."

    predictedLabel, predictedAcc, predictedValue = svm_predict(testing_label, test_vectors, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
    return predictedLabel


def svm_classifier_predict(training_label, train_vectors, test_vectors):
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model = svm_train(training_label, train_vectors)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model('.//code//sentimentAnalysisSVM.model', model)
    print "Model Saved. Proceed to test..."

    testing_label = gen_random_label(len(test_vectors))
    predictedLabel, predictedAcc, predictedValue = svm_predict(testing_label, test_vectors, model)

    return predictedLabel


def gen_random_label(size):
    labels = []

    for i in range(size):
        t = random.randint(0, 3)
        labels.append(t)

    return labels

def naivebayes_gaussian_classifier(training_label, testing_label, train_vectors, test_vectors):
    print "Create NaiveBayes Gaussian Model"
    nb_clf = GaussianNB()
    nb_clf.fit(train_vectors, training_label)
    predict_label = nb_clf.predict(test_vectors)

    num_true = 0
    for i in range(0, len(predict_label)):
        if predict_label[i] == testing_label[i]:
            num_true += 1

    print "Accuracy {0}".format(num_true * 1.0 / len(testing_label))
    return predict_label


def naivebayes_bernouli_classifier(training_label, testing_label, train_vectors, test_vectors):
    print "Create NaiveBayes Model"
    nb_clf = BernoulliNB()
    nb_clf.fit(train_vectors, training_label)
    predict_label = nb_clf.predict(test_vectors)

    numTrue = 0
    for i in range(0, len(predict_label)):
        if predict_label[i] == testing_label[i]:
            numTrue += 1

    print "Accuracy {0}".format(numTrue * 1.0 / len(testing_label))
    return predict_label


