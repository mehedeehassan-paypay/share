#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
from deep_translator import GoogleTranslator
# translated = GoogleTranslator(source='ja', target='en').translate("毛活塾 リアン -RIANT-")  # output -> Weiter so, du bist großartig
import pandas as pd


import pykakasi
kks = pykakasi.kakasi()


# In[2]:


import MeCab
wakati = MeCab.Tagger("-Owakati")


# In[3]:


wakati.parse("ニクトセイセンジャンボイチシキシマヤ")


# In[15]:


# import fugashi

# # This is our sample text.
# # "Fugashi" is a Japanese snack primarily made of gluten.
# text = "ニクトセイセンジャンボイチシキシマヤ"

# # The Tagger object holds state about the dictionary. 
# tagger = fugashi.Tagger()

# words = [word.surface for word in tagger(text)]
# print(*words)
# # => 麩 菓子 は 、 麩 を 主材 料 と し た 日本 の 菓子 。


# In[16]:


# from konoha import WordTokenizer

# sentence = '自然言語処理を勉強しています'

# tokenizer = WordTokenizer('MeCab')
# print(tokenizer.tokenize(sentence))


# In[17]:


merchant_ppsearch = "merchant_names.csv"


# In[18]:


df = pd.read_csv(merchant_ppsearch)


# In[19]:





# In[22]:


import time


# In[ ]:


my_romaji2=[]
def char_is_katakana(c)->bool:

    return u'\u30A0' <= c <= u'\u30FF'

for i,r in df.iterrows():
# #     if i >10:
# #         break
#     if i <= 72532:
#         continue
        
        
    test_string = str(r["title"])
    
    templist_detect_kana = []
    templist = []
    kana = ""
    notkana = ""
    test_string_list = test_string.split(u'\u3000')
    final_test_string_list = []

    for non_unicode_space in test_string_list:


        test_string_list2 = non_unicode_space.split(' ')
#         print(test_string_list2)
        if len(test_string_list2) > 1:
            final_test_string_list.extend(test_string_list2)

        else:
            final_test_string_list.append(test_string_list2[0])




    print(test_string_list)
    for test_string in test_string_list:
        kana = ""
        notkana = ""
        for a in test_string:
#             print(a)
    #         if a == u'\u3000':
    #             print(' here')
    #             templist.append(' ')
    #             templist_detect_kana.append(0)
            if char_is_katakana(a) == True:
                if notkana != "":
                    templist.append(notkana)
                    templist_detect_kana.append(0)
                    notkana = ""

                kana += a
            else:
                notkana += a
                if kana != "":
                    templist.append(kana)
                    templist_detect_kana.append(1)
                    kana = ""

#         print(kana, 'not',notkana)    
        if kana != "":
            templist.append(kana)
            templist_detect_kana.append(1)
        if notkana != "":
            templist.append(notkana)    
            templist_detect_kana.append(0)


#         print("templist",templist)

        romaji = []
        for a in zip(templist_detect_kana,templist):
            if a[0] == 1:
                taglist = wakati.parse(a[1]).split()
                for tag in taglist:
                    if tag!= '':
                    
                        mm = kks.convert(tag)
                        romaji.append([x['hepburn'] for x in mm])
            else:
#                 print('a',a)
                taglist = wakati.parse(a[1]).split()
                for tag in taglist:
                    if tag!= '':
                    
                        mm = kks.convert(tag)
                        romaji.append([x['hepburn'] for x in mm])
    
    romaji_list = [x[1] if isinstance(x, tuple) else x for x in romaji]

    full=""
    for item in romaji:

        if type(item) ==list:
            full += ' '
            full += ' '.join(item)
        else:
            full += ' '
            full += item
    # ''.join(romaji_list)

    print(i , " :--------",r['title'],'   ',full, ' ',romaji)
    full = full.split(' ')
    print(full)
    
    res = []
    for a in full:
        if a != '':
            res.append(a)
    
    my_romaji2.append(' '.join(res))
    
#     if i > 10:
#         break
    if i % 10000 == 0:
        
        time.sleep(1)


# In[29]:


res


# In[30]:


my_romaji2


# In[31]:


len(my_romaji2)


# In[32]:


df2= df.copy()


# In[33]:


df2['kana_romaji'] = my_romaji2


# In[34]:


df2.to_csv("kana_romaji.csv")


# In[35]:


len(df)


# In[ ]:



