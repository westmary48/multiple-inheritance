from arrangement import Arrangement
from valentinesday import ValentinesDay


class Rose(Arrangement, ValentinesDay):

    def __init__(self):
        Arrangement.__init__(self, "rose", 7)
        ValentinesDay.__init__(self, "red", 0, 0)