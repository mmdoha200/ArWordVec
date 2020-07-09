# -*- coding: utf-8 -*-

"""
Created on Sun Feb 10 02:42:28 2019
@author: Mohammed M. Fouad
"""

import re
import string

#Clean and Normalize Tweets
def CleanNormalizeTweet(inTweet):

    #RegEx Patterns
    p_mention = r'\@[\_0-9a-zA-Z]+\:?'
    p_url = r'https?://[A-Za-z0-9./]+'
    p_others = r'[a-zA-Z0-9]+'

    text = inTweet
    
    if(not isinstance(text, str)):
        return ''
    
    #Cleaning
    text = re.sub(p_mention, 'تنويهحساب', text)  #check mentions
    text = re.sub(p_url, 'وجودرابط', text)   #check URLs
        
    text = re.sub('['+string.punctuation+']', ' ', text)  # Remove punctuation    
    text = re.sub(p_others, '', text)  #remove english chars and numbers
    
    #Normalization
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    
    text = re.sub(r'(.)\1+', r'\1\1', text) #repeated chars
    
    #Removing linebreaks and extra whitespaces
    text = text.replace('\n', ' ').replace('\r', ' ')  
    text = re.sub('\W', ' ', text)
    text = re.sub(' +', ' ', text)
    
    return text.strip()

