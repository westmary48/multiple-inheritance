from arrangement import Arrangement
from mothersday import MothersDay


class BabysBreath(Arrangement, MothersDay):

    def __init__(self):
        Arrangement.__init__(self, "baby's breath", 4)
        MothersDay.__init__(self, "white", 0, 0)