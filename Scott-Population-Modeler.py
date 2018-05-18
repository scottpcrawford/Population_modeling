# Attempt to build a program that models and tracks population genetics

import random
import csv # reads the SSA's list of most popular baby names for 2017
import numpy as np # extra python package to do some math things, install it with "pip install numpy" on the command line

# open the babynames file
with open('babynames.csv', 'r') as f:
    reader = csv.reader(f)
    names_list = list(reader)
# =============================================================================
# define a class of beings with some basic attributes
class Creature:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.genome = []
        self.genome_length = 10 # change this to make a longer genome
        self.allele_length = 2
        self.generations_remaining = random.randint(1,4) # creature will be capable of reproduction for 1 - 4 generations
        self.capable_of_breeding = True

    def get_older(self):
        self.generations_remaining -= 1
        if self.generations_remaining < 1:
            self.capable_of_breeding = False

    def make_sterile(self):
        self.capable_of_breeding = False


    # randomly generate a genome sequence for our initial population
    def generate_genome(self):
        for i in range (self.genome_length):
            self.genome.append(tuple(np.random.randint(2, size=self.allele_length))) # generate a genome with random values for each allele

# =============================================================================
# a class with some population characteristics
class Population:
    members = [] # initial empty population list
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        return self

    def add_member(self,creature):
        self.members.append(creature) # add a creature to the population pool

    def print_members(self): # helper file to see who is in the group
        print ("\nCurrent breeding members: ")
        for creature in self.members:
            print(creature.name,'genome:',creature.genome)
        print("")

    def population_size(self):
        return len(self.members)

    def return_member_list(self):
        return self.members

    def remove_member(self, name):
        self.members.remove(name)

    def clean_up(self):
        for item in self.members:
            if item.generations_remaining < 1:
                #print("removing",item.name,"from breeding population")
                self.remove_member(item)

# do gross stuff
    def mate(self, parentA, parentB):
        if parentA.capable_of_breeding and parentB.capable_of_breeding:
            if parentA.name == parentB.name:
                return #no self-fertilization
            if parentA.sex == parentB.sex:
                if random.randint(0,100) < 2: # 2% chance of one member deciding not to breed
                    random.choice([parentA,parentB]).make_sterile() # remove one from breeding pool
            else:
                creatureAttribute = random.choice(names_list) # randomly choose a name and gender from the names_list
                a = Creature(creatureAttribute[0],creatureAttribute[1]) # create a new instance of a creature with a name and sex
                aSplit, bSplit = [], [] # create empty list for parents chromosomes
                for item in parentA.genome: # split parent A's chromosomes in half
                    aSplit.append(item[random.randint(0,1)])
                for item in parentB.genome: # split parent B's chromosomes in half
                    bSplit.append(item[random.randint(0,1)])
                    a.genome = list(zip(aSplit,bSplit)) # combine the chromosomes in their new offspring
                #print(parentA.name," & ",parentB.name,'mated to produce:',a.name)
                self.add_member(a) # add the offspring to the population

# =============================================================================
def setUpWorld(initialPop):
    a = Creature('Adam', 'M')
    b = Creature('Eve', 'F')
    a.generate_genome()
    b.generate_genome()
    myPopulation = Population(initialPop) # create a population
    myPopulation.add_member(a) # add the initial pairing
    myPopulation.add_member(b) # and don't forget the ladies
    for x in range(0,initialPop): # have them do the nasty to build out your first generation.. Cain and Abel and so forth
        myPopulation.mate(a,b)
    return a,b,myPopulation

        
def processGeneration(currentPop):
    populationList = currentPop.return_member_list()
    for creature in populationList:
        currentPop.mate(creature,random.choice(populationList)) # first shot at love
        currentPop.mate(creature,random.choice(populationList)) # second shot at love
        creature.get_older()
    currentPop.clean_up()
    print("population size is: ",currentPop.population_size())
    return currentPop
        



def main():
    # create our initial population and randomly generate a genome for them
    initialPopulationSize = int(input('Enter Initial Population Size: '))
    numberOfGenerations = int(input('Enter Number of Generations: '))
    patriarch, matriarch, population = setUpWorld(initialPopulationSize) # save the details of the patriarch, matriach, and the initial population

    
    for i in range(0,numberOfGenerations):
        population = processGeneration(population)


    #population.print_members()
    #print ("population size is: ",population.population_size())
    print (patriarch.name,"genome: ",patriarch.genome)
    print (matriarch.name,"genome: ",matriarch.genome)


if __name__ == "__main__":
    main()
