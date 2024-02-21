"""Test Uniprot class functions"""

import pytest
from app import literatureFetch

@pytest.fixture(name="inputs")
def inputs_fixture() -> literatureFetch.Arxiv:
    """Return objet of Uniprot class"""
    obj = literatureFetch.Arxiv("1706.03762")
    return obj

def test_get_arxiv_id(inputs) -> None:
    """Test get_arxiv_data method"""
    arxiv_id = inputs.get_arxiv_id()
    assert arxiv_id == inputs.arxiv_id

def test_get_semantic_scholar_data(inputs) -> None:
    """Test get_semantic_scholar_data method"""
    inputs.semantic_scholar_data = literatureFetch.get_semantic_scholar(["ARXIV:"+inputs.arxiv_id])
    semantic_scholar_data = inputs.get_semantic_scholar_data()
    assert semantic_scholar_data[0]['title'] == "Attention is All you Need"

def test_get_semantic_scholar(inputs) -> None:
    """Test get_semantic_scholar function"""
    semantic_scholar_data = literatureFetch.get_semantic_scholar(["ARXIV:"+inputs.arxiv_id])
    assert semantic_scholar_data[0]['referenceCount'] == 42
