import re

from time import sleep

from Automa_Post_Blog import publicar_no_blogger, get_service
from Banco_Dados import ler_COPY_PRODUTO, ler_COPY_PRODUTO_sit, ler_COPY_PRODUTO_MIDIA

from Function import formatar_chaves_coloridas, youtube_to_embed


def Regaras_Respostas_IA():
    return ''' 
    
REGRAS BASICAS PARA IA:--------------------------------
Não escreva absolutamente nada fora do DE QUE TE PEDI.
Não use markdown, comentários ou explicações.
Não use enfeites emojis, asteriscos caracteres especiais.
Quero apenas o texto claro e objetivo!

TUDO EXATAMENTE do tipo que mais funciona para o algoritmo do YouTube hoje, focado em atrair clique, reter público, e que tenha potencial de viralizar. Não quero padrão, quero alto desempenho.”
“Faça tudo pensado em CTR, retenção e engajamento, usando técnicas que criadores grandes usam para se destacar.”
-------------------------------------------------------

    '''

def Contextualizar_Chat(transcricao_completa):
	return f'''Gemma Responda exclusivamente OS CAMPOS
Não escreva absolutamente nada fora do DE QUE TE PEDI.
Não use markdown, comentários ou explicações.
Todos os campos são obrigatórios.
Não repita títulos ou conteúdos entre campos.
Use linguagem neutra, clara e informativa.

IMPORTANTE SOBRE FORMATO
- Todo campo que NÃO for título deve ser escrito em formato de parágrafo completo.
- Todo campo deve ser otimizada para SEO.
- Não crie títulos fora dos campos de título.

Apenas o campo introduction_:
- Deve ser um parágrafo completo com pelo menos 400 caracteres.
- Insira  em negrito entre <strong> palavras-chaves </strong> de forma natural dentro do texto.
- O texto deve ser fluido, informativo e otimizado para SEO.

No Campos de lista deve ter no mínimo 5 itens e devem ser texto corrido em formato de lista, com itens iniciados por vírgula.
No Campos parágrafo_faq Invente um parágrafo você deve criar algumas pergunta? e você deve criar respostas! relacionadas ao texto.
Todo o conteúdo a seguir deverá ser baseado exclusivamente no texto\n
\n{transcricao_completa}"\n

RESPONDA CAMPOS ABAIXO
title_seo_ = título chamativo e otimizado para SEO do post
title_h2_= título principal com promessa clara.
introduction_ = parágrafo introdutório de pelo menos 400 caracteres, text<strong>chave</strong>  text<strong>chave</strong>  text<strong>chave</strong>
card_description_ = parágrafo resumido dentro do card
title_details_= título focado nos detalhes importantes do texto.
parágrafo_details_= parágrafo explicando os detalhes importantes do texto no mínimo 400 caracteres.
benefits_title_ = título da seção de benefícios (H2)
benefits_list_ = lista de benefícios (mínimo 5 itens cada item iniciado por vírgula)
h2_faq_title_= título para seção de perguntas frequentes.
parágrafo_faq_= parágrafo Você Crie algumas perguntas? e você responde! 
alt_image_= descrição objetiva da imagem com foco em SEO.
keywords_ = palavra - chave principal, variação 1, variação 2, termo relacionado, long tail term
'''


#  keywords_ = [palavra - chave principal, variação 1, variação 2, termo relacionado, long tail term]
#

def RAIO_X_PRODUTO_(LINK):
	return F'''FAZE 1 ----------------------------------------------------------------------------
{Regaras_Respostas_IA()}
COM ESSE LINK FAÇA UM RAIO X COMPLETO:
{LINK}

Analise exclusivamente o produto do link abaixo.
Gere um texto informativo e comercial ao mesmo tempo, próprio para site de vendas.
Informe com clareza, detalhe e objetividade, sempre apresentando característica.
Não critique, não compare negativamente, não levante limitações do produto.
Tudo deve aumentar confiança, entendimento e intenção de compra.

Descrição geral do produto,Como funciona, Como usa, etc....
Linguagem clara, objetiva e profissional.

'''

def CRIAR_ABERTURA_GROK(TEXTO):
    return f'''
`{Regaras_Respostas_IA()}

TEXTO:
{TEXTO}

BASEADO NA FRAZE ACIMA CRIE UM prompt de comando para eu usar em uma IA grok.com, para eu criar 
um vídeo ULTRA REALISTA dinâmico de 15-30 segundos em formato, estilo moderno e atrativo para YouTube, com transições suaves,

Cena inspirada no TEXTO.
Basear-se na auria e filosofia do texto, tentando passar a vibe de ter comprado esse produto.

”'''

def CRIAR_chamada_para_acao(TEXTO,FRAZE):
    return  f'''
`{Regaras_Respostas_IA()}
    
TEXTO:
{TEXTO}

BASEADO NA FRAZE ACIMA CRIE UM prompt de comando para eu usar em uma IA grok.com, para eu criar 
um vídeo dinâmico de 15-30 segundos em formato, estilo moderno e atrativo para YouTube, com transições suaves,
com texto grande aparecendo: "{FRAZE}"

- Início (0-5s): Cena animada inspirada no TEXTO.
- Meio (5-20s): Mostre clipes rápidos e envolventes do tema principal
com imagens geradas por IA, gráficos animados e texto na tela destacando 'Top Code Buy Trap'


NO ESCURO:
Use apenas detalhes sutis de cor para indicar benefício, cores chamativas.
retro games: pixel art, 16-8 bits, efeito sutil de glitch
Cartoon/ação: cores vivas em detalhes (laranja, verde, ciano), elementos dinâmicos
Sério/profissional: contraste DISCRETO (preto + laranja), layout limpo
Incluir elementos simbólicos que representem:
Alguns detalhes em pixel RETRO art 16-bit e 8-bit , sutis, saindo de traz da IMAGEM PRINCIPAL).
Linhas de código discretas e elementos de interface tech ao fundo, composição limpa com foco central,
sem poluição visual criando reflexos controlados alaranjado ou dourado bem suave.

Paleta de cores:
Basear-se na auria e filosofia do texto, tentando passar a vibe de ter comprado esse produto.

”'''

def CRIAR_Imagen_intro(texto):
    return f'''
{texto}

----------------------------------------------------------------

baseado no texto acima:
`{Regaras_Respostas_IA()}
PARA CRIAR 2 IMAGENS COM A FRAZE TEXTO E CRIAR 1 IMAGENS SEM A FRAZE TEXTO na capa ESSE É O ESTILO:
“Imagem estilo thumbnail minimalista e profissional, focada em vendas.
Visual elegante, premium, de alto valor, com aparência profissional e foco total no produto e na mensagem de venda.”

NO FUNDO ESCURO:
Use apenas detalhes sutis de cor para indicar benefício.
Estilo retro games: pixel art, 16-8 bits, efeito sutil de glitch
Cartoon/ação: cores vivas em detalhes (laranja, verde, ciano), elementos dinâmicos
Sério/profissional: contraste DISCRETO (preto + laranja), layout limpo
Incluir elementos simbólicos que representem:
Alguns detalhes em pixel RETRO art 16-bit e 8-bit , sutis, saindo de traz da IMAGEM PRINCIPAL).
Linhas de código discretas e elementos de interface tech ao fundo, composição limpa com foco central,
sem poluição visual criando reflexos controlados alaranjado ou dourado bem suave.

Paleta de cores:
Basear-se na auria e filosofia do texto, tentando passar a vibe de ter comprado esse produto.

IMAGEM DO PRODUTO:
Cena central ou equilibrada, refletindo o clima emocional e a narrativa do texto.
Visual elegante, premium, de alto valor, com aparência profissional e foco total no produto e na venda.”

CRIE UM prompt de comando para eu usar em uma IA, para eu criar uma 
1 imagem para esse produto para thumbnail uma de 16:9 COM TEXTO,
1 imagem para esse produto para thumbnail uma de 9:16 COM TEXTO,
"1 imagem para esse produto para thumbnail uma de 16:9 SEM TEXTO",
 **atenção de DESTAQUE ENFAZE AO CRIAR O PROMPT PARA O PAISAGEM AMBIEMTIZAÇÃO DO FUNDO  SE INSPIRAR NO TEXTO e PARA O TEXTO APARECER NA IMAGEM (destaque o texto) 
E PEÇA PARA NUNCA, NUNCA ALTERERAR A IMAGEM PRINCIPAL DO PRODUTO**


TUDO EXATAMENTE do tipo que mais funciona para o algoritmo do YouTube hoje, focado em atrair clique, reter público, e que tenha potencial de viralizar. Não quero padrão, quero alto desempenho.”
“Faça tudo pensado em CTR, retenção e engajamento, usando técnicas que criadores grandes usam para se destacar.”
'''

def PROMPT_ANALISE(RAIO_X):
	return f'''VOCÊ É UM ANALISTA SÊNIOR DE PRODUTO E PSICOLOGIA DO CONSUMO.

Sua função NÃO é vender.
Sua função é decidir se este produto é psicologicamente vendável em escala para tráfego pago e propaganda direta.

Analise o produto EXCLUSIVAMENTE com base na página informada (título, descrição, imagens, vídeos, preço, avaliações, volume de vendas).
Não invente benefícios.
Não force conclusões.

Avalie silenciosamente TODOS os critérios abaixo (NÃO escreva a análise):

– Existe PROBLEMA real, comum e reconhecível em até 5 segundos?
– O BENEFÍCIO principal é entendido rápido, em uma frase simples?
– O USO é simples, “pegou e usou”, sem curva de aprendizado?
– O valor pode ser PROVADO visualmente em vídeo curto?
– Há PROVA SOCIAL ou sinais claros de adoção?
– O PREÇO parece pequeno diante da dor resolvida?
– O RISCO psicológico é baixo (confiança, segurança, devolução)?
– O produto combina com a IDENTIDADE do público, sem estranheza?

Regra de decisão obrigatória:
Se o produto falhar em 3 ou mais pontos acima → NÃO é escalável.
Se o produto passar na maioria com clareza → É escalável.

FORMATO DE RESPOSTA (REGRA ABSOLUTA)

Responda APENAS com UM campo preenchido.
Não escreva explicações.
Não escreva textos adicionais.
Não use emojis.
Não use markdown fora do campo.

Campo único de retorno:

RESULTADO_FINAL_ = TRUE
ou
RESULTADO_FINAL_ = FALSE

TRUE = Produto psicologicamente vendável em escala
FALSE = NÃO recomendado para propaganda

PRODUTO PARA ANÁLISE:
{RAIO_X}'''

def PROMPT_MARK(LINK):
	return F'''FAZE 1 ----------------------------------------------------------------------------

COM ESSE LINK FAÇA UM RAIO X COMPLETO:
{LINK}

EXTRAIA DADOS DO PRODUTO (ANÁLISE BASE):
Produto: [DESCREVA O PRODUTO AQUI]
Problema real que ele resolve: [Descreva um incômodo cotidiano, comum e muitas vezes ignorado, de forma concreta]
Erro que as pessoas cometem sem perceber: [Explique o hábito errado normalizado, direto e reconhecível]
Solução que o produto oferece: [Mostre como ele corrige o erro de forma simples, prática e lógica]
Facilidade de uso: [Explique por que é intuitivo, seguro e prático]
Preço percebido: [Explique o valor real do produto, custo-benefício, sem exageros]
Palavras chaves: [Liste 8 palavras-chave reais, incluindo variações e long tail; destaque no texto entre colchetes [palavras chaves]]
Dica: palavras-chave devem aparecer de forma natural no texto, integradas ao raciocínio, sem interromper fluidez.

Gatilhos Mentais:
Medo de perda: mostrar prejuízo invisível ou desgaste por manter hábito errado.
Facilidade: mostrar que a correção é simples.
Transformação: antes errado, depois corrigido.
Autoridade/prova: apenas se fizer sentido naturalmente, sem exagero.

Estrutura de Copywriting:
Use PAS como estrutura principal:
Problema: explique o erro cotidiano normalizado.
Agitação: destaque consequências acumuladas do erro.
Solução: mostre o produto como correção lógica e prática.
AIDA pode ser usado apenas como ajuste de ritmo, não como estrutura central.

Storytelling:
Começo: situação comum que o leitor reconhece.
Meio: percepção de que ele faz errado.
Fim: correção simples com o produto.
Evite romantizar, exagerar ou empolgação artificial.

Linguagem e Empatia:
Tom direto, cotidiano, sem marketing explícito.
Foco no erro do leitor e na solução prática. Produto em segundo plano.

SEO:
Palavras-chave integradas de forma natural, reforçando problema, solução e benefício.
Evite excesso de repetição; priorize fluidez e leitura agradável.

FAZE 2 ----------------------------------------------------------------------------

Crie propaganda BASEADO NO TEXTO ACIMA:
Conexão emocional via storytelling (problema → solução → transformação “antes/depois”).
Foco em benefícios reais, não specs técnicas.
Emoção ativa atenção, lógica reforça credibilidade.
Autenticidade e clareza aumentam persuasão.
Priorize fluidez sobre SEO mecânico.

REGRAS PARA LIST_:
Campo BENEFITS_LIST_ com mínimo 5 itens, lista corrida, cada item iniciado por vírgula, focando em transformação prática e benefícios claros.

REGRAS PARA TITULO_:
TITULO_ curto, direto, diagnóstico de erro comum, contém palavra-chave principal.

REGRAS PARA PARÁGRAFOS:
Parágrafos mínimo 200 caracteres.
Priorize clareza e fluidez, sem repetir ideias.

REGRAS PARA PALAVRAS-CHAVE:
Destaque as palavras-chave entre colchetes [palavras chaves].
Todas as 8 palavras-chave devem aparecer naturalmente, contextualizadas.
Evite repetições excessivas ou agrupamentos mecânicos.

REGRAS ABSOLUTAS:
Responda exclusivamente os campos_.
Texto deve gerar desejo de compra baseado em incômodo + correção de erro.
Sem romantização, hype, promessas falsas ou linguagem neutra.
Tom: conversa direta, sensação “como eu não percebi isso antes?”.

FAZE 3 ----------------------------------------------------------------------------

ESTRUTURA OBRIGATÓRIA DO TEXTO:
PALAVRAS_CHAVES_ = 8 palavras-chave relevantes, incluindo chave principal, variações e long tail.
TITULO_SEO_H1_ = Diagnóstico curto, direto, afirmativo, conter a palavra-chave principal do produto..
INCOMODO_IMEDIATO_ = Mostre perda ou hábito errado que a pessoa acha normal.
QUEBRA_EXPECTATIVA_ = Explique que o problema real não é o que o leitor pensa.
TITULO_CONSEQUENCIAS_DO_ERRO_H2_ = Título claro sobre prejuízo invisível ou correção de erro.
PROBLEMA_REAL_ = Erro cotidiano explicado de forma direta e desconfortável.
AGITACAO_PERDA_CONTINUA_ = Consequências acumuladas do erro: esforço, tempo, dinheiro, desgaste.
VIRADA_PSICOLOGICA_ = Mostre que não é normal nem inevitável; apenas falta da solução correta.
TITULO_SEO_H2_ = Pergunta que gere dúvida ou incômodo imediato.
INTRODUCAO_PRODUTO_ = Produto como correção óbvia, prática, lógica; ajusta hábito.
BENEFICIO_CENTRAL_ = Antes e depois; transformação prática objetiva.
DEMONSTRACAO_MENTAL_ = 3-4 ações simples para o leitor imaginar o uso sem esforço.
NORMALIZACAO_PROVA_ = Mostre que pessoas já usam a solução sem exagero.
TITULO_SEGURANCA_E_SIMPLICIDADE_H2_ = Remove medo, resistência, dúvida sobre uso.
REDUCAO_RISCO_ = Mostre simplicidade, baixo risco, facilidade de devolução ou segurança percebida.
PARAGRAFO_DETAILS_ = Detalhes conectados à praticidade e correção do erro, sem linguagem técnica.
BENEFITS_LIST_ = Lista corrida de 5+ benefícios práticos, iniciando cada item com vírgula.
H2_FAQ_TITLE_ = Título da seção de perguntas frequentes.
PARAGRAFO_FAQ_ = Perguntas reais do comprador, respostas curtas e tranquilizadoras.
ALT_IMAGE_1_ = Descrição objetiva do produto com foco em SEO e uso real.
ALT_IMAGE_2_ = Descrição objetiva do produto voltada para marketing e prática.
ALT_IMAGE_3_ = Descrição objetiva do produto destacando design e multifuncionalidade.
CTA_NATURAL_ = Frase neutra reforçando lógica e correção, sem pedir compra.
CHAMADA_ACAO_ = Informe que quem quiser ver detalhes e preço pode acessar o link.
'''

# ======================= PROMPTS YOUTUBE
def PROMPT_Titulos_youtube(TEXTO,REGRAS):
    return f"""{REGRAS}
Você é um estrategista de crescimento para YouTube, especializado em CTR, retenção e recomendação algorítmica.
Vou te enviar o texto base de um vídeo sobre assuntos gerais (conteúdo técnico, educacional ou explicativo).
Seu objetivo é gerar títulos de alta performance, baseados em vídeos que realmente performam hoje, não em teoria.

REGRAS GERAIS
Não use títulos genéricos ou educativos demais
Evite linguagem de curso, tutorial básico ou promessa milagrosa
Priorize curiosidade, posicionamento claro e conflito implícito
Linguagem direta, humana, sem parecer texto de IA
Não use emojis
Não use palavras vazias como “guia completo”, “passo a passo”, “aprenda agora”

ENTREGAS OBRIGATÓRIAS
1. TÍTULOS PRINCIPAIS (3 opções)

Crie 3 títulos principais para o vídeo, focados em:
Alto CTR
Clareza de tema
Retenção nos primeiros 30 segundos
Compatibilidade com público técnico / curioso / intermediário
Cada título deve ter no máximo 70 caracteres.

2. TÍTULOS ALTERNATIVOS (2 opções)
Crie 2 variações alternativas, com abordagem diferente dos principais, por exemplo:
Mais provocativo
Mais técnico
Mais “quebra de expectativa”
Também com no máximo 70 caracteres.

3. TEXTO PARA THUMBNAIL (2 opções)
Crie 2 frases curtas para thumbnail, obedecendo:
Máximo de 4 a 5 palavras
Linguagem visual, forte e direta
Não repetir exatamente o título
Foco em impacto, curiosidade ou contraste
Essas frases devem funcionar sozinhas na imagem.

CONTEXTO IMPORTANTE
O título e a thumbnail devem se complementar, não repetir a mesma ideia
Pense em feeds concorridos, onde o usuário decide em menos de 1 segundo
O objetivo é clique + permanência, não apenas SEO

Se algum título parecer curso, promessa financeira, marketing afiliado genérico ou clickbait óbvio, descarte e gere outro.
Prefira títulos que soem como observação real ou descoberta prática.

Agora, gere tudo isso com base no texto abaixo:
{TEXTO}
"""
def PROMPT_produtos_vendas_DESCRTT_youtube(LINK,CHAMAD1,LINK_FILIADO_1,CHAMAD2,LINK_FILIADO_2,CHAMAD3,LINK_FILIADO_3,REDES_SOCIAL):
	return F'''
COM ESSE LINK FAÇA UM RAIO X COMPLETO:
{LINK}
AGORA 
Você é um especialista em SEO para YouTube, comportamento de usuário e marketing de afiliados.
Sua tarefa é criar uma DESCRIÇÃO PROFISSIONAL, REALISTA e OTIMIZADA PARA YOUTUBE, focada em decisão de compra.
Use esse texto como matéria-prima, mas reescreva tudo estrategicamente.

_OBJETIVO PRINCIPAL_
Maximizar:
Clique (CTR)
Retenção inicial
Engajamento (comentários, likes, inscrição)
Conversão em links de compra
Nada criativo sem função.
Tudo deve servir ao algoritmo e à decisão de compra.

_REGRAS OBRIGATÓRIAS_
Linguagem direta, honesta e orientada à decisão.
Nada de hype vazio.
O texto deve parecer feito por um canal grande de review sério.
Repetir o nome do produto de forma estratégica (SEO).
Pensar sempre: “isso faz alguém continuar assistindo ou clicar?”

_ESTRUTURA OBRIGATÓRIA (ORDEM EXATA)_
_(1) TEXTO ACIMA DA DOBRA (3 LINHAS – O MAIS IMPORTANTE)_
Crie 3 linhas curtas que:
Confirmem a intenção de busca (“vale a pena comprar?”)
Prometam análise honesta e uso real
Criem medo racional de erro de compra
Esse texto deve funcionar mesmo se a pessoa não clicar em ‘mostrar mais’.

_(2) TÍTULO SEO REFORÇADO (1 LINHA)_
Crie um título contendo:
Nome completo do produto
“Review” ou “Análise”
“Vale a pena comprar?”
O título deve ser claro, pesquisável e competitivo.

_(3) INTRODUÇÃO DE DECISÃO DE COMPRA_
Explique rapidamente:
Para quem o vídeo é
Por que assistir antes de comprar
O que a pessoa vai descobrir que não vê em anúncio

_(4) CONTEXTO COMERCIAL E USO REAL_
Explique:
Para quem o produto faz sentido
Para quem NÃO faz
Onde ele se destaca
Onde ele perde
Sempre com foco em expectativa vs realidade.

_(5) BLOCO DE INTENÇÃO DE COMPRA_
Deixe explícito:
Que o vídeo existe para evitar erro de compra
Que não é propaganda
Que o foco é custo-benefício real

_(6) BLOCO “COMPRAR O PRODUTO” (ORGANIZADO E LIMPO)_
Use exatamente este formato:

LINKS ONDE COMPRAR:
{CHAMAD1}:
{LINK_FILIADO_1}

{CHAMAD2}:
{LINK_FILIADO_2}

{CHAMAD3}:
{LINK_FILIADO_3}

_(7) QUEBRA DE OBJEÇÕES_
Crie dois blocos:
Vantagens reais
– Benefícios objetivos e práticos
Limitações reais
– Pontos negativos honestos

_(8) CONTEXTO COMPARATIVO_
Compare com:
Produtos maiores
Produtos mais baratos
Produtos premium
Explique o posicionamento real do produto.

_(9)) CALL TO ACTION (CURTO E FUNCIONAL)_
Like
Comentário
Inscrição
Sem texto longo.

REDES SOCIAIS:
{REDES_SOCIAL}

_(11) HASHTAGS (3 A 5)  HASHTAGS (4 A 6) palavras #hashtags NA HORIZONTAL_
Misture:
Produto
Intenção de compra
Categoria

_(12) PALAVRAS-CHAVE (TAGS PARA YOUTUBE) NA HORIZONTAL e 'palavras-chave SEPARADAS POR VIRGULAS'_
Liste 12 a 15 tags, incluindo:
Frases curtas
Foco em:
nome do produto
review
vale a pena
análise
intenção de compra

“NÃO inclua títulos técnicos, numeração, nomes de blocos ou explicações na resposta final.
Entregue a descrição como texto natural pronto para colar no YouTube.”
'''
def PROMPT_assuntos_gerais_DESCRTT_youtube(TEXTO,MEUS_SITES,MINHAS_REDES_SOCIAL,LINKS_USADO_SITES):
    return f'''
LEIA ESSE TEXTO BASE DO VÍDEO:
{TEXTO}

------------------------------------------------------------------------------

CONTEXTO DO CANAL E DO CONTEÚDO (USO INTERNO)
Sites oficiais do projeto:
{MEUS_SITES}

Redes sociais oficiais:
{MINHAS_REDES_SOCIAL}

Sites, plataformas ou links utilizados como referência ou apoio para o conteúdo:
{LINKS_USADO_SITES}

Use essas informações como CONTEXTO para entendimento do ecossistema do canal.
Não transforme o texto principal em venda.
Não force menções dentro do conteúdo editorial.

------------------------------------------------------------------------------

AGORA ATUE COMO UM ESTRATEGISTA DE CRESCIMENTO PARA YOUTUBE,
especializado em vídeos de assuntos gerais que ganham alcance, retenção e engajamento real.

Sua tarefa é criar uma DESCRIÇÃO OTIMIZADA PARA O ALGORITMO DO YOUTUBE,
baseada em práticas reais usadas por vídeos que performam hoje,
não em teoria genérica ou SEO artificial.

Você receberá um texto base (transcrição, roteiro ou ideia).
Use como referência, mas REESCREVA tudo estrategicamente,
pensando em leitura humana, distribuição e engajamento.

------------------------------------------------------------------------------

OBJETIVOS DA DESCRIÇÃO
- Ajudar o algoritmo a entender claramente o tema
- Aumentar o interesse de quem abre a descrição
- Estimular comentários reais
- Reforçar retenção indireta
Nada de texto acadêmico.
Nada de enrolação.
Cada linha precisa ter função prática.

------------------------------------------------------------------------------

REGRAS OBRIGATÓRIAS
- Linguagem natural, simples e direta
- Texto deve parecer escrito por um criador experiente
- Sem tom de venda
- Sem títulos técnicos visíveis
- Sem numeração
- Palavras-chave usadas naturalmente
- Pense sempre: isso ajuda o vídeo a continuar sendo recomendado?

------------------------------------------------------------------------------

ESTRUTURA QUE O ALGORITMO RESPONDE MELHOR
(use internamente, NÃO MOSTRE a estrutura no texto final)

- Texto acima da dobra com 3 linhas curtas, claras e chamativas
- Contexto do tema explicando por que isso importa agora
- Desenvolvimento resumindo ideias centrais do vídeo
- Identificação com o público usando situações reais
- Perguntas abertas para estimular comentários
- Call to action discreto e natural

------------------------------------------------------------------------------

REGRAS DE SAÍDA OBRIGATÓRIAS (ESSENCIAL)

INDEPENDENTE DO TEMA DO VÍDEO, ao FINAL da descrição você DEVE incluir:

1) Um bloco listando TODAS as redes sociais abaixo, exatamente como fornecidas,
sem alterar links e sem comentários adicionais.

2) Um bloco listando TODOS os sites oficiais do projeto.

3) Um bloco listando os sites, plataformas ou links utilizados como referência,
quando existirem.

Esses blocos são FIXOS e OBRIGATÓRIOS.
Não explicar.
Não vender.
Apenas listar.

------------------------------------------------------------------------------

HASHTAGS
Inclua de 3 a 5 hashtags relacionadas ao tema principal.

------------------------------------------------------------------------------

PALAVRAS-CHAVE (TAGS PARA YOUTUBE)
Liste de 10 a 15 palavras-chave relacionadas ao assunto do vídeo.
Esse bloco deve ser o ÚLTIMO da descrição.

------------------------------------------------------------------------------

REGRA FINAL
- NÃO mostrar títulos internos
- NÃO usar numeração visível
- NÃO explicar a estrutura
- Entregar o texto FINAL como descrição humana pronta para colar no YouTube
'''
def PROMPT_musicas_vibesinha_DESCRTT_youtube(NOME_DA_MUSICA,LETRA_DA_MUSICA,LINKS_DE_DIVULGACAO,MINHAS_REDES_SOCIAL):
    return  f'''
Você é um estrategista de crescimento para YouTube Music, especializado em retenção,
identidade artística e recomendação algorítmica de músicas autorais..
{Regaras_Respostas_IA()}
Use as informações fornecidas apenas como CONTEXTO.
Não faça venda.
Não use linguagem de marketing.
Não force links no meio do texto.
A música é o centro de tudo.

=====================================

DADOS DA MÚSICA
Nome da música:
{NOME_DA_MUSICA}

Letra da música:
{LETRA_DA_MUSICA}

Redes sociais oficiais:
{MINHAS_REDES_SOCIAL}

Sites e plataformas de divulgação:
{LINKS_DE_DIVULGACAO}

=====================================

OBJETIVO DA DESCRIÇÃO

Ajudar o algoritmo a identificar:
- clima emocional
- gênero e subgênero musical
- atmosfera sonora
- público ideal

Ajudar o ouvinte a:
- sentir a vibe antes de ouvir
- se conectar emocionalmente
- ouvir até o final

Reforçar identidade artística.
Nada técnico.
Nada institucional.
Nada genérico.

=====================================

REGRAS OBRIGATÓRIAS

- Linguagem humana, artística e direta
- Texto deve parecer escrito pelo artista
- Sem tom de autopromoção
- Sem emojis
- Sem numeração
- Sem títulos internos
- Sem clichês motivacionais

=====================================

ESTRUTURA (USO INTERNO — NÃO MOSTRAR)

1) TEXTO ACIMA DA DOBRA  
3 linhas curtas que transmitam o clima emocional da música.

2) CONTEXTO ARTÍSTICO  
Sensações, momento ideal de escuta e atmosfera.

3) IDENTIDADE SONORA  
Gênero, subgênero e elementos musicais (trap, jazz, blues, piano, 808, etc).

4) IDENTIFICAÇÃO COM O OUVINTE  
Para quem ouve sozinho, de madrugada, com fone.

5) CALL TO ACTION SUAVE  
Ouvir até o final, comentar o sentimento, salvar se fizer sentido.

6) REDES SOCIAIS  
Listar todas no final, exatamente como fornecidas.

7) LINKS DE DIVULGAÇÃO  
Listar no final, sem comentários extras.

8) HASHTAGS  
Usar de 10 hashtags relacionadas a gênero e clima.

9) PALAVRAS-CHAVE MUSICAIS (OBRIGATÓRIO)

Liste de 15 a 25 palavras-chave separadas por vírgula,
relacionadas a:
- gênero
- subgênero
- clima emocional
- atmosfera
- estilo sonoro
- tipo de ouvinte

Esse bloco deve ficar no FINAL da descrição.

=====================================

REGRA FINAL

Não explique a estrutura.
Não mencione instruções.
Entregue apenas a descrição final,
pronta para colar no YouTube.
'''

    return str(texto.replace( ':',"").replace( ' = ',"")).replace("Palavras-chave",'').replace("Palavras chave",'').replace("HASHTAGS_",'').replace("TEXT_ACIMA_DA_DOBRA_",'').replace("CONTEXTO_ARTÍSTICO_",'').replace("DENTIDADE_SONORA_",'').replace("IDENTIFICAÇÃO_COM_O_OUVINTE_",'').replace("CALL_TO_ACTION_SUAVE_",'').replace("PALAVRAS_CHAVE_MUSICAIS_",'').strip()



def colc_virg(texto):
    texto_modificado = re.sub(r'[\*\+\-:\\]', ',', texto)
    texto_modificado = re.sub(r',+', ',', texto_modificado)
    texto_modificado = texto_modificado.strip(',')
    partes = [parte.strip() for parte in texto_modificado.split(',') if parte.strip()]
    html = '\n'.join(f'<li>{parte}</li>' for parte in partes)
    return html

def colc_hif(texto):
    texto_modificado = re.sub(r'[\*\+\-:\\]', ',', texto)
    texto_modificado = re.sub(r',+', ',', texto_modificado)
    texto_modificado = texto_modificado.strip(',')
    partes = [parte.strip() for parte in texto_modificado.split(',') if parte.strip()]
    html = '<br>'.join(f'- {parte}' for parte in partes)
    return html

def gerar_html_seo(st,ID_PROD, titulo_pag, titulo_post, INTRODITION, DESCRITION,
                   Titulo_Detalhes,DETALHES, Titulo_lista,lista
                   ,titulo_faq,faq,DESC_IMAGEM, CHAVES, LINK_AFILIADO,LINK_CATEGORIA, LIMK_IMAGEM,LINK_SIT,MARCAD_CATGORIAS):
    from Banco_Dados import aplicar_links_bloco, esc_D_LINKS
    from Minhas_Chaves_Api import chave_api_blogger_AQUI_ACHEI, chave_api_blogger_ACHEI_TOP

    # INTRODUÇÃO
    introdution, usados_intro = aplicar_links_bloco(INTRODITION)

    # DESCRIÇÃO CURTA
    descrition, usados_desc = aplicar_links_bloco( DESCRITION)

    # DETALHES (apenas o texto, não o <strong>)
    Detalhes, usados_det = aplicar_links_bloco(DETALHES)


    '''tg = ler_A_PROD_ENTRADA(ID_PROD, 'TAGS')[0][0]
    TAGS = tg if tg != ',' else marcadores
'''
    if titulo_faq:
        titulo_formatado = titulo_faq[1:].capitalize() if titulo_faq[0] == ':' else titulo_faq.capitalize()
    else:
        titulo_formatado = "Perguntas Frequentes:"

    html = f'''
    <!-- INTRODUÇÃO SEO -->
    <section>
      <p style="color:#333;">{introdution}</p>
    </section>

    <!-- BLOCO CLICÁVEL (IMAGEM + TEXTO) -->
    <a href="{LINK_CATEGORIA}"
       target="_blank"
       rel="nofollow sponsored"
       style="text-decoration:none;color:inherit;display:block;">

      <section style="
        background:#fafafa;
        padding:20px;
        border-radius:10px;
        border:1px solid #eee;
        margin:20px 0;
      ">

        <img src="{LIMK_IMAGEM}"
             alt="{DESC_IMAGEM}"
             style="max-width:100%;border-radius:8px;display:block;margin-bottom:12px;">

        <h2 style="color:#222;margin:0 0 8px 0;">
          {titulo_post}
        </h2>

        <p style="color:#333;margin:0;">
          {descrition}
        </p>

      </section>
    </a>

    <!-- DESCRIÇÃO DETALHADA -->
    <section>
      <h2>{Titulo_Detalhes}</h2>
      <p style="color:#333;">
        <strong>{titulo_pag}</strong> {Detalhes}
      </p>
    </section>

    <!-- BENEFÍCIOS -->
    <section>
      <h3>{Titulo_lista}</h3>
      <ul style="color:#333; padding-left:20px;">
        {colc_virg(lista.replace('<br>', ''))}
      </ul>
    </section>

    <!-- BOTÃO CTA -->
    <section style="margin-top:24px;">
      <a href="{LINK_AFILIADO}"
         target="_blank"
         rel="nofollow sponsored"
         style="
           display:inline-block;
           padding:14px 22px;
           background:#ee4d2d;
           color:#ffffff !important;
           font-weight:bold;
           border-radius:6px;
           text-decoration:none;
           font-size:16px;
         ">
         Ver oferta da PROMOÇÃO
      </a>
    </section>

    <!-- FAQ -->
    <section style="margin-top:30px;">
      <h3>{titulo_formatado}?</h3>
      <p>{colc_hif(faq.lower().replace('pergunta:', '').replace('resposta:', '')
       .replace('pergunta;', '').replace('resposta;', '')
        .replace('<br>', '').replace('?','?<br>'))}</p>
    </section>

    <!-- TAGS / CHAVES -->
    <section style="margin-top:20px;">
      {formatar_chaves_coloridas(CHAVES)}
    </section>
    '''

    st.code(html)
    try:
        service = get_service()
        url = publicar_no_blogger(service, chave_api_blogger_AQUI_ACHEI(), titulo_pag.upper(), MARCAD_CATGORIAS, html,rascunho=False)
        sleep(2)
        publicar_no_blogger(service, chave_api_blogger_ACHEI_TOP(),titulo_pag.upper(), MARCAD_CATGORIAS, html,rascunho=False)

        for PALAVRA in CHAVES.split(','):
            esc_D_LINKS(str(PALAVRA).strip().title(), titulo_pag, url)
    except RuntimeError:
        st.warning('Erro ao mandar para site automatico:')
    return html


def gerar_html_seo_video(ID_COPY,LINK_FIL_1,LINK_FIL_2,LINK_FIL_3):
    ID_COPY = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][0]).replace('[', '').replace(']', '')
    PALAVRAS_CHAVES = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][1]).replace('[', '').replace(']', '')
    TITULO_SEO_H1 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][2]).replace('[', '').replace(']', '')
    INCOMODO_IMEDIATO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][3]).replace('[', '').replace(']', '')
    QUEBRA_EXPECTATIVA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][4]).replace('[', '').replace(']', '')
    TITULO_CONSEQUENCIAS_DO_ERRO_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][5]).replace('[', '').replace(']', '')
    PROBLEMA_REAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][6]).replace('[', '').replace(']', '')
    AGITACAO_PERDA_CONTINUA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][7]).replace('[', '').replace(']', '')
    VIRADA_PSICOLOGICA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][8]).replace('[', '').replace(']', '')
    TITULO_SEO_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][9]).replace('[', '').replace(']', '')
    INTRODUCAO_PRODUTO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][10]).replace('[', '').replace(']', '')
    BENEFICIO_CENTRAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][11]).replace('[', '').replace(']', '')
    DEMONSTRACAO_MENTAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][12]).replace('[', '').replace(']', '')
    NORMALIZACAO_PROVA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][13]).replace('[', '').replace(']', '')
    TITULO_SEGURANCA_E_SIMPLICIDADE_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][14]).replace('[', '').replace(']', '')
    REDUCAO_RISCO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][15]).replace('[', '').replace(']', '')
    PARAGRAFO_DETAILS = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][16]).replace('[', '').replace(']', '')
    BENEFITS_LIST = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][17]).replace('[', '').replace(']', '')
    H2_FAQ_TITLE = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][18]).replace('[', '').replace(']', '')
    PARAGRAFO_FAQ = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][19]).replace('[', '').replace(']', '')
    ALT_IMAGE_1 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][20]).replace('[', '').replace(']', '')
    ALT_IMAGE_2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][21]).replace('[', '').replace(']', '')
    ALT_IMAGE_3 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][22]).replace('[', '').replace(']', '')
    CTA_NATURAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][23]).replace('[', '').replace(']', '')
    CHAMADA_ACAO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][24]).replace('[', '').replace(']', '')
    MARCATION = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][25]).replace('[', '').replace(']', '')

    link_vid = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][2]).replace('[', '').replace(']', '')
    link_af1 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][3]).replace('[', '').replace(']', '')
    link_af2 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][4]).replace('[', '').replace(']', '')
    link_af3 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][5]).replace('[', '').replace(']', '')
    IMAGE_LINK_1 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][6]).replace('[', '').replace(']', '')
    IMAGE_LINK_2 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][7]).replace('[', '').replace(']', '')
    IMAGE_LINK_3 = str(ler_COPY_PRODUTO_MIDIA(ID_COPY)[0][8]).replace('[', '').replace(']', '')

    def botao_afiliado(link, texto, cor):
        if not link:
            return ''
        return f'''
    <a href="{link}"
       target="_blank"
       rel="nofollow sponsored"
       style="
         background:{cor};
         color:#fff;
         text-align:center;
         padding:14px;
         border-radius:6px;
         font-weight:bold;
         text-decoration:none;
         display:block;
       ">
      {texto}
    </a>
    '''


    VIDEO_LINK = ''
    if link_vid:
        VIDEO_LINK = f'''
  
<!-- FAIXA DE VÍDEO COM IMAGEM + ÍCONE YOUTUBE -->
<a href="{link_vid}"
   target="_blank"
   rel="nofollow sponsored"
   style="text-decoration:none;color:inherit;display:block;">

  <section style="
    display:flex;
    gap:16px;
    align-items:center;
    background:#f5f5f5;
    padding:16px;
    border-radius:8px;
    border:1px solid #ddd;
    margin:32px 0;
  ">

    <img src="{IMAGE_LINK_3}"
         alt="{ALT_IMAGE_3}"
         style="
           width:140px;
           height:90px;
           object-fit:cover;
           border-radius:6px;
           flex-shrink:0;
         ">

    <div>
      <div style="display:flex;align-items:center;gap:8px;">
        <svg width="24" height="18" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="24" height="16" rx="3" fill="#FF0000"/>
          <polygon points="9,4 16,8 9,12" fill="#FFFFFF"/>
        </svg>
        <strong>Veja o funcionamento em vídeo</strong>
      </div>

      <p style="margin:6px 0 0 0;font-size:14px;line-height:1.4;">
        Demonstração real do produto, sem cortes e sem exagero.
      </p>
    </div>

  </section>
</a>
'''

    LINK_AFILIADO_1 = botao_afiliado(link_af1, LINK_FIL_1, '#ff9900')
    LINK_AFILIADO_2 = botao_afiliado(link_af2, LINK_FIL_2, '#333')
    LINK_AFILIADO_3 = botao_afiliado(link_af3, LINK_FIL_3, '#1e3a5f')

    from Banco_Dados import aplicar_links_bloco

    # INTRODUÇÃO
    incomodo, usados_intro = aplicar_links_bloco(INCOMODO_IMEDIATO)

    # DESCRIÇÃO CURTA
    agita, usados_desc = aplicar_links_bloco( AGITACAO_PERDA_CONTINUA)

    # DETALHES (apenas o texto, não o <strong>)
    intro, usados_det = aplicar_links_bloco(INTRODUCAO_PRODUTO)

    demost, usados_det = aplicar_links_bloco(DEMONSTRACAO_MENTAL)

    html = f'''
    <!-- INTRODUÇÃO SEO -->
    <section>
      <p style="color:#333;">{incomodo}</p>
      <p><strong>{QUEBRA_EXPECTATIVA}</strong></p>

    </section>

    <!-- BLOCO CLICÁVEL (IMAGEM + TEXTO) -->
    <a href="{link_af2}"
       target="_blank"
       rel="nofollow sponsored"
       style="text-decoration:none;color:inherit;display:block;">

      <section style="
        background:#fafafa;
        padding:20px;
        border-radius:10px;
        border:1px solid #eee;
        margin:20px 0;
      ">
      <img src="{IMAGE_LINK_1}" alt="{ALT_IMAGE_1}" style="max-width:100%;border-radius:8px;margin-bottom:12px;">

        <h2 style="color:#222;margin:0 0 8px 0;">
          {TITULO_CONSEQUENCIAS_DO_ERRO_H2}
        </h2>

        <p style="color:#333;margin:0;">
          {PROBLEMA_REAL}
        </p>

      </section>
    </a>
    

    <!-- CONSEQUÊNCIAS DO ERRO -->
    <section>
      <p>{agita}</p>
      <p><strong>{VIRADA_PSICOLOGICA}</strong></p>
    </section>

    <!-- INTRODUÇÃO DO PRODUTO -->
    <section>
      <h2>{TITULO_SEO_H2}</h2>
      <img src="{IMAGE_LINK_2}" alt="{ALT_IMAGE_2}" style="max-width:100%;border-radius:8px;margin-bottom:12px;">
      <p>{intro}</p>
</section>

    <!-- BLOCO DE BENEFÍCIO CENTRAL -->
    <section>
      <p><strong>{BENEFICIO_CENTRAL}</strong></p>
      <p>{demost.replace('1)', '<br>1').replace('2)', '<br>2').replace('3)', '<br>3').replace('4)', '<br>4').replace('5)', '<br>5')}</p>
      <p>{NORMALIZACAO_PROVA.replace(')', '<br>')}</p>
    </section>

    <!-- SEGURANÇA E SIMPLICIDADE -->
    <section>
      <h2>{TITULO_SEGURANCA_E_SIMPLICIDADE_H2}</h2>
      <p>{REDUCAO_RISCO}</p>

    <!-- LISTA DE BENEFÍCIOS -->
      <h3>{PARAGRAFO_DETAILS}</h3>
      <ul style="color:#333; padding-left:20px;">
        {colc_virg(BENEFITS_LIST.replace('<br>', ''))}
      </ul>
    </section>

    <!-- CTA NATURAL -->
    <section>
      <p>{CTA_NATURAL}</p>
    </section>
    
    {VIDEO_LINK}
      
    <!-- CHAMADA FINAL -->
    <section style="margin-top:30px; text-align:center;">
        <p><strong>{CHAMADA_ACAO}</strong></p>
    </section>

    <!-- BOTÕES DE AFILIADO -->
<section style="margin-top:30px;display:flex;flex-direction:column;gap:12px;">
    {LINK_AFILIADO_1}
    {LINK_AFILIADO_2}
    {LINK_AFILIADO_3} 
</section>




    <!-- FAQ -->
    <section style="margin-top:40px;">
      <h2>{H2_FAQ_TITLE}</h2>
      <p>{PARAGRAFO_FAQ.replace('pergunta:', '').replace('resposta:', '')
       .replace('pergunta;', '').replace('resposta;', '').replace('"', '')
        .replace('<br>', '').replace('?','?<br>')}</p>
    </section>
    <!-- PALAVRAS-CHAVE -->
    <section style="margin-top:20px;">
      {formatar_chaves_coloridas(PALAVRAS_CHAVES.replace('"',''))}
    </section>
    '''






    return html, MARCATION, TITULO_SEO_H1, PALAVRAS_CHAVES.replace('"','')


def gerar_texto_txt_site(ID_COPY):
    ID_COPY = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][0]).replace('[', '').replace(']', '')
    PALAVRAS_CHAVES = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][1]).replace('[', '').replace(']', '')
    TITULO_SEO_H1 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][2]).replace('[', '').replace(']', '')
    INCOMODO_IMEDIATO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][3]).replace('[', '').replace(']', '')
    QUEBRA_EXPECTATIVA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][4]).replace('[', '').replace(']', '')
    TITULO_CONSEQUENCIAS_DO_ERRO_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][5]).replace('[', '').replace(']', '')
    PROBLEMA_REAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][6]).replace('[', '').replace(']', '')
    AGITACAO_PERDA_CONTINUA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][7]).replace('[', '').replace(']', '')
    VIRADA_PSICOLOGICA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][8]).replace('[', '').replace(']', '')
    TITULO_SEO_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][9]).replace('[', '').replace(']', '')
    INTRODUCAO_PRODUTO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][10]).replace('[', '').replace(']', '')
    BENEFICIO_CENTRAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][11]).replace('[', '').replace(']', '')
    DEMONSTRACAO_MENTAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][12]).replace('[', '').replace(']', '')
    NORMALIZACAO_PROVA = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][13]).replace('[', '').replace(']', '')
    TITULO_SEGURANCA_E_SIMPLICIDADE_H2 = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][14]).replace('[', '').replace(']', '')
    REDUCAO_RISCO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][15]).replace('[', '').replace(']', '')
    PARAGRAFO_DETAILS = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][16]).replace('[', '').replace(']', '')
    BENEFITS_LIST = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][17]).replace('[', '').replace(']', '')
    H2_FAQ_TITLE = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][18]).replace('[', '').replace(']', '')
    PARAGRAFO_FAQ = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][19]).replace('[', '').replace(']', '')
    CTA_NATURAL = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][23]).replace('[', '').replace(']', '')
    CHAMADA_ACAO = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][24]).replace('[', '').replace(']', '')
    MARCATION = str(ler_COPY_PRODUTO_sit(ID_COPY)[0][25]).replace('[', '').replace(']', '')

    txt = f"""
{TITULO_SEO_H1}
{INCOMODO_IMEDIATO}
{QUEBRA_EXPECTATIVA}

{TITULO_CONSEQUENCIAS_DO_ERRO_H2}
{PROBLEMA_REAL}
{AGITACAO_PERDA_CONTINUA}
{VIRADA_PSICOLOGICA}

{TITULO_SEO_H2}
{INTRODUCAO_PRODUTO}
{BENEFICIO_CENTRAL}
{DEMONSTRACAO_MENTAL}
{NORMALIZACAO_PROVA}

{TITULO_SEGURANCA_E_SIMPLICIDADE_H2}
{REDUCAO_RISCO}
{PARAGRAFO_DETAILS}
{BENEFITS_LIST}

{CTA_NATURAL}
{CHAMADA_ACAO}

{H2_FAQ_TITLE}
{PARAGRAFO_FAQ}

{MARCATION}
{PALAVRAS_CHAVES}
"""


    return txt
