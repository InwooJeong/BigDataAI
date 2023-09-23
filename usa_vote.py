# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %matplotlib nbagg
# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# # 데이터 읽기

primary = pd.read_csv("primary_results.csv",sep=",")
counties = pd.read_csv("country_facts.csv",sep=",")
# primary에는 미국내 주 - 카운티별 각 정당, 후보자의 데이터 및 득표율
# counties에는 primary 컬럼 중 fips 코드를 기준, 각 유권자별 데이터

print(primary.shape)
primary.head()

print(counties.shape)
counties.head()

primary.columns

counties.columns

# # 데이터 분석 - 1 : 각 후보별 전체지역 득표수

primary["candidate"].unique()

primary.groupby("candidate")["votes"].sum()

# 투표수(성분)별 정렬 -> 변수에 담기(plot 그리기)
candidate_to_votes = primary.groupby("candidate")["votes"].sum().sort_values()
candidate_to_votes

candidate_to_votes.plot(kind="barh",fontsize=8)

# # 데이터 분석 - 2 : 각 주별 공화당, 민두장 득표비율

primary.head()

# - 각 주별 -> state
# - 공화당, 민주당 -> party
# - -> groupby() 함수의 기준열
# - 득표비율 -> votes
# - -> 추출열

# 데이터 그룹화 기윤열을 state, party 순으로 주어 각 주별 공화당/민주당 득표수 합을 계산
# 계층적 인덱스가 주-당 형태
state_party_votes = primary.groupby(["state","party"])["votes"].sum()
state_party_votes

# 비율을 구하기 위해 각 주 전체 득표수
# 기준열에 state열 넣고 votes를 추출, sum을 사용하면 각 주별 전체 득표수를 구할 수 있음
state_to_votes = primary.groupby("state")["votes"].sum()
state_to_votes

state_vote_pct = state_party_votes/state_to_votes
state_vote_pct

# 비율을 바탕으로 bar plot
# stacked=True - 막대에 합쳐진 비율
state_vote_pct.unstack().plot(kind="barh",stacked=True,fontsize=8)

# # 데이터 분석3 : 사용자 정의 함수 -> 각 county별 당선된 후보 비율

# 데이터 그룹화 결과물에 대해 votes열을 내림차순으로 정렬, 첫번째 성분을 보여줌
func = lambda agg_df: agg_df.sort_values("votes",ascending=False).iloc[0]

primary.head()

# county - primary의 fips 열
winners = primary.groupby("fips").apply(func)
winners

# 각 county별 백인유권자 정보와 합쳐야함 -> counties의 RHI825214
counties["RHI825214"].head()

# - winners와 county 행 갯수가 서로 다르다 -> 병합 key열을 지정, 동일한 기존성분에 대해 m x n 형태로 합쳐야함
# - pd.merge() 필요.
# - fips를 기준, winner에 county 백인 유권자 정보를 병합(한쪽 데이터를 고정시켜서 병합 - how = left(right) 인자)

winners.head(3)

# counties에서 fips열과 RHI825214 열을 병합 -> merge 인자에 열 인덱싱을 리스트 형식
# winners에서는 fips가 그룹화 기준 -> index / counties -> fips가 열
# pd.merge() 인자에 left_index = True, right_on="fips" how="left"
winners_county_merge = pd.merge(winners, counties[["fips","RHI825214"]],left_index=True, right_on="fips", how="left")
winners_county_merge

winners_county_merge.rename(columns={"RHI825214":"white_pct"},inplace=True)
winners_county_merge.head()

# - 각 county별 최다 득표자의 백인 유권자 비율이 표시된 데이터 완성
# - 정당과 당선자를 그룹화 한 뒤, 각 정당별 백인 유권자 비율 평균을 계산

winners_white = winners_county_merge.groupby(["party","candidate"])["white_pct"].mean()
winners_white

winners_white.plot(kind="barh",fontsize="8")

# # Pivot Table
#
# - values = 통계 함수 적용 열
# - index = 그룹화 1번째 기준
# - columns = 그룹화 2번째 기준
# - aggfun = 통계함수

# fil_value -> NaN 처리
total = primary.pivot_table(values="votes",index="state",columns="candidate",aggfunc=np.sum,fill_value=0)
total

primary.pivot_table(values="fraction_votes",index="state_abbreviation",columns="party",aggfunc=np.mean)
