import json
import re
import subprocess
import traceback
import requests
from datetime import datetime
import streamlit as st

from Function import Caves_Pri
from Minhas_Chaves_Api import chave_gpt, chave_ollama


def IA(text):
    # 🛠️ ESTRATÉGIA DO HEADERS (KISS): Idêntico ao seu exemplo convertido que funciona
    try:
        chaves = chave_gpt()
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\n================ 🔍 [TRACE REQUISIÇÃO DIRETA GEMINI - {agora}] ================")
        
        if "GeminiMVP" in chaves and chaves["GeminiMVP"]:
            api_key = str(chaves["GeminiMVP"]).strip()
            
            # Endpoint oficial v1beta idêntico ao seu cURL
            url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent'
            
            # Passando a chave no cabeçalho exatamente como a ferramenta online gerou
            headers = {
                'Content-Type': 'application/json',
                'X-goog-api-key': api_key,
            }
            
            json_data = {
                'contents': [
                    {
                        'parts': [
                            {
                                'text': text, # Injeta o prompt do Raio-X do produto aqui
                            },
                        ],
                    },
                ],
            }
            
            # Faz o disparo HTTP nativo e limpo
            resp = requests.post(url, headers=headers, json=json_data, timeout=30)
            dados_resposta = resp.json()
            
            # Validação do retorno estruturado do Google
            if resp.status_code == 200 and "candidates" in dados_resposta:
                texto_gerado = dados_resposta["candidates"][0]["content"]["parts"][0]["text"]
                print("[+] COPIES E RAIO-X GERADOS COM SUCESSO VIA HEADERS DA GOOGLE!")
                print("========================================================================\n")
                return texto_gerado.strip()
            else:
                print(f"❌ [ERRO SERVIDOR GOOGLE] Status: {resp.status_code} | Payload: {dados_resposta}")
                print("========================================================================\n")
                return f"Erro na API do Gemini: {dados_resposta.get('error', {}).get('message', 'Falha de Autenticação / Token Inválido')}"
        else:
            print("❌ [ERRO] Chave GeminiMVP ausente no arquivo de chaves.")
            print("========================================================================\n")
            return "Erro: Chave GeminiMVP ausente."
            
    except Exception as e:
        print(f"\n❌ ================ [FALHA EXCEÇÃO HTTP GEMINI] ================")
        print(f"[-] Mensagem do erro bruto: {str(e)}")
        print("========================================================================\n")
        return f"Falha na requisição direta: {str(e)}"


def Texto_para_json(texto):
    """
    Recebe um texto bruto e extrai as chaves definidas, retornando um dicionário.
    """
    dados = {}
    for chave in Caves_Pri():
        padrao = rf"{chave}\s*=?\s*(.+?)(?=(\n\w+_?\s*=)|$)"
        resultado = re.search(padrao, texto, re.DOTALL)
        if resultado:
            valor = resultado.group(1).strip()
            valor = valor.replace("\n", "<br>")
            valor = valor.replace('"', '')
            valor = valor.replace("'", '')
            dados[chave] = valor
    return dados


def json_completo(dados):
    """
    Verifica se todas as chaves obrigatórias estão presentes e não vazias.
    """
    for chave in Caves_Pri():
        if chave not in dados or not str(dados[chave]).strip():
            return False
    return True


def OLLAMA_CHAT_IA_jason(id_link, prompt, max_tentativas=5):
    """
    Chama o Ollama LLaMA, processa a resposta e garante que todas as chaves existam.
    Re-tenta automaticamente caso alguma chave esteja faltando.
    """
    st1, st2 = st.columns(2)
    texto_formatado = id_link.replace(".", ".\n")[:600]
    st1.code(f'CHAT RECEBEU: {texto_formatado}')

    for tentativa in range(1, max_tentativas + 1):
        processo = subprocess.Popen(
            [chave_ollama(), "run", chave_ollama()],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
            universal_newlines=True
        )

        stdout, stderr = processo.communicate(input=prompt)
        resposta = str(stdout.strip()).replace('*', '').replace('"', '').replace("'", '').replace(':', ';')

        dados = Texto_para_json(resposta)

        if json_completo(dados):
            json_final = json.dumps(dados, ensure_ascii=False, indent=4)
            st2.code(f'CHAT RETORNOU (OK NA TENTATIVA {tentativa}): {json_final}')
            return json_final

    raise RuntimeError("Falha: modelo não retornou todas as chaves após várias tentativas")


def OLLAMA_CHAT_IA(prompt):
    processo = subprocess.Popen(
        [chave_ollama(), "run", chave_ollama()], #gemma3:1b  e  llama3.2
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        universal_newlines=True
    )

    stdout, stderr = processo.communicate(input=prompt)

    resposta = stdout.strip()

    return resposta
