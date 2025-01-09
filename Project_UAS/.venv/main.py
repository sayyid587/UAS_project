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