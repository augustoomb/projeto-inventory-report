from inventory_report.importer.importer import Importer
import os
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def get_extension(cls, path):
        file_name, file_extension = os.path.splitext(path)
        return file_extension

    @classmethod
    def get_data_in_xml(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @classmethod
    def import_data(cls, path):
        if cls.get_extension(path) != ".xml":
            raise ValueError("Arquivo inválido")

        return cls.get_data_in_xml(path)


# try:
#     print(XmlImporter.import_data("inventory_report/data/inventory.txt"))
# except ValueError as err:
#     print(err)
