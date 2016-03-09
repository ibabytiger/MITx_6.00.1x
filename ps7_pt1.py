class AdoptionCenter(object):
    def __init__(self, name, species_type, location):
        '''  '''
        self.name = name
        self.species_type = species_type
        self.location = location

    def get_name(self):
        ''' Returns the name of the adoption center '''
        return self.name

    def get_location(self):
        ''' Returns the location of the adoption center '''
        return "(%.1f, %.1f)" % (self.location[0], self.location[1])

    def get_species_count(self):
        ''' Returns a copy of the species (dict) '''
        s = self.species_type.copy()
        return s

    def get_number_of_species(self, species_name):
        ''' Returns the number of a specified species '''
        if species_name not in self.species_type:
            return 0
        else:
            return self.species_type[species_name]

    def adopt_pet(self, species_name):
        ''' Mutates the species dictionary and decrements a species '''
        if species_name in self.species_type:
            self.species_type[species_name] -= 1
            if self.species_type[species_name] == 0:
                del self.species_type[species_name]
