class MessageTemplate:

    MessageTemplateName="";
    DestinationFolderName="";
    DestinationFolderPath="";
    OutputFormat="";

    def __init__(self,MessageTemplateName,DestinationFolderName,DestinationFolderPath,OutputFormat):

        self.MessageTemplateName = MessageTemplateName
        self.DestinationFolderName = DestinationFolderName
        self.DestinationFolderPath = DestinationFolderPath
        self.OutputFormat = OutputFormat

    def generate(self,):
        pass

    def access(self,):
        pass