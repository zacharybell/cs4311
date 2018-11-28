from datetime import datetime
from xml.etree import ElementTree
import re
from typing import List

class Packet():
    
    def __init__(self, name, size):
        self.name = name
        self.size = size    # might be determined through computation
        self.protocols = []

class Pdml():

    __STAGE = ['setup', 'analysis', 'sequencing', 'generation']


    def __init__(self, date: datetime, creator: str, stage=0):
        
        assert stage >= 0 and stage < len(Pdml.__STAGE)
        
        self.stage = stage
        self.name = ''
        self.description = ''
        self.date = date
        self.creator = creator
        self.packets = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def packets(self) -> List[Packet]:
        return self._packets

    @packets.setter
    def packets(self, packets: List[Packet]) -> None:
        self._packets = packets
    
    def add_packet(self, packet: Packet) -> None:
        self.packets.append(packet)


    def next_stage(self) -> None:
        """Sets moves the stage of the PDML to the next stage.

        Raises:
            Exception: If the stage doesn't exist.
        """

        if self.stage >= len(Pdml.__STAGE) - 1:
            raise Exception('Attempting to reach stage that doesn\'t exist!')
        self.stage = self.stage + 1


    def prev_stage(self) -> None:
        """Sets moves the stage of the PDML to the previous stage.

        Raises:
            Exception: If the stage doesn't exist.
        """

        if self.stage <= 0:
            raise Exception('Attempting to reach stage that doesn\'t exist!')
        self.stage = self.stage - 1


    @staticmethod
    def __create_datetime(date_time_str: str) -> datetime:
        """Takes a string containing the date and time and creates a datetime object.

        The input string must contain the month (MMM), date (DD), year (YYYY), and 
        the time (HH:MM:SS). Each of these must be separated by spaces.

        Args:
            str: a string containing the date and time

        Returns:
            A datetime object from the standard library.
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
    def convert_element_to_pdml(xml_element: ElementTree.Element) -> 'Pdml':
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
            assert xml_element.tag == 'pdml', 'Not a PDML element!'
            date = Pdml.__create_datetime(xml_element.attrib['time'])
            if 'stage' in xml_element.attrib:
                stage = int(xml_element.attrib['stage'])
            else:
                stage = 0
            pdml = Pdml(date, xml_element.attrib['creator'], stage)
            return pdml
        except (AssertionError, KeyError):
            raise ValueError('malformed XML Element')




class Protocol():
    
    def __init__(self, field_name, show_name, size, position, show, value):
        self.field_name = field_name
        self.show_name = show_name
        self.size = size
        self.position = position
        self.show = show
        self.value = value
        self.fields = []

class Field():

    def __init__(self, name, show_name, size, value, show):
        self.name = name
        self.show_name = show_name
        self.size = size    # might be determined through computation
        self.value = value
        self.show = show
