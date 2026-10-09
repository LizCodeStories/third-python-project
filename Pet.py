class Pet:
    # This class stores information about a pet and provides methods
    # to read or update that information.

    def __init__(self, name, species, family_type, owner):
        # Store each pet's data in private attributes.
        self.__petName = name
        self.__petSpecies = species
        self.__petFamilyType = family_type
        self.__petOwnerName = owner

    # Set the pet's name.
    def set_Name(self, name):
        self.__petName = name

    # Set the pet's species.
    def set_Species(self, species):
        self.__petSpecies = species

    # Set the pet's family type (for example: dog, cat, snake).
    def set_Family_Type(self, family_type):
        self.__petFamilyType = family_type

    # Set the pet's owner.
    def set_Owner(self, owner):
        self.__petOwnerName = owner

    # Return the pet's name.
    def get_Name(self):
        return self.__petName

    # Return the pet's species.
    def get_Species(self):
        return self.__petSpecies

    # Return the pet's family type.
    def get_Family_Type(self):
        return self.__petFamilyType

    # Return the pet's owner.
    def get_Owner(self):
        return self.__petOwnerName

    # Create a readable string with all pet details.
    def __str__(self):
        return f"Pet Name: {self.__petName}\nSpecies: {self.__petSpecies}\nFamily Type: {self.__petFamilyType}\nOwner: {self.__petOwnerName}"