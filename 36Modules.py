#import all the function from the module
import utils

print(utils.kg_to_lbs(70))

#import specific function from the module
import utils
from utils import kg_to_lbs

print(kg_to_lbs(100))
