from arrangement import Arrangement
from mothersday import MothersDay


class Daisies(Arrangement, MothersDay):

    def __init__(self):
        Arrangement.__init__(self, "daisies", 4)
        MothersDay.__init__(self, "white", 0, 0)