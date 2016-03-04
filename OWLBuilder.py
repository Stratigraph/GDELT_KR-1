import csv
import os

# Set path to rdf file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


# Read in data
f = open(os.path.join(__location__, 'actorlist.txt'))
entries = list(csv.reader(f, delimiter='\t'))
f.close()
fw = open(os.path.join(__location__, 'actorlist.ttl'), 'w+')
