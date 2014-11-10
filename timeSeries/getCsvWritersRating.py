from pandas import read_csv, DataFrame
import csv
import statsmodels.api as sm
from statsmodels.iolib.table import SimpleTable


def getSimpleWriterRating(df):
	nthLastEl = 10
	rs = df.values.tolist()
	if len(rs) > nthLastEl:
		return sum(rs[-nthLastEl:])/len(rs[-nthLastEl:])
	else:
		return sum(rs)/len(rs)	
		
def getWriterRatingWithTimeSeries(df):
	df.set_index(keys=['Year'],drop=False,inplace=True)
	rs = df.Rating.values.tolist()
	df = df.Rating
	#print df
	nthLastEl = 15
	if len(rs) < nthLastEl:
		return getSimpleWriterRating(df)
	arma_mod20 = sm.tsa.ARMA(df, (2,0)).fit()
	return arma_mod20.params.const
	#arma_mod30 = sm.tsa.ARMA(dta, (3,0)).fit()
				
	
df = read_csv('../Data/WriterFULL.csv',',', parse_dates=['Year'])
#dataset = read_csv('WritersFULL.csv',',', index_col=['date_oper'], parse_dates=['date_oper'], dayfirst=True)

writer = csv.writer(open('./results/WritersRating.csv', 'wb'), quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Writer','Rating'])
   
#df = df[df.Writer <= 624181] #524181
#df = df[df.Writer <= 1]

df.sort(columns=['Writer'], inplace=True)
ids = df['Writer'].unique()

for curId in ids:
	data = df.loc[df.Writer == curId]
	data = data[['Year','Rating']]
	rating = getWriterRatingWithTimeSeries(data)
	writer.writerow([curId, round(rating, 2)])



