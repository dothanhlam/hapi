from humanapi import allergies, encounters, functional_statuses
from medical.allergen import Allergen

from tabulate import tabulate # pip install tabulate

  
def execute_hapi():
    allergies_list = allergies()
    allergies_table = []
    
    for item in allergies_list:
        allergen = Allergen.from_json(item)
        allergies_table.append(allergen.get_tabulate_value())
      
    print tabulate(allergies_table, headers=Allergen.from_json(allergies_list[0]).get_tabulate_header())
    

if __name__ == '__main__':
    execute_hapi()