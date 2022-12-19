from inventory_report.importer.importer import Importer
import os
import json


class JsonImporter(Importer):
    @classmethod
    def get_extension(cls, path):
        file_name, file_extension = os.path.splitext(path)
        return file_extension

    @classmethod
    def get_data_in_json(cls, path):
        with open(path) as file:
            data = file.read()
            return json.loads(data)

    @classmethod
    def import_data(cls, path):
        if cls.get_extension(path) != ".json":
            raise ValueError("Arquivo inválido")

        return cls.get_data_in_json(path)


# try:
#     print(JsonImporter.import_data("inventory_report/data/inventory.txt"))
# except ValueError as err:
#     print(err)
