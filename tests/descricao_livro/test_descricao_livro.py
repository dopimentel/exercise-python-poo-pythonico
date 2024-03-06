from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1000)
    assert (
        repr(livro)
        == "O livro O Senhor dos Anéis de J.R.R. Tolkien possui 1000 páginas."
    )
