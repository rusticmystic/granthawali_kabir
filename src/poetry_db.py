from base_db          import JsonDB
from poetrygranthavli import Pada,Sakhi

class PadaDb(JsonDB):
    def prepare(self):
        super(PadaDb,self).prepare()
        self.dict_pada = self.dict[u"pad"][0]
        
        #self.dict_raag = self.dict[self.dict.keys()[1]][0]
    def get_objn(self,number):
        if unicode(number) in self.dict_pada.keys():
            pada      = Pada(number)
            pada.prepare()
            text = self.dict_pada[unicode(number)]
            if text.__len__() == 1:
                pada.text = text[0]
            elif text.__len__() > 1:
                pada.text = text[0]
                pada.text1 = text[1]
            return pada
    def search(self, word):
        self.total_padas = 403
        found=[]
        for pada_num in range(1,403):
            pada = self.get_objn(pada_num)
            if pada.has_text(word):
                found.append(pada_num)
        return found
    pass

class SakhiDb(JsonDB):
    def prepare(self):
        super(SakhiDb,self).prepare()
        self.sakhi_pada_db     = self.dict[u"sakhi_db"][0]
        self.sakhi_sequence =  self.dict[u"seq"]
        
        #self.dict_raag = self.dict[self.dict.keys()[1]][0]
    def get_objn(self,number):
        pass
    def get_sakhi_pada(self,sakhi,number):
        if sakhi in self.sakhi_sequence:
            if unicode(number) in self.sakhi_pada_db[sakhi][0].keys():
                pada = Sakhi(number)
                pada.prepare()
                text = self.sakhi_pada_db[sakhi][0][unicode(number)]
                pada.text = text
                return pada
  
    pass
    def search(self,word):
        found=[]
        for sakhi_chapter in self.sakhi_sequence:
            sakhidb = self.sakhi_pada_db[sakhi_chapter][0]
            
            for sakhi in sakhidb.keys():
                sakhi_pad  = self.get_sakhi_pada(sakhi_chapter,int(sakhi))
                if sakhi_pad.has_text(word):
                    found.append([sakhi_chapter,sakhi])
        return found
        pass


class RamainiDb(JsonDB):
    pass

class PadaDbExtra(JsonDB):
    pass

class PadaSakhiExtra(JsonDB):
    pass