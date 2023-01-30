#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd 
import spacy
import pytesseract
from glob import glob
import re 
import string 
import cv2
import warnings 
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from spacy import displacy

def proper(text):
    spaces = string.whitespace
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    a = str.maketrans('','',spaces)
    b = str.maketrans('','',punctuation)
    text = str(text)
    text = text.lower()
    removewhitespaces = text.translate(a)
    removepun = removewhitespaces.translate(b)

    
    return str(removepun)
#class
class kamal():
    def __init__(self):
        self.id = 0
        self.text = ''
        
    def e(self,text):
        if self.text == text:
            return self.id
        else:
            self.id +=1
            self.text = text
            return self.id
        
ob = kamal()

#re
def clean(text,label):
    if label == 'PHONE':
        text = text.lower()
        text = re.sub(r'\D','',text)
    elif label == 'EMAIL':
        text = text.lower()
        a_s_c = '@_.\-'
        text = re.sub(r'[^A-Za-z0-9{} ]'.format(a_s_c),'',text)
    elif label == 'WEB':
        text = text.lower()
        a_s_c = ':/.%#\-'
        text = re.sub(r'[^A-Za-z0-9{} ]'.format(a_s_c),'',text)
    elif label in ("NAME","DES"):
        text = text.lower()
       # a_s_c = '@_.-'
        text = re.sub(r'[^a-z]','',text)
        text = text.title()
    elif label == "ORG":
        text = text.lower()
       # a_s_c = '@_.-'
        text = re.sub(r'[^a-z0-9]','',text)
        text = text.title()
    return text


model1 = spacy.load("./1_BusinessCardNER/output/model-best")

def getPredictions(image):
    pydata = pytesseract.image_to_data(image)
    #print(pydata)
    data = list(map(lambda a:a.split("\t") , pydata.split('\n')))
    #data
    data_1 = pd.DataFrame(data[1:] , columns=data[0])
    data_1.dropna(inplace=True)
    data_1['text'] = data_1['text'].apply(proper)
    df = data_1.query('text != "" ')
    content = " ".join([i for i in df['text']])
    print(content)
    sol = model1(content)
    #displacy.render(sol , style='ent')
    soljson = sol.to_json()

    soljson.keys()

    sol_text = soljson['text']

    soljson['ents']


    soljson['tokens']

    df_tokens = pd.DataFrame(soljson['tokens'])

    df_tokens['token'] = df_tokens[['start','end']].apply(
        lambda x:sol_text[x[0]:x[1]] , axis = 1)

    k = pd.DataFrame(soljson['ents'])[['start','label']]
    df_tokens = pd.merge(df_tokens,k,how='left',on='start')



    df_tokens.fillna('O',inplace=True)
    df['end'] = df['text'].apply(lambda x: len(x)+1).cumsum() - 1 
    df['start'] = df[['text','end']].apply(lambda x: x[1] - len(x[0]),axis=1)

    df_c = pd.merge(df,df_tokens[['start','token','label']],how='inner',on='start')

    d = df_c.query("label != 'O' ")
   # img = image.copy()


    # In[169]:


    d['label'] = d['label'].apply(lambda x: x[2:])

    d['group'] = d['label'].apply(ob.e)


    # In[172]:


    d[['left','top','width','height']] = d[['left','top','width','height']].astype(int)
    d['right'] = d['left'] + d['width']
    d['bottom'] = d['top'] + d['height']


    # In[173]:


    qq = ['left','top','right','bottom','label','token','group']
    x = d[qq].groupby(by='group')


    # In[174]:


    img_tagging = x.agg({

        'left':min,
        'right':max,
        'top':min,
        'bottom':max,
        'label':np.unique,
        'token':lambda k: " ".join(k)

    })

    #image = cv2.imread("./data/156.jpeg")

    img_r = image.copy()
    for l,r,t,b,label,token in img_tagging.values:
        cv2.rectangle(img_r,(l,t),(r,b),(0,255,0),2)

        cv2.putText(img_r,label,(l,t),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)


    #cv2.imshow('img',img_r)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    clean("korla##$kuntasaikamal@&*gmail.,com","EMAIL")

    info_array = df_c.query('label != "O"')[['token','label']].values

    entities = dict(NAME=[],ORG=[],DES=[],PHONE=[],EMAIL=[],WEB=[])
    previous = ''
    for tok, lab in info_array:
        bio_tag = lab[:1]
        label_tag = lab[2:]

        text = clean(tok,label_tag)



        if previous != label_tag:
            entities[label_tag].append(text)

        else:
            if bio_tag == 'B':
                entities[label_tag].append(text)

            else:
                if label_tag in ('NAME','ORG','DES'):
                    entities[label_tag][-1] = entities[label_tag][-1]+" "+text

                else:
                    entities[label_tag][-1] = entities[label_tag][-1]+text

        previous = label_tag

    #print(entities)
    return img_r , entities





