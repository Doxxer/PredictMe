__author__ = 'antonio'

from math import log

# format film_data - dict("Year", "Budget", "Actor", "Director", "Writer", "Popularity")
# def predictRating(film_data, ):
#     y = film_data["Year"]
#     b = film_data["Budget"]
#     a = film_data["Actor"]
#     d = film_data["Director"]
#     w = film_data["Writer"]
#     p = 1
#     if film_data["Popularity"]:
#         p = -1
#     rating = -41.018525739 + 0.023349906 * y + 12.050324479 * a - 6.538574953 * d + 0.569198951 * w - 0.494886545 * log(b
#         ) - 0.013572359 * p - 0.006469572 * y * a + 0.003447241 * y * d + 0.097790321 * log(b
#         ) * a - 0.019537897 * log(b) * d + 0.074386146 * a * d - 0.065110729 * d * w
#
#     return rating

def predictRating(film_data):
    y = film_data["Year"]
    a = film_data["Actor"]
    d = film_data["Director"]
    w = film_data["Writer"]
    rating = -6.019606736 + 0.002546918*y + 5.676063315*a - 5.636471665*d + 0.606485770*w - 0.002621657*y*a + 0.002766083*y*d + 0.101135496*a*d - 0.068869599*d*w
    return rating



if __name__ == '__main__':
    #Test data for film Interstellar from test sample
    data_test = {
        "Year": 2014,
        "Actor": 8.108857337964904,
        "Director": 8.28333338101705,
        "Writer": 8.583333452542622
    }
    print predictRating(data_test)