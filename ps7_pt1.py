class AdoptionCenter(object):
    def __init__(self, name, species_type, location):
        '''  '''
        self.name = name
        self.species_type = species_type
        self.location = location

    def get_name():
        return self.name

    def get_location():
        return self.location

    def get_species_count():
        pass

    def get_number_of_species(species_name):
        pass

    def adopt_pet(species_name):
        pass


dfl = AdoptionCenter("Dumb Friends League", (12.0, 123.0), {"Dog": 10, "Cat": 5, "Lizard": 3})
print dfl.get_name()
print dfl.get_location()
