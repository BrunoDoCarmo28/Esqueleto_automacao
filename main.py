# o objetivo aqui é aprender automação pra tudo
# sempre que ficar na duvida pense: como eu resolveria isso no manual, e anotar.

# 1 - entrar no site da empresa
# 2 - logar no site
# 3 - abrir a lista/base para saber o que cadastrar
# 4 - cadastrar um produto
# 5 - repetir o passo 4 até acabar

import time
import pyautogui
import pandas as pd

# 1 - entrar no site da empresa

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "youtube.com"
pyautogui.write(link)
pyautogui.press("enter")

# ter uma pausa maior pro site carregar
time.sleep(20)

# 2 - logar no site

pyautogui.click(20, 700)  # posição x e y
pyautogui.write("inserir o login aqui")

pyautogui.press("tab")
pyautogui.write("inserir a senha aqui")
pyautogui.press("enter")

time.sleep(5)

# 3 - abrir a lista/base para saber o que cadastrar

tabela = pd.read_csv("produtos.csv")
print(tabela)

# 4 - cadastrar os produtos

for linha in tabela.index:

    pyautogui.click(20, 40)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if pd.notna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("tab")

    pyautogui.press("enter")

    # voltar para o início do formulário
    pyautogui.scroll(6000)
