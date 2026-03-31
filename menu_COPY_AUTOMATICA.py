import json

from slugify import slugify


from Banco_Dados import esc_A_PROD_ENTRADA, ler_COPY_PRODUTO, ler_A_PROD_ENTRADA, existe_em_C_ONLINE_BAIXADOS, \
	Del_A_PROD_ENTRADA, esc_A_PROD_SAIDA, esc_C_ONLINE
from Function import salvar_copy_produto, upload_image_freeimage, limpar_texto_contexto, remover_chaves
from Pag_Chats_IA import OLLAMA_CHAT_IA, OLLAMA_CHAT_IA_jason
from Prompts_HTML import PROMPT_ANALISE, PROMPT_MARK, CRIAR_Imagen_intro, Contextualizar_Chat, gerar_html_seo


def extrair_dados(st,ID_PROD,NOME_PROD_ORIG,DESCRIT_ORIGINAL,LINK_AFILIADO,LINK_CATEGORIA,LIMK_IMAGEM,CATEG1,CATEG2):

    # ==============================
    contexto = Contextualizar_Chat(limpar_texto_contexto(f"{NOME_PROD_ORIG}\n{DESCRIT_ORIGINAL}"))
    json_result = OLLAMA_CHAT_IA_jason(DESCRIT_ORIGINAL, contexto)

    data = json.loads(json_result)
    tam_1 = [2, 8]
    tam_ = [2, 3, 5]

    st1, st2 = st.columns(tam_1)  # 4️⃣ Título SEO
    TITULO_PAG = remover_chaves(data.get("title_seo_", ""))
    st1.write("**🎯 Título da Página (SEO):**")
    st2.code(f"{TITULO_PAG}".upper())

    st1, st2 = st.columns(tam_1)  # 5️⃣ H1 Título Principal
    TITULO_POST = remover_chaves(data.get("title_h2_", ""))
    st1.write("**📢 H1 Título Principal:**")
    st2.code(f"{TITULO_POST}".title())

    st1, st2 = st.columns(tam_1)  # 6️⃣ Introdução Explicativa
    INTRODUTION = remover_chaves(data.get("introduction_", ""))
    st1.write("**🚀 Introdução Explicativa:**")
    st2.code(INTRODUTION)

    st1, st2 = st.columns(tam_1)  # 7️⃣ Meta Description
    DESCRITION = remover_chaves(data.get("card_description_", ""))
    st1.write("**📝 Meta Description:**")
    st2.code(f"{DESCRITION}".capitalize())

    st1, st2, st3 = st.columns(tam_)  # 10️⃣ Seções Contexto, Detalhes, Lista, Comentários
    TITULO_DETALHES = remover_chaves(data.get("title_details_", ""))
    DETALHES = remover_chaves(data.get("parágrafo_details_", ""))
    st1.write("**🔍 Detalhes:**")
    st2.code(f"{TITULO_DETALHES}".capitalize())
    st3.code(f"{DETALHES}".capitalize())
    st1, st2, st3 = st.columns(tam_)  # 10️⃣ Seções Contexto, Detalhes, Lista, Comentários


    TITULO_LISTA = remover_chaves(data.get("benefits_title_", ""))
    LISTA = remover_chaves(data.get("benefits_list_", ""))
    st1.write("**📋 Lista:**")
    st2.code(f"{TITULO_LISTA}".capitalize())
    st3.code(f"{LISTA}".capitalize())

    st1, st2 = st.columns(tam_1)  # 11️⃣ FAQ
    TITULO_FAQ = remover_chaves(data.get("h2_faq_title_", ""))
    st1.write("**❓ Título FAQ (H2):**")
    st2.code(f"{TITULO_FAQ}".capitalize())

    FAQ = remover_chaves(data.get("parágrafo_faq_", ""))
    st1.write("**🤔 FAQ:**")
    st2.code(FAQ)

    st1, st2 = st.columns(tam_1)  # 12️⃣ ALT SEO
    DESC_IMAGEM = remover_chaves(data.get("alt_image_", ""))
    st1.write("**🖼️ ALT SEO:**")
    st2.code(f"{DESC_IMAGEM}")

    st1, st2 = st.columns(tam_1)  # 8️⃣ Link do site
    LINK_SIT = f"https://www.aquiachei.top/{slugify(data.get('title_seo_', ''))}"
    st1.write("**🔗 Link do Site:**")
    st2.code(f"{LINK_SIT}")

    st.subheader("🏷️ MARCADORES DO SITE (copiar)")

    CHAVES = str(data['keywords_']).strip(',')

    gerar_html = gerar_html_seo(st,ID_PROD, TITULO_PAG, TITULO_POST, INTRODUTION, DESCRITION,
                                TITULO_DETALHES[0:100], DETALHES,
                                TITULO_LISTA[0:100], LISTA, TITULO_FAQ, FAQ,DESC_IMAGEM,
                                CHAVES, LINK_AFILIADO,LINK_CATEGORIA, LIMK_IMAGEM,LINK_SIT,[CATEG1,CATEG2])
    st.success('Salvo com Sucesso, se for salvar denovo deslisigar: esc_D_LINKS !')

    esc_A_PROD_SAIDA(ID_PROD, TITULO_PAG, TITULO_POST, INTRODUTION, DESCRITION,
                     TITULO_DETALHES, DETALHES,
                     TITULO_LISTA, LISTA, TITULO_FAQ, FAQ,
                     LINK_SIT,LINK_AFILIADO,  DESC_IMAGEM, CHAVES,CATEG1,CATEG2,'OUTROS')

    esc_C_ONLINE(ID_PROD,NOME_PROD_ORIG, TITULO_PAG, LINK_SIT, CATEG1,CATEG2)

    st.subheader("HTML Gerado")
    with st.expander('HTML Gerado'):
        st.code(gerar_html, language="html")
    st.success(f'Publicado em: {NOME_PROD_ORIG}')


def COPY_AUTOMATICO(st):
	from shopee_api import Api_Shopee, Api_Shopee_LOOP_INFINITO
	Api_Shopee_LOOP_INFINITO(st)

