class Pessoa:
    def __init__(self, nome, github, foto="https://icons.veryicon.com/png/o/miscellaneous/xdh-font-graphics-library/anonymous-user.png"):
        self.nome= nome
        self.github = github
        self.foto = foto

pessoas = {
    "cane" : Pessoa("Rodrigo Cane", "https://github.com/rodrigocane", "https://m.media-amazon.com/images/M/MV5BMTY4NTQzMDcxMl5BMl5BanBnXkFtZTcwNTEwNTYyMg@@._V1_.jpg"),
    "maria": Pessoa("Maria", "https://github.com/mariazinha", "https://i.pravatar.cc/300?img=47"),
    "anonimo": Pessoa("Anônimo", "https://github.com/anonimo"),
}