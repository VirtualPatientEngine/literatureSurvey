"""
A class to extract the data from Uniprot
for a given protein
"""

import re
import requests

class Uniprot:
    """A class to extract the data from Uniprot
    for a given uniprot accession
    """

    def __init__(self, uniprot_acc: str):
        """Initialize the class"""
        self.uniprot_acc = uniprot_acc

    def get_uniprot_status(self) -> int:
        """Get the status of the protein

        Returns:
            int: status of the protein
        """
        url = f"https://rest.uniprot.org/uniprotkb/{self.uniprot_acc}.fasta"
        response = requests.get(url, timeout=10)
        return response.status_code

    def get_protein_name(self) -> str:
        """Get the name of the protein

        Returns:
            str: name of the protein
        """
        url = f"https://rest.uniprot.org/uniprotkb/{self.uniprot_acc}.txt"
        response = requests.get(url, timeout=10)
        protein_name = re.search(r"RecName: Full=(.+);", response.text).group(1)
        return protein_name

    def get_protein_sequence(self) -> str:
        """Get the sequence of the protein

        Returns:
            str: sequence of the protein
        """
        url = f"https://rest.uniprot.org/uniprotkb/{self.uniprot_acc}.fasta"
        response = requests.get(url, timeout=10)
        protein_sequence = "".join(response.text.split("\n")[1:])
        return protein_sequence

    def get_reactome_pathways(self) -> list:
        """Get the Reactome pathways for the protein

        Returns:
            str: Reactome pathways for the protein
        """
        url = f"https://rest.uniprot.org/uniprotkb/{self.uniprot_acc}.txt"
        response = requests.get(url, timeout=10)
        # reactome_pathways = re.search(r"Reactome; (.+)", response.text)
        reactome_pathways = re.findall(r"Reactome; (.+)", response.text)
        return reactome_pathways

if __name__ == "__main__":
    # Run the script from command line
    UNIPROT_ACC = "P0DTC2"
    obj = Uniprot(UNIPROT_ACC)
    status_code = obj.get_uniprot_status()
    if status_code == 200:
        print(obj.get_protein_name())
        print(obj.get_protein_sequence())
        print(obj.get_reactome_pathways())
    else:
        print("Protein not found")
