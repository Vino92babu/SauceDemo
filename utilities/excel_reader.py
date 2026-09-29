import openpyxl


class ExcelReader:

    def __init__(self, file_path):

        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    def get_data(self):

        data = []

        for row in self.sheet.iter_rows(
            min_row=2,
            values_only=True
        ):
            data.append(row)

        return data