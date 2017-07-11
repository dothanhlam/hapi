class Organization(object):
    
    def __init__(self, id='', name='', href=''):
        self.id = id
        self.name = name
        self.href = href
        
    @staticmethod
    def from_json(organization_json):
        organization = Organization(organization_json['id'], organization_json['name'], organization_json['href'])
        return organization