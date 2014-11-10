from pandas import read_csv, DataFrame
import csv
import statsmodels.api as sm
from statsmodels.iolib.table import SimpleTable


def getSimpleActorRating(df):
	nthLastEl = 10
	rs = df.values.tolist()
	if len(rs) > nthLastEl:
		return sum(rs[-nthLastEl:])/len(rs[-nthLastEl:])
	else:
		return sum(rs)/len(rs)		
		
		
def getActorRatingWithTimeSeries(df):
	df.set_index(keys=['Year'],drop=False,inplace=True)
	rs = df.Rating.values.tolist()
	df = df.Rating
	nthLastEl = 15
	if len(rs) < nthLastEl:
		return getSimpleActorRating(df)
	arma_mod20 = sm.tsa.ARMA(df, (2,0)).fit()
	return arma_mod20.params.const
	#arma_mod30 = sm.tsa.ARMA(dta, (3,0)).fit()
				
	
df = read_csv('../Data/ActorsFULL.csv',',', parse_dates=['Year'])
#dataset = read_csv('ActorsFULL.csv',',', index_col=['date_oper'], parse_dates=['date_oper'], dayfirst=True)

writer = csv.writer(open('./results/ActorsRating2.csv', 'wb'), quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Actor','Rating'])
   
#df = df[df.Actor >= 2737070] #524181
#df = df[df.Actor <= 1]

df.sort(columns=['Actor'], inplace=True)
ids = df['Actor'].unique()

for curId in ids:
	data = df.loc[df.Actor == curId]
	data = data[['Year','Rating']]
	rating = getActorRatingWithTimeSeries(data)
	writer.writerow([curId, round(rating, 2)])



