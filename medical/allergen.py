# coding: utf-8
from code import Code
from organization import Organization
from patient import Patient
from datetime import datetime

class Allergen(object):
    
    def __init__(self, id='', source='',
                 updated_at='', created_at='',
                 name='', patient=None, organization=None,
                 reactions_full=[], allergen=None,
                 status='', severity='',
                 date_range=None, codes=None):
        self.id  = id  # String    The Id of the resource
        self.source = source    # String    The name of the originating service
        self.updated_at = updated_at   # Date    The time the record was updated on the Human API server
        self.created_at = created_at   # Date    The time the record was created on the Human API server
        self.name = name # String    The name of the allergy (e.g. ‘Etomidate’, 'Fluconazole’, 'Metaxalone’)
        self.patient = patient   # Object    Patient information (“name” and other optional attributes)
        self.organization = organization   # Object    Hospital information (See organizations)
        self.reactions_full = reactions_full  # Array[Object]    Reactions information (see below)
        self.allergen = allergen   # Object    Allergen information (see below)
        self.status = status   # String    The status of the allergy
        self.severity = severity   # String    The severity of the allergy
        self.date_range = date_range   # Object    Date Range information (see below)
        self.codes = codes   # Object    See codes object
       
    @staticmethod 
    def from_json(allergen_json):
        codes = []
        for code in allergen_json['codes']:
            codes.append(Code.from_json(code))
        
        allergen = Allergen(allergen_json['id'], 
                            allergen_json['source'], 
                            allergen_json['updatedAt'],
                            allergen_json['createdAt'],
                            allergen_json['name'],
                            Patient.from_json(allergen_json['patient']) if bool(allergen_json.get('patient')) else None ,
                            Organization.from_json(allergen_json['organization']) if bool(allergen_json.get('organization')) else None,
                            [],
                            None,
                            '',
                            '',
                            '',
                            codes)
        return allergen
    
    def get_tabulate_header(self):
        return self.__dict__.keys()
    
    def get_tabulate_value(self):
        return self.__dict__.values()
                