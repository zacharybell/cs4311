import MessageType
class MessageTypeManager:
	def __init__(self, MessageType,FieldValuePair):
		self.MessageType = MessageType
		self.FieldValuePair = FieldValuePair


		
	def CreateMessageType(MessageTypeName,color,FieldValuePair):
		messType = MessageType()
		messType.MessageTypeName = MessageTypeName
		messType.color = color
		messType.FieldValuePair = FieldValuePair
		return messType



	#[SRS 157]	When an existing message type is selected, the system shall provide the ability to update the message type name and the message type field value pair(s).
	def UpdateMessageType(MessageType, FieldValuePair): 
		MessageType.FieldValuePair = FieldValuePair


	#[SRS 154]	When the user selects the “Delete” button and an existing message type is selected, the system shall delete the selected message type.
	def DeleteMessageType(MessageType):
		if(MessageType!= None):
			MessageType = None
		#[SRS 155]	When the user selects the “Delete” button and without a selected existing message type, the system shall display an error message.
		else:
			print("Error Meassage")

