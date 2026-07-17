import json

from slugify import slugify

from shopee_api import Api_Shopee
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


def COPY_SIMPLES(tt):
	import  streamlit as st
	st1, st2 = st.columns(2)
	st.title("📦 Cadastro Manual de Produtos")


	st.header("Dados do Produto")
	with st.expander('API:'):
		Api_Shopee(st)
	from Function import card_mostra
	from Banco_Shopee import ler_B_DADOS_AFILIADOS

	card_mostra(ler_B_DADOS_AFILIADOS()[-1][0])
	col_SITE, col_VIDEO = st.columns(2)
	REDES_SOCIAL = col_VIDEO.text_area('Redes Sociais:', f'''SITES: 
https://www.aquiachei.top
https://www.acheitop.top

YouTube: https://youtube.com/@achei-top
YouTube: https://youtube.com/@topcodebuytrap
TikTok: https://tiktok.com/@topcodebuytrap
Instagram: https://instagram.com/granazoada
Twitter / X: https://x.com/granazoada
Liste exatamente como fornecido.
		''',height=250)
	with (col_SITE):
		ULT_ID = ler_B_DADOS_AFILIADOS()[-1][0]
		produto = ler_B_DADOS_AFILIADOS()[-1][2]
		link_IMAG = ler_B_DADOS_AFILIADOS()[-1][3]
		link = ler_B_DADOS_AFILIADOS()[-1][10]
		link_afiliad = ler_B_DADOS_AFILIADOS()[-1][11]
		link_cat_1 = ler_B_DADOS_AFILIADOS()[-1][12]
		link_cat_2 = ler_B_DADOS_AFILIADOS()[-1][13]
		categoria = ler_B_DADOS_AFILIADOS()[-1][14]
		raio_x = ler_B_DADOS_AFILIADOS()[-1][15]

		c1, c2, c3, c4, c5 = st.columns([4, 3, 2, 3, 2])
		c3.write('')
		c4.write('')
		LINK = c1.text_input('LINK:', link)
		if st.button("MONTAR PROMPT IMAGEM", use_container_width=True):
			# -------"CAPA DE INTRO"
			imag = OLLAMA_CHAT_IA(CRIAR_Imagen_intro(raio_x))
			if imag == None:
				st.error(f'PROMPT CAPAS FALHOU!')
			CAPAS_P = F'BASEADO NESSA IMAGEM:\nE NEESE TEXT:\n{raio_x}\n------- CRIE IMAGENS:\n{imag}'
			with st.expander('Questiona ia!'):
				st.code(CRIAR_Imagen_intro(raio_x))
			with st.expander('Resposta ia!'):
				st.code(CAPAS_P)

			# ---------- PARTE QUE CRIA A PASTA DO DOWNLOADS COM OS ARQUIVOS
			from Criando_Pasta_Arquivos import baixar_imagem_e_criar_pasta
			new_past = limpar_texto_contexto(produto)
			baixar_imagem_e_criar_pasta(link_IMAG,new_past , raio_x, 'raio_x')
			st.success(f"✅ Pasta {new_past} Criada com sucesso!")

		# --------------------------------------------------------------

		def image_input(col,col2, label):
			# link = col.text_input(f"{label} (URL)")
			file = col.file_uploader(f"{label} (Upload)", type=["png", "jpg", "jpeg"])

			if file:
				url = upload_image_freeimage(file)
				if url:
					#col2.write(url)
					col2.image(url)
				else:
					col2.error("Erro ao enviar imagem")
				return url
			else:
				#col2.write(link_IMAG)
				col2.image(link_IMAG)
				return link_IMAG

			return link

		c1, c2, c3 = st.columns(3)

		IMAGEM_1 = image_input(c1,c2, "CAPA DE INTRO")

		# --------------------------------------------------------------
	st1, st2 = st.columns(2)

	st1.text_input("Link Imagem a ser Enviada",IMAGEM_1)
	LINK_AFILIADO = st1.text_input("Link Afiliado",link_afiliad)

	# 🛠️ CORREÇÃO CIRÚRGICA CONTRA VALOR NULO (KISS)
	if categoria:
		cat_limpa = categoria.replace('[','').replace(']','')
		partes_cat = [c.strip() for c in cat_limpa.split(',') if c.strip()]
		cat2 = partes_cat[0] if len(partes_cat) > 0 else "Geral"
		cat3 = partes_cat[1] if len(partes_cat) > 1 else "Diversos"
	else:
		cat2 = "Geral"
		cat3 = "Diversos"

	st1.code(f"Categoria Principal: {cat2} , {cat3}")

	IMAGEM = st2.text_input("Link da Imagem",IMAGEM_1)
	DESCRITION = st2.text_area("Descrição do Produto",raio_x)

	btn_cadastrar = st2.button("✅ Cadastrar Produto")

	if btn_cadastrar:
		if not LINK_AFILIADO.strip():
			st.error("⚠️ O ID do produto é obrigatório.")
		else: # ID_PROD, TITULO, DESCRITION, IMAGEM, LINK_ORIGINAL, LINK_AFILIADO, CATEGORIA_1, CATEGORIA_2,OUTROS
			esc_A_PROD_ENTRADA(ULT_ID,
				produto.strip(),
				DESCRITION.strip(),
				IMAGEM.strip(),
				link_cat_1,     # henrique o LINK_ORIGINAL esta recebendo o link afiliado categoria
				LINK_AFILIADO,
				cat2.strip(),
				cat3.strip(),
				link_cat_2
			)

			st.success("✅ Produto cadastrado com sucesso!")
	st0, st1, st2 = st.columns([1, 8, 2])

	IDES_NOVOS = []
	for link in ler_A_PROD_ENTRADA():
		if existe_em_C_ONLINE_BAIXADOS(link[0]):
			pass
		else:
			IDES_NOVOS.append(link[0])
	st.title(f"🔥 Postando! {IDES_NOVOS}" if len(IDES_NOVOS) != 0 else "Nada a Postar!!!")

	for p, i in enumerate(IDES_NOVOS):
		ID_PROD = i

		NOME_PROD_ORIG = ler_A_PROD_ENTRADA(ID_PROD, 'TITULO')[0][0]
		DESCRIT_ORIGINAL = ler_A_PROD_ENTRADA(ID_PROD, 'DESCRITION')[0][0]
		LINK_CATEGORIA = ler_A_PROD_ENTRADA(ID_PROD, 'LINK_ORIGINAL')[0][0]

		LINK_AFILIADO = ler_A_PROD_ENTRADA(ID_PROD, 'LINK_AFILIADO')[0][0]
		LIMK_IMAGEM = ler_A_PROD_ENTRADA(ID_PROD, 'IMAGEM')[0][0]
		CATEG1 = ler_A_PROD_ENTRADA(ID_PROD, 'CATEGORIA_1')[0][0]
		CATEG2 = ler_A_PROD_ENTRADA(ID_PROD, 'CATEGORIA_2')[0][0]
		st1.code(f'{ID_PROD} : {NOME_PROD_ORIG}')
		st0.write(f"{p} de {len(IDES_NOVOS)}")
		if st2.button('Apagar:', key=ID_PROD):
			st.error(f'APAGANDO ID:`{ID_PROD} / {ID_PROD} = {Del_A_PROD_ENTRADA(ID_PROD)}')
			st.rerun()

		extrair_dados(st,ID_PROD, NOME_PROD_ORIG, DESCRIT_ORIGINAL, LINK_AFILIADO, LINK_CATEGORIA, LIMK_IMAGEM, CATEG1,
		              CATEG2)
