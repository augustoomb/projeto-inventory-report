import csv
import json
import os
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def generate_list_with_data(cls, data):
        list_dict = []

        for item in data:
            list_dict.append(item)

        return list_dict

    @classmethod
    def get_data_in_csv(cls, path):
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return cls.generate_list_with_data(data)

    @classmethod
    def get_data_in_json(cls, path):
        with open(path) as file:
            data = file.read()
            return json.loads(data)

    @classmethod
    def get_data_in_xml(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @classmethod
    def get_extension(cls, path):
        file_name, file_extension = os.path.splitext(path)
        return file_extension

    @classmethod
    def get_data(cls, path):
        file_extension = cls.get_extension(path)

        if file_extension == ".csv":
            data = cls.get_data_in_csv(path)
            return data

        if file_extension == ".json":
            data = cls.get_data_in_json(path)
            return data

        if file_extension == ".xml":
            data = cls.get_data_in_xml(path)
            return data

    @classmethod
    def import_data(cls, path, type_report):

        content = cls.get_data(path)

        if type_report == "simples":
            return SimpleReport.generate(content)

        else:
            return CompleteReport.generate(content)


# Inventory.import_data("inventory_report/data/inventory.xml", "simples")


# referencias:
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# https://www.digitalocean.com/community/tutorials/get-file-extension-in-python
