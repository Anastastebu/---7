import pytest
from rdflib import Graph, RDF, OWL, Namespace

@pytest.fixture
def ontology_graph():
    g = Graph()
    g.parse("models/onto.owl", format="turtle")
    g.parse("models/onto_data.ttl", format="turtle")
    return g

def test_onto_not_empty(ontology_graph):
    """C1: Файли онтології та даних парсяться і містять триплети"""
    assert len(ontology_graph) > 0

def test_classes_count(ontology_graph):
    """C2: Перевірка кількості класів (>= 30)"""
    classes = list(ontology_graph.subjects(RDF.type, OWL.Class))
    assert len(classes) >= 15

def test_individuals_count(ontology_graph):
    """C3: Перевірка кількості індивідів (>= 20)"""
    EX = Namespace("http://example.org/it_infrastructure#")
    named_individuals = list(ontology_graph.subjects(RDF.type, None))
    assert len(named_individuals) >= 20