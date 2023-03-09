#Crear un modelo general que permita la interaccion con la base de datos de una forma ordenada y limpia

class DAO: 
    def __init__(self, model): 
        self.model = model

    def get_all(self): 
        return self.model.objects.all()
    
    def get_by_id(self, pk): 
        return self.model.objects.filter(id = pk).first()
    
