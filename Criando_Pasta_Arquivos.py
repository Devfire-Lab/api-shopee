import os
import requests
from PIL import Image
from io import BytesIO
from pathlib import Path

def baixar_imagem_e_criar_pasta(url_imagem, titulo_pasta, texto_conteudo1,nome1,texto_conteudo2=''):
    # Detecta pasta de Downloads do usuário
    downloads = Path.home() / "Downloads"
    pasta_destino = downloads / titulo_pasta
    pasta_destino.mkdir(parents=True, exist_ok=True)

    # Baixa a imagem
    response = requests.get(url_imagem)
    if response.status_code != 200:
        print("Não foi possível baixar a imagem.")
        return

    img = Image.open(BytesIO(response.content))
    caminho_imagem = pasta_destino / "imagem_capa_principal.png"
    img.save(caminho_imagem)
    print(f"Imagem salva em: {caminho_imagem}")

    # Cria arquivo de texto
    caminho_txt = pasta_destino / f"{nome1}.txt"
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(texto_conteudo1)
    if texto_conteudo2:
        caminho_txt = pasta_destino / "Para Site.txt"
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(texto_conteudo2)
        print(f"Arquivo de texto salvo em: {caminho_txt}")

        print(f"Tudo pronto! Pasta criada em: {pasta_destino}")



def adicionar_arquivo_pasta(titulo_pasta, arquivo_url=None, texto=None, nome_arquivo=None):

    downloads = Path.home() / "Downloads"
    pasta_destino = downloads / titulo_pasta
    pasta_destino.mkdir(parents=True, exist_ok=True)

    if arquivo_url:
        response = requests.get(arquivo_url)
        if response.status_code != 200:
            print(f"Não foi possível baixar a imagem de {arquivo_url}")
        else:
            img = Image.open(BytesIO(response.content))
            nome_img = nome_arquivo if nome_arquivo else f"imagem_{len(list(pasta_destino.glob('*.png')))+1}"
            caminho_imagem = pasta_destino / f"{nome_img}.png"
            img.save(caminho_imagem)
            print(f"Imagem salva em: {caminho_imagem}")

    if texto:
        nome_txt = nome_arquivo if nome_arquivo else f"texto_{len(list(pasta_destino.glob('*.txt')))+1}"
        caminho_txt = pasta_destino / f"{nome_txt}.txt"
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Arquivo de texto salvo em: {caminho_txt}")

