__author__ = 'antonio'

import rpy
import pandas

#format data - (ActorRating<2.5, ActorRating<5, ActorRating<7.5, ActorRating<10, DirectorRating, WriterRating)
#coefficients from R
def predictRating(film_data):
    predicted_value = 0.0882967271 - 0.0120020289 * film_data[0] - 0.0106449352 * film_data[1] +  0.0003242131 * film_data[2] +
        0.0117709794 * film_data[3] + 0.3486407973 * film_data[4] + 0.6362357986 * film_data[5]
    return predicted_value
    
if __name__ == '__main__' :
    data = pandas.read_csv("DataRegression.csv")
    data_test = (data['Actor.Group1'][0], data['Actor.Group2'][0], data['Actor.Group3'][0], data['Actor.Group4'][0], data['Director'][0], data['Writer'][0])
    print predictRating(data_test)
