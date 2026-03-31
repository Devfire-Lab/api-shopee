# pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

'''
1) O que seu script já faz
get_service():

Crie/usa um token.picklecom credenciais OAuth2.

EUA Cliente_Auto_blogger.json(que é o credentials.jsondo Google Cloud).

publicar_no_blogger:

Envia titulo, marcadores(tags) e html_conteudopara o Blogger.

Trata erro 429(taxa limite) com back‑off exponencial.

Ou seja: se você tiver o credentials.jsoncerto e o blog_idcerto, ele já publicou no Blogger sozinho .

2) Onde você precisa e o que você faz
Passo 1 – Ativar a API do Blogger no Google Cloud
Acesse:
https://console.cloud.google.com/

Crie ou selecione um projeto.

No menu, vá em APIs e Serviços → Biblioteca .

Obtenha por “Blogger API” e ativo.

Passo 2 – Criar credenciais OAuth2 ( Cliente_Auto_blogger.json)
No mesmo projeto:

Vá em APIs e Serviços → Credenciais .

Clique em “Criar credenciais → ID do cliente OAuth” .

Escolha “Aplicativo de desktop” (porque seu script roda local).

Baixe o JSON e renomeie para Cliente_Auto_blogger.jsone coloque na raiz do seu projeto, junto com o seu script.

Depois disso, na primeira execução, o script vai:

Abrir o navegador.

Pedir para você logar com o Google e dar permissão “https://www.googleapis.com/auth/blogger” .

Gerar ou token.picklereutilizar nas próximas execuções.

Passo 3 – Pegar o blog_idseu blog
Acesse seu blog no:
https://www.blogger.com/

Veja a URL do painel do blog. Em geral é algo como:
https://www.blogger.com/blogger.b?blogID=1234567891234567890

O número depois de blogID=é o blog_id.

Exemplo:

Python
blog_id = "1234567891234567890"


'''
import pickle, os, time


SCOPES = ['https://www.googleapis.com/auth/blogger']

def get_service():
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Cliente_Auto_blogger.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as f:
            pickle.dump(creds, f)
    return build('blogger', 'v3', credentials=creds)


def publicar_no_blogger_ANTIG(service, blog_id, titulo, marcadores, html_conteudo, rascunho=False):
    """
    titulo: string
    marcadores: lista de strings, ex.: ['YouTube', 'IA']
    html_conteudo: string com HTML completo do post
    rascunho: True para salvar como rascunho, False para publicar
    """
    post_body = {
        'kind': 'blogger#post',
        'title': titulo,
        'content': html_conteudo
    }

    if marcadores:
        post_body['labels'] = marcadores

    req = service.posts().insert(
        blogId=blog_id,
        body=post_body,
        isDraft=rascunho
    )
    res = req.execute()
    return res['url']



def publicar_no_blogger(
    service,
    blog_id,
    titulo,
    marcadores,
    html_conteudo,
    rascunho=False,
    max_retries=5,
    base_sleep=2
):
    from googleapiclient.errors import HttpError
    post_body = {
        'kind': 'blogger#post',
        'title': titulo,
        'content': html_conteudo
    }

    if marcadores:
        post_body['labels'] = marcadores

    for attempt in range(max_retries):
        try:
            req = service.posts().insert(
                blogId=blog_id,
                body=post_body,
                isDraft=rascunho
            )
            res = req.execute()
            return res['url']

        except HttpError as e:
            if e.resp.status == 429:
                sleep_time = base_sleep * (2 ** attempt)
                time.sleep(sleep_time)
                continue
            else:
                raise

    raise RuntimeError("Falha ao publicar no Blogger após exceder tentativas por rate limit.")

