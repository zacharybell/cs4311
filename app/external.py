from xml.etree import ElementTree

import pdml


def convert_pcap_to_pdml(src: str, dest: str) -> int:
    """ Converts a PCAP file to PDML using TShark

    Args:
        src (str) : the path to the source (pcap) file
        dest (str): the path to the destination (pdml)

    Returns:
        int: 0 if successful, 1 if failure
    """
    
    import subprocess

    args = f'tshark -r {src} -T pdml > {dest}'
    return subprocess.call(args, shell=True)


def parse_pdml(file: str) -> pdml.Pdml:
    
    pdml_tree = ElementTree.parse(file)

    pdml_element = pdml_tree.getroot()

    if pdml_element.tag == 'pdml':
        root = pdml.Pdml.convert_element_to_pdml(pdml_element)
        
    #     packet_elements = pdml_element.getchildren()

    print(root)

    return root


parse_pdml('samples/cubic.pdml')
