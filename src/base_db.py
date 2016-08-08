import         json as js


class JsonDB(object):
    def __init__(self,file):
        self.file = file
        
        pass
    def prepare(self):
        f = open(self.file)
        json_data = js.loads(f.read())
        self.dict = json_data[0]
        f.close()
        return 
    def get_db_dict(self):
        return self.dict
        pass
    def get_objn(self,number):

        pass
    #for un-numbered return the full chunk
    def get_obj(self):
        pass
