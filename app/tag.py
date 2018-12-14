

class Tag:

    def __init__(self, name, field, annotation):
        self.name = name
        self.field = field
        self.annotation = annotation

    def updateName(self, name):
        self.name = name


    def updateField(self, field):
        self.field = field

    def updateAnnotation(self, annotation):
        self.annotation = annotation



class TagManager:

    def __init__(self):
        self.tags = []


    def addTag(self, name, field, annotation):
        self.tags.append(Tag(name,field,annotation))

    def removeTag(self, name):
        for tag in self.tags:
            if tag.name == name:
                self.tags.remove(tag)
                break


