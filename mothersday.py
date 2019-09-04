class MothersDay:

      def __init__(self, color, temperature, pesticides):
          self.color = color
          self.temperature = temperature
          self.pesticides = pesticides

      def transportation(self, zero):
          self.temperature -= zero
          print(f'You require {self.temperature} for transportation')

      def pesticides(self, nothing):
          self.pesticides -= nothing
          print(f'Our flowers have {self.pesticides} and are organically grown')


