from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

# FLUXO:
# simpleRep = SimpleReport()

# coloredRep = ColoredReport(simpleRep)
# print(coloredRep.generate(list_test))

# RESPOSTA
# Data de fabricação mais antiga: 2010-04-04
# Data de validade mais próxima: 2023-02-09
# Empresa com mais produtos: Forces of Nature


def test_decorar_relatorio():

    list_test = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 2,
            "nome_do_produto": "MESA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2010-04-04",
            "data_de_validade": "2021-01-08",
            "numero_de_serie": "GR98",
            "instrucoes_de_armazenamento": "Instrução 2",
        },
        {
            "id": 3,
            "nome_do_produto": "GELADEIRA",
            "nome_da_empresa": "Brastemp",
            "data_de_fabricacao": "2021-01-04",
            "data_de_validade": "2026-09-03",
            "numero_de_serie": "HG97",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 4,
            "nome_do_produto": "SOFA",
            "nome_da_empresa": "Fábrica de Sofas 123",
            "data_de_fabricacao": "2020-10-09",
            "data_de_validade": "2025-02-09",
            "numero_de_serie": "BC55",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
    ]

    green_words = [
        "\033[32mData de fabricação mais antiga:\033[0m ",
        "\033[32mData de validade mais próxima:\033[0m ",
        "\033[32mEmpresa com mais produtos:\033[0m ",
    ]

    content = [
        "\033[36m2010-04-04\033[0m",
        "\033[36m2023-02-09\033[0m",
        "\033[31mForces of Nature\033[0m",
    ]

    simpleRep = SimpleReport()
    coloredRep = ColoredReport(simpleRep)
    str_report = coloredRep.generate(list_test)

    split_report = str_report.split("\n")

    for index, item in enumerate(green_words):
        assert split_report[index] == green_words[index] + content[index]
        # print("aqui")
        # print(content[index])
        # print("fim aqui")
