
class Button():
    #constructor
    def __init__(self,labelText,status,value):
        self.labelText = labelText
        self.status = status
        self.value = value

    def getStatus(self):
        return self.status
    def getValue(self):
        return self.value    
    def getLabelText(self):
        return self.labelText
    def flipStatus(self):
       self.status = not self.status