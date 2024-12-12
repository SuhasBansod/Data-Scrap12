from utilis.getdata import Ghtml
import pandas as pd
Furl='https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=1ba12086-0177-4c14-9c3b-0c95a1c53806'
Fheader={
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.6778.110\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.110\", \"Chromium\";v=\"131.0.6778.110\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=TI173390756385300131334612737533821400069915008245435792175079092975; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzU2MzU1NjMsImlhdCI6MTczMzkwNzU2MywiaXNzIjoia2V2bGFyIiwianRpIjoiODc2ZmQ4NGYtYTNkMy00MzRmLTlhN2QtZmEzNmZlODg2OTBhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzMzOTA3NTYzODUzMDAxMzEzMzQ2MTI3Mzc1MzM4MjE0MDAwNjk5MTUwMDgyNDU0MzU3OTIxNzUwNzkwOTI5NzUiLCJrZXZJZCI6IlZJREY3QTVFMDc3QTlBNDUzRDgyNjU1RDk1NjU3Rjc1MzkiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.7mlDrQtGgzyyPtupXR5oHi1aUgnJOWXhjd-ML3u2zJg; rt=null; K-ACTION=null; ud=2.VogYwlUWqZC3mok_5Tvo2stTYjZu5u2qDbEYJRpeUrEiIztHA4giwD8hAU652G1fRModCoaWXDgXvHElraL3Ew52qTfbEu9Yk5Q1UVtjioP1QzbjLJNScgJ_AD36WgYGVrvvBrKzi6XfaAc4wDq8IA; qH=312f91285e048e09; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20069%7CMCMID%7C91367865737753796394558311805353284181%7CMCAAMLH-1734512365%7C12%7CMCAAMB-1734512365%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1733914766s%7CNONE%7CMCAID%7CNONE; S=d1t16Pz8/Pz8/fkM/OD93KzU/Q9g96q2JnEf9nu5EtbMDZqUKMVwloH5qyHW2l8aRWzGwecxoh9+M/bytfatbiO654Q==; Network-Type=4g; SN=VIDF7A5E077A9A453D82655D95657F7539.TOK102C3FF465104C09ADA1BD9799BD202A.1733988153893.LO; vd=VIDF7A5E077A9A453D82655D95657F7539-1733907565995-2.1733988153.1733988090.154392358"
  }
if __name__ == "__main__":
  FData = Ghtml(WUrl=Furl,SBrowser=False,SStName='LAPTOP')
  Fitem=[]
  for i in FData.css('div[class="tUxRFH"]'):
    PIMg= i.css_first( 'img[loading="eager"][class="DByuf4"]')
    IMg={ 'Src': PIMg.attrs['src'], 'Alt': PIMg.attrs['alt'] }     
    PName= i.css_first('div[class="KzDlHZ"]').text()
    PRating= i.css_first('span > div[class="XQDdHH"]').text()
    PNRatingReview= i.css_first('span[class="Wphh3N"]').text()
    Pdetail = i.css_first('ul[class="G4BRas"]').text()
    Oprice=i.css_first('div[class="Nx9bqj _4b5DiR"]').text()
    Bdiscount=i.css_first('div[class="yRaY8j ZYYwLA"]')
    if Bdiscount:
      Bdis=Bdiscount.text()
    else:
      Bdis= None
    Pdis=i.css_first('div[class="UkUFwK"]')
    if Pdis:
      Perdis=Pdis.text()
    else:
      Perdis=None
    Fdict={
      'Product Name':PName ,
      'BeforeDiscount':Bdis,
      '%Discount':Perdis,
      'Price': Oprice,
      'Product Detail':Pdetail,
      'Rating': PRating,
      'Number of rating and review': PNRatingReview,
      'Image':IMg      
    }
    Fitem.append(Fdict)
  Fitempd= pd.DataFrame(Fitem)
  Fitempd.to_csv('FlipkartData.csv')
  
    