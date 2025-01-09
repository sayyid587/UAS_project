class View:
    def display_table(self, data):
        print("\ndata mahasiswa")
        print("+----+------------+-----------------------------+")
        print("| No |    Nim     |             Nama            |")
        print("+----+------------+-----------------------------+")
        for i, value in enumerate(data, 1):
            print(f"| {i:2} | {value.nim:<10} | {value.nama:<27} |")
        print("+----+------------+-----------------------------+")