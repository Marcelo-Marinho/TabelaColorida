import pandas as eu_tbm_escolho_o_urso
from termcolor import colored

#pegar arquivo
print(colored("Dados coloridos :3", "blue"))
tabelita = input("Coloque o caminho da sua tabela (csv ou xlsx):\n> ")

infos = tabelita.split(".")
extensaoExtensa = infos[len(infos)-1]

#----
def transformar_em_ascii(tbl):
    maioral = 0
    linhas = len(tbl)
    colunas = len(tbl.columns)
    
    tabela_final = ""
    
    for y in range(0, linhas):
        for x in range(0, colunas):
            tamanhozito = len(str(tbl.iloc[y, x]))
            if tamanhozito > maioral:
                maioral = tamanhozito
    
    tabela_final = tabela_final + "\033[0m\n╬" + ((("═" * maioral) + "═╬") * colunas) + "\n║"
    for y in range(0, linhas):
        for x in range(0, colunas):
            tamanhozito = len(str(tbl.iloc[y, x]))
            quantd_espacos = maioral - tamanhozito
            tabela_final = tabela_final + ("\033[38;2;" + str(int((256/linhas) * (linhas - y)))) + ";" + str(int((256/colunas) * x)) + ";" + str(int((256/linhas) * y)) + "m" + str(tbl.iloc[y, x]) + "\033[0m" + (" " * quantd_espacos) +" ║"
        tabela_final = tabela_final + "\n╬" + ((("═" * maioral) + "═╬") * colunas) + "\n║"
    
    tabela_final = tabela_final[0:-1]
    return tabela_final

#verificar formato
if extensaoExtensa == "csv":
    LerTabelita = eu_tbm_escolho_o_urso.read_csv(tabelita, sep=';')
    print(transformar_em_ascii(LerTabelita))
    
elif extensaoExtensa == "xlsx":
    LerTabelita = eu_tbm_escolho_o_urso.read_excel(tabelita)
    print(transformar_em_ascii(LerTabelita))
    
else:
    try:
        print(colored("Tentando ler " + str(tabelita + ".csv"), "green"))
        LerTabelita = eu_tbm_escolho_o_urso.read_csv(str(tabelita + ".csv"), sep=";")
        print(transformar_em_ascii(LerTabelita))
    except:
        print(colored("Um erro ocorreu ao tentar ler sua tabela", "red"))