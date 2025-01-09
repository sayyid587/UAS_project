class Process:
    def __init__(self):
        self.data_list = []

    def add_data(self, data):
        if data.validate_nim() and data.validate_nama():
            self.data_list.append(data)
        else:
            print("Input tidak valid. Nim harus berupa angka dan Nama harus berupa huruf.")

    def get_data_list(self):
        return self.data_list