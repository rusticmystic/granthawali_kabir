from poetry import PoemObject 

class Pada(PoemObject):
    def __init__(self,number):
        pass
    def prepare(self):
        super(Pada,self).prepare()
        self.raga          = u""
        self.raga_sggs     = u""
        self.text1         = ""

class Ramaini(PoemObject):
    pass

class Sakhi(PoemObject):
    def __init__(self,number):
        pass
    def prepare(self):
        super(Sakhi,self).prepare()
        self.name          = u""
        self.group         = u""
        self.text1         = ""

    pass

