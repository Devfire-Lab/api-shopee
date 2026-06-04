# Minhas_Chaves_Api.py
# ---------------------------------------------------------------------------
# Este arquivo armazena todas as credenciais e chaves de API usadas no sistema.
# Ele é importado pelos outros scripts para:
#   - Conectar com a API da Shopee
#   - Publicar no Blogger
#   - Usar Ollama localmente
#   - Usar OpenAI (ChatGPT)
# ---------------------------------------------------------------------------



def chave_api_shopee_afiliado():

    """
    Retorna as credenciais da API do Programa de Afiliados da Shopee.
    Elas são usadas para:
      - Buscar produtos
      - Gerar links de afiliado
      - Puxar comissões, preço, imagens, etc.

    Como conseguir:
      1. Acesse: https://affiliate.shopee.com.br/
      2. Logue com sua conta Shopee.
      3. Vá em "Minha conta" ou "Configurações de API / Desenvolvedor".
      4. Crie um novo app/cliente e copie:
            • APP_ID
            • SECRET_KEY
      5. Cole aqui no código (não compartilhe com ninguém!).
    """

    keys = {
        "app_id": "18323300326",
        "app_secret": "L3Y44MMVH3E4HY4XPLSDXRW2LD7F5SQY",
    }
    return [keys["app_id"], keys["app_secret"]]


def chave_api_blogger_AQUI_ACHEI():
    """
    Retorna o ID do blog "Aqui Achei" para usar na API do Blogger.
    Cada blog que você quiser automatizar precisa de um ID separado.

    Como conseguir o blog_id:
      1. Acesse: https://www.blogger.com/
      2. Vá no painel do seu blog (ex.: "Aqui Achei").
      3. Veja a URL da página de gerenciamento, exemplo:
            https://www.blogger.com/blogger.b?blogID=1234567891234567890
      4. O número depois de "blogID=" é o blog_id.
      5. Cole no lugar do valor abaixo.
    """
    blog_id_AQUI_ACHEI = '18323300326'  # ID do blog "Aqui Achei"
    return blog_id_AQUI_ACHEI


def chave_api_blogger_ACHEI_TOP():
    """
    Retorna o ID do outro blog: "Achei Top".
    Só repita o mesmo processo do comentário acima para esse blog.
    """
    blog_id_ACHEI_TOP = '5715345972014270232'  # ID do blog "Achei Top"
    return blog_id_ACHEI_TOP


def chave_ollama():
    """
    Configuração do Ollama rodando localmente no seu PC.
    É usado como alternativa ao ChatGPT (modelo local, sem custo por uso).

    Como conseguir / usar:
      1. Instale o Ollama: https://ollama.com/
      2. Baixe um modelo no prompt, por exemplo:
            ollama pull llama3.2
      3. Ajuste o caminho abaixo para o executável do Ollama no seu Windows.
      4. Ajuste o nome do modelo (version) para o que você instalou.
    """
    caminho = r"C:\Users\henri\AppData\Local\Programs\Ollama\ollama.exe"
    version = "llama3.2"  # Modelo que você instalou via `ollama pull ...`

    return caminho, version


def chave_gpt():
    """
    Retorna as chaves da API da OpenAI (ChatGPT).
    Você pode usar várias chaves (ex.: contas diferentes, planos diferentes).

    Como conseguir:
      1. Acesse: https://platform.openai.com/api-keys
      2. Logue com sua conta.
      3. Clique em "Create new secret key".
      4. Copie a chave (ela começa com "sk-...").
      5. Cole aqui dentro do dicionário, com um nome amigável.

    ATENÇÃO:
      - NUNCA publique esse arquivo em um repositório público.
      - Considere usar um arquivo .env ou variáveis de ambiente na versão final.
    """
    keys = {
       "api-shopee-openai": "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",
    }

    return keys