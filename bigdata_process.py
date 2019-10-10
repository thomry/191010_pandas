import os
import urllib.request
import glob
import pandas as pd


with open('raw_data_urls.txt', 'r') as data_urls:
    for line, url in enumerate(data_urls):     # data_urls을 열거
        if line == 5:                          # 5개의 data만 사용할 것이므로 5에서 break
            break
        fn = url.split('/')[-1].strip()        # url을 /따라 strip
        fp = os.path.join('','..', fn)         # 상위 폴더에 경로 새로 생성
        print(url)                             # url 출력
        print(fp)                              # 만든 파일 위치 출력
        urllib.request.urlretrieve(url, fp),   # url의 data를 fp위치에 파일을 직접 저장

# glob함수를 쓰면 특정 패턴의 파일을 읽을 수 있음을 이용해 사용.
nyc_taxi_data = glob.glob('../fhv_*')
print(nyc_taxi_data)
# 각각의 파일을 dataframe으로 저장
taxi1 = pd.read_csv(nyc_taxi_data[0])
taxi2 = pd.read_csv(nyc_taxi_data[1])
taxi3 = pd.read_csv(nyc_taxi_data[2])
taxi4 = pd.read_csv(nyc_taxi_data[3])
taxi5 = pd.read_csv(nyc_taxi_data[4])
# data처리를 위해 dataframe을 연결
taxi = pd.concat([taxi1, taxi2, taxi3, taxi4, taxi5])
print(taxi.head())
