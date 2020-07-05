#https://blog.cgfm.jp/garyu/archives/3396
#https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_name=text_to_speech&p_name=api_7#tag01

import requests

API_KEY = '7a7674596949456866644e3431366c4876374c6f32664b67467974384d6b504b4764576669364550676538'
url     = 'https://api.apigw.smt.docomo.ne.jp/crayon/v1/textToSpeech' + '?APIKEY=' + API_KEY

headers = {
         'Content-Type': 'application/json',
          }

data = {
         'Command': 'AP_Synth',
         'SpeakerID': '1',
         'StyleID': '1',
         'TextData' : 'お兄ちゃん大好き'
         }

r_post = requests.post(url, headers=headers, json=data)
print(r_post)
print(r_post.headers)
