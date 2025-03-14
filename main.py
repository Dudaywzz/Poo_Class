from pessoa import Pessoa
from bebe import Bebe



p1 = Pessoa("Pedro", "25/01/2010","DF123")
p2 = Pessoa("Amanda", "26/12/1987","DF222")
p3 = Pessoa("Felipe", "26/12/1987","DF222", estudando=False,trabalhando=True)
p4 = Pessoa("Andre", "26/12/1987","DF222")
b1 = Bebe("Pedro Neto Junior", "25/01/2010","DF123")
b2 = Bebe("Ana B", "26/12/1987","DF222")
b3 = Bebe("Felino  Mleo", "26/12/1987","DF222", estudando=False,trabalhando=True)
b4 = Bebe("Adriando", "26/12/1987","DF222")
b6 = Bebe("JM","22/10/2024","KJH090")

def main():
    print(b6.is_trabalhando())
    print(b1.get_nome())
    print(b6.is_trabalhando())

# o IF garante que o programa seja executado apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()