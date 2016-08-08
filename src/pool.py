from poetrygranthavli import Pada,Sakhi, Ramaini
from poetry_db import PadaDb,SakhiDb

class ResourcePool(object):
    def __init__(self):
        self.pada_json_file             = u""  
        self.sakhi_json_file            = u""
        self.ramaini_json_file          = u""
        self.pada_extra_json_file       = u""
        self.sakhi_extra_json           = u""
        self.db                         = {}
        pass
    def prepare(self):
        if(self.pada_json_file):
            pada_db         = PadaDb(self.pada_json_file)
            self.db["pada"] = pada_db
        if(self.sakhi_json_file):
            sakhi_db        = SakhiDb(self.sakhi_json_file)
            self.db["sakhi"] = sakhi_db
        pass
    def show_resource_list(self):
        return self.db.keys()
        pass
    def get_resource(self,res):
        if self.db.has_key(res):
            return self.db[res]
        pass
