from daisies import Daisies
from rose import Rose
from poppies import Poppies
from organic_van import OrganicVan
from van import Van

pop = Poppies()
rose = Rose()
daisies = Daisies()



organic = OrganicVan()
notorganic = Van()

notorganic.add_flower(rose)
organic.add_flower(rose)
