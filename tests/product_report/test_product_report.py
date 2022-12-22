from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product_ok():
    return {
        "id": 10,
        "nome_do_produto": "farinha",
        "nome_da_empresa": "Farinini",
        "data_de_fabricacao": "01-05-2021",
        "data_de_validade": "02-06-2023",
        "numero_de_serie": "58451491",
        "instrucoes_de_armazenamento": "ao abrigo de luz",
    }


@pytest.fixture
def result_ok():
    return (
        "O produto farinha fabricado em 01-05-2021 por Farinini com "
        "validade até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    )


def test_relatorio_produto(product_ok, result_ok):

    product = Product(
        product_ok["id"],
        product_ok["nome_do_produto"],
        product_ok["nome_da_empresa"],
        product_ok["data_de_fabricacao"],
        product_ok["data_de_validade"],
        product_ok["numero_de_serie"],
        product_ok["instrucoes_de_armazenamento"],
    )

    assert repr(product) == result_ok


# https://stackoverflow.com/questions/32569732/correct-way-of-unit-testing-repr-with-dict
