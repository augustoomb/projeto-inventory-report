import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        with open(path, encoding="utf-8") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')

            list_dict = []

            for item in content:
                list_dict.append(item)

            if type_report == "simples":
                return SimpleReport.generate(list_dict)

            # if type_report == "completo":
            else:
                return CompleteReport.generate(list_dict)


# Inventory.import_data("inventory_report/data/inventory.csv", "simples")
