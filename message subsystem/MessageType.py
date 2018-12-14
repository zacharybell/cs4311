class MessageType:
	def __init__(self, MessageTypeName, Color, FieldValuePair):
		self.MessageTypeName = MessageTypeName
		self.Color = Color
		self.FieldValuePair = FieldValuePair
		self.next = None