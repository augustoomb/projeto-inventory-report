from inventory_report.importer.importer import Importer
import os
import csv


class CsvImporter(Importer):
    @classmethod
    def generate_list_with_data(cls, data):
        list_dict = []

        for item in data:
            list_dict.append(item)

        return list_dict

    @classmethod
    def get_extension(cls, path):
        file_name, file_extension = os.path.splitext(path)
        return file_extension

    @classmethod
    def get_data_in_csv(cls, path):
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return cls.generate_list_with_data(data)

    @classmethod
    def import_data(cls, path):
        if cls.get_extension(path) != ".csv":
            raise ValueError("Arquivo inválido")

        return cls.get_data_in_csv(path)


# try:
#     print(CsvImporter.import_data("inventory_report/data/inventory.txt"))
# except ValueError as err:
#     print(err)
