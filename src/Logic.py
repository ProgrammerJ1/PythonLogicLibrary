import types
class Logic:
    @staticmethod
    def nand(self,inputone:bool,inputtwo:bool):
        return not(inputone and inputtwo)
    @staticmethod
    def converse(self,inputone:bool,inputtwo:bool):
        return inputone or (not inputtwo)
    @staticmethod
    def imply(self,inputone:bool,inputtwo:bool):
        return (not inputone) or inputtwo
    @staticmethod
    def Or(self,inputone:bool,inputtwo:bool):
        return inputone or inputtwo
    @staticmethod
    def Not(self,inputone:bool):
        return not inputone
    @staticmethod
    def xor(self,inputone:bool,inputtwo:bool):
        return not(inputone==inputtwo)
    @staticmethod
    def xnor(self,inputone:bool,inputtwo:bool):
        return inputone==inputtwo
    @staticmethod
    def nor(self,inputone:bool,inputtwo:bool):
        return not (inputone or inputtwo)
    @staticmethod
    def nimply(self,inputone:bool,inputtwo:bool):
        return inputone and (not inputtwo)
    @staticmethod
    def conversenimply(self,inputone:bool,inputtwo:bool):
        return (not inputone) and inputtwo
    @staticmethod
    def And(self,inputone:bool,inputtwo:bool):
        return inputone and inputtwo