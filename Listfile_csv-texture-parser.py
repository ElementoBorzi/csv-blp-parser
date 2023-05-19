import csv

def contar_linhas(arquivo_csv):
    with open(arquivo_csv, "r", encoding="utf-8") as csv_file:
        return sum(1 for _ in csv_file) - 1

def extrair_texturas(arquivo_csv, arquivo_txt):
    total_linhas = contar_linhas(arquivo_csv)
    linha_atual = 0

    with open(arquivo_csv, "r", encoding="utf-8") as csv_file:
        with open(arquivo_txt, "w", encoding="utf-8") as txt_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                texture_1 = row["TextureName_1"].strip()
                texture_2 = row["TextureName_2"].strip()
                texture_3 = row["TextureName_3"].strip()

                if texture_1:
                    txt_file.write(texture_1 + "\n")
                if texture_2:
                    txt_file.write(texture_2 + "\n")
                if texture_3:
                    txt_file.write(texture_3 + "\n")

                linha_atual += 1
                porcentagem_concluida = (linha_atual / total_linhas) * 100
                print(f"Progress {texture_1} ... {porcentagem_concluida:.2f}% finished")

    print("All lines where correct extracted!")
    print(r'''
███████╗██╗░░░░░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░░░░░░░██████╗░░█████╗░██████╗░███████╗██╗
██╔════╝██║░░░░░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗╚════██║██║
█████╗░░██║░░░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║█████╗██████╦╝██║░░██║██████╔╝░░███╔═╝██║
██╔══╝░░██║░░░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║╚════╝██╔══██╗██║░░██║██╔══██╗██╔══╝░░██║
███████╗███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝░░░░░░██████╦╝╚█████╔╝██║░░██║███████╗██║
╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝                                          \/       
''')

arquivo_csv = r"C:\wow335\CharSections.csv"
arquivo_txt = r"C:\wow335\Listfile2.txt"

extrair_texturas(arquivo_csv, arquivo_txt)

print("\nPress Enter to close...")
