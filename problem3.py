#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:26:35 2017

@author: denya
"""
from sklearn import cross_validation, svm, grid_search
from sklearn.cross_validation import train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def prediction_models(filename="input3.csv", output="output3.csv"):
    
    try:
        data = pd.read_csv(filename, delimiter =',')
    except:
         raise NameError ("unusual filename") 
    
    plt.figure (1)
    plt.subplot(211)
    
    plt.plot(data[data.dtypes.index [1]],"r--")
    plt.subplot(212)
    
    plt.plot(data[data.dtypes.index [3]])
    plt.show()
    data.sort(columns=data.dtypes.index [-1],inplace=True)
    print(data)
    X = np.array(data.drop(data.dtypes.index [-1],1))
    y = np.array(data[data.dtypes.index [-1]])
    
    
    kfold = 5
    kf = KFold(len(y),n_folds=kfold)
    
    X_train,X_test,y_train,y_test = [],[],[],[]
    test,train = [],[]
    for i, j in kf:
        
        j_tr,j_te = train_test_split(j,test_size=0.4)
        j_tr = list(j_tr)
        j_te = list(j_te)
        
        train = train + j_tr
        test += j_te
        
    for i in train:
        X_train.append(X[i])
        y_train.append(y[i])
        
    for i in test:
        X_test.append(X[i])
        y_test.append(y[i])

    
    out=[]


    parameters={'kernel':["linear"], 'C':[0.1, 0.5, 1, 5, 10, 50, 100]} 
   
    model_svc_lin = svm.SVC()
    clf = grid_search.GridSearchCV(model_svc_lin, parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train=cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["linear SVC",ac_best_train, ac_test]
    out.append(a)
    

    
    parameters = {'kernel':'poly','C':[0.1, 1, 3],'degree':[4, 5, 6]}

    model_svc_non_lin = svm.SVC()
    clf = grid_search.GridSearchCV(model_svc_non_lin,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["poly SVC",ac_best_train, ac_test]
    out.append(a)
   
    

    parameters = {"C":[0.1, 0.5, 1, 5, 10, 50, 100],  "gamma":[0.1, 0.5, 1, 3, 6, 10]}

    model_svc_rbf = svm.SVC()
    clf = grid_search.GridSearchCV(model_svc_rbf,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    
    out.append(["rbf SVC",ac_best_train, ac_test])
    
    
    
    parameters = {'C':[0.1, 0.5, 1, 5, 10, 50, 100], 'tol':[0.01]}

    log_reg = LogisticRegression()
    clf = grid_search.GridSearchCV(log_reg,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["log_reg ",ac_best_train, ac_test]
    out.append(a)
    
    
    
    a = [i for i in range(1,51)]
    leaf = [i for i in range(5,61,5)]    
    parameters = {'n_neighbors': a, 'leaf_size':leaf}

    knn = KNeighborsClassifier()
    clf = grid_search.GridSearchCV(knn,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["knn ",ac_best_train, ac_test]
    out.append(a)
    
    
    
    dept=[i for i in range(1,51)]
    samp_spl=[i for i in range(1,11)]    
    parameters = {'max_depth': dept, 'min_samples_split':samp_spl}

    DT = DecisionTreeClassifier()
    clf = grid_search.GridSearchCV(DT,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["des_tree",ac_best_train, ac_test]
    out.append(a)
    
    
    
    dept = [i for i in range(1,51)]
    samp_spl = [i for i in range(1,11)]    
    parameters = {'max_depth': dept, 'min_samples_split':samp_spl}

    RF = RandomForestClassifier()
    clf = grid_search.GridSearchCV(RF,parameters)
    clf.fit(X_train, y_train)
    
    ac_best_train = cross_validation.cross_val_score(clf,X_train, y_train, cv=kfold).mean()
    ac_test = clf.score(X_test, y_test)
    
    a = ["rand_forest ",ac_best_train, ac_test]
    out.append(a)
    
    out = pd.DataFrame(out)
    out.to_csv(output ,encoding="utf-8",mode='w')
    
if __name__ == "__main__":--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    import sys
    try:
        a = sys.argv[1]
        b = sys.argv[2]
    
        prediction_models(a,b)
    except:
        prediction_models()
