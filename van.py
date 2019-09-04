class Van:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        try:
            if flower.temperature < 0 and flower.pestisides < 0:
                self.__flowers.append(flower)
        except AttributeError:
            print(f'organic flowers are too expensive to send here')
