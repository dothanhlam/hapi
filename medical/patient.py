class Patient(object):
    
    def __init__(self, name=''):
        self.name = name
    
    @staticmethod
    def from_json(patient_json):
        patient = Patient(patient_json['name'])
        return patient