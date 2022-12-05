from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self,codigoAlu,nomeAlu,matriculaAlu,semestre):
        super().__init__(codigoAlu,nomeAlu,matriculaAlu)
        self.semestre = semestre
        print("Aluno Curso Superior Cadastrado!")

    def imprimirSemestre(self):
        print("Semestre: ",self.semestre)
