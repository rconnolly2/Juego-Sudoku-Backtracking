# Singleton básicamente en un patron de diseño creacional que obliga solo poder tener un solo objeto
# mientras da solo un punto de acceso global https://refactoring.guru/design-patterns/singleton
# Resuelve dos problemas:
# Obliga que solo se puede crear un objeto, y porque queremos esto?: Por ejemplo para acceder un recurso
# como una base de datos o un archivo de texto para no crear conflictos.
#
# Da un punto de acceso global a los atributos del objeto, pero protege de ser sobrescrita por otros programas.
def singleton(cls):
    instances = {}  #Diccionario para almacenar los objetos únicos

    def return_objeto(*args, **kwargs):
        if not (cls in instances):
            instances[cls] = cls(*args, **kwargs) 
        return instances[cls]  #Si ya existe devuelve el mismo objeto

    return return_objeto

# Ejemplo:
@singleton
class Usuario:
    def __init__(self):
        self.estado_login = False

def hola():
    print("hola")