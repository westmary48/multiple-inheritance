class OrganicVan:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        try:
            if flower.temperature > 0 and flower.pestisides > 0:
                self.__flowers.append(flower)
        except AttributeError:
            print(f'You cannot send any pestiside ridden flowers here')
