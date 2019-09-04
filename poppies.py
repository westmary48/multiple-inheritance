from arrangement import Arrangement
from mothersday import MothersDay


class Poppies(Arrangement, MothersDay):

    def __init__(self):
        Arrangement.__init__(self, "poppies", 4)
        MothersDay.__init__(self, "red", 0, 0)