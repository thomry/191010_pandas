import pandas as pd
from numpy import NAN, NaN, nan
import numpy as np

gapminder = pd.read_csv('gapminder.tsv', sep='\t')
# gapminder dataframe을 year별로 그룹화한후 lifeExp의 평균을 구하기.
life_exap = gapminder.groupby(['year'])['lifeExp'].mean()
# 그중 2000~2009년의 데이터 추출
print(life_exap.loc[range(2000,2010), ])
# lifeExp가 없던 년도때문에 nan값 발생으로 오류가 생김
# 이때 발생한 문제를 해결하려면 불린추출을 사용하여 뽑으면 됨.
y2000 = life_exap[life_exap.index > 2000]

ebola = pd.read_csv('country_timeseries.csv')
# 누락값 개수 구하기
num_rows    = ebola.shape[0]
# shape[0]에 전체 행데이터 개수 저장 되어 있으므로 .count()사용해 빼면 누락값의 갯수가 나옴
num_missing = num_rows - ebola.count()
print(num_missing)

# count메서드 의외 누락값 개수 구해보기
print(np.count_nonzero(ebola.isnull()))
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))
# .value_counts는 지정 열의 빈도를 구하는 함수
print(ebola.Cases_Guinea.value_counts(dropna=False).head())

# fillna에 0을 대입시 누락값이 0으로 대체됨. 메모리를 효율적으로 사용할때 사용.
print(ebola.fillna(0).iloc[0:10, 0:5])
# method를 ffill로 지정하면 누락값 나타나기전의 값으로 누락값이 변경됨.
print(ebola.fillna(method='ffill').iloc[0:10, 0:5])
# bfill은 누락값이 나타난 후의 첫번째 값으로 변경됨.(ffill)과 반대. 그러나 이것도 뒷 값은 처리못함.
print(ebola.fillna(method='bfill').iloc[0:10, 0:5])
# interpolate는 누락값 양쪽 값을 이용해 중간값을 구해 누락값 처리함.
print(ebola.interpolate().iloc[0:10, 0:5])

# 누락값 삭제
ebola_dropna = ebola.dropna()
print(ebola_dropna)

# 누락값 포함된 데이터 계산
ebola['Cases_multiple'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[ :, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n=10))
# sum 메서드를 사용하면 누락값 포함해 계산함. 이때 누락값 무시해서 구하려면 skipna 인자 사용
print(ebola.Cases_Guinea.sum(skipna = True))    # 누락값 무시
print(ebola.Cases_Guinea.sum(skipna = False))   # 누락값 포함

