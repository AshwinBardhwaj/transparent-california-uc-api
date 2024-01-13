from collections import OrderedDict
import itertools

class Person:
    id_iter = itertools.count()
    
    def __init__(self, json: dict):
        self.id = next(self.id_iter)
        values = OrderedDict()
        values["ID"] = self.id
        info = self.retrieve_person_from_json(json, values)
        self.info = info
    
    def retrieve_person_from_json(self, json, values):
        values['Name'] = json['td'][0]['a'][0]['_value']
        values["Job Tile"] = json['td'][1]['a'][0]['_value']
        values["Regular Pay"] = json['td'][2]['_value']
        values["Overtime Pay"] = json['td'][3]['_value']
        values["Other Pay"] = json['td'][4]['_value']
        values["Total Pay"] = json['td'][5]['_value']
        values["Benefits"] = json['td'][6]['_value']
        values["Total Pay and Benefits"] = json['td'][7]['_value']
        return values
    
    
    def __str__(self):
        return str(tuple(self.info.values()))
        