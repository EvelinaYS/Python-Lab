import math

def run():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    distances = {
        'Moscow': {
            'London': round(
                math.sqrt(
                    (sites['Moscow'][0] - sites['London'][0]) ** 2 +
                    (sites['Moscow'][1] - sites['London'][1]) ** 2
                ),
                2
            ),
            'Paris': round(
                math.sqrt(
                    (sites['Moscow'][0] - sites['Paris'][0]) ** 2 +
                    (sites['Moscow'][1] - sites['Paris'][1]) ** 2
                ),
                2
            )
        },

        'London': {
            'Moscow': round(
                math.sqrt(
                    (sites['London'][0] - sites['Moscow'][0]) ** 2 +
                    (sites['London'][1] - sites['Moscow'][1]) ** 2
                ),
                2
            ),
            'Paris': round(
                math.sqrt(
                    (sites['London'][0] - sites['Paris'][0]) ** 2 +
                    (sites['London'][1] - sites['Paris'][1]) ** 2
                ),
                2
            )
        },

        'Paris': {
            'Moscow': round(
                math.sqrt(
                    (sites['Paris'][0] - sites['Moscow'][0]) ** 2 +
                    (sites['Paris'][1] - sites['Moscow'][1]) ** 2
                ),
                2
            ),
            'London': round(
                math.sqrt(
                    (sites['Paris'][0] - sites['London'][0]) ** 2 +
                    (sites['Paris'][1] - sites['London'][1]) ** 2
                ),
                2
            )
        }
    }

    print(distances)

if __name__ == '__main__':
    run()