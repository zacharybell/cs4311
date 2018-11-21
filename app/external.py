def convert_pcap_to_pdml(src, dest): # type: (str, str) -> int
    """ Converts a PCAP file to PDML using TShark

    Args:
        src (str) : the path to the source (pcap) file
        dest (str): the path to the destination (pdml)

    Returns:
        int: 0 if successful, 1 if failure
    """
    
    import subprocess

    args = 'tshark -r {} -T pdml > {}'.format(src, dest)
    return subprocess.call(args, shell=True)