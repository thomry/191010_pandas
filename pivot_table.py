import pandas as pd


weather = pd.read_csv('weather.csv')

weather_melt  = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
weather_tidey = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'element'], # 위치를 그대로 유지할 열 이름 저장
    columns='element',                        # 피벗할 열 이름 지정
    values='temp',                            # 새로운 열 데이터가 될 열 이름 지정
    dropna=False                              # nan값 포함(true는 nan값 무시)
)
print(weather_tidey)
weather_tidey_flat = weather_tidey.reset_index()
print(weather_tidey_flat.head())