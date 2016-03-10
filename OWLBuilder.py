import csv
import os

# Set path to rdf file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Read in data
inputFile = 'GDELT_1mil.txt'
f = open(os.path.join(__location__, inputFile))
entries = list(csv.reader(f, delimiter='\t'))
f.close()

# Write to file
outputFile = 'GDELT.owl'
fw = open(os.path.join(__location__, outputFile), 'w+')

# remove header
entries.pop(0)

print("Writing Headers...\n")

# Write header to file
fw.write("@prefix eventDB: <http://www.kearnsw.com/> .\n"
         "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
         "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
         "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")

dbPrefix = 'eventDB:'
chars_to_remove = [' ', "'", ',', '(', ')', '[', ']', '.', '-', '+', ';']

print("Building File...\n")

fw.write(""":hasActor1code rdf:type owl:ObjectProperty ;
                   owl:inverseOf :isActor1Of ;
                   rdf:type owl:TransitiveProperty ;
                   rdfs:domain :GlobalEventID ;
               	   rdfs:range :Actor1Code .

:hasActor2code rdf:type owl:ObjectProperty ;

                   owl:inverseOf :isActor2Of ;
                   rdf:type owl:TransitiveProperty;
                   rdfs:domain :GlobalEventID ;
               	   rdfs:range :Actor2Code .

:hasEvent rdf:type owl:ObjectProperty ;
                   rdfs:domain :GlobalEventID ;
                   rdfs:range :EventName .

:hasDate rdf:type owl:ObjectProperty ;

	               owl:inverseOf :isDateOf ;
                   rdf:type owl:TransitiveProperty;
                   rdfs:domain :GlobalEventID ;
                   rdfs:range :Date .

:hasLocation rdf:type owl:ObjectProperty ;

         	       rdfs:domain :GlobalEventID ;
                   rdfs:range :ActionGeo_Fullname .

:hasLatitude rdf:type owl:ObjectProperty ;

                   rdfs:domain :GlobalEventID ;
                   rdfs:range :ActionGeo_Lat .

:hasLongtitude rdf:type owl:ObjectProperty ;

                   rdfs:domain :GlobalEventID ;
                   rdfs:range :ActionGeo_Long .

:hasTheme rdf:type owl:ObjectProperty ;

                   rdfs:domain :GlobalEventID ;
                   rdfs:range :Theme .

:hasTheme rdf:type owl:ObjectProperty ;

                   rdfs:domain :SourceURL ;
                   rdfs:range :Theme .

:hasSource rdf:type owl:ObjectProperty ;

                   rdfs:domain :GlobalEventID ;
                   rdfs:range :SourceURL .

:hasName rdf:type owl:ObjectProperty ;

                   rdfs:domain :ActorCode ;
                   rdfs:range :ActorName .


:hasCountry rdf:type owl:ObjectProperty ;

                   rdfs:domain :ActorCode ;
                   rdfs:range :CountryCode .

#################################################################
#
#	Classes
#
#################################################################

:GlobalEventID rdf:type owl:Class ;
                           rdfs:subClassOf :Event .

:ActorCode rdf:type owl:Class ;
                           rdfs:subClassOf :Actor .
:ActorName rdf:type owl:Class ;
                           rdfs:subClassOf :Actor .
:EventName  rdf:type owl:Class ;
           	               rdfs:subClassOf :Event .

:Date  rdf:type owl:Class ;
                           rdfs:subClassOf :Event .

:ActionGeo_Fullname  rdf:type owl:Class ;
                           rdfs:subClassOf :Location .

:ActionGeo_Lat rdf:type owl:Class ;
                           rdfs:subClassOf :Location .

:ActionGeo_Long rdf:type owl:Class ;
                           rdfs:subClassOf :Location .

:Theme rdf:type owl:Class .

:Actor rdf:type owl:Class .

:Location rdf:type owl:Class .

:Event rdf:type owl:Class .

:SourceURL rdf:type owl:Class ;
                           rdfs:subClassOf :Event .

:CountryCode rdf:type owl:Class ;
                           rdfs:subClassOf :Location .

:Actor1Code rdf:type owl:Class ;
                           rdfs:subClassOf :Actor .
:Actor2Code rdf:type owl:Class ;
                           rdfs:subClassOf :Actor .
                           """)

for i in range(25):
    entry = entries[i]
    # remove special characters that are not recognized by RDF-S
    entry[0] = entry[0].translate(''.join(chars_to_remove))
    entry[2] = entry[2].translate(''.join(chars_to_remove))
    entry[1] = entry[1].translate(''.join(chars_to_remove))
#   entry[50] = entry[50].translate(''.join(chars_to_remove))
#   entry[58] = entry[58].translate(''.join(chars_to_remove))

    # Create triples
    fw.write(':' + entry[0] + '\t' + '\t' +
             'rdf:type  owl:class ;' + '\n' + '\t' +
             'rdfs:subClassOf :GlobalEventID .' + '\n'
             )
    fw.write(':' + entry[1] + '\t' + '\t' +
             'rdf:type  owl:class ;' + '\n' + '\t' +
             'rdfs:subClassOf :Date .' + '\n'
             )
    fw.write(':' + entry[5] + '\t' + '\t' +
             'rdf:type  owl:class ;' + '\n' + '\t' +
             'rdfs:subClassOf :ActorCode .' + '\n'
             )
    if entry[5] != '':
        fw.write(':' + entry[5] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :Actor1Code .' + '\n'
                 )
    if entry[15] != '':
        fw.write(':' + entry[15] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :Actor2Code .' + '\n'
                 )
    if entry[6] != '':
        fw.write(':' + entry[6] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActorName .' + '\n'
                 )
    if entry[16] != '':
        fw.write(':' + entry[16] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActorName .' + '\n'
                 )
    if entry[7] != '':
        fw.write(':' + entry[7] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :CountryCode .' + '\n'
                 )
    if entry[17] != '':
        fw.write(':' + entry[17] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :CountryCode .' + '\n'
                 )
    if entry[36] != '':
        fw.write(':' + entry[36] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActionGeo_Fullname .' + '\n'
                 )
    if entry[50] != '':
        fw.write(':' + entry[50] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActionGeo_Fullname .' + '\n'
                 )
    if entry[53] != '':
        fw.write(':' + entry[53] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActionGeo_Lat .' + '\n'
                 )
    if entry[54] != '':
        fw.write(':' + entry[54] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :ActionGeo_Long .' + '\n'
                 )
    fw.write(':' + entry[57] + '\t' + '\t' +
                 'rdf:type  owl:class ;' + '\n' + '\t' +
                 'rdfs:subClassOf :SourceURL .' + '\n'
                 )
    # Equivalent to
    fw.write(':' + entry[0] + '\t' + '\t' +
             'rdf:type  owl:class ;' + '\n' + '\t' +
             'owl:equivalentClass [ owl:intersectionOf (rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasActor1Code ;' + '\n' +
             'owl:someValueFrom :' + entry[5] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasActor2Code ;' + '\n' +
             'owl:someValueFrom :' + entry[15] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasDate ;' + '\n' +
             'owl:someValueFrom :' + entry[0] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasLocation ;' + '\n' +
             'owl:someValueFrom :' + entry[36] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasLatitude ;' + '\n' +
             'owl:someValueFrom :' + entry[53] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasLongtitude ;' + '\n' +
             'owl:someValueFrom :' + entry[54] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasSource ;' + '\n' +
             'owl:someValueFrom :' + entry[57] + ')] .' + '\n'
             )
    fw.write(':' + entry[5] + '\t' + '\t' +
             'owl:equivalentClass [ owl:intersectionOf (rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasName ;' + '\n' +
             'owl:someValueFrom :' + entry[6] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasCountry ;' + '\n' +
             'owl:someValueFrom :' + entry[7] + ')' + '\n'
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :isActor1Of ;' + '\n' +
             'owl:someValueFrom :' + entry[0] + ')] .' + '\n'
             )
    fw.write(':' + entry[15] + '\t' + '\t' +
             'owl:equivalentClass [ owl:intersectionOf (rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasName ;' + '\n' +
             'owl:someValueFrom :' + entry[16] + ')' + '\n' +
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :hasCountry ;' + '\n' +
             'owl:someValueFrom :' + entry[17] + ')' + '\n'
             '(rdf:type owl:Restriction ;' + '\n' +
             'owl:onProperty  :isActor1Of ;' + '\n' +
             'owl:someValueFrom :' + entry[0] + ')]' + '\n'
             )

fw.close()
