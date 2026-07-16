import streamlit as st
import os
import sqlite3
from pathlib import Path

# ALGUMAS OPC:
# ID INTEGER PRIMARY KEY AUTOINCREMENT,

# ------------------- ALGUMAS OPÇÕES:
# ORDENS = ORDER BY COLUNA ASC ou DESC

# dirname: PASTA ATUAL, basename: NOME ARQUIVO, abspath: PASTA ATUAL+NOME ARQUIVO ATUAL
Pasta_Projeto = os.path.dirname(__file__)
Pasta_Atual = Path(Pasta_Projeto).parent

# Conecta ao banco de dados com o caminho completo
dbase = sqlite3.connect('Base_Dados_Shopee.db', check_same_thread=False)
c = dbase.cursor()
# __________________________________________------------------------------>  A_CATEGORIAS


dbase.execute('''CREATE TABLE IF NOT EXISTS A_CATEGORIAS(
    ID_CAT TEXT PRIMARY KEY NOT NULL,
    TITULO TEXT,
    LINK TEXT,
    OUTROS TEXT)''')
# =======================================_ A_CATEGORIAS
def esc_A_CATEGORIAS(ID_CAT, TITULO, LINK, OUTROS):
    try:
        c.execute('''INSERT INTO A_CATEGORIAS (ID_CAT, TITULO, LINK, OUTROS)
                    VALUES (?,?,?,?)''',
                  (ID_CAT, TITULO, LINK, OUTROS))
        dbase.commit()
    except sqlite3.IntegrityError:
        pass

def ler_A_CAT_temp(ID):
    c.execute(
        F"SELECT TITULO, LINK FROM A_CATEGORIAS WHERE ID_CAT = '{ID}' ")
    result = c.fetchall()
    if result !=[]:
        return result[0][0], result[0][1]
    else:
        return ID,''

def ler_A_CAT(conn, ID, item_id=""):
    c.execute(
        F"SELECT TITULO, LINK FROM A_CATEGORIAS WHERE ID_CAT = '{ID}' ")
    result = c.fetchall()
    if result !=[]:
        if result[0][1] != '':
            return result[0][0], result[0][1]
        else:
            LINK = st.text_input(f'Link: {result[0][0]}', key=ID)
            if st.button(f'Cadastra: {ID}', key=int(ID) + 2):
                if LINK:
                    if 'https' in LINK:
                        Del_C_ONLINE(ID)
                        esc_A_CATEGORIAS(ID, result[0][0], LINK, 'OUTROS')
                        st.write('Cadastrando Categ...')
                    else:
                        st.error('link errado!')
            return None,None
    else:      
        TITULO = st.text_input(f'Nome: {ID}', key = f"txt_cat_{ID}_{item_id}")
        LINK = st.text_input(f'Link: {ID}', key = f"txt_link_{ID}_{item_id}")

        if st.button(f'Cadastra: {ID}', key = f"btn_cadastra_{ID}_{item_id}"):

            if TITULO and LINK:
                if 'https' in LINK:
                    esc_A_CATEGORIAS(ID, TITULO, LINK, 'OUTROS')
                    st.write('Cadastrando Categ...')
                else:
                    st.error('link errado!')

        return 'None','Vazio'



def Del_C_ONLINE(ID_CAT=''):
    if ID_CAT:
        c.execute("DELETE FROM A_CATEGORIAS WHERE ID_CAT = ?", (ID_CAT,))
        dbase.commit()
    else:
        c.execute(f"DELETE FROM C_ONLINE")
        dbase.commit()
    return True

# __________________________________________------------------------------>  B_TEMPORARIOS
dbase.execute('''CREATE TABLE IF NOT EXISTS B_TEMPORARIOS(
    ITEM_ID TEXT,
    SHOP_ID TEXT,
    TITULO TEXT,
    IMAGEM TEXT,
    LOJA TEXT,
    CAT_1 INTEGER,
    CAT_2 INTEGER,
    VALOR TEXT,
    COMITION TEXT,
    LINK TEXT,
    OUTROS TEXT)''')

def esc_B_TEMPORARIOS(ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK, OUTROS):
    c.execute(
        "INSERT INTO B_TEMPORARIOS (ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK, OUTROS) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK, OUTROS)
    )
    dbase.commit()


def ler_B_TEMPORARIOS():
    c.execute(
        F"SELECT * FROM B_TEMPORARIOS ")
    result = c.fetchall()
    return result

def Del_B_TEMPORARIOS():
    c.execute(f"DELETE FROM B_TEMPORARIOS")
    dbase.commit()



# __________________________________________------------------------------>  B_DADOS_AFILIADOS
dbase.execute('''CREATE TABLE IF NOT EXISTS B_DADOS_AFILIADOS(
    ITEM_ID TEXT,
    SHOP_ID TEXT,
    TITULO TEXT,
    IMAGEM TEXT,
    LOJA TEXT,
    CAT_1 INTEGER,
    CAT_2 INTEGER,
    VALOR TEXT,
    COMITION TEXT,
    LINK_ORIGINAL TEXT,
    LINK_PUBLICO TEXT,
    LINK_AFILIADO TEXT,
    LINK_CATEGORIA_1 TEXT,
    LINK_CATEGORIA_2 TEXT,
    CATEGORIAS TEXT,
    RAIO_X TEXT)''')

def esc_B_DADOS_AFILIADOS(ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK_ORIGINAL,LINK_PUBLICO,LINK_AFILIADO,LINK_CATEGORIA_1,LINK_CATEGORIA_2,CATEGORIAS, RAIO_X):
    c.execute(
        "INSERT INTO B_DADOS_AFILIADOS (ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK_ORIGINAL,LINK_PUBLICO,LINK_AFILIADO,LINK_CATEGORIA_1,LINK_CATEGORIA_2,CATEGORIAS, RAIO_X) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (ITEM_ID, SHOP_ID, TITULO, IMAGEM, LOJA, CAT_1, CAT_2, VALOR, COMITION, LINK_ORIGINAL,LINK_PUBLICO,LINK_AFILIADO,LINK_CATEGORIA_1,LINK_CATEGORIA_2,CATEGORIAS, RAIO_X)
    )
    dbase.commit()


def ler_B_DADOS_AFILIADOS(ITEM_ID=''):
    if ITEM_ID:
        c.execute(
            F"SELECT * FROM B_DADOS_AFILIADOS where ITEM_ID = '{ITEM_ID}' ")
        result = c.fetchall()
        return result
    else:
        c.execute(
            F"SELECT * FROM B_DADOS_AFILIADOS ")
        result = c.fetchall()
        return result