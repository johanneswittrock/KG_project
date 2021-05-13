from rdflib import Graph

g = Graph()
g.parse("kg-mini-project-train.ttl", format="turtle")

print(len(g))
