class PDML():
    
    __STAGE = ['setup', 'analysis', 'sequencing', 'generation']

    def __init__(self, name, date, time, creator, stage=0):
        self.stage = stage
        self.name = name
        self.date = date
        self.creator = creator
        self.packets = []

    def next_stage(self):
        """Sets moves the stage of the PDML to the next stage.

        Raises:
            Exception: If the stage doesn't exist.
        """

        if self.stage >= len(PDML.__STAGE) - 1:
            raise Exception('Attempting to reach stage that doesn\'t exist!')
        self.stage = self.stage + 1

    def prev_stage(self):
        """Sets moves the stage of the PDML to the previous stage.

        Raises:
            Exception: If the stage doesn't exist.
        """

        if self.stage <= 0:
            raise Exception('Attempting to reach stage that doesn\'t exist!')
        self.stage = self.stage - 1

class Packet():
    
    def __init__(self, name, size):
        self.name = name
        self.size = size    # might be determined through computation
        self.protocols = []

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
