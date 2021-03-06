import unittest
from HW1.smu.grid_search_week2 import GridSearch as GridSearch_W2
from HW1.smu.grid_search_week3 import GridSearch as GridSearch_W3
from HW1.smu.grid_search_week4 import GridSearch as GridSearch_W4
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model.perceptron import Perceptron
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

import numpy as np

class GridSearchCase(unittest.TestCase):
    def test_grid_search_week2(self):
        classifier = LogisticRegression
        X = np.array([[1, 2], [3, 4], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5]])
        y = np.array([0, 1, 0, 0, 1, 1, 1, 0])
        data = (X,y)
        grid_search = GridSearch_W2()
        result = grid_search.run(classifier, data , {'C':2, 'class_weight': 'balanced'})
        print(result)

    def test_grid_search_week2_multi_param(self):
        classifier = LogisticRegression
        X = np.array([[1, 2], [3, 4], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5]])
        y = np.array([0, 1, 0, 0, 1, 1, 1, 0])
        data = (X, y)
        grid_search = GridSearch_W2()
        param1 = {'C': 2, 'class_weight': 'balanced'}
        param2 = {'C': 5, 'class_weight': None}
        result = grid_search.run_multi_params(classifier, data, [param1, param2])
        #print(result)

    def test_grid_search_week3(self):
        classifier = LogisticRegression
        classifier = SVC
        X = np.array([[1, 2], [3, 4], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5]])
        y = np.array([0, 1, 0, 0, 1, 1, 1, 0])
        iris_data = load_iris()

        X= iris_data.data
        y= iris_data.target
        data = (X,y)
        grid_search = GridSearch_W3()
        result = grid_search.run(classifier, data , {'C':2, 'class_weight': 'balanced'})
        acc_scores = [result[res]['accuracy'] for res in result]
        clf_names = [res for res in result]
        plt.bar(clf_names, acc_scores)
        plt.show()
        print(result)


    def test_grid_search_week4(self):
        classifier = LogisticRegression
        classifier = SVC

        X = np.array([[1, 2], [3, 4], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5]])
        y = np.array([0, 1, 0, 0, 1, 1, 1, 0])
        iris_data = load_iris()

        X = iris_data.data
        y = iris_data.target
        data = (X,y)
        grid_search = GridSearch_W4()
        result = grid_search.run(classifier, data , {'C':2, 'class_weight': 'balanced'})
        acc_scores = [result[res]['accuracy'] for res in result]
        clf_names = [res for res in result]
        plt.bar(clf_names, acc_scores)
        plt.xlabel('classifier')
        plt.ylabel('accuracy score')
        plt.show()
        print(result)


if __name__ == '__main__':
    unittest.main()
