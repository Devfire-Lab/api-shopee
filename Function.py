import  streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO



def Caves_Pri():
    return [
    'title_seo_','title_h2_','introduction_',
    'card_description_','title_details_','parágrafo_details_',
    'benefits_title_','benefits_list_','h2_faq_title_',
    'parágrafo_faq_','alt_image_', 'keywords_']




# =================== AOAGAR QRQUIVOS
def Apagar_Arquivos():
    import glob
    import os
    BASE_DIR = os.path.abspath("arquivos")
    extensoes = [
        "wav", "mp3", "m4a", "aac", "flac", "ogg",
        "webm", "vtt", "srt", "part"
    ]
    for ext in extensoes:
        for f in glob.glob(os.path.join(BASE_DIR, f"*.{ext}")):
            os.remove(f)
    print(f'APAGANDO ID: AUDIOS!')

# ================= MANIPULAÇÃO DE TEXTO =================

def Ret_cha_NLTK(dados, limite):
    from langdetect import detect
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    texto = f"""
    {dados}"""
    idioma_detectado = detect(texto)

    mapa_idiomas = {
        'pt': 'portuguese',
        'en': 'english'
    }

    idioma = mapa_idiomas.get(idioma_detectado, 'english')

    stop_words = set(stopwords.words(idioma))
    palavras = word_tokenize(texto.lower())

    keywords = [
        p for p in palavras
        if p.isalpha() and p not in stop_words
    ]

    return keywords[:limite]

def limpa_ruido(texto):
    texto = re.sub(r'http\S+', ' ', texto)          # URLs
    texto = re.sub(r'#\w+', ' ', texto)             # hashtags
    texto = re.sub(r'[@🔔👍🏼😊😉🤔]', ' ', texto)    # emojis comuns
    texto = re.sub(r'\s+', ' ', texto)              # espaços
    return texto.strip()

def Retira_chaves(dados, limite=10):
    from langdetect import detect
    import nltk, yake

    nltk.download('punkt')
    nltk.download('stopwords')
    texto = f"""
    {dados}"""

    texto = limpa_ruido(texto)
    texto2 = Ret_cha_NLTK(dados, limite)
    idioma = 'pt' if detect(texto) == 'pt' else 'en'

    kw_extractor = yake.KeywordExtractor(
        lan=idioma,
        n=3,  # até 3 palavras por chave
        top=limite,
        dedupLim=0.9,  # remove repetições tipo "luxo / clínica de luxo"
        features=None
    )

    keywords = kw_extractor.extract_keywords(texto)
    return texto2 + [k for k, _ in keywords]

def resumir_texto_coerente(texto, max_chars, max_sentences=10):
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.summarizers.lex_rank import LexRankSummarizer
    from sumy.utils import get_stop_words

    """
    Resume qualquer texto de forma coerente, sem repetir sentenças,
    mantendo no máximo max_chars caracteres.
    """
    if len(texto) <= max_chars:
        return texto

    # Parser e tokenizer para português
    parser = PlaintextParser.from_string(texto, Tokenizer("portuguese"))

    # Summarizer LexRank
    summarizer = LexRankSummarizer()
    summarizer.stop_words = get_stop_words("portuguese")

    # Gera resumo com até max_sentences
    resumo_sentences = summarizer(parser.document, max_sentences)

    # Remove repetições de sentenças
    seen = set()
    resumo_unico = []
    for sentenca in resumo_sentences:
        s = str(sentenca).strip()
        if s not in seen:
            seen.add(s)
            resumo_unico.append(s)

    # Junta sentenças sem ultrapassar max_chars
    resumo_final = ""
    for s in resumo_unico:
        if len(resumo_final) + len(s) + 1 > max_chars:  # +1 para espaço
            break
        resumo_final += s + " "

    resumo_final = resumo_final.strip()
    if len(resumo_final) < len(texto):
        resumo_final += "..."  # Indica que o texto foi resumido

    return resumo_final

def limpar_texto_contexto(texto):
    # Remove emojis
    texto = re.sub(
        r"["
        r"\U0001F600-\U0001F64F"
        r"\U0001F300-\U0001F5FF"
        r"\U0001F680-\U0001F6FF"
        r"\U0001F700-\U0001F77F"
        r"]+", "", texto
    )

    # Remove aspas, asteriscos, markdown e símbolos de formatação
    texto = re.sub(r"[\"'`*#_=~<>|]+", "", texto)

    # Remove caracteres invisíveis / lixo comum de cópia
    texto = re.sub(r"[\u200b\u200c\u200d\uFEFF]", "", texto)

    # Normaliza espaços (preserva pontuação)
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def remover_chaves(texto ):
    padrao = r'(' + '|'.join(map(re.escape, Caves_Pri())) + r')'
    return re.sub(padrao, '', texto)

def formatar_chaves_coloridas(chaves):
    import re

    texto = re.sub(r'[\*\+\-:\\]', ',', chaves)
    texto = re.sub(r',+', ',', texto).strip(',')

    itens = [i.strip() for i in texto.split(',') if i.strip()]

    html_itens = []
    for item in itens:
        html_itens.append(
            f'''
            <span style="
                display:inline-block;
                background:#f1f1f1;
                color:#333;
                padding:6px 12px;
                border-radius:16px;
                font-size:13px;
                margin:4px;
                border:1px solid #e0e0e0;
            ">
                {str(item).title()}
            </span>
            '''
        )

    return f'''
    <div style="
        display:flex;
        flex-wrap:wrap;
        margin-top:16px;
    ">
        {''.join(html_itens)}
    </div>
    '''

def salvar_copy_produto(raw_text, CATEGORIA):
    import re
    import uuid
    from Banco_Dados import esc_COPY_PRODUTO

    def remove_lixo(txt):
        if txt is None:
            return ""
        return str(txt).replace('"', "")

    def ext(campo):
        m = re.search(
            rf'{campo}\s*=\s*(.*?)(?=\n\n[A-Z0-9_]+\s*=|\Z)',
            raw_text,
            re.S
        )
        return m.group(1).strip() if m else ""

    ID_COPY = str(uuid.uuid4())

    esc_COPY_PRODUTO(
        ID_COPY,
        remove_lixo(ext('PALAVRAS_CHAVES_')),
        remove_lixo(ext('TITULO_SEO_H1_')),
        remove_lixo(ext('INCOMODO_IMEDIATO_')),
        remove_lixo(ext('QUEBRA_EXPECTATIVA_')),
        remove_lixo(ext('TITULO_CONSEQUENCIAS_DO_ERRO_H2_')),
        remove_lixo(ext('PROBLEMA_REAL_')),
        remove_lixo(ext('AGITACAO_PERDA_CONTINUA_')),
        remove_lixo(ext('VIRADA_PSICOLOGICA_')),
        remove_lixo(ext('TITULO_SEO_H2_')),
        remove_lixo(ext('INTRODUCAO_PRODUTO_')),
        remove_lixo(ext('BENEFICIO_CENTRAL_')),
        remove_lixo(ext('DEMONSTRACAO_MENTAL_')),
        remove_lixo(ext('NORMALIZACAO_PROVA_')),
        remove_lixo(ext('TITULO_SEGURANCA_E_SIMPLICIDADE_H2_')),
        remove_lixo(ext('REDUCAO_RISCO_')),
        remove_lixo(ext('PARAGRAFO_DETAILS_')),
        remove_lixo(ext('BENEFITS_LIST_')),
        remove_lixo(ext('H2_FAQ_TITLE_')),
        remove_lixo(ext('PARAGRAFO_FAQ_')),
        remove_lixo(ext('ALT_IMAGE_1')),
        remove_lixo(ext('ALT_IMAGE_2')),
        remove_lixo(ext('ALT_IMAGE_3')),
        remove_lixo(ext('CTA_NATURAL_')),
        remove_lixo(ext('CHAMADA_ACAO_')),
        remove_lixo(CATEGORIA if CATEGORIA is not None else "")
    )

    return ID_COPY


import textwrap


def wrap_text(text, width=80):
    # Quebra o texto nas linhas originais
    lines = text.splitlines()
    wrapped_lines = []
    for line in lines:
        # Aplica wrap apenas em cada linha separadamente
        wrapped_lines.extend(textwrap.wrap(line, width=width) or [""])
    return "\n".join(wrapped_lines)




def upload_image_freeimage(file):

    API_KEY = "6d207e02198a847aa98d0a2a901485a5"
    url = "https://freeimage.host/api/1/upload"

    response = requests.post(
        url,
        data={
            "key": API_KEY,
            "action": "upload",
            "format": "json"
        },
        files={
            "source": file
        }
    )

    data = response.json()

    if data.get("status_code") == 200:
        return data["image"]["url"]
    else:
        return None


def gerar_qr(link, cor_qr, cor_fundo, logo_file=None, texto_abaixo=None):
    import qrcode

    # Criar QR Code
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    # Gerar imagem do QR
    img_qr = qr.make_image(
        fill_color=cor_qr,
        back_color=cor_fundo
    ).convert("RGB")

    # Inserir logo no centro (se fornecido)
    if logo_file:
        logo = Image.open(logo_file).convert("RGBA")
        qr_w, qr_h = img_qr.size
        logo_size = qr_w // 4
        logo = logo.resize((logo_size, logo_size))
        pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
        img_qr.paste(logo, pos, logo)

    # Adicionar texto abaixo
    if texto_abaixo:
        largura, altura = img_qr.size
        nova_img = Image.new("RGB", (largura, altura + 60), cor_fundo)
        nova_img.paste(img_qr, (0, 0))

        draw = ImageDraw.Draw(nova_img)
        try:
            font = ImageFont.truetype("arial.ttf", 28)
        except:
            font = ImageFont.load_default()

        # Centralizar texto
        bbox = draw.textbbox((0, 0), texto_abaixo, font=font)
        w_text = bbox[2] - bbox[0]
        h_text = bbox[3] - bbox[1]
        draw.text(((largura - w_text) / 2, altura + 10), texto_abaixo, fill=cor_qr, font=font)
        img_qr = nova_img

    # Salvar em buffer para Streamlit
    buffer = BytesIO()
    img_qr.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer



def youtube_to_embed(url):
    import re
    from urllib.parse import urlparse, parse_qs

    if not url:
        return ''

    # Se já for embed, retorna como está
    if 'youtube.com/embed/' in url:
        return url

    video_id = None
    start = None

    # youtu.be/ID
    if 'youtu.be' in url:
        parsed = urlparse(url)
        video_id = parsed.path.strip('/')
        qs = parse_qs(parsed.query)
        if 't' in qs:
            start = qs['t'][0].replace('s','')

    # youtube.com/watch?v=ID
    elif 'youtube.com' in url:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        video_id = qs.get('v', [None])[0]
        if 't' in qs:
            start = qs['t'][0].replace('s','')

    if not video_id:
        return ''

    embed = f"https://www.youtube.com/embed/{video_id}"
    if start and start.isdigit():
        embed += f"?start={start}"

    return embed

import re
import urllib.parse

def gerar_link_public0_shopee(nome,shop_id,item_id):
    nome = nome.strip()

    # Mantém travessão (Shopee usa e apenas faz URL encode)
    # Se quiser normalizar, comente a linha abaixo
    # nome = nome.replace("–", "-").replace("—", "-")

    # Remove caracteres não usados no slug
    nome = re.sub(r"[^\w\s\-–À-ÿ]", "", nome)

    # Espaços -> hífen
    nome = re.sub(r"\s+", "-", nome)

    # Remove hífens duplicados
    nome = re.sub(r"-{2,}", "-", nome)

    slug_encoded = urllib.parse.quote(nome, safe='-')

    LINK_PUBLICO = (
        f"https://shopee.com.br/"
        f"{slug_encoded}-i.{shop_id}.{item_id}"
    )
    return LINK_PUBLICO


def card_mostra(ITEM_ID):
    from Banco_Shopee import ler_B_DADOS_AFILIADOS
    for i in ler_B_DADOS_AFILIADOS(ITEM_ID):
        col_a, col_b = st.columns(2)

        col_b.markdown(
            f'<a href="{i[11]}" target="_blank">'
            f'<button style="margin: 10px; padding: 5px; background-color: #f0f0f0;font-size: 16px; '
            f'border: none; border-radius: 5px; cursor: pointer; color: #BD5908 ;">'
            f'<b>**{i[2].strip()}**</b></button>'
            f'</a>', unsafe_allow_html=True
        )
        col_b.markdown(f"Loja: **{i[4].strip()}**")

        with col_b:
            c1, c2 = st.columns(2)
            c1.metric("Preco", f"R$ {i[7]}")
            c2.metric("Comissao", f"R$ {i[8]}")

        if i[3]:
            col_a.image(i[3], width=220)

