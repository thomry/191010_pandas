import pandas as pd

pew       = pd.read_csv('pew.csv')
billboard = pd.read_csv('billboard.csv')
ebola     = pd.read_csv('country_timeseries.csv')

# 6개 열만 출력
print(pew.iloc[:, 0:6])
# religion 열을 고정하여 피벗
pew_long = pd.melt(pew, id_vars='religion')
print(pew_long.head())
# variable과 value 열 이름 바꾸기
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')

# 피벗해보기
billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week', value_name='rating')
ebola_long     = pd.melt(ebola, id_vars=['Date', 'Day'])

# split으로 열이름 분리
variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])

# 0번째 index에 담긴 문자열은 cases와 deaths 상태 의미.
# 1번째 index에 담긴 문자열은 나라이름을 의미
status_values  = variable_split.str.get(0)
country_values = variable_split.str.get(1)
# 분리한 문자열을 dataframe에 추가하기
ebola_long['status']  = status_values
ebola_long['country'] = country_values
print(ebola_long.head())