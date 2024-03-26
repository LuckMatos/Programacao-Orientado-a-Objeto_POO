class Professor():
    def __init__(self,componente, salario, formacao):
        self.componente = componente
        self.salario = salario
        self.formacao = formacao
        self.aula = None
    
    
    def atribuir_aula(self, aula):
        self.aula = aula
    
        return self.aula  
    
    def lancar_nota(self, nota):
        self.nota = nota
        return self.nota  
    
    