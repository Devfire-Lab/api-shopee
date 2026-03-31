# API Shopee + Automação de Blogs (Afiliado Inteligente)

Projeto de automação para **afiliados Shopee** usando **Python + Streamlit + API do Blogger**, com geração automática de HTML e SEO inteligente.

O objetivo é **buscar produtos na Shopee, gerar textos/copys com IA e publicar diretamente no seu blog (Blogger)**, tudo em um único fluxo.

🔗 **Assista à vídeo aula completa (em português)**:
👉 https://www.youtube.com/watch?v=uwo0BqBkR5A

---

## 🎯 O que esse repositório faz

Esse projeto é resultado de uma **vídeo aula prática**, onde você aprende a:

* Integrar **API de afiliados da Shopee** com Python
* Criar um **app Streamlit com interface estilo desktop**
* Automatizar **publicação no Blogger**
* Gerar **HTML otimizado + SEO + copy com IA (OpenAI / Ollama)**
* Criar **links de afiliado e QR Code automaticamente**

Fluxo direto:

1. Busca produto na Shopee
2. Gera copy (simples, avançada ou automática)
3. Publica no Blogger com SEO pronto

---

## 📹 Sobre o vídeo + PDF de fluxo

Durante a aula existe um **PDF explicativo (fluxo do sistema)** que mostra:

* Arquitetura completa:
  **Shopee API → Streamlit → IA → Blogger → Monetização**
* Onde instalar dependências
* Como configurar APIs
* Organização dos arquivos

Esse PDF funciona como **guia visual do projeto**, permitindo:

* Entender o fluxo completo rapidamente
* Acompanhar o código junto com a aula
* Replicar ou adaptar para outros nichos

⚠️ O PDF não está no repositório (normalmente fica na descrição do vídeo).

---

## 🗂️ Estrutura do projeto

```
api-shopee/
├── App_Inicio.py
├── App_Streamlit.py
├── shopee_api.py
├── Banco_Shopee.py
├── Banco_Dados.py
├── Function.py
├── menu_COPY_SIMPLES.py
├── menu_COPY_VIDEO.py
├── menu_COPY_AUTOMATICA.py
├── Automa_Post_Blog.py
├── Pag_Chats_IA.py
├── Prompts_HTML.py
├── Criando_Pasta_Arquivos.py
├── Minhas_Chaves_Api.py
├── Instalações_Pendencias
├── requirements.txt
└── README.md
```

Resumo dos principais módulos:

* **App_Inicio.py** → Interface inicial (Tkinter)
* **App_Streamlit.py** → Painel principal
* **shopee_api.py** → Integração Shopee
* **menu_COPY_*** → Geração de textos
* **menu_COPY_AUTOMATICA.py** → Post automático
* **Automa_Post_Blog.py** → Publicação Blogger
* **Prompts_HTML.py** → SEO + estrutura HTML
* **Banco_*.py** → Persistência SQLite

---

## ⚙️ Instalação

Clone o projeto:

```bash
git clone https://github.com/seu-usuario/api-shopee.git
cd api-shopee
```

Crie ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale dependências:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 Configuração

### Google Blogger

1. Acesse: https://console.cloud.google.com
2. Ative a **Blogger API**
3. Crie credenciais OAuth (Desktop)
4. Baixe o arquivo e renomeie para:

```
Cliente_Auto_blogger.json
```

Coloque na raiz do projeto.

---

### Arquivo de chaves

Edite:

```
Minhas_Chaves_Api.py
```

Configure:

* Shopee (APP_ID / SECRET_KEY)
* Blogger (blog_id)
* OpenAI (API Key)
* Ollama (opcional local)

---

## ▶️ Execução

Modo padrão:

```bash
python App_Inicio.py
```

Ou direto no Streamlit:

```bash
streamlit run App_Streamlit.py
```

---

## ⚙️ Fluxo automático (POSTAR AUTOMATICO)

1. Acessa menu **POSTAR AUTOMATICO**
2. Sistema executa:

   * Busca produto na Shopee
   * Gera HTML com IA
   * Publica no Blogger

Resultado:

* Post com SEO
* Título otimizado
* Conteúdo estruturado (H2, H3)
* Link afiliado
* QR Code

---

## 🔒 Segurança

Nunca publique:

```
Minhas_Chaves_Api.py
```

Sugestão futura:

```python
import os
APP_ID = os.getenv("APP_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
```

---

## 📚 Integração (vídeo + PDF + código)

* Vídeo → prática
* PDF → visão estrutural
* Código → execução

Use os três juntos para dominar o sistema.

---

## ⭐ Contribuição

Se esse projeto te ajudar:

* Deixe uma ⭐ no repositório
* Compartilhe com outros afiliados
* Adapte para outros marketplaces

---

## 🚀 Resultado final

Você terá um sistema que:

* Automatiza posts
* Escala conteúdo
* Gera tráfego orgânico
* Monetiza com afiliado + AdSense

---
