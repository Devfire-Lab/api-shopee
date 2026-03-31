



# ================= STREAMLIT =================
def app():

    menu = st.sidebar.selectbox('Menu:',['','API','COPY SIMPLES','COPY AVANÇADO','POSTAR AUTOMATICO'])

    if menu == 'API':
        from shopee_api import Api_Shopee
        Api_Shopee(st)

    if menu == 'COPY SIMPLES':
        from menu_COPY_SIMPLES import COPY_SIMPLES
        COPY_SIMPLES(st)
    if menu == 'COPY AVANÇADO':
        from  menu_COPY_VIDEO import  COPY_ADVENT
        COPY_ADVENT(st)

    if menu == 'POSTAR AUTOMATICO':
        st.title("🔥 POSTAR AUTOMATICO Gerador HTML SEO Inteligentes".title())
        from menu_COPY_AUTOMATICA import COPY_AUTOMATICO
        COPY_AUTOMATICO(st)

    if menu == '':
        st.write('''## 🔑 Configuração obrigatória (Minhas_Chaves_Api.py)

Para o sistema funcionar corretamente, você **precisa obrigatoriamente preencher o arquivo**:

```bash
Minhas_Chaves_Api.py
```

Nesse arquivo ficam **todas as credenciais do projeto**. Sem isso, nenhuma automação vai funcionar.

Preencha com:

* **Shopee API**

  * APP_ID
  * SECRET_KEY

* **Google Blogger**

  * blog_id (de cada blog que você usa)

* **OpenAI (ChatGPT)**

  * API Key

* **Ollama (opcional)**

  * Caminho do executável
  * Modelo configurado

⚠️ Se esse arquivo não estiver configurado corretamente:

* A API da Shopee não retorna produtos
* O Blogger não publica posts
* A IA não gera conteúdo

Resumindo: **esse é o arquivo mais importante do projeto**.
''')

if __name__ == '__main__':
    import streamlit as st
    
    # Define o título, o ícone e o layout da página
    st.set_page_config(page_title="Api Shopee", layout="wide")

    # Adiciona o estilo da página
    page_bg = """
           <style>
           @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
           div {
               font-size:13px;
               border-radius: 5px;
               color: orange;
           }
           p {
               font-size:10px;
               color: orange;
               font-weight: lighter;
               text-shadow: 0 0 3px black;
               -webkit-text-stroke-width: 5x;
               -webkit-text-stroke-color: black;
           }
           </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
    
    app()
    

