import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def product_ok():
    return {
        "id": 10,
        "nome_do_produto": "Chocolate",
        "nome_da_empresa": "Nestle",
        "data_de_fabricacao": "2022-10-10",
        "data_de_validade": "2023-11-11",
        "numero_de_serie": "58489491",
        "instrucoes_de_armazenamento": "Local fresco",
    }


def test_cria_produto(product_ok):

    prod = Product(
        product_ok["id"],
        product_ok["nome_do_produto"],
        product_ok["nome_da_empresa"],
        product_ok["data_de_fabricacao"],
        product_ok["data_de_validade"],
        product_ok["numero_de_serie"],
        product_ok["instrucoes_de_armazenamento"],
    )

    # assert type(prod.id) is int
    assert product_ok["id"] == prod.id

    # assert type(prod.nome_do_produto) is str
    assert product_ok["nome_do_produto"] == prod.nome_do_produto

    # assert type(prod.nome_da_empresa) is str
    assert product_ok["nome_da_empresa"] == prod.nome_da_empresa

    # assert type(prod.data_de_fabricacao) is str
    assert product_ok["data_de_fabricacao"] == prod.data_de_fabricacao

    # assert type(prod.data_de_validade) is str
    assert product_ok["data_de_validade"] == prod.data_de_validade

    # assert type(prod.numero_de_serie) is str
    assert product_ok["numero_de_serie"] == prod.numero_de_serie

    # assert type(prod.instrucoes_de_armazenamento) is str
    assert (
        product_ok["instrucoes_de_armazenamento"]
        == prod.instrucoes_de_armazenamento
    )
