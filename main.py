from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

aluno1 = AlunoEnsinoMedio(1,"Diego","12345",8)
aluno1.imprimir()
aluno1.imprimirAno()

print("----------------------------")

aluno2 = AlunoGraduacao(2,"Amanda","54321",6)
aluno2.imprimir()
aluno2.imprimirSemestre()
