class Code(object):
    
    def __init__(self, code='', code_system='', code_system_name='', name=''):
        self.code = code #    String    Medical code
        self.code_system  = code_system #   String    The identifier of the code system that the code belongs to
        self.code_system_name = code_system_name #  String    The name of the code system that the code belongs to
        self.name = name #  String    The name of the code
    
    @staticmethod
    def from_json(code_json):
        code = Code(code_json['code'], code_json['codeSystem'], code_json['codeSystemName'], code_json['name'])
        return code