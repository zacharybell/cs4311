from MessageType import MessageType
from FieldValuePair import FieldValuePair

class MessageTypeManager:
	def __init__(self, MessageType=None):
		self.MessageType = MessageType

	def CreateMessageType(self, name, color, fieldValuePair):
		return MessageType(name, color, fieldValuePair)

	#[SRS 157]	When an existing message type is selected, the system shall provide the ability to update the message type name and the message type field value pair(s).
	def UpdateMessageType(self, MessageType, FieldValuePair): 
		MessageType.FieldValuePair = FieldValuePair

	#[SRS 154]	When the user selects the “Delete” button and an existing message type is selected, the system shall delete the selected message type.
	def DeleteMessageType(self, MessageType):
		if(MessageType!= None):
			MessageType = None
		#[SRS 155]	When the user selects the “Delete” button and without a selected existing message type, the system shall display an error message.
		else:
			print("Error Meassage")


f = FieldValuePair("name", "value")
mtm = MessageTypeManager()
lol = mtm.CreateMessageType("message1","green", f)
