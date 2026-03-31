import json
import re
import subprocess

from openai import OpenAI
from openai import OpenAIError, RateLimitError
import streamlit as st

from Function import Caves_Pri
from Minhas_Chaves_Api import chave_gpt, chave_ollama


def IA(text):
    try:
        last_error = None

        for nome, key in chave_gpt().items():
            try:
                client = OpenAI(api_key=key)

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": text}],
                    temperature=0.3
                )

                return response.choices[0].message.content.strip()

            except RateLimitError:
                st.warning(f"Rate limit atingido na key: {nome}")
                last_error = "rate_limit"
                continue

            except OpenAIError as e:
                msg = str(e).lower()

                if "quota" in msg or "insufficient" in msg or "billing" in msg:
                    st.warning(f"Sem crédito na key: {nome}")
                    last_error = "sem_credito"
                    continue

                if "invalid api key" in msg or "authentication" in msg:
                    st.error(f"API key inválida: {nome} (descartando)")
                    last_error = "key_invalida"
                    continue

                st.error(f"Erro inesperado com key {nome} → {e}")
                last_error = "erro_desconhecido"
                break

        raise RuntimeError(f"Nenhuma API key válida disponível. Último erro: {last_error}")
    except RuntimeError: pass
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
            [chave_ollama()[0], "run", chave_ollama()[1]],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
            creationflags=subprocess.CREATE_NO_WINDOW,
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
        [chave_ollama()[0], "run", chave_ollama()[1]], #gemma3:1b  e  llama3.2
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        creationflags=subprocess.CREATE_NO_WINDOW,
        universal_newlines=True
    )

    stdout, stderr = processo.communicate(input=prompt)

    resposta = stdout.strip()

    return resposta