



class Filter():

    def __init__(name, expression):
        self.name = name
        self.expression = expression

    def updateFilterName(name):
        self.name = name

    def updateFilterExpression(expr):
        self.expression = expt


class FilterManager():

    def __init__(self):
        
        self.filters = []


    def addFilter(name, expression):

        filter = Filter(name, expression)
        filters.append(filter)

    def removeFilter(name):

        for filter in filters:
            if filter.name == name:
                filters.remove(filter)


        
