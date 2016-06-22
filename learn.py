#e-*- coding: utf-8 -*-
import fileinput
import sys
import json
import re
import requests
import csv
import warnings
import numpy as np
import pandas as pd
from StringIO import StringIO
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import MySQLdb

mysql_cn= MySQLdb.connect(host='localhost', port=3306,user='root', passwd='1234',db='ml')
mysql_cn.query("set character_set_connection=utf8;")
mysql_cn.query("set character_set_server=utf8;")
mysql_cn.query("set character_set_client=utf8;")
mysql_cn.query("set character_set_results=utf8;")
mysql_cn.query("set character_set_database=utf8;")
df_mysql = pd.read_sql(sql='select item,enr_cate_id from itemcsv', con=mysql_cn)  
#df_mysql2 = pd.read_sql(sql='select item,enr_cate_id from model',con=mysql_cn)
print 'loaded dataframe from MySQL. records:', len(df_mysql)

enr_cate_id = []
enr_cate_id.append('02')
enr_cate_id.append('03')
enr_cate_id.append('04')
enr_cate_id.append('05')
enr_cate_id.append('06')
enr_cate_id.append('07')
enr_cate_id.append('08')
enr_cate_id.append('09')
enr_cate_id.append('10')
enr_cate_id.append('12')
enr_cate_id.append('14')
enr_cate_id.append('15')
enr_cate_id.append('16')
enr_cate_id.append('18')
enr_cate_id.append('21')
enr_cate_id.append('22')
enr_cate_id.append('23')
enr_cate_id.append('24')
enr_cate_id.append('86')
enr_cate_id.append('90')
enr_cate_id.append('91')
enr_cate_id.append('93')
enr_cate_id.append('95')


vectorizer = CountVectorizer(min_df=1, tokenizer=lambda x: list(x), ngram_range=(2, 4))
corpus = [name for name in df_mysql.item]
analyze = vectorizer.build_analyzer()

X = vectorizer.fit_transform(corpus)
Y = map(enr_cate_id.index, df_mysql.enr_cate_id.tolist())

clf = LinearSVC(C=1.0)
clf.fit(X[:-32000], Y[:-32000])

P = clf.predict(X[-200:])
print accuracy_score(Y[-200:], P) * 100
print enr_cate_id[clf.predict(vectorizer.transform([u'차량용 블루투스 충전기']))[0]]
#cursor = mysql_cn.cursor()
#cursor.execute('select item,enr_cate_id from model')
#
#for (item,enr_cate_id_data) in cursor:
#  result = enr_cate_id[clf.predict(vectorizer.transform([item]))[0]]
#  if result != enr_cate_id_data:
#    print "result: " + result  + " expect : "+ enr_cate_id_data  + " item : " + item
#
#cursor.close()
#mysql_cn.close()
#X2 = vectorizer.fit_transform(corpus2)
#Y2 = map(enr_cate_id.index, df_mysql2.NUMBER.tolist())
#clf.fit(X2[:-200], Y2[:-200])

#P2 = clf.predict(X2[-200:])
#print accuracy_score(Y2[-200:], P2) * 100

joblib.dump(clf, 'filename.pkl') 
joblib.dump(corpus, 'vec.dic')


