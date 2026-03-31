from time import sleep


from Automa_Post_Blog import publicar_no_blogger, get_service
from Banco_Dados import esc_D_LINKS, ler_COPY_PRODUTO_video, ler_COPY_PRODUTO, \
    esc_COPY_PRODUTO_MIDIA, ler_COPY_PRODUTO_MIDIA, esc_P_PROMPTS_COPY_PRODUTOS, ler_P_PROMPTS_COPY_PRODUTOS, Del_P_PROMPTS_COPY_PRODUTOS, \
    ATUAL_P_PROMPTS_COPY_PRODUTOS, ATUAL_COPY_PRODUTO_MIDIA
from Criando_Pasta_Arquivos import adicionar_arquivo_pasta
from Function import salvar_copy_produto, wrap_text, upload_image_freeimage, gerar_qr, \
    youtube_to_embed

from Prompts_HTML import PROMPT_ANALISE, PROMPT_MARK, PROMPT_produtos_vendas_DESCRTT_youtube, gerar_html_seo_video, CRIAR_Imagen_intro
from Pag_Chats_IA import IA


def COPY_ADVENT(st):
	from shopee_api import Api_Shopee
	ULT_ID = str(ler_COPY_PRODUTO()[-1][0]).strip()
	ULT_NOM = ler_COPY_PRODUTO()[-1][2]

	st.header("Dados do Produto")
	with st.expander('API:'):
		Api_Shopee(st)
	from Function import card_mostra
	from Banco_Shopee import ler_B_DADOS_AFILIADOS

	card_mostra(ler_B_DADOS_AFILIADOS()[-1][0])
	col_SITE, col_VIDEO = st.columns(2)
	REDES_SOCIAL = st.text_input('Redes Sociais:', f'''
	SITE: 
	https://www.aquiachei.top
	https://www.acheitop.top

	YouTube: https://youtube.com/@achei-top
	YouTube: https://youtube.com/@topcodebuytrap
	TikTok: https://tiktok.com/@topcodebuytrap
	Instagram: https://instagram.com/granazoada
	Twitter / X: https://x.com/granazoada
	Liste exatamente como fornecido.
	''')
	with (col_SITE):
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
		CATEGORIA = c2.text_input('CATEGORIA:', categoria)
		TESTAR = c4.checkbox('TESTAR PISC:')

		if c3.button('CRIAR:'):
			if TESTAR == False:
				permit = IA(PROMPT_ANALISE(LINK))
				if permit == 'RESULTADO_FINAL_ = TRUE':
					prop = IA(PROMPT_MARK(LINK))
					with st.expander('Resposta ia!'):
						st.write(prop)
					print('=======', prop)
					c5.success('TRUE')
					salvar_copy_produto(prop.replace("*", "").replace("/", ""), CATEGORIA)
				else:
					c5.error('False')
			else:
				prop = IA(PROMPT_MARK(LINK))
				with st.expander('Questiona ia!'):
					st.code(PROMPT_MARK(LINK))
				with st.expander('Resposta ia!'):
					st.write(prop)

			# ---------- PARTE QUE CRIA A PASTA DO DOWNLOADS COM OS ARQUIVOS
			from Criando_Pasta_Arquivos import baixar_imagem_e_criar_pasta
			from Prompts_HTML import gerar_texto_txt_site
			res = []
			for i in ler_COPY_PRODUTO_video(ULT_ID)[0]:
				res.append(i)
			texto_para_criar_video = str(wrap_text('\n\n'.join(res), width=80))
			texto_sit = gerar_texto_txt_site(ULT_ID)
			baixar_imagem_e_criar_pasta(link_IMAG, produto, texto_para_criar_video,'Para Video', texto_sit)
		# --------------------------------------------------------------

		st.text_input('Titulo', ULT_NOM)

		c1, c2, c3 = st.columns(3)
		LINK_FIL_1 = c1.selectbox('Botão 1:',
		                          [f'Comprar {produto}', 'Ver Oferta Principal ', 'Produto Similar Disponível',
		                           'Ver Outra Oferta', 'Ver Mais Opções da Categoria'])
		LINK_FIL_2 = c2.selectbox('Botão 2:', ['Ver Outra Oferta', 'Comprar Agora', 'Ver Oferta Principal ',
		                                       'Produto Similar Disponível', 'Ver Mais Opções da Categoria'])
		LINK_FIL_3 = c3.selectbox('Botão 3:',
		                          [f'Outras Opções {categoria.split(",")[0]}', 'Comprar Agora', 'Ver Oferta Principal ',
		                           'Produto Similar Disponível', 'Ver Outra Oferta'])

		LINK_FILIADO_1 = c1.text_input('AFILIADO shopee:', link_afiliad)
		LINK_FILIADO_2 = c2.text_input('AFILIADO amazon:', )
		if LINK_FILIADO_2:
			ATUAL_COPY_PRODUTO_MIDIA(ULT_ID, 'LINK_AFILIADO_2', LINK_FILIADO_2, )
		LINK_FILIADO_3 = c3.text_input('AFILIADO categoria:', link_cat_1)
		with st.expander('2 passo montar prompts'.upper()):
			from Prompts_HTML import CRIAR_chamada_para_acao, CRIAR_ABERTURA_GROK
			res = []
			# ULT_ID = ler_COPY_PRODUTO()[-1][0]
			CHAMA_ACTION = ler_COPY_PRODUTO()[-1][-2]
			INTRO = F'{ler_COPY_PRODUTO()[-1][3]} {ler_COPY_PRODUTO()[-1][4]}'
			ABERTURA = F'{ler_COPY_PRODUTO()[-1][6]} {ler_COPY_PRODUTO()[-1][7]}'
			for i in ler_COPY_PRODUTO_video(ULT_ID)[0]:
				res.append(i)

			if st.button("MONTAR PROMPTS", use_container_width=True):
				Del_P_PROMPTS_COPY_PRODUTOS(ULT_ID)
				texto_para_criar_video = str(wrap_text('\n\n'.join(res), width=80)).replace('"', ''
				                                                                            ).replace('[', '').replace(
					']', '')
				# -------"CAPA DE INTRO"
				imag = IA(CRIAR_Imagen_intro(texto_para_criar_video))
				if imag == None:
					st.error(f'PROMPT CAPAS FALHOU!')
				sleep(5)
				CAPAS_P = F'BASEADO NESSA IMAGEM:\nE NEESE TEXT:\n{texto_para_criar_video}\n------- CRIE IMAGENS:\n{imag}'
				INTRO_VIDEO = IA(CRIAR_ABERTURA_GROK(INTRO))
				if imag == INTRO_VIDEO:
					st.error(f'PROMPT INTRO VIDEO VIDEO FALHOU!')
				sleep(5)
				ABET_VIDEO = IA(CRIAR_ABERTURA_GROK(ABERTURA))
				if imag == ABET_VIDEO:
					st.error(f'PROMPT ABERTURA VIDEO FALHOU!')
				sleep(5)
				CHAMADA_VIDEO = IA(CRIAR_chamada_para_acao(texto_para_criar_video, CHAMA_ACTION))
				if imag == CHAMADA_VIDEO:
					st.error(f'PROMPT CHAMADA VIDEO FALHOU!')
				esc_P_PROMPTS_COPY_PRODUTOS(ULT_ID, CAPAS_P, INTRO_VIDEO, ABET_VIDEO, CHAMADA_VIDEO, '')
				st.success(imag)
				text_promt = f'''
	                    -------------------- PARA CAPA: ---------------------------
	                                        {CAPAS_P}\n 
	                    -------------------- PARA INTRO DO VIDEO: -------------------- 
	                                        {INTRO_VIDEO}\n
	                    -------------------- PARA ABERTURA DO VIDEO: -------------------- 
	                                        {ABET_VIDEO}\n
	                    -------------------- PARA CHAMAD FINALDO VIDEO: -------------------- 
	                                        {CHAMADA_VIDEO}\n
	                                '''
				adicionar_arquivo_pasta(produto, '', text_promt, 'Prompts COPY')
			P1, P2, P3, P4 = st.columns(4)
			ppt_cap = ler_P_PROMPTS_COPY_PRODUTOS(ULT_ID)[0][1]
			ppt_int = ler_P_PROMPTS_COPY_PRODUTOS(ULT_ID)[0][2]
			ppt_abet = ler_P_PROMPTS_COPY_PRODUTOS(ULT_ID)[0][3]
			ppt_cham = ler_P_PROMPTS_COPY_PRODUTOS(ULT_ID)[0][4]
			if ppt_cap:
				P1.code(f'CAPAS:, {ppt_cap}')
			else:
				if P1.button('CAPAS'):
					imag = IA(CRIAR_Imagen_intro(texto_para_criar_video))
					CAPAS_P = F'BASEADO NESSA IMAGEM:\nE NEESE TEXT:\n{texto_para_criar_video}\n------- CRIE IMAGENS:\n{imag}'
					ATUAL_P_PROMPTS_COPY_PRODUTOS(ULT_ID, 'CAPAS', IA(CRIAR_ABERTURA_GROK(CAPAS_P)))
					st.rerun()

			if ppt_int:
				P2.code(f'INTRODUÇÃO:, {ppt_int}')
			else:
				if P2.button('INTRODUÇÃO'):
					ATUAL_P_PROMPTS_COPY_PRODUTOS(ULT_ID, 'INTRO_VIDEO', IA(CRIAR_ABERTURA_GROK(INTRO)))
					st.rerun()

			if ppt_abet:
				P3.code(f'ABERTURA:, {ppt_abet}')
			else:
				if P3.button('ABERTURA'):
					ATUAL_P_PROMPTS_COPY_PRODUTOS(ULT_ID, 'ABET_VIDEO', IA(CRIAR_ABERTURA_GROK(ABERTURA)))
					st.rerun()

			if ppt_cham:
				P4.code(f'CHAMADA:, {ppt_cham}')
			else:
				if P4.button('CHAMADA'):
					ATUAL_P_PROMPTS_COPY_PRODUTOS(ULT_ID, 'CHAMADA_VIDEO', IA(CRIAR_ABERTURA_GROK(CHAMA_ACTION)))
					st.rerun()
		# ------ parte de gerar qr code
		if 1 + 1 == 2:
			logo_qr = ''
			cor_fundo = ''
			c1, c2, c3 = st.columns(3)
			link = c1.text_input("Link Qr-Code", )
			if c1.radio('COR QR', ['Clara', 'Escura']) == 'Clara':
				cor_fundo = '#FFFFFF'
				logo_qr = 'qr_branca.jpeg'
			else:
				cor_fundo = '#000000'
				logo_qr = 'qr_preta.jpg'
			texto_QR = ''
			c2.write(' ')
			if c2.button("Gerar QR Code"):
				if link:
					qr_img = gerar_qr(
						link,
						'#FD650D',
						cor_fundo,
						logo_qr,
						texto_QR
					)

					c3.image(qr_img)
					c2.download_button(
						"Baixar QR Code",
						qr_img,
						file_name="qr_afiliado.png",
						mime="image/png"
					)
				else:
					st.error("Informe o link")

		def image_input(col, label):
			# link = col.text_input(f"{label} (URL)")
			file = col.file_uploader(f"{label} (Upload)", type=["png", "jpg", "jpeg"])

			if file:
				url = upload_image_freeimage(file)
				if url:
					col.write(url)
					col.image(url)
				else:
					col.error("Erro ao enviar imagem")
				return url

			return link

		c1, c2, c3 = st.columns(3)

		IMAGEM_1 = image_input(c1, "CAPA DE INTRO")
		IMAGEM_2 = image_input(c2, "CAPA DO PRODUTO")
		IMAGEM_3 = image_input(c3, "CAPA DO VIDEO")

		if IMAGEM_1 and IMAGEM_2 and IMAGEM_3:  # -------- se tiver as 3 imagens monta o html
			esc_COPY_PRODUTO_MIDIA(ULT_ID, '', '', link_afiliad, '',
			                       link_cat_1, IMAGEM_1, IMAGEM_2, IMAGEM_3, '')
	with col_VIDEO:
		with st.expander('Criar Video'):

			res = []
			for i in ler_COPY_PRODUTO_video(ULT_ID)[0]:
				res.append(i)
			texto_para_criar_video = str(wrap_text('\n\n'.join(res), width=80))
			if st.checkbox(f'{len(texto_para_criar_video)} Com Marcação Chaves'):
				st.markdown(texto_para_criar_video.replace('"', '').replace('[', '**').replace(']', '**'))
			else:
				st.code(texto_para_criar_video, language="python")

			# ----------------- MONTAR A DESCRIÇÃO DO YOUTUBE VIDEO
			c1, c2, c3 = st.columns(3)
			VIDEO = c1.text_input('LINK DO VIDEO CRIADO PARA YOUTUBE:', )
			coontexto = PROMPT_produtos_vendas_DESCRTT_youtube(LINK, LINK_FIL_1, LINK_FILIADO_1, LINK_FIL_2, LINK_FILIADO_2, LINK_FIL_3,
			                          LINK_FILIADO_3, REDES_SOCIAL)
			c2.write('')
			if c2.button('Montar'):

				# Del_COPY_PRODUTO_MIDIA()
				st.code(coontexto)
				desc = str(IA(coontexto)).replace('*', '').replace('---', '')
				esc_COPY_PRODUTO_MIDIA(ULT_ID, desc, VIDEO, LINK_FILIADO_1, LINK_FILIADO_2,
				                       LINK_FILIADO_3, IMAGEM_1, IMAGEM_2, IMAGEM_3, youtube_to_embed(VIDEO))
				if desc == None:
					st.success('Essa desg... nao funcionou!')
				ATUAL_COPY_PRODUTO_MIDIA(ULT_ID, 'DESCRIT_VIDEO', desc)
				ATUAL_COPY_PRODUTO_MIDIA(ULT_ID, 'VIDEO_LINK', VIDEO)
				ATUAL_COPY_PRODUTO_MIDIA(ULT_ID, 'VIDEO', youtube_to_embed(VIDEO))
				st.rerun()

			# ------------ PARTE QUE LE A DESCRIÇÃO
			try:
				ID_PROD_MID = ler_COPY_PRODUTO_MIDIA(ULT_ID)[-1][0]
				DESC_PROD_MID = ler_COPY_PRODUTO_MIDIA(ULT_ID)[0][1]
				texto_wrap = wrap_text(DESC_PROD_MID, width=80)
				st.code(texto_wrap, language="python")
			except IndexError:
				pass
	with col_VIDEO:
		with st.expander('Criar HTML'):
			st.title("Preview de HTML")
			try:
				html, MARCATION, TITULO_SEO_H1, PALAVRAS_CHAVES = gerar_html_seo_video(ID_PROD_MID, LINK_FIL_1,
				                                                                       LINK_FIL_2, LINK_FIL_3)
				import streamlit.components.v1 as components
				if st.button('publicar'):
					service = get_service()
					blog_id_AQUI_ACHEI = '3695058109147479032'  # Aqui Achei
					blog_id_ACHEI_TOP = '413958215810482139'  # Achei Top

					publicar_no_blogger(service, blog_id_AQUI_ACHEI, TITULO_SEO_H1.upper(), [MARCATION], html,
					                    rascunho=False)
					url = publicar_no_blogger(service, blog_id_ACHEI_TOP, TITULO_SEO_H1.upper(), [MARCATION], html,
					                          rascunho=False)

					for PALAVRA in PALAVRAS_CHAVES.split(','):
						esc_D_LINKS(str(PALAVRA).strip().title(), TITULO_SEO_H1, url)
					st.success('Salvo com Sucesso, se for salvar denovo deslisigar: esc_D_LINKS !')

				cch1 = '{'
				cch2 = '}'
				components.html(f'''
	                <!DOCTYPE html>
	                <html lang="pt-BR">
	                <head>
	                    <meta charset="UTF-8">
	                    <title>Página Simples</title>
	                    <style>
	                        body {cch1}
	                            margin: 0;
	                            padding: 0;
	                            background-color: #ffffff;
	                            font-family: Arial, Helvetica, sans-serif;
	                        {cch2}
	                    </style>
	                </head>
	                <body>
	                <h1> {TITULO_SEO_H1} </h1> <br>
	                {html}
	                </body>
	                </html>

	                '''
				                ,
				                height=1000,
				                scrolling=True
				                )


			except UnboundLocalError:
				pass
	st.code(html)