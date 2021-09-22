import pytest

from graph.graph import Graph, Vertex, Edge

def test_can_instantiate_Graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list() == {}


def test_can_instantiate_Vertex():
    vertex = Vertex()
    assert vertex
    assert vertex.value == None


def test_can_instantiate_Edge():
    pass


def test_vertex_can_be_added_to_graph():
    pass


def test_an_edge_can_be_added_to_graph():
    pass


def test_a_collection_of_all_nodes_can_be_retrieved_from_graph():
    pass


def test_all_neighbors_can_be_retrieved_from_graph():
    pass


def test_neighbors_are_returned_with_weights_between_nodes_included():
    pass


def test_size_returns_correct_size():
    pass


def test_a_graph_with_only_one_node_and_edge_can_be_returned():
    pass


def test_an_empty_graph_properly_returns_null():
    pass
