import time
import json
import hashlib
import requests
import pandas as pd
import streamlit as st
import math

from Minhas_Chaves_Api import chave_api_shopee_afiliado

# ===============================
# CONFIGURAÇÃO DA API

# Carrega as chaves
chaves = chave_api_shopee_afiliado()

if chaves is None or len(chaves) < 2:
    raise ValueError("❌ Chaves da Shopee não foram carregadas!")

APP_ID = chaves[0]
SECRET_KEY = chaves[1]

URL = "https://open-api.affiliate.shopee.com.br/graphql"

def sign(app_id, timestamp, body, secret):
    raw = app_id + str(timestamp) + body + secret
    return hashlib.sha256(raw.encode()).hexdigest()

def buscar_produtos(keyword, listType, sort_type, page, limit):
    st.write()
    query = f"""
    query {{
      productOfferV2(
        sortType: {sort_type} # Números menores = mais precisão na busca por keyword, números maiores = mais relevância/comercial. USE DE 1 A 5
        listType: {listType}  # 0 Padrão/Todos produtos ✅ (seu atual)  1  # Produtos em promoção
        page: {page}
        limit: {limit}
        keyword: "{keyword}"
      ) {{
        nodes {{
          itemId
          shopId
          shopName
          price
          commissionRate
          productName
          imageUrl
          productCatIds
        }}
      }}
    }}
    """

    body = json.dumps({"query": query}, separators=(",", ":"))
    timestamp = int(time.time())
    signature = sign(APP_ID, timestamp, body, SECRET_KEY)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"SHA256 Credential={APP_ID},Timestamp={timestamp},Signature={signature}"
    }
    try:
        resp = requests.post(URL, headers=headers, data=body, timeout=30)
        return resp.json()
    except Exception as e:
        return {"errors": [str(e)]}

def GERAR_link_afiliado(shopee_url: str):
    query = """
    mutation GenerateShortLink($input: ShortLinkInput!) {
      generateShortLink(input: $input) {
        shortLink
      }
    }
    """

    body = json.dumps({
        "query": query,
        "variables": {
            "input": {
                "originUrl": shopee_url
            }
        }
    }, separators=(",", ":"))

    timestamp = int(time.time())
    signature = sign(APP_ID, timestamp, body, SECRET_KEY)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"SHA256 Credential={APP_ID},Timestamp={timestamp},Signature={signature}"
    }

    resp = requests.post(URL, headers=headers, data=body, timeout=30)
    short_link = resp.json()["data"]["generateShortLink"]["shortLink"]

    return short_link

def calcular_indice_venda(preco, comissao, preco_max=1000):
    preco = max(preco, 1)
    # Produtos mais baratos têm maior chance de venda
    fator_preco = math.log10(preco_max / preco) if preco < preco_max else 0.1
    indice = (comissao / preco) * fator_preco * 100
    return indice

def produtos_mais_vendaveis(lista, top_n=5):
    produtos_validados = []
    for p in lista:
        try:
            preco = float(p[7])
            comissao = float(p[8])
            if preco <= 0 or comissao <= 0:
                continue
            indice = calcular_indice_venda(preco, comissao)
            produtos_validados.append((p, indice))
        except:
            continue
    produtos_ordenados = sorted(produtos_validados, key=lambda x: x[1], reverse=True)
    return produtos_ordenados[:top_n]

def calcular_porcentagem_lucro(valor_original, lucro):
    if valor_original == 0:
        raise ValueError("O valor original não pode ser zero.")
    porcentagem_lucro = (lucro / valor_original) * 100
    return round(porcentagem_lucro)

def Api_Shopee(st):
    from Prompts_HTML import RAIO_X_PRODUTO_

    st.title("Shopee Afiliados - 4 BOTÕES")

    col0,col1, col2, col3, col4, col5, col6 = st.columns(7)
    with col0:
        qt = st.selectbox("Quantidades", [3,6,9,18,36,50])
    with col1:
        keyword = st.text_input("Buscar", value="")
    with col2:
        sort_label = st.selectbox("Ordenar", ["Específico","Maior comissao", "Mais recentes"])
    with col3:
        listType = st.selectbox("Ordenar", ["Padrão", "Produtos em promoção"])
    with col4:
        preco_min = st.number_input("Preco Min", value=10.0)
    with col5:
        preco_max = st.number_input("Preco Max", value=10000.0)
    with col6:
        comissao_min = st.slider("Comissao min", 0.0, 100.0, 3.0)

    page = 1
    limit = int(qt)
    sort_map = { "Específico": 1, "Mais recentes": 2, "Maior comissao": 5}
    list_map = {"Padrão": 0, "Produtos em promoção": 1}

    if st.button("BUSCAR",):
        from Banco_Shopee import ler_A_CAT_temp, Del_B_TEMPORARIOS, esc_B_TEMPORARIOS
        Del_B_TEMPORARIOS()

        with st.spinner("Carregando..."):
            data = buscar_produtos(str(keyword).title(), list_map[listType], sort_map[sort_label], page, limit)

        if "errors" in data:
            st.error(f"API Error: {data['errors']}")
            st.stop()

        if "data" not in data or not data["data"]["productOfferV2"]["nodes"]:
            st.warning("Sem produtos")
            st.stop()

        nodes = data["data"]["productOfferV2"]["nodes"]
        df = pd.DataFrame(nodes)
        df["price"] = pd.to_numeric(df["price"], errors='coerce')
        df["commissionRate"] = pd.to_numeric(df["commissionRate"], errors='coerce')
        df["commissionValue"] = df["price"] * df["commissionRate"]
        df["imagem"] = df["imageUrl"]

        df_filtrado = df[
            (df["price"] >= preco_min) &
            (df["price"] <= preco_max) &
            (df["commissionValue"] >= comissao_min)
        ].copy()

        if df_filtrado.empty:
            st.warning("Sem produtos nos filtros. Mostrando todos:")
            df_filtrado = df.copy()

        st.success(f"{len(df_filtrado)} produtos encontrados!")

        for i in range(0, len(df_filtrado), 3):
            cols = st.columns(3)

            for j, (idx, row) in enumerate(df_filtrado.iloc[i:i + 3].iterrows()):
                with cols[j]:
                    cat_ids = row.get('productCatIds')
                    if cat_ids and isinstance(cat_ids, list) and len(cat_ids) >= 3:
                        LINK = f"https://shopee.com.br/product/{row['shopId']}/{row['itemId']}"

                        esc_B_TEMPORARIOS(row['itemId'],row['shopId'],row['productName'], row["imagem"], row['shopName'], cat_ids[1], cat_ids[2], round(float(row['price']),2),
                                          round(float(row['commissionValue']),2), LINK,'')

    from Banco_Shopee import ler_B_TEMPORARIOS, ler_A_CAT,esc_B_DADOS_AFILIADOS

    lista = ler_B_TEMPORARIOS()
    qt_col = 3
    st.markdown("### Produtos recomendados para vender")
    top_produtos = produtos_mais_vendaveis(lista, top_n=3)
    for p, indice in top_produtos:
        st1, st2, st3, st4, st5 = st.columns([1,3, 1, 1,1])
        st1.image(p[3], width=50)
        st2.markdown(f"**{p[2]}**")
        st3.metric("Preço", f" {p[7]}")
        st4.metric("% Lucro", f"{calcular_porcentagem_lucro(float(p[7]), float(p[8]))}%")
        st5.metric("Comissão", f"R$ {p[8]}")
    for im in range(0, len(lista), qt_col):
        linha = st.columns(qt_col)
        for j, i in enumerate(lista[im:im + qt_col]):
            with linha[j]:
                st.markdown("---")
                link = f"https://shopee.com.br/product/{i[1]}/{i[0]}"
                st.markdown(
                    f'<a href="{link}" target="_blank">'
                    f'<button style="margin: 10px; padding: 5px; background-color: #f0f0f0;font-size: 16px; '
                    f'border: none; border-radius: 5px; cursor: pointer; color: #BD5908 ;">'
                    f'<b>**{i[2][:63].strip()}**</b></button>'
                    f'</a>', unsafe_allow_html=True
                )
                col_a, col_b = st.columns(2)
                col_b.markdown(f"Loja: **{i[4].strip()}**")
                nome1, link1 = ler_A_CAT(col_b, i[5])
                nome2, link2 = ler_A_CAT(col_b, i[6])

                if nome1 != None:
                    col_b.markdown(
                        f'<a href="{link1}" target="_blank">'
                        f'<button style="margin: 10px; padding: 5px; background-color: gray;font-size: 16px; '
                        f'border: none; border-radius: 5px; cursor: pointer; color: #f0f0f0;">'
                        f'<b>{nome1}</b></button>'
                        f'</a>', unsafe_allow_html=True)

                if nome2 != None:
                    col_b.markdown(
                        f'<a href="{link2}" target="_blank">'
                        f'<button style="margin: 10px; padding: 5px; background-color: gray;font-size: 16px; '
                        f'border: none; border-radius: 5px; cursor: pointer; color: #f0f0f0;">'
                        f'<b>{nome2}</b></button>'
                        f'</a>', unsafe_allow_html=True)


                with col_b:
                    c1, c2, c3 = st.columns(3)
                    c1.text("Preco")
                    c1.write(f"R$ {i[7]}")
                    c2.text("%")
                    c2.write(f" {calcular_porcentagem_lucro(float(i[7]),float(i[8]))}")
                    c3.text("Comissão")
                    c3.write(f"R$ {i[8]}")

                if i[3]:
                    col_a.image(i[3], width=220)


                if st.button(f" 🔗 Gerar links Afiliado: {nome1[:15]}...",
                             key=f"btn_{i[0]}",
                             use_container_width=True):
                    origin_url = f"https://shopee.com.br/product/{int(i[1])}/{int(i[0])}"


                    from Function import gerar_link_public0_shopee
                    link_pul = gerar_link_public0_shopee(i[2],int(i[1]),int(i[0]))

                    link_af = GERAR_link_afiliado(origin_url)
                    link_ct1 = GERAR_link_afiliado(link1)
                    link_ct2 = GERAR_link_afiliado(link2)
                    from Pag_Chats_IA import IA
                    raio_X = IA(RAIO_X_PRODUTO_(link_pul))
                    #with st.expander('Questiona ia!'):
                        #st.code(RAIO_X_PRODUTO_(link_pul))
                    with st.expander('Descrição Gerada!'):
                        st.write(raio_X)


                    esc_B_DADOS_AFILIADOS(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],
                                              origin_url,link_pul, link_af, link_ct1, link_ct2,
                                              f'{nome1},{nome2}',raio_X)

                    st.success("✅ AFILIADOS GERADO: esrito em B_DADOS_AFILIADOS!")
                    st.code(F'AFILIADO = {link_af}')
                    st.code(F'CATEGORIA = {link_ct1}')
                    st.code(F'SUB CATEG = {link_ct2}')
                    st.balloons()

    st.markdown("---")


def Api_Shopee_LOOP_INFINITO(st):

    from Prompts_HTML import RAIO_X_PRODUTO_
    from menu_COPY_AUTOMATICA import extrair_dados
    from Banco_Dados import esc_A_PROD_ENTRADA, ler_A_PROD_ENTRADA, existe_em_C_ONLINE_BAIXADOS, Del_A_PROD_ENTRADA
    from Banco_Shopee import Del_B_TEMPORARIOS, esc_B_TEMPORARIOS
    Del_B_TEMPORARIOS()
    col0,col1, col2, col3, col4, col5, col6 = st.columns(7)
    with col0:
        qt = st.selectbox("Quantidades", [3,6,9,18,36,50])
    with col1:
        keyword = st.text_input("Buscar", value="")
    with col2:
        sort_label = st.selectbox("Ordenar", ["Específico","Maior comissao", "Mais recentes"])
    with col3:
        listType = st.selectbox("Ordenar", ["Padrão", "Produtos em promoção"])
    with col4:
        preco_min = st.number_input("Preco Min", value=10.0)
    with col5:
        preco_max = st.number_input("Preco Max", value=10000.0)
    with col6:
        comissao_min = st.slider("Comissao min", 0.0, 100.0, 3.0)

    page = 1
    limit = int(qt)
    sort_map = { "Específico": 1, "Mais recentes": 2, "Maior comissao": 5}
    list_map = {"Padrão": 0, "Produtos em promoção": 1}

    if st.button("BUSCAR",):
        Del_B_TEMPORARIOS()

        with st.spinner("Carregando..."):
            data = buscar_produtos(str(keyword).title(), list_map[listType], sort_map[sort_label], page, limit)

        if "errors" in data:
            st.error(f"API Error: {data['errors']}")
            st.stop()

        if "data" not in data or not data["data"]["productOfferV2"]["nodes"]:
            st.warning("Sem produtos")
            st.stop()

        nodes = data["data"]["productOfferV2"]["nodes"]
        df = pd.DataFrame(nodes)
        df["price"] = pd.to_numeric(df["price"], errors='coerce')
        df["commissionRate"] = pd.to_numeric(df["commissionRate"], errors='coerce')
        df["commissionValue"] = df["price"] * df["commissionRate"]
        df["imagem"] = df["imageUrl"]

        df_filtrado = df[
            (df["price"] >= preco_min) &
            (df["price"] <= preco_max) &
            (df["commissionValue"] >= comissao_min)
        ].copy()

        if df_filtrado.empty:
            st.warning("Sem produtos nos filtros. Mostrando todos:")
            df_filtrado = df.copy()

        st.success(f"{len(df_filtrado)} produtos encontrados!")

        for i in range(0, len(df_filtrado), 3):
            cols = st.columns(3)

            for j, (idx, row) in enumerate(df_filtrado.iloc[i:i + 3].iterrows()):
                with cols[j]:
                    cat_ids = row.get('productCatIds')
                    if cat_ids and isinstance(cat_ids, list) and len(cat_ids) >= 3:
                        LINK = f"https://shopee.com.br/product/{row['shopId']}/{row['itemId']}"

                        esc_B_TEMPORARIOS(row['itemId'],row['shopId'],row['productName'], row["imagem"], row['shopName'], cat_ids[1], cat_ids[2], round(float(row['price']),2),
                                          round(float(row['commissionValue']),2), LINK,'')

    from Banco_Shopee import ler_B_TEMPORARIOS, ler_A_CAT,esc_B_DADOS_AFILIADOS

    lista = ler_B_TEMPORARIOS()
    qt_col = 1
    st.markdown("### Produtos recomendados para vender")
    top_produtos = produtos_mais_vendaveis(lista, top_n=len(lista))
    for p, indice in top_produtos:
        st1, st2, st3, st4, st5 = st.columns([1,3, 1, 1,1])
        st1.image(p[3], width=50)
        st2.markdown(f"**{p[2]}**")
        st3.metric("Preço", f"R$ {p[7]}")
        st4.metric("% Lucro", f"{calcular_porcentagem_lucro(float(p[7]), float(p[8]))}%")
        st5.metric("Comissão", f"R$ {p[8]}")
    for im in range(0, len(lista), qt_col):
        linha = st.columns(qt_col)
        for j, i in enumerate(lista[im:im + qt_col]):
            with linha[j]:
                st.markdown("---")
                LINK_ORIGINAL_NAO_PUBLICO = f"https://shopee.com.br/product/{i[1]}/{i[0]}"
                st.markdown(
                    f'<a href="{LINK_ORIGINAL_NAO_PUBLICO}" target="_blank">'
                    f'<button style="margin: 10px; padding: 5px; background-color: #f0f0f0;font-size: 16px; '
                    f'border: none; border-radius: 5px; cursor: pointer; color: #BD5908 ;">'
                    f'<b>**{i[2][:63].strip()}**</b></button>'
                    f'</a>', unsafe_allow_html=True
                )
                col_a, col_b = st.columns(2)
                col_b.markdown(f"Loja: **{i[4].strip()}**")
                cat2, link1 = ler_A_CAT(col_b, i[5])
                cat3, link2 = ler_A_CAT(col_b, i[6])

                if cat2 != None:
                    col_b.markdown(
                        f'<a href="{link1}" target="_blank">'
                        f'<button style="margin: 10px; padding: 5px; background-color: gray;font-size: 16px; '
                        f'border: none; border-radius: 5px; cursor: pointer; color: #f0f0f0;">'
                        f'<b>{cat2}</b></button>'
                        f'</a>', unsafe_allow_html=True)

                if cat3 != None:
                    col_b.markdown(
                        f'<a href="{link2}" target="_blank">'
                        f'<button style="margin: 10px; padding: 5px; background-color: gray;font-size: 16px; '
                        f'border: none; border-radius: 5px; cursor: pointer; color: #f0f0f0;">'
                        f'<b>{cat3}</b></button>'
                        f'</a>', unsafe_allow_html=True)


                with col_b:
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Preco", f"R$ {i[7]}")
                    c2.metric("%", f" {calcular_porcentagem_lucro(float(i[7]),float(i[8]))}")
                    c3.metric("Comissao", f"R$ {i[8]}")

                if i[3]:
                    col_a.image(i[3], width=220)
                if existe_em_C_ONLINE_BAIXADOS(i[0]) == False:
                    #if st.button(f"🔗 Afiliado R${i[8]}",key=f"btn_{i[0]}",use_container_width=True):
                    origin_url = f"https://shopee.com.br/product/{int(i[1])}/{int(i[0])}"

                    from Function import gerar_link_public0_shopee
                    link_pul = gerar_link_public0_shopee(i[2],int(i[1]),int(i[0]))

                    link_af = GERAR_link_afiliado(origin_url)
                    link_ct1 = GERAR_link_afiliado(link1)
                    link_ct2 = GERAR_link_afiliado(link2)
                    from Pag_Chats_IA import IA
                    raio_X = IA(RAIO_X_PRODUTO_(link_pul))
                    with st.expander('Descrição Gerada!'):
                        st.write(raio_X)


                    esc_B_DADOS_AFILIADOS(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],
                                              origin_url,link_pul, link_af, link_ct1, link_ct2,
                                              f'{cat2},{cat3}',raio_X)

                    st.success("✅ Produto cadastrado  B_DADOS_AFILIADOS com sucesso!")

                    ID_PROD = i[0]
                    produto = i[2]
                    link_IMAG = i[3]
                    link = link_pul
                    link_afiliad = link_af
                    link_cat_1 = link_ct1
                    link_cat_2 = link_ct2

                    # --------------------------------------------------------------

                    st1, st2 = st.columns(2)
                    LINK = st1.text_input('LINK PUBLICO:', link)

                    LINK_AFILIADO = st1.text_input("Link Afiliado", link_afiliad)
                    st1.text_input("Link Categoria 1", link_cat_1)


                    st1.code(f"Categoria Principal: {cat2} , {cat3}")

                    IMAGEM = st2.text_input("Link da Imagem", link_IMAG)
                    DESCRITION = st2.text_area("Descrição do Produto", raio_X)


                    if not LINK_AFILIADO.strip():
                        st.error("⚠️ O ID do produto é obrigatório.")
                    else:  # ID_PROD, TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2,OUTROS
                        esc_A_PROD_ENTRADA(ID_PROD,produto.strip(), DESCRITION.strip(),IMAGEM.strip(),
                                           link_cat_1, # henrique o LINK_ORIGINAL esta recebendo o link afiliado categoria
                                           LINK_AFILIADO, cat2.strip(),cat3.strip(),link_cat_1)

                        st.success("✅ Produto cadastrado  A_PROD_ENTRADA com sucesso!")
                    st0, st1, st2 = st.columns([1, 8, 2])

                    IDES_NOVOS = []
                    for links in ler_A_PROD_ENTRADA():
                        if existe_em_C_ONLINE_BAIXADOS(links[0]):
                            pass
                        else:
                            IDES_NOVOS.append(links[0])
                    st.title(f"🔥 Postando! {IDES_NOVOS}" if len(IDES_NOVOS) != 0 else "Nada a Postar!!!")

                    st1.code(f'{ID_PROD} : {produto}')
                    st0.write(f"{len(IDES_NOVOS)}")
                    if st2.button('Apagar:', key=ID_PROD):
                        st.error(f'APAGANDO ID:`{ID_PROD} / {ID_PROD} = {Del_A_PROD_ENTRADA(ID_PROD)}')
                        st.rerun()

                    extrair_dados(st, ID_PROD, produto, raio_X, link_afiliad, link_cat_1,link_IMAG, cat2, cat3)
                    Del_B_TEMPORARIOS()
                    st.balloons()
                else:
                    st.warning(f'{i[0]}, {i[1]}, {i[2]} Já em SITES')

    st.markdown("---")











