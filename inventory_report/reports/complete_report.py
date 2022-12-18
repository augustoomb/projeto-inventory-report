from simple_report import SimpleReport

# from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    # retorna o relatório simples (sem quantidade de produtos por empresa)
    @staticmethod
    def get_simple_report(list_dic_products):
        simple_report = SimpleReport.generate(list_dic_products)
        return simple_report

    # retorna uma lista com todas as empresas (com repetição)
    @staticmethod
    def get_all_companies(list_dic_products):
        list_companies = []

        for prod in list_dic_products:
            list_companies.append(prod["nome_da_empresa"])

        return list_companies

    # retorna a relação de empresa => quantidade de produtos
    @staticmethod
    def get_products_by_company(list_dic_products):

        companies = CompleteReport.get_all_companies(list_dic_products)

        product_by_company = dict(Counter(companies))

        #         >>> for key, value in a_dict.items():
        # ...     print(key, '->', value)

        str_return = "Produtos estocados por empresa:\n"

        for key, value in product_by_company.items():
            str_return += f"- {key}: {value}\n"

        return str_return

        # return (
        #     f"Produtos estocados por empresa: \n"
        #     f"{product_by_company['Forces of Nature']}\n"
        #     f"- {}\n"
        #     f"Produtos estocados por empresa: "
        # )

        # return product_by_company

    @staticmethod
    def generate(list_dic_products):
        s_report = CompleteReport.get_simple_report(list_dic_products)
        prods_by_company = CompleteReport.get_products_by_company(
            list_dic_products
        )

        print(s_report)
        print(prods_by_company)


dados = [
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
        "nome_da_empresa": "Fábrica de Sofas",
        "data_de_fabricacao": "2020-10-09",
        "data_de_validade": "2025-02-09",
        "numero_de_serie": "BC55",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]

CompleteReport.generate(dados)
