from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import re

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

    # str_retorno = (
    # "Data de fabricação mais antiga: 2010-04-04\n"
    # "Data de validade mais próxima: 2023-02-09\n"
    # "Empresa com mais produtos: Forces of Nature"
    # )
    # datas = re.findall(r"(\d+-\d+-\d+)", str_retorno)

    # print(datas)

    # executando...
    simpleRep = SimpleReport()
    coloredRep = ColoredReport(simpleRep)
    str_report = coloredRep.generate(list_test)

    # frases verdes que a string deve conter
    green_phrases = [
        "Data de fabricação mais antiga:",
        "Data de validade mais próxima:",
        "Empresa com mais produtos:",
    ]

    # checando se as frases acima estão na string devolvida (e se são verdes)
    for phrase in green_phrases:
        assert f"\033[32m{phrase}\033[0m" in str_report

    # pegar as datas da string
    arr_dates = re.findall(r"(\d+-\d+-\d+)", str_report)

    # checando se as datas são azuis
    for item_date in arr_dates:
        assert f"\033[36m{item_date}\033[0m" in str_report

    # my_string="hello python world , i'm a beginner"
    # print(my_string.split("world",1)[1])
    # SAÍDA: , i'm a beginner

    # pegando nome da empresa:
    company = str_report.split("produtos:", 1)[1]

    # checando se nome da empresa está em vermelho
    assert f"\033[31m{company}\033[0m" in str_report

    # assert repr(coloredRep.generate(list_test))
