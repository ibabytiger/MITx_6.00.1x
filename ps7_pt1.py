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

class Adopter(object):
    def __init__(self, name, desired_species):
        ''' '''
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        ''' Returns a string containing the name of the adopter '''
        return self.name

    def get_desired_species(self):
        ''' Returns a string containing the adopter's desired species '''
        return self.desired_species

    def get_score(self, AdoptionCenter):
        ''' Returns a floating point containing the score of an adopter '''
        return float(1 * AdoptionCenter.get_number_of_species(self.get_desired_species()))

class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, AdoptionCenter):
        ''' Returns a floating point containing the score of a flexible adopter '''
        #score = AdoptionCenter.get_number_of_species(self.get_desired_species())
        score = Adopter.get_score(Adopter, AdoptionCenter)
        numother = 0
        for pet in self.considered_species:
            numother += AdoptionCenter.get_number_of_species(pet)
        return float(score + .03 * numother)

class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, AdoptionCenter):
        ''' Returns a floating point containing the score of a fearful adopter '''
        score = AdoptionCenter.get_number_of_species(self.get_desired_species())
        numother = 0
        for pet in self.considered_species:
            numother += AdoptionCenter.get_number_of_species(pet)
        return float(score - .03 * numother)


# Basic Tests for AdoptionCenter
dfl = AdoptionCenter("Dumb Friends League", {"Dog": 10, "Cat": 5, "Lizard": 3}, (1.0, 2.0))
'''
print dfl.get_name()
print dfl.get_location()
print dfl.get_species_count()
print dfl.get_number_of_species("Dog")
print dfl.get_number_of_species("Llama")
dfl.adopt_pet("Dog")
fl.adopt_pet("Dog")
'''

# Basic Tests for Adopter
sara = Adopter("Sara", "Dog")
'''
print sara.get_name()
print sara.get_desired_species()
print sara.get_score(dfl)
'''

# Basic Tests for FlexibleAdopter
troy = FlexibleAdopter("Troy", "Dog", ["Cat", "Spider", "Ferret"])
print troy.get_score(dfl)

# Basic Tests for FearfulAdopter
lauren = FearfulAdopter("Lauren", "Dog", "Lizard")
