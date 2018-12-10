from datetime import datetime
from xml.etree import ElementTree
import re
from typing import List

class Entropy():
    ## FIXME how is this computed?
    ## entropy = #unique vals for field of message type / # number of packets of message type
    pass

class Field():

    def __init__(self, name, show_name, size, value, show, fields):
        self.name      = name
        self.show_name = show_name
        self.size      = size
        self.value     = value
        self.show      = show
        self.fields    = fields

    @staticmethod
    def _convert_element_to_field(xml_element: ElementTree.Element) -> 'Field':
        assert xml_element.tag == 'field', f'{xml_element.tag} is not a Field element!'

        name      = xml_element.attrib.get('name')
        show_name = xml_element.attrib.get('showname')
        size      = xml_element.attrib.get('size')
        value     = xml_element.attrib.get('value')
        show      = xml_element.attrib.get('show')

        fields = []
        for element in xml_element.getchildren():
            fields.append(Field._convert_element_to_field(element))

        return Field(name, show_name, size, value, show, fields)

class Protocol():
    
    def __init__(self, field_name, show_name, size, position, fields):
        self.field_name = field_name
        self.show_name  = show_name
        self.size       = size
        self.position   = position
        self.show       = ''          ##FIXME Didn't see this in the pdml file
        self.value      = ''          ##FIXME Didn't see this in the pdml file
        self.fields     = fields

    @staticmethod
    def _convert_element_to_protocol(xml_element: ElementTree.Element) -> 'Protocol':
        assert xml_element.tag == 'proto', f'{xml_element.tag} is not a Protocol element!'

        field_name = xml_element.attrib.get('name')
        show_name  = xml_element.attrib.get('showname')
        size       = xml_element.attrib.get('size')
        position   = xml_element.attrib.get('pos')

        fields = []
        for element in xml_element.getchildren():
            fields.append(Field._convert_element_to_field(element))

        return Protocol(field_name, show_name, size, position, fields)


class Packet():
    
    def __init__(self, protocols):
        self.name = ''  ##FIXME where is this set?
        self.size = 0   ##FIXME where is this set?
        self.protocols = protocols

    @staticmethod
    def _convert_element_to_packet(xml_element: ElementTree.Element) -> 'Packet':
        assert xml_element.tag == 'packet', f'{xml_element.tag} is not a Packet element!'

        protocols = []
        for element in xml_element.getchildren():
            protocols.append(Protocol._convert_element_to_protocol(element))

        return Packet(protocols)


class Pdml():


    def __init__(self, date: datetime, creator: str, packets: List[Packet]):
        
        self.name = ''
        self.description = ''
        self.date = date
        self.creator = creator
        self.packets = packets


    @staticmethod
    def _datetime_to_pdml_datestr(dt: datetime) -> str:
        """Takes a python standard datetime object and creates a date string for a pdml file.

        The output is formated Www Mmm DD HH:MM:SS YYYY.

        Example: Sat Sep 17 01:03:30 2016

        Args:
            dt (datetime): a datetime object containing the month, day, hour, minutes, and seconds of a pdml's creation
        
        Returns:
            str: A pdml formated date time string.
        """

        return dt.strftime(r'%a %b %d %H:%M:%S %Y')


    @staticmethod
    def _pdml_datestr_to_datetime(date_time_str: str) -> datetime:
        """Takes a string containing the date and time and creates a datetime object.

        The input string must contain the month (MMM), date (DD), year (YYYY), and 
        the time (HH:MM:SS). Each of these must be separated by spaces.

        Args:
            date_time_str (str): a string containing the date and time

        Returns:
            datetime: A datetime object from the standard library.
        """

        MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

        try:
            # Month
            month_str = re.search(r'|'.join(MONTHS), date_time_str.lower()).group()
            month = MONTHS.index(month_str)

            # Date (regex matches digit 01-31 with whitespace or line ending/beginning surrounding)
            date = int(re.search(r'(?!^|\s)([1-2][0-9]|3[0-1]|[1-9]|0[1-9])(?=\s|$)', date_time_str).group())

            # Year (matches 4 digit ints)
            year = int(re.search(r'(?!^|\s)(\d{4})(?=\s|$)', date_time_str).group())

            # Time (matches dd:dd:dd)
            time = list(map(int, re.search(r'(?!^|\s)\d{2}:\d{2}:\d{2}(?=\s|$)', date_time_str).group().split(':')))

            hour   = time[0]
            minute = time[1]
            second = time[2]

            return datetime(year, month, date, hour, minute, second)

        except AttributeError:
            raise ValueError(f'must have a valid date/time string, {date_time_str}')
   

    @staticmethod
    def _convert_element_to_pdml(xml_element: ElementTree.Element) -> 'Pdml':
        """Converts an XML tree element to a PDML object.

        This function can be used by an xml parser to efficiently create PDML objects 
        that coincide with their xml elements.

        Args:
            Element: an xml element containing attributes that can be used to create a pdml object
        
        Returns:
            Pdml: A constructed pdml object.
        
        Raises:
            ValueError: if the XML element doesn't contain the proper attributes to construct a PDML object
        """

        try:
            assert xml_element.tag == 'pdml', f'{xml_element.tag} is not a PDML element!'
            date = Pdml._pdml_datestr_to_datetime(xml_element.attrib['time'])

            packets = []
            for element in xml_element.getchildren():
                packets.append(Packet._convert_element_to_packet(element))

            return Pdml(date, xml_element.attrib['creator'], packets)
        except (AssertionError, KeyError):
            raise ValueError('malformed XML Element')


    @staticmethod
    def unmarshall(file: str) -> 'Pdml':
        """Unmarshalls a PDML file into a Pdml object.

        Args:
            file (str): a file path to a pdml file

        Returns:
            Pdml: A constructed Pdml object
        """

        pdml_tree = ElementTree.parse(file)
        pdml_element = pdml_tree.getroot()

        return Pdml._convert_element_to_pdml(pdml_element)


    def marshall(self, path: str, name: str=None) -> None:
        """Saves the Pdml object as a Pdml formated file.
        
        Args:
            path (str): the path to the target directory
            name (str): the target file name (defaults to the pdml name)

        Returns:
            None
        """

        pass
        