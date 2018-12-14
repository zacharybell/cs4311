


class Filter():

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def updateFilterName(self, name):
        self.name = name

    def updateFilterExpression(self, expr):
        self.expression = expr
        


class FilterManager():

    def __init__(self):
        
        self.filters = []


    def addFilter(self, name, expression):

        filter = Filter(name, expression)
        filters.append(filter)

    def removeFilter(self, name):

        for filter in self.filters:
            if filter.name == name:
                self.filters.remove(filter)
           
