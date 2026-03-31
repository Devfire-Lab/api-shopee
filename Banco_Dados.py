import os
import sqlite3
from pathlib import Path
from time import sleep

# ALGUMAS OPC:
# ID INTEGER PRIMARY KEY AUTOINCREMENT,

# ------------------- ALGUMAS OPÇÕES:
# ORDENS = ORDER BY COLUNA ASC ou DESC

# dirname: PASTA ATUAL, basename: NOME ARQUIVO, abspath: PASTA ATUAL+NOME ARQUIVO ATUAL
Pasta_Projeto = os.path.dirname(__file__)
Pasta_Atual = Path(Pasta_Projeto).parent

# Conecta ao banco de dados com o caminho completo
dbase = sqlite3.connect('Base_Dados.db',timeout=5, check_same_thread=False)
c = dbase.cursor()
# __________________________________________------------------------------>  A_PROD_ENTRADA
dbase.execute('''CREATE TABLE IF NOT EXISTS A_PROD_ENTRADA(
    ID_PROD TEXT PRIMARY KEY NOT NULL,
    TITULO TEXT,
    DESCRITION TEXT,
    IMAGEM TEXT,
    LINK_ORIGINAL TEXT,
    LINK_AFILIADO TEXT,
    CATEGORIA_1 TEXT,
    CATEGORIA_2 TEXT,
    OUTROS TEXT)''')


# =======================================_ A_PROD_ENTRADA
def esc_A_PROD_ENTRADA(ID_PROD, TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2,
                       OUTROS):
    try:
        c.execute('''INSERT INTO A_PROD_ENTRADA (ID_PROD,TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2, OUTROS)
                VALUES (?,?,?,?,?,?,?,?,?)''',
              (ID_PROD, TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2, OUTROS))
        dbase.commit()

    except sqlite3.IntegrityError:
        return 'Ja estava cadastrado!'

    except sqlite3.OperationalError as e:
        if 'locked' in str(e).lower():
            sleep(1)
            return 'Banco ocupado, tentativa ignorada'
        raise

def ler_A_PROD_ENTRADA(ID='', COLUNA='', VALOR=''):
    if ID != '' and COLUNA != '' and VALOR != '':  # Retorna ITENS onde COLUNA igual ao ID_PROD expecific...
        c.execute(
            F"SELECT ID_PROD,TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2, OUTROS FROM A_PROD_ENTRADA WHERE {COLUNA} = {VALOR} AND ID_PROD = '{ID}' ")
        result = c.fetchall()
        return result
    if ID == '' and COLUNA != '' and VALOR == '':  # ler todas as colunas com esse nome..
        c.execute(F"SELECT {COLUNA} FROM A_PROD_ENTRADA ")
        result = c.fetchall()
        return result

    if ID != '' and COLUNA == '' and VALOR == '':  # ler todos os valores de um ID_PROD especifico....
        c.execute(
            F"SELECT ID_PROD,TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2, OUTROS FROM A_PROD_ENTRADA WHERE ID_PROD = '{ID}' ")
        result = c.fetchall()
        return result

    if ID != '' and COLUNA != '' and VALOR == '':  # ler todos os valores de um ID_PROD especifico....
        c.execute(F"SELECT {COLUNA} FROM A_PROD_ENTRADA  WHERE ID_PROD = '{ID}' ")
        result = c.fetchall()
        return result

    if ID == '' and COLUNA == '' and VALOR == '':  # ler toda a tabela..
        c.execute(
            F"SELECT ID_PROD,TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2, OUTROS FROM A_PROD_ENTRADA")
        result = c.fetchall()
        return result


def existe_em_A_PROD_ENTRADA(video_id):
    c.execute(
        "SELECT 1 FROM A_PROD_ENTRADA WHERE ID_PROD = ? LIMIT 1",
        (video_id,)
    )
    return c.fetchone() is not None


def ler_A_PROD_ENTRADA_colunas(COLUNA):  # ler APENAS uma coluna expecifica
    c.execute(F"SELECT ID_PROD, {COLUNA} FROM A_PROD_ENTRADA ")
    result = c.fetchall()
    return result


def se_A_PROD_ENTRADA(COLUNA, ID=''):  # se True ou False , vazio ou cheio
    if ID != '':  # se uma coluna com ID expecifico
        c.execute(F"SELECT * FROM A_PROD_ENTRADA WHERE {COLUNA} = ? AND ID_PROD = '{ID}' ", (COLUNA, {ID}))
        result = c.fetchall()
        if result == []:
            return True
        else:
            return False

    else:  # se todas essas COLUNAS for.....
        c.execute(F"SELECT * FROM A_PROD_ENTRADA WHERE {COLUNA} = ?", (COLUNA,))
        result = c.fetchall()
        if result == []:
            return True
        else:
            return False


def ATUAL_A_PROD_ENTRADA(ID, COLUNA, CONTEUDO, CONTEUDO2=''):
    if CONTEUDO2:  # Convertendo o conteúdo para string e adicionando ao valor do ID
        conteudo = CONTEUDO2 + CONTEUDO
        print('ATUAL_A_PROD_ENTRADA: ', conteudo)
        query = f''' UPDATE A_PROD_ENTRADA SET {COLUNA} =? WHERE ID_PROD = '{ID}' '''.format(COLUNA=COLUNA)
        c.execute(query, (conteudo,))
        dbase.commit()
    else:
        print('ATUAL_A_PROD_ENTRADA: ', CONTEUDO)
        query = f''' UPDATE A_PROD_ENTRADA SET {COLUNA} =? WHERE ID_PROD = '{ID}' '''.format(COLUNA=COLUNA)
        c.execute(query, (CONTEUDO,))
        dbase.commit()


def Del_A_PROD_ENTRADA(ID=''):
    if ID:
        c.execute(f"DELETE FROM A_PROD_ENTRADA WHERE ID_PROD = '{ID}' ")
        dbase.commit()
    else:
        c.execute(f"DELETE FROM A_PROD_ENTRADA")
        dbase.commit()


def DROP_A_PROD_ENTRADA():
    c.execute(f"DROP TABLE A_PROD_ENTRADA")
    dbase.commit()


# Criação da tabela
dbase.execute('''
CREATE TABLE IF NOT EXISTS A_PROD_SAIDA(
    ID_PROD TEXT NOT NULL,
    TITULO_PAG TEXT,
    TITULO_POST TEXT,
    INTRODUTION TEXT,
    DESCRITION TEXT,
    TITULO_DETALHES TEXT,
    DETALHES TEXT,
    TITULO_LISTA TEXT,
    LISTA TEXT,
    TITULO_FAQ TEXT,
    FAQ TEXT,
    LINK_SIT TEXT,
    LINK_AFILIADO TEXT,
    DESC_IMAGEM TEXT,
    CHAVES TEXT,
    CATEG1 TEXT,
    CATEG2 TEXT,
    OUTROS TEXT
)
''')

# =======================================_ A_PROD_SAIDA
def esc_A_PROD_SAIDA(ID_PROD, TITULO_PAG, TITULO_POST, INTRODUTION, DESCRITION, TITULO_DETALHES, DETALHES,
                     TITULO_LISTA, LISTA, TITULO_FAQ, FAQ, LINK_SIT, LINK_AFILIADO, DESC_IMAGEM, CHAVES, CATEG1, CATEG2, OUTROS):
    try:
        c.execute('''
            INSERT INTO A_PROD_SAIDA (
                ID_PROD, TITULO_PAG, TITULO_POST, INTRODUTION, DESCRITION, 
                TITULO_DETALHES, DETALHES, TITULO_LISTA, LISTA, TITULO_FAQ, FAQ, 
                LINK_SIT, LINK_AFILIADO, DESC_IMAGEM, CHAVES, CATEG1, CATEG2, OUTROS
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (ID_PROD, TITULO_PAG, TITULO_POST, INTRODUTION, DESCRITION,
              TITULO_DETALHES, DETALHES, TITULO_LISTA, LISTA, TITULO_FAQ, FAQ,
              LINK_SIT, LINK_AFILIADO, DESC_IMAGEM, CHAVES, CATEG1, CATEG2, OUTROS))
        dbase.commit()
    except sqlite3.IntegrityError:
        pass

def ler_A_PROD_SAIDA(ID):
    c.execute("SELECT TITULO_PAG, LINK_SIT FROM A_PROD_SAIDA WHERE ID_PROD = ?", (ID,))
    return c.fetchall()

def ler_A_PROD_SAID():
    c.execute("SELECT ID_PROD,TITULO_PAG, TITULO_PAG, LINK_SIT, CATEG1,CATEG2 FROM A_PROD_SAIDA")
    return c.fetchall()

def ler_A_PROD_SAIDA_colunas(COLUNA): # ler apenas uma coluna específica
    c.execute(f"SELECT ID_PROD, {COLUNA} FROM A_PROD_SAIDA")
    return c.fetchall()

def se_A_PROD_SAIDA(COLUNA, ID=''): # se True ou False, vazio ou cheio
    if ID:
        c.execute(f"SELECT * FROM A_PROD_SAIDA WHERE {COLUNA} IS NULL OR {COLUNA} = '' AND ID_PROD = ?", (ID,))
    else:
        c.execute(f"SELECT * FROM A_PROD_SAIDA WHERE {COLUNA} IS NULL OR {COLUNA} = ''")
    result = c.fetchall()
    return result == []

def ATUAL_A_PROD_SAIDA(ID, COLUNA, CONTEUDO, CONTEUDO2=''):
    conteudo_final = (CONTEUDO2 + CONTEUDO) if CONTEUDO2 else CONTEUDO
    c.execute(f"UPDATE A_PROD_SAIDA SET {COLUNA} = ? WHERE ID_PROD = ?", (conteudo_final, ID))
    dbase.commit()

def Del_A_PROD_SAIDA(ID=''):
    if ID:
        c.execute("DELETE FROM A_PROD_SAIDA WHERE ID_PROD = ?", (ID,))
    else:
        c.execute("DELETE FROM A_PROD_SAIDA")
    dbase.commit()

def DROP_A_PROD_SAIDA():
    c.execute("DROP TABLE IF EXISTS A_PROD_SAIDA")
    dbase.commit()


# __________________________________________------------------------------>  C_ONLINE
dbase.execute('''CREATE TABLE IF NOT EXISTS C_ONLINE(
    ID_PROD TEXT PRIMARY KEY NOT NULL,
    TITULO_ORIGINAL TEXT,
    TITULO_NOVO TEXT,
    LINK_PAGINA TEXT,
    CATGO_1 TEXT,
CATGO_2 TEXT)''')

# =======================================_ C_ONLINE
def esc_C_ONLINE(ID_PROD,TITULO_ORIGINAL, TITULO_NOVO, LINK_PAGINA, CATGO_1,CATGO_2):
    c.execute('''INSERT INTO C_ONLINE (ID_PROD,TITULO_ORIGINAL, TITULO_NOVO, LINK_PAGINA, CATGO_1,CATGO_2)
                VALUES (?,?,?,?,?,?)''',
              (ID_PROD,TITULO_ORIGINAL, TITULO_NOVO, LINK_PAGINA, CATGO_1,CATGO_2))
    dbase.commit()

def existe_em_C_ONLINE_BAIXADOS(video_id):
    c.execute(
        "SELECT 1 FROM C_ONLINE WHERE ID_PROD = ? LIMIT 1",
        (video_id,)
    )
    return c.fetchone() is not None

def ler_C_ONLINE():
    c.execute(F"SELECT * FROM C_ONLINE ")
    result = c.fetchall()
    return result

def Del_C_ONLINE(LINK_VIDEO=''):
    if LINK_VIDEO:
        c.execute("DELETE FROM C_ONLINE WHERE LINK_VIDEO = ?", (LINK_VIDEO,))
        dbase.commit()

        return c.fetchall()

    else:
        c.execute(f"DELETE FROM C_ONLINE")
        dbase.commit()
    return True



# __________________________________________------------------------------>  D_LINKS
dbase.execute('''CREATE TABLE IF NOT EXISTS D_LINKS(
    PALAVRA TEXT NOT NULL,
    NOME_PAGINA TEXT,
    LINK_PAGINA TEXT)''')

# =======================================_ C_ONLINE
def esc_D_LINKS(PALAVRA,NOME_PAGINA,LINK_PAGINA):
    c.execute('''INSERT INTO D_LINKS (PALAVRA,NOME_PAGINA,LINK_PAGINA)
                VALUES (?,?,?)''',
              (str(PALAVRA).strip(),NOME_PAGINA,LINK_PAGINA))
    dbase.commit()

def aplicar_links_bloco(texto, limite_links=2):
    import re
    import random

    if not texto or limite_links <= 0:
        return texto, 0

    c.execute("SELECT PALAVRA, LINK_PAGINA FROM D_LINKS")
    registros = c.fetchall()

    if not registros:
        return texto, 0

    random.shuffle(registros)

    usados = 0
    texto_modificado = texto
    links_usados = set()

    for palavra, link in registros:
        if usados >= limite_links:
            break

        if not palavra or not link or link in links_usados:
            continue

        padrao = r'(?<!>)\b(' + re.escape(palavra) + r')\b(?![^<]*>)'

        if re.search(padrao, texto_modificado, flags=re.IGNORECASE):
            texto_modificado = re.sub(
                padrao,
                rf'<a href="{link}" target="_blank" rel="nofollow sponsored">\1</a>',
                texto_modificado,
                count=1,
                flags=re.IGNORECASE
            )
            usados += 1
            links_usados.add(link)

    return texto_modificado, usados


# =======================================_ COPY_PRODUTO
dbase.execute('''CREATE TABLE IF NOT EXISTS COPY_PRODUTO(
              ID_COPY TEXT PRIMARY KEY NOT NULL,
              PALAVRAS_CHAVES TEXT,
              TITULO_SEO_H1 TEXT,
              INCOMODO_IMEDIATO TEXT,
              QUEBRA_EXPECTATIVA TEXT,
              TITULO_CONSEQUENCIAS_DO_ERRO_H2 TEXT,
              PROBLEMA_REAL TEXT,
              AGITACAO_PERDA_CONTINUA TEXT,
              VIRADA_PSICOLOGICA TEXT,
              TITULO_SEO_H2 TEXT,
              INTRODUCAO_PRODUTO TEXT,
              BENEFICIO_CENTRAL TEXT,
              DEMONSTRACAO_MENTAL TEXT,
              NORMALIZACAO_PROVA TEXT,
              TITULO_SEGURANCA_E_SIMPLICIDADE_H2 TEXT,
              REDUCAO_RISCO TEXT,
              PARAGRAFO_DETAILS TEXT,
              BENEFITS_LIST TEXT,
              H2_FAQ_TITLE TEXT,
              PARAGRAFO_FAQ TEXT,
              ALT_IMAGE_1 TEXT,
              ALT_IMAGE_2 TEXT,
              ALT_IMAGE_3 TEXT,
              CTA_NATURAL TEXT,
              CHAMADA_ACAO TEXT,
              CATEGORIA TEXT)''')


def esc_COPY_PRODUTO(ID_COPY,PALAVRAS_CHAVES,TITULO_SEO_H1,INCOMODO_IMEDIATO,QUEBRA_EXPECTATIVA,TITULO_CONSEQUENCIAS_DO_ERRO_H2,PROBLEMA_REAL,AGITACAO_PERDA_CONTINUA,VIRADA_PSICOLOGICA,TITULO_SEO_H2,INTRODUCAO_PRODUTO,BENEFICIO_CENTRAL,DEMONSTRACAO_MENTAL,NORMALIZACAO_PROVA,TITULO_SEGURANCA_E_SIMPLICIDADE_H2,REDUCAO_RISCO,PARAGRAFO_DETAILS,BENEFITS_LIST,H2_FAQ_TITLE,PARAGRAFO_FAQ,ALT_IMAGE_1,ALT_IMAGE_2,ALT_IMAGE_3,CTA_NATURAL,CHAMADA_ACAO,CATEGORIA):
    c.execute('INSERT INTO COPY_PRODUTO VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              (ID_COPY,PALAVRAS_CHAVES,TITULO_SEO_H1,INCOMODO_IMEDIATO,QUEBRA_EXPECTATIVA,TITULO_CONSEQUENCIAS_DO_ERRO_H2,PROBLEMA_REAL,AGITACAO_PERDA_CONTINUA,VIRADA_PSICOLOGICA,TITULO_SEO_H2,INTRODUCAO_PRODUTO,BENEFICIO_CENTRAL,DEMONSTRACAO_MENTAL,NORMALIZACAO_PROVA,TITULO_SEGURANCA_E_SIMPLICIDADE_H2,REDUCAO_RISCO,PARAGRAFO_DETAILS,BENEFITS_LIST,H2_FAQ_TITLE,PARAGRAFO_FAQ,ALT_IMAGE_1,ALT_IMAGE_2,ALT_IMAGE_3,CTA_NATURAL,CHAMADA_ACAO,CATEGORIA))
    dbase.commit()

def ler_COPY_PRODUTO_video(ID_COPY):
    try:
        col = 'INCOMODO_IMEDIATO, QUEBRA_EXPECTATIVA, PROBLEMA_REAL, AGITACAO_PERDA_CONTINUA, VIRADA_PSICOLOGICA, INTRODUCAO_PRODUTO,BENEFICIO_CENTRAL, DEMONSTRACAO_MENTAL, NORMALIZACAO_PROVA, REDUCAO_RISCO, PARAGRAFO_DETAILS, CTA_NATURAL,CHAMADA_ACAO'
        c.execute(F"SELECT {col} FROM COPY_PRODUTO WHERE ID_COPY = '{ID_COPY}' ")
        return c.fetchall()
    except sqlite3.OperationalError:
        return ''
def ler_COPY_PRODUTO():
    try:
        c.execute(F"SELECT * FROM COPY_PRODUTO ")
        return c.fetchall()
    except sqlite3.OperationalError:
        return ''


def ler_COPY_PRODUTO_sit(ID_COPY):
    try:
        c.execute(F"SELECT * FROM COPY_PRODUTO WHERE ID_COPY = '{ID_COPY}' ")
        return c.fetchall()
    except sqlite3.OperationalError:
        return ''

def ATUAL_COPY_PRODUTO(ID, COLUNA, CONTEUDO, CONTEUDO2=''):
    conteudo_final = (CONTEUDO2 + CONTEUDO) if CONTEUDO2 else CONTEUDO
    c.execute(f"UPDATE COPY_PRODUTO SET {COLUNA} = ? WHERE ID_PROD = ?", (conteudo_final, ID))
    dbase.commit()



# __________________________________________------------------------------>  COPY_PRODUTO_MIDIA
dbase.execute('''CREATE TABLE IF NOT EXISTS COPY_PRODUTO_MIDIA(
    ID_PROD TEXT PRIMARY KEY NOT NULL,
    DESCRIT_VIDEO TEXT,
    VIDEO_LINK TEXT,
    LINK_AFILIADO_1 TEXT,
    LINK_AFILIADO_2 TEXT,
    LINK_AFILIADO_3 TEXT,
    IMAGE_LINK_1 TEXT,
    IMAGE_LINK_2 TEXT,
    IMAGE_LINK_3 TEXT,
    VIDEO TEXT)''')

# =======================================_ COPY_PRODUTO_MIDIA
def esc_COPY_PRODUTO_MIDIA(ID_PROD,DESCRIT_VIDEO, VIDEO_LINK, LINK_AFILIADO_1, LINK_AFILIADO_2,LINK_AFILIADO_3,IMAGE_LINK_1,IMAGE_LINK_2,IMAGE_LINK_3,VIDEO):
    try:
        c.execute('''INSERT INTO COPY_PRODUTO_MIDIA VALUES (?,?,?,?,?,?,?,?,?,?)''',
                  (ID_PROD,DESCRIT_VIDEO, VIDEO_LINK, LINK_AFILIADO_1, LINK_AFILIADO_2,LINK_AFILIADO_3,IMAGE_LINK_1,IMAGE_LINK_2,IMAGE_LINK_3,VIDEO))
        dbase.commit()
        return 'Ok cadastrado!'

    except sqlite3.IntegrityError:
        return 'Ja estava cadastrado!'

def ler_COPY_PRODUTO_MIDIA(ID_PROD):
    c.execute(F"SELECT * FROM COPY_PRODUTO_MIDIA WHERE ID_PROD = '{ID_PROD}' ")
    result = c.fetchall()
    return result

def Del_COPY_PRODUTO_MIDIA(LINK_VIDEO=''):
    if LINK_VIDEO:
        c.execute("DELETE FROM COPY_PRODUTO_MIDIA WHERE LINK_VIDEO = ?", (LINK_VIDEO,))
        dbase.commit()

        return c.fetchall()

    else:
        c.execute(f"DELETE FROM COPY_PRODUTO_MIDIA")
        dbase.commit()
    return True

def ATUAL_COPY_PRODUTO_MIDIA(ID, COLUNA, CONTEUDO,):
    c.execute(f"UPDATE COPY_PRODUTO_MIDIA SET {COLUNA} = ? WHERE ID_PROD = ?", (CONTEUDO, ID))
    dbase.commit()

def ler_dados_html_seo_video(ID_COPY, ID_PROD):
    # ===== COPY_PRODUTO =====
    c.execute("""
        SELECT
            ID_COPY,
            PALAVRAS_CHAVES,
            TITULO_SEO_H1,
            INCOMODO_IMEDIATO,
            QUEBRA_EXPECTATIVA,
            TITULO_CONSEQUENCIAS_DO_ERRO_H2,
            PROBLEMA_REAL,
            AGITACAO_PERDA_CONTINUA,
            VIRADA_PSICOLOGICA,
            TITULO_SEO_H2,
            INTRODUCAO_PRODUTO,
            BENEFICIO_CENTRAL,
            DEMONSTRACAO_MENTAL,
            NORMALIZACAO_PROVA,
            TITULO_SEGURANCA_E_SIMPLICIDADE_H2,
            REDUCAO_RISCO,
            PARAGRAFO_DETAILS,
            BENEFITS_LIST,
            H2_FAQ_TITLE,
            PARAGRAFO_FAQ,
            ALT_IMAGE_1,
            ALT_IMAGE_2,
            ALT_IMAGE_3,
            CTA_NATURAL,
            CHAMADA_ACAO
        FROM COPY_PRODUTO
        WHERE ID_COPY = ?
    """, (ID_COPY,))
    cp = c.fetchone()

    if cp is None:
        raise ValueError(f"COPY_PRODUTO não encontrado para ID_COPY = {ID_COPY}")

    # ===== COPY_PRODUTO_MIDIA =====
    c.execute("""
        SELECT
            DESCRIT_VIDEO,
            VIDEO_LINK,
            LINK_AFILIADO_1,
            LINK_AFILIADO_2,
            LINK_AFILIADO_3,
            IMAGE_LINK_1,
            IMAGE_LINK_2,
            IMAGE_LINK_3,
            VIDEO
        FROM COPY_PRODUTO_MIDIA
        WHERE ID_PROD = ?
    """, (ID_PROD,))
    md = c.fetchone()

    if md is None:
        raise ValueError(f"COPY_PRODUTO_MIDIA não encontrado para ID_PROD = {ID_PROD}")

    return {
        "ID_COPY": cp[0],
        "PALAVRAS_CHAVES": cp[1],
        "TITULO_SEO_H1": cp[2],
        "INCOMODO_IMEDIATO": cp[3],
        "QUEBRA_EXPECTATIVA": cp[4],
        "TITULO_CONSEQUENCIAS_DO_ERRO_H2": cp[5],
        "PROBLEMA_REAL": cp[6],
        "AGITACAO_PERDA_CONTINUA": cp[7],
        "VIRADA_PSICOLOGICA": cp[8],
        "TITULO_SEO_H2": cp[9],
        "INTRODUCAO_PRODUTO": cp[10],
        "BENEFICIO_CENTRAL": cp[11],
        "DEMONSTRACAO_MENTAL": cp[12],
        "NORMALIZACAO_PROVA": cp[13],
        "TITULO_SEGURANCA_E_SIMPLICIDADE_H2": cp[14],
        "REDUCAO_RISCO": cp[15],
        "PARAGRAFO_DETAILS": cp[16],
        "BENEFITS_LIST": cp[17],
        "H2_FAQ_TITLE": cp[18],
        "PARAGRAFO_FAQ": cp[19],
        "ALT_IMAGE_1": cp[20],
        "ALT_IMAGE_2": cp[21],
        "ALT_IMAGE_3": cp[22],
        "CTA_NATURAL": cp[23],
        "CHAMADA_ACAO": cp[24],

        "DESCRIT_VIDEO": md[0],
        "VIDEO_LINK": md[1],
        "LINK_AFILIADO_1": md[2],
        "LINK_AFILIADO_2": md[3],
        "LINK_AFILIADO_3": md[4],
        "IMAGE_LINK_1": md[5],
        "IMAGE_LINK_2": md[6],
        "IMAGE_LINK_3": md[7],
        "VIDEO": md[8]
    }


# __________________________________________------------------------------>  P_PROMPTS_COPY_PRODUTOS
dbase.execute('''CREATE TABLE IF NOT EXISTS P_PROMPTS_COPY_PRODUTOS(
    ID_PROD TEXT PRIMARY KEY NOT NULL,
    CAPAS TEXT,
    INTRO_VIDEO TEXT,
    ABET_VIDEO TEXT,
    CHAMADA_VIDEO TEXT,
    OUTROS TEXT)''')

# =======================================_ P_PROMPTS_COPY_PRODUTOS
def esc_P_PROMPTS_COPY_PRODUTOS(ID_PROD,CAPAS, INTRO_VIDEO, ABET_VIDEO, CHAMADA_VIDEO,OUTROS):
    try:
        c.execute('''INSERT INTO P_PROMPTS_COPY_PRODUTOS VALUES (?,?,?,?,?,?)''',
                  (ID_PROD,CAPAS, INTRO_VIDEO, ABET_VIDEO, CHAMADA_VIDEO,OUTROS))
        dbase.commit()
        return 'Ok cadastrado!'

    except sqlite3.IntegrityError:
        return 'Ja estava cadastrado!'

def ler_P_PROMPTS_COPY_PRODUTOS(ID_PROD):
    c.execute(F"SELECT * FROM P_PROMPTS_COPY_PRODUTOS WHERE ID_PROD = '{ID_PROD}' ")
    result = c.fetchall()
    return result

def Del_P_PROMPTS_COPY_PRODUTOS(LINK_VIDEO=''):
    if LINK_VIDEO:
        c.execute("DELETE FROM P_PROMPTS_COPY_PRODUTOS WHERE ID_PROD = ?", (LINK_VIDEO,))
        dbase.commit()

        return c.fetchall()

    else:
        c.execute(f"DELETE FROM P_PROMPTS_COPY_PRODUTOS")
        dbase.commit()
    return True


def ATUAL_P_PROMPTS_COPY_PRODUTOS(ID, COLUNA, CONTEUDO,):
    c.execute(f"UPDATE P_PROMPTS_COPY_PRODUTOS SET {COLUNA} = ? WHERE ID_PROD = ?", (CONTEUDO, ID))
    dbase.commit()
