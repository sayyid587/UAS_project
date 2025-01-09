class Data:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def validate_nim(self):
        try:
            self.nim = int(self.nim)
            return True
        except (ValueError):
            return False

    def validate_nama(self):
        if self.nama.replace(" ", "").isalpha():
            return True
        return False

class View:
    def display_table(self, data):
        print("\ndata mahasiswa")
        print("+----+------------+-----------------------------+")
        print("| No |    Nim     |             Nama            |")
        print("+----+------------+-----------------------------+")
        for i, value in enumerate(data, 1):
            print(f"| {i:2} | {value.nim:<10} | {value.nama:<27} |")
        print("+----+------------+-----------------------------+")

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


if __name__ == "__main__":
    process = Process()
    view = View()

    while True:
        input_nim = input("Masukkan Nim (atau 'exit' untuk keluar): ")
        input_nama = input("Masukkan Nama : ")
        if input_nim.lower() == 'exit':
            break
        data = Data(input_nim, input_nama)
        process.add_data(data)

    view.display_table(process.get_data_list())
