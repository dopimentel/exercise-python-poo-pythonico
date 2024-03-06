from src.livro.livro import Livro


def test_cria_livro(livro):
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1000)
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == "J.R.R. Tolkien"
    assert livro.paginas == 1000