__author__ = 'antonio'

import rpy
import pandas

#format data - (ActorRating<2.5, ActorRating<5, ActorRating<7.5, ActorRating<10, DirectorRating, WriterRating)
def predictRating(film_data):
    data = pandas.read_csv("DataRegression.csv")
    rpy.set_default_mode(rpy.NO_CONVERSION)
    linear_model = rpy.r.lm(rpy.r("Rating ~ ."), data = rpy.r.data_frame(Rating=data['Rating'],
                                                                     Director=data['Director'],
                                                                     Writer=data['Writer'],
                                                                     Actor1=data['Actor.Group1'],
                                                                     Actor2=data['Actor.Group2'],
                                                                     Actor3=data['Actor.Group3'],
                                                                     Actor4=data['Actor.Group4']))

    predicted = rpy.r.predict(linear_model, rpy.r.data_frame(Actor1=film_data[0],
                                                         Actor2=film_data[1],
                                                         Actor3=film_data[2],
                                                         Actor4=film_data[3],
                                                         Director=film_data[4],
                                                         Writer=film_data[5]))





    rpy.set_default_mode(rpy.BASIC_CONVERSION)
    # print linear_model.as_py()['coefficients']
    # print predicted.as_py()
    # print data['Rating'][0]
    return predicted.as_py()['1']



if __name__ == '__main__' :
    data = pandas.read_csv("DataRegression.csv")
    data_test = (data['Actor.Group1'][0], data['Actor.Group2'][0], data['Actor.Group3'][0], data['Actor.Group4'][0], data['Director'][0], data['Writer'][0])
    print predictRating(data_test)
