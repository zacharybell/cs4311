class FieldValuePair:
	def __init__(self, FieldName, FieldValue):
		self.FieldName = FieldName
		self.FieldValue = FieldValue

	#	[SRS 149]	When the user selects the “Plus Arrow” and the “Select both Field Name and Value” option is selected, the system shall insert the field name and field value of the selected field in the field area to the input area of the message type field value pair(s).  
	def Add(self, MessageType, FieldName, FieldValue):
		fvp = FieldValuePair(FieldName, FieldValue);
		MessageType.FieldValuePair = fvp

	#[SRS 151]	When the user selects the “Minus Arrow” and the “Message Type Field Value Pair(s)” input area is not empty, the system shall remove the field name and field value of the selected field in the field area from the input area of the message type field value pair(s) in the “Message Type Area”.  
	def Remove(self, MessageType, FieldName, FieldValue):
		MessageType.FieldValuePair = None

	#[SRS 157]	When an existing message type is selected, the system shall provide the ability to update the message type name and the message type field value pair(s).
	def Update(self, MessageType, FieldName, FieldValue):
		MessageType.FieldValuePair.FieldName = FieldName
		MessageType.FieldValuePair.FieldValue = FieldValue