class Encounter(object):
    
    def __init__(self, id='', source='', updated_at='', created_at=''):
        self.id = id
        self.source = source
        self.updated_at = updated_at
        self.created_at = created_at
    
    @staticmethod
    def from_json(encounter_json):
        encounter = Encounter()