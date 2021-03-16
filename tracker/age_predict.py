import pandas as pd 
from datetime import datetime

def toDate(List) :
  try : 
    for i in range(len(List)) : 
      List[i] = datetime.strptime(List[i] , "%Y-%m-%d")
  except : 
    print(List[i])
  return List


link = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
covid = pd.read_csv(link, usecols=['location','date','median_age','aged_65_older','aged_70_older','cardiovasc_death_rate','diabetes_prevalence','female_smokers','male_smokers',] , )
                    
covid.date = toDate(covid.date)
age_predict = covid.groupby("location").apply(lambda x : x[x.date == covid.date.max()] ).fillna(0)
age_predict.sort_values("male_smokers", ascending=False).reset_index(drop=True)[: 60]


