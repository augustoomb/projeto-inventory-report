from datetime import datetime, date
from collections import Counter


# https://stackoverflow.com/questions/6252280/find-the-most-frequent-number-in-a-numpy-array


class SimpleReport:
    @classmethod
    def get_oldest_date(cls, arr):
        return min(arr)

    @classmethod
    def get_newer_date(cls, arr):
        if len(arr) > 0:
            return min(arr)

    @classmethod
    def count_products(cls, arr):
        count = Counter(arr)
        return count.most_common(1)[0][0]

    @classmethod
    def mount_report(cls, arr_data_fab, arr_data_validade, arr_donas_produtos):

        return (
            f"Data de fabricação mais antiga: "
            f"{cls.get_oldest_date(arr_data_fab)}\n"
            f"Data de validade mais próxima: "
            f"{cls.get_newer_date(arr_data_validade)}\n"
            f"Empresa com mais produtos: "
            f"{cls.count_products(arr_donas_produtos)}"
        )

    @classmethod
    def convert_string_to_date(cls, str):
        return datetime.strptime(str, "%Y-%m-%d").date()

    @classmethod
    def generate(cls, list_dict_products):
        arr_data_fabricacao = []
        arr_data_validade = []
        arr_donas_produtos = []

        for product in list_dict_products:
            data_fabricacao_convertida = cls.convert_string_to_date(
                product["data_de_fabricacao"]
            )
            arr_data_fabricacao.append(data_fabricacao_convertida)

            data_validade_convertida = cls.convert_string_to_date(
                product["data_de_validade"]
            )

            if data_validade_convertida >= date.today():
                arr_data_validade.append(data_validade_convertida)

            arr_donas_produtos.append(product["nome_da_empresa"])

        return cls.mount_report(
            arr_data_fabricacao, arr_data_validade, arr_donas_produtos
        )


# print(
#     SimpleReport.generate(
#         [
#             {
#                 "id": 1,
#                 "nome_do_produto": "CADEIRA",
#                 "nome_da_empresa": "Forces of Nature",
#                 "data_de_fabricacao": "2022-04-04",
#                 "data_de_validade": "2023-02-09",
#                 "numero_de_serie": "FR48",
#                 "instrucoes_de_armazenamento": "Conservar em local fresco",
#             },
#             {
#                 "id": 2,
#                 "nome_do_produto": "MESA",
#                 "nome_da_empresa": "Forces of Nature",
#                 "data_de_fabricacao": "2010-04-04",
#                 "data_de_validade": "2021-01-08",
#                 "numero_de_serie": "GR98",
#                 "instrucoes_de_armazenamento": "Instrução 2",
#             },
#             {
#                 "id": 3,
#                 "nome_do_produto": "GELADEIRA",
#                 "nome_da_empresa": "Brastemp",
#                 "data_de_fabricacao": "2021-01-04",
#                 "data_de_validade": "2026-09-03",
#                 "numero_de_serie": "HG97",
#                 "instrucoes_de_armazenamento": "Conservar em local fresco",
#             },
#             {
#                 "id": 4,
#                 "nome_do_produto": "SOFA",
#                 "nome_da_empresa": "Fábrica de Sofas 123",
#                 "data_de_fabricacao": "2020-10-09",
#                 "data_de_validade": "2025-02-09",
#                 "numero_de_serie": "BC55",
#                 "instrucoes_de_armazenamento": "Conservar em local fresco",
#             },
#         ]
#     )
# )
