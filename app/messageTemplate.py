#!/usr/bin/env python3


class messageTemplate():

    def __init__(self, name, folderName, folderPath, outputFormat):

        self.messageTemplateName = name
        self.destinationFolderName = folderName
        self.destinationFolderPath = folderPath
        self.outputFormat = outputFormat
        self.messageTypes = []
        self.fieldEquivalenceDependeny = []
        self.fieldLengthDependency = []
        self.packeLengthDependency = []
        self.checksum = []


    def generateScapyFile(self):
        pass


    def setMessageTemplateName(self, name):
        self.messageTemplateName = name

    def setDestinationFolderName(self, name):
        self.destinationFolderName = name

    def setDestinationFolderPath(self, path):
        self.destinationFolderPath = path

    def setOutputFormat(self, format):
        self.outoutFormat = format

    def addMessageType(self, messageType):
        self.messageTypes.append(messageType)

    def setFieldEquivalenceDependency(self, fed):
        self.fieldEquivalenceDependency = fed

    def setFieldLengthDependency(self, fld):
        self.fieldEquivalenceDependency = fld

    def setPacketLengthDependency(self, pld):
        self.packetLengthDependecny = pld

    def setChecksum(self, checksum):
        self.checksum = checksum

        
