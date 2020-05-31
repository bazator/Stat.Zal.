import random
import nltk


def gender_features(word):
    return {'last_letter': word[-1]}    # ostatnia litera imienia jako cecha okreslajaca plec


def predict_gender(labeled_names, name_to_predict):
    # losowanie wczytanych imion
    random.shuffle(labeled_names)

    # konwersja zbioru imion na zbior cech
    feature_set = [(gender_features(n), gender) for (n, gender) in labeled_names]

    # Podzial listy imion na zbior treningowy i testowy
    half = int(len(feature_set) / 2)
    train_set, test_set = feature_set[half:], feature_set[:half]

    # trenowanie klasyfikatora naive Bayes, danymi z bazy danych
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    # uzycie klasyfikatora, do przewidzenia odpowiedzi
    return classifier.classify(gender_features(name_to_predict))
