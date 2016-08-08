# Each Pada has an owner. 
# Owner =0 means Granthawli
# Owner =1 means SGGS and Granthawli
# Owner =2 means only SGGS, those padas which are published in parshisht

class PoemObject(object):
    def __init__(self,number):
        pass
    def prepare(self):
        self.owner         = 0
        self.number        = 1
        self.text          = u""
        self.lines         = 0
    def has_text(self,word):
        pass
    def get_line_containing(self,word):
        pass
    def checknumber(self,text):
        tlist = text.split(u"?")
        if tlist.__len__() > 1:     
            n1 = tlist[-2]
            if tlist.__len__() > 2:
		         n2 =  tlist[-3]
		         if n2.isnumeric():
			         return n2
            if n1.isnumeric():
                return n1
    def has_text(self,word):
        self.wordlist = self.text.split()
        if word in self.wordlist:
            return True
        else:
            return False
        
    def get_line_containing(self,word):
        if self.has_text(word):
            sentences = self.text.split("\n")
            for sentence in sentences:
                if word in sentence:
                    return sentence
        
    def __unicode__(self):
        return self.text
