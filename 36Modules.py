#import all the function from the module
import converter_module

print(converter_module.kg_to_lbs(70))

#import specific function from the module
import converter_module
from converter_module import kg_to_lbs

print(kg_to_lbs(100))
