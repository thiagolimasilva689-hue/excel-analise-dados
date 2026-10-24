class Campeonato:
    def _init_(self, nome: str):
        self.nome = nome
        self.times = []
        self.jogos = []

        
class Time:
    def _init_(self, nome: str):
        self.nome = nome
        self.jogos = 0 ## tente retirar este atributo
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        
    @property
    def saldo_de_gols(self):
        return self.gols_marcados - self.gols_sofridos
    
    @property
    def pontos(self):
        return self.vitorias * 3 + self.empates
    

class Jogo:
    def _init_(
        self, 
        time_casa: str, 
        gols_casa: int, 
        time_visitante: str, 
        gols_visitante: int
    ):
        pass


def main():
    with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            print(linha)


if __name__ == "__main__":
    main()