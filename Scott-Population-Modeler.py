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
        self.generations_remaining = random.randint(1,4)
        self.capable_of_breeding = True

    def get_older(self):
        self.generations_remaining -= 1
        if self.generations_remaining < 1:
            self.capable_of_breeding = False

    def make_sodomite(self):
        self.capable_of_breeding = False


    # randomly generate a genome sequence for our initial population
    def generate_genome(self):
        for i in range (a.genome_length):
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
        print ("These are the current group members: ")
        for creature in self.members:
            print(creature.name,"- sex:",creature.sex,"- Can breed?", creature.capable_of_breeding,"- virility remaining: ",creature.generations_remaining,", genome:",creature.genome)
        print("")

    def return_member_list(self):
        return self.members

    def remove_member(self, name):
        self.members.remove(name)

    def clean_up(self):
        for item in self.members:
            if item.generations_remaining < 1:
                self.remove_member(item)

# do gross stuff
    def mate(self, parentA, parentB):
        if parentA.capable_of_breeding and parentB.capable_of_breeding:
            if parentA.name == parentB.name:
                return #don't f- yourself
            if parentA.sex == parentB.sex:
                print(parentA.name,"shall not lay down with ",parentB.name,",breeding impossible, God will randomly smite one of them")
                if random.randint(0,100) < 2: # 2% chance of God being an awful human being
                    random.choice([parentA,parentB]).make_sodomite() # remove one from breeding pool
            else:
                playGod = random.choice(names_list) # randomly choose a name and gender from the names_list
                a = Creature(playGod[0],playGod[1]) # create a new instance of a creature with a name and sex
                aSplit, bSplit = [], [] # create empty list for parents chromosomes
                for item in parentA.genome: # split parent A's chromosomes in half
                    aSplit.append(item[random.randint(0,1)])
                for item in parentB.genome: # split parent B's chromosomes in half
                    bSplit.append(item[random.randint(0,1)])
                    a.genome = list(zip(aSplit,bSplit)) # combine the chromosomes in their new offspring
                print(parentA.name," & ",parentB.name,'f-ed each other and now there is a new creature:',a.name)
            #   print ("aSplit: ",aSplit) # print parentA's chromosome split
            #   print ("bSplit: ",bSplit) # print parentB's chromosome split
                self.add_member(a) # add the offspring to the population

# =============================================================================

# create our initial population and randomly generate a genome for them
a = Creature('Adam', 'M')
b = Creature('Eve', 'F')
a.generate_genome()
b.generate_genome()
initialPopulationSize = int(input('Enter Initial Population Size: '))
#initialPopulationSize = 50
numberOfGenerations = int(input('Enter Number of Generations: '))
#numberOfGenerations = 10
myPopulation = Population(initialPopulationSize) # create a population
myPopulation.add_member(a) # add the initial pairing
myPopulation.add_member(b) # and don't forget the ladies
for x in range(0,initialPopulationSize): # have them do the nasty to build out your first generation.. Cain and Abel and so forth
    myPopulation.mate(a,b)

#print (a.name,": ", a.genome)
#print (b.name,": ", b.genome)

#myPopulation.print_members()

for i in range(0,numberOfGenerations):

    theNextGeneration = myPopulation.return_member_list();
    for x in range(0,len(theNextGeneration)): # go through every member of the population and find them a random hookup
        for j in range(0,2): # give everyone a couple chances per generation to breed
            myPopulation.mate(theNextGeneration[x],random.choice(theNextGeneration))
        theNextGeneration[x].get_older() # reduce everyone's life counter
    myPopulation.clean_up() # remove non-virile people from the breeding pool
    #myPopulation.print_members()

myPopulation.print_members()
print (a.name,": ", a.genome)
print (b.name,": ", b.genome)