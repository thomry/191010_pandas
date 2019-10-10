import pandas as pd

billboard = pd.read_csv('billboard.csv')
billboard_long = pd.melt(billboard, id_vars=["year", "artist", "track", "time", "date.entered"], var_name='week', value_name='rating')
# track이 중복인 data만('Loser') 모아 살펴보기
print(billboard_long[billboard_long.track == 'Loser'].head())
# 중복 데이터인 year, artists, track, time을 모아 dataframe에 따로 저장
billboard_songs = billboard_long[["year", "artist", "track", "time"]]
# 중복 데이터 제거
billboard_songs = billboard_songs.drop_duplicates()
# 제거한 dataframe에 id 추가
billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n=10))
# 노래 정보와 주간 순위 데이터를 합침
billboard_ratings = billboard_long.merge(billboard_songs, on=['year', 'artist', 'track', 'time'])
print(billboard_ratings.head())
