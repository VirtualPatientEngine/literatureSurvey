"""Test Uniprot class functions"""

import pytest
from app import uniprot

@pytest.fixture(name="inputs")
def inputs_fixture() -> uniprot.Uniprot:
    """Return objet of Uniprot class"""
    obj = uniprot.Uniprot("P0DTC4")
    return obj

@pytest.fixture(name="inputs2")
def inputs2_fixture() -> uniprot.Uniprot:
    """Return objet of Uniprot class"""
    obj = uniprot.Uniprot("P0XXX0")
    return obj

def test_get_uniprot_status(inputs) -> None:
    """Test get_uniprot_status method"""
    status_code = inputs.get_uniprot_status()
    assert status_code == 200

def test_get_uniprot_status_incorrect(inputs2) -> None:
    """Test get_uniprot_status method with incorrect input"""
    status_code = inputs2.get_uniprot_status()
    assert status_code != 200

def test_get_protein_name(inputs) -> None:
    """Test get_protein_name method"""
    protein_name = inputs.get_protein_name()
    assert protein_name == "Envelope small membrane protein {ECO:0000255|HAMAP-Rule:MF_04204}"

def test_get_protein_sequence(inputs) -> None:
    """Test get_protein_sequence method"""
    protein_sequence = inputs.get_protein_sequence()
    true_sequence = "MYSFVSEETGTLIVNSVLLFLAFVVFLLVTLAILTALRLCAYCCNIVNVSLVKPSFYVYSRVKNLNSSRVPDLLV"
    assert protein_sequence == true_sequence

def test_get_reactome_pathways(inputs) -> None:
    """Test get_reactome_pathways method"""
    reactome_pathways = inputs.get_reactome_pathways()
    assert 'R-HSA-9694493; Maturation of protein E.' in reactome_pathways
