#-*- coding: utf-8 -*-
import json
import requests
import csv
import warnings
import numpy as np
import pandas as pd 
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request
app = Flask(__name__)

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

clf = joblib.load('filename.pkl') 
corpus = joblib.load('vec.dic')
vectorizer = CountVectorizer(min_df=1, tokenizer=lambda x: list(x), ngram_range=(2, 4))
vectorizer.fit_transform(corpus)
transform = vectorizer.transform([u'자동 물걸레 청소기'])
transform1 = vectorizer.transform([u'에센스 커버 팩트 리미티드 패키지'])

print enr_cate_id[clf.predict(transform)[0]]
print enr_cate_id[clf.predict(transform1)[0]]
print enr_cate_id[clf.predict(vectorizer.transform([u'로이드미 블루투스 차량용 충전기']))[0]]

@app.route('/predict', methods=['GET', 'POST'])
def getPredict():
  post_id = request.args.get('data')
  print post_id
  transform = vectorizer.transform([post_id])
  result = enr_cate_id[clf.predict(transform)[0]]
  if result == "02":
    output = "영상,디카"
  elif result == "03":
    output = "디지털"
  elif result == "04":
    output = "컴퓨터"
  elif result == "05":
    output = "생활가전"
  elif result == "06":
    output = "주방가전"
  elif result == "07":
    output = "부품"
  elif result == "08":
    output = "화장품"
  elif result == "09":
    output = "스포츠"
  elif result == "10":
    output = "유아,완구"
  elif result == "12":
    output = "가구"
  elif result == "14":
    output = "패션,잡화"
  elif result == "15":
    output = "식품"
  elif result == "16":
    output = "생활,취미"
  elif result == "18":
    output = "문구,사무"
  elif result == "21":
    output = "자동차용품"
  elif result == "22":
    output = "액세서리"
  elif result == "24":
    output = "계절가전"
  elif result == "86":
    output = "백화점관"
  elif result == "90":
    output = "메인배너"
  elif result == "91":
    output = "여행"
  elif result == "93":
    output = "도서"
  elif result == "95":
    output = "음반,기타"
  return output

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

#print loaded.transform([u'자동 물걸레 청소기'])
