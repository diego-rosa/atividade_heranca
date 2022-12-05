from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self,codigoAluno,nomeAluno,matriculaAluno,ano):
        super().__init__(codigoAluno,nomeAluno,matriculaAluno)
        self.ano = ano
        print("Aluno ensino médio Cadastrado!")

    def imprimirAno(self):
        print("Ano: ",self.ano)
