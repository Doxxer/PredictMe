__author__ = 'antonio'


def calc_movie_rating(film_data, ):
    """
    Calculate movie rating

    :param film_data: dict("Year", "Actor", "Director", "Writer")
    :return: film rating
    """
    y = film_data["Year"]
    a = film_data["Actor"]
    d = film_data["Director"]
    w = film_data["Writer"]
    rating = -6.019606736 + 0.002546918 * y + 5.676063315 * a - 5.636471665 * d \
             + 0.606485770 * w - 0.002621657 * y * a + 0.002766083 * y * d \
             + 0.101135496 * a * d - 0.068869599 * d * w
    return rating


if __name__ == '__main__':
    # Test data for film Interstellar from test sample
    data_test = {
        "Year": 2014,
        "Actor": 8.108857337964904,
        "Director": 8.28333338101705,
        "Writer": 8.583333452542622
    }
    print calc_movie_rating(data_test)