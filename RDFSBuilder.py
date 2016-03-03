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

# remove header
entries.pop(0)

print "Writing Headers...\n"

# Write header to file
fw.write("@prefix actorDB: <http://www.kearnsw.com/> .\n"
         "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
         "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
         "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")

chars_to_remove = [' ',"'", ',', '(', ')', '[', ']', '.', '-', '+']

print "Building File...\n"
for entry in entries:
    # remove special characters that are not recognized by RDF-S
    entry[0] = entry[0].translate(None, ''.join(chars_to_remove))
    entry[2] = entry[2].translate(None, ''.join(chars_to_remove))
    entry[1] = entry[1].translate(None, ''.join(chars_to_remove))

    # make sure that there are no missing values and create triples
    if entry[0] != '' and entry[1] != '':
        fw.write('actorDB:' + entry[0] + '\t' +
		 'hasActor' +
                 'actorDB:' + entry[2] + '\n' +
                 'actorDB:' + entry[1] + ' .\n')

fw.close()
