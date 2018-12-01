class FieldEquivalence:
    SourceMessageType = "";
    SourceFieldName = "";
    TargetMessageType = "";
    TargetFieldName = "";

    def __init__(self, SourceMessageType, SourceFieldName, TargetMessageType, TargetFieldName):
        self.SourceMessageType = SourceMessageType
        self.SourceFieldName = SourceFieldName
        self.TargetMessageType = TargetMessageType
        self.TargetFieldName = TargetFieldName

    def add(self):
        pass

    def remove(self):
        pass
