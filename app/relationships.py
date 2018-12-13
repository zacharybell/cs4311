#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alex2195
"""

class RelationshipManager():
    
    def__init__(self):
        self.FieldEquivalences = []
        self.PacketLengthDependencies = []
        self.FieldLengthDependencies = []
        self.Checksums = []
    
    create_FieldEquivalence(self, src_messagetype: MessageType, src_fieldname: str, target_messagetype: MessageType, target_fieldname: str) -> None:
        self.FieldEquivalences.append(FieldEquivalence(src_messagetype, src_fieldname, target_messagetype, target_fieldname))
        
    create_FieldLengthDependency(self, src_fieldname: str, target_fieldname: str) -> None:
        self.FieldLengthDependencies.append(FieldLengthDependency(src_fieldname), target_fieldname))
    
    create_PacketLengthDependecy(self, packetname: str, fieldname: str) -> None:
        self.PacketLengthDependencies.append(PacketLengthDependency(packetname, fieldname))
        
    create_Checksum(self, packetname: str, fieldname: str) -> None:
        self.Checksums(Checksum(packetname, fieldname))
        
    get_field_equivalences(self, src_messagetype = None, src_fieldname = None, target_messagetype = None, target_fieldname = None):
        found = []
        add = True
        if src_messagetype == None and src_fieldname == None and target_messagetype == None and target_fieldname == None:
            return found
        
        for fe in self.FieldEquivalences:
            
            if src_messagetype != None and fe.src_messagetype != src_messagetype:
                add = False
            if src_fieldname != None and fe.src_fieldname != src_fieldname:
                add = False
            if target_messagetype != None and fe.target_messagetype != target_messagetype:
                add = False
            if target_fieldname != None and fe.target_fieldname != target_fieldname:
                add = False
            
            if add == True:
                found.append(fe)
                
        return found
    
    get_field_length_dependencies(self, src_fieldname = None, target_fieldname = None):
        found = []
        add = True
        if src_fieldname == None and target_fieldname == None:
            return found
        
        for fl in self.FieldLengthDependencies:
            if src_fieldname != None and fl.fieldname != src_fieldname:
                add = False
            if target_fieldname != None and fl.target_fieldname != target_fieldname:
                add = False
            
            if add == True:
                found.append(fl)
                
        return found
    
    get_packet_length_dependencies(self, packetname = None, fieldname = None):
        found = []
        add = True
        if packetname == None and fieldname == None:
            return found
        
        for fl in self.PacketLengthDependencies:
            if packetname != None and pl.packetname != packetname:
                add = False
            if fieldname != None and pl.fieldname != fieldname:
                add = False
            
            if add == True:
                found.append(pl)
                
        return found
            
    get_checksums(self, packetname = None, fieldname = None):
        found = []
        add = True
        if packetname == None and fieldname == None:
            return found
        
        for cs in self.Checksums:
            if packetname != None and cs.packetname != packetname:
                add = False
            if fieldname != None and cs.fieldname != fieldname:
                add = False
            
            if add == True:
                found.append(cs)
                
        return found
    
    update_field_equivalence(self, fieldEquivalence, attribute, change) -> None:
        if attribute = 'source_message_type':
            fieldEquivalence.src_messagetype = change
        if attribute = 'source_field_name':
            fieldEquivalence.src_fieldname = change
        if attribute = 'target_message_type':
            fieldEquivalence.target_messagetype = change
        if attribute = 'target_field_name':
            fieldEquivalence.target_fieldname = change
    
    update_field_length_dependency(self, fieldLengthDependency, attribute, change) -> None:
        if attribute = 'source_field_name':
            fieldLengthDependency.src_fieldname = change
        if attribute = 'target_field_name':
            fieldLengthDependency.target_fieldname = change
            
    update_packet_length_dependency(self, packetLengthDependency, attribute, change) -> None:
        if attribute = 'packet_name':
            packetLengthDependency.packetname = change
        if attribute = 'field_name':
            packetLengthDependency.fieldname = change
            
    update_checksum(self, checksum, attribute, change) -> None:
        if attribute = 'packet_name':
            checksum.packetname = change
        if attribute = 'field_name':
            checksum.fieldname = change    


class FieldEquivalence():
    
    def __init__(self, src_messagetype: MessageType, src_fieldname: str, target_messagetype: MessageType, target_fieldname: str):
        self.src_messagetype = src_messagetype
        self.src_fieldname = src_fieldname
        self.target_messagetype = target_messagetype
        self.target_fieldname = target_fieldname
        
        
    def set_src_messagetype(self, src_messagetype: MessageType) -> None:
        self.src_messagetype = src_messagetype
    
    def get_src_messagetype(self) -> 'MessageType':
        return self.src_messagetype
    
    def set_src_fieldname(self, src_fieldname: str) -> None:
        self.src_fieldname = src_fieldname
    
    def get_src_fieldname(self) -> str:
        return self.src_fieldname
    
    def set_target_messagetype(self, target_messagetype: MessageType) -> None:
        self.target_messagetype = target_messagetype
    
    def get_target_messagetype(self) -> 'MessageType':
        return self.target_messagetype
    
    def set_target_fieldname(self, target_fieldname: str) -> None:
        self.target_fieldname = target_fieldname
    
    def get_target_fieldname(self) -> str:
        return self.target_fieldname
    
    

class FieldLengthDependency():
    
    def __init__(self, src_fieldname: str, target_fieldname: str):
        self.src_fieldname = src_fieldname
        self.target_fieldname = target_fieldname
        
    def set_src_fieldname(self, src_fieldname: str) -> None:
        self.src_fieldname = src_fieldname
    
    def get_src_fieldname(self) -> str:
        return self.src_fieldname
    
    def set_target_fieldname(self, target_fieldname: str) -> None:
        self.target_fieldname = target_fieldname
    
    def get_target_fieldname(self) -> str:
        return self.target_fieldname
    
    
    
class PacketLengthDependency():
    
    def __init__(self, packetname: str, fieldname: str):
        self.packetname = packetname
        self.fieldname = fieldname
        
    def set_src_packetname(self, packetname: str) -> None:
        self.packetname = packetname
    
    def get_packetname(self) -> str:
        return self.packetname
    
    def set_fieldname(self, fieldname: str) -> None:
        self.fieldname = fieldname
    
    def get_fieldname(self) -> str:
        return self.fieldname
    
    
    
class Checksum():
    
    def __init__(self, packetname: str, fieldname: str):
        self.packetname = packetname
        self.fieldname = fieldname
        
    def set_src_packetname(self, packetname: str) -> None:
        self.packetname = packetname
    
    def get_packetname(self) -> str:
        return self.packetname
    
    def set_fieldname(self, fieldname: str) -> None:
        self.fieldname = fieldname
    
    def get_fieldname(self) -> str:
        return self.fieldname