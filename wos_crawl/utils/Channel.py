import random
class Channel:
    @staticmethod
    def getRandChannel():
        channels = [
            'https://sci-hub.mksa.top/',
            'https://sci-hub.shop/',
            'https://sci-hub.ren/',
            'https://sci-hub.se/',
            'https://sci-hub.st/',
            'https://sci-hub.ru/'
        ]
        return random.choice(channels)