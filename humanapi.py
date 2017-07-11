import requests # pip install requests

VERSION = 'v1'
END_POINT = 'https://api.humanapi.co/'+VERSION+'/human/'
ACCESS_TOKEN = 'demo'

medical_items = {'allergies':'allergies', 
                    'encounters':'encounters', 
                    'functional_statuses':'functional_statuses', 
                    'immunizations':'immunizations',
                    'instructions':'instructions',
                    'medications':'medications',
                    'narratives':'narratives',
                    'organizations':'organizations',
                    'plans_of_care':'plans_of_care',
                    'issues':'issues',
                    'procedures':'procedures',
                    'profile':'profile',
                    'test_results':'test_results',
                    'timeline':'timeline',
                    'vitals':'vitals',
                    'ccds':'ccds'}

def get_medical_item(entity, id=None):
    enpoint = END_POINT + 'medical/' + entity
    payload = {'access_token' : ACCESS_TOKEN}
    
    if id != None:
        payload.id = id
      
    try:
        r = requests.get(enpoint, params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print 'error: ', e
        return None 
      
    return r.json()
    
def allergies(id=None):
    return get_medical_item(medical_items['allergies'], id)

def encounters(id=None):
    return get_medical_item(medical_items['encounters'], id)

def functional_statuses(id=None):
    return get_medical_item(medical_items['functional_statuses'], id)

def immunizations(id=None):
    return get_medical_item(medical_items['immunizations'], id)

def instructions(id=None):
    return get_medical_item(medical_items['instructions'], id)

def medications(id=None):
    return get_medical_item(medical_items['medications'], id)


def narratives(id=None):
    return get_medical_item(medical_items['narratives'], id)

def organizations(id):
    return get_medical_item(medical_items['organizations'], id)


def plans_of_care(id=None):
    return get_medical_item(medical_items['plans_of_care'], id)


def issues(id=None):
    return get_medical_item(medical_items['issues'], id)


def procedures(id=None):
    return get_medical_item(medical_items['procedures'], id)


def profile(id=None):
    return get_medical_item(medical_items['profile'], id)


def test_results(id=None):
    return get_medical_item(medical_items['test_results'], id)


def timeline(id=None):
    return get_medical_item(medical_items['timeline'], id)


def vitals(id=None):
    return get_medical_item(medical_items['vitals'], id)


def ccds(id=None):
    return get_medical_item(medical_items['ccds'], id)
