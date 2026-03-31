
import os
import subprocess
from time import sleep
from tkinter import *
import threading
from PIL import Image, ImageTk

Pasta_Atual = os.path.dirname(__file__)

SCRIPT = 'App_Streamlit'
PORTA = 8555


# Lista de portas a serem monitoradas
processos = []

# Label global para mensagens
mensagem_label = None
def atualizar_mensagem(mensagem, cor="black"):
    mensagem_label.config(text=mensagem, fg=cor)
    mensagem_label.update()

def encerrar_processo_por_porta(porta):
    try:
        comando_pid = f"netstat -ano | findstr :{porta}"
        saida = subprocess.check_output(comando_pid, shell=True, text=True)
        linhas = saida.strip().split("\n")

        for linha in linhas:
            partes = linha.split()
            if len(partes) >= 5 and partes[1].endswith(f":{porta}"):
                pid = partes[4]
                comando_kill = f"taskkill /PID {pid} /F"
                subprocess.run(comando_kill, shell=True, check=True)
                atualizar_mensagem(f"Encerrado com sucesso!", "green")
    except subprocess.CalledProcessError as e:
        atualizar_mensagem(f"Encerrado porta {porta}!", "red")

def start_apps(porta,script):
    global processos
    if processos:
        atualizar_mensagem("Já estão em execução.", "orange")
        return

    try:
        command = fr"python -m streamlit run {Pasta_Atual}\{SCRIPT}.py  --server.port={porta}"
        processo = subprocess.Popen(command, shell=True)
        processos.append((porta, processo))
        atualizar_mensagem(f"Aplicação na porta {porta}", "green")
    except Exception as e:
        atualizar_mensagem(f"Encerrado na porta {porta}", "red")

def stop_apps():
    global processos
    if not processos:
        atualizar_mensagem("Nenhum servidor!.", "orange")
        return

    for porta, processo in processos:
        try:
            encerrar_processo_por_porta(porta)
        except Exception as e:
            atualizar_mensagem(f"Erro de encerramento!", "red")

    processos.clear()

def fechar_aplicacao(root):
    stop_apps()
    sleep(1)
    root.destroy()


def abrir_link1():
    import webbrowser  # Importa o módulo para abrir URLs
    webbrowser.open("https://sites.google.com/view/henriqls/in%C3%ADcio")

def main(SCRIPT,PORTA):
    root = Tk()
    root.title("")
    root.geometry("200x360")
    root.resizable(False, False)
    root.config(bg="#020239")
    global mensagem_label

    # COLUNAS --------
    GRADE_1 = Frame(root)

    GRADE_1.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')

    Label(GRADE_1, text=" API SHOPEE ", bg="#020239", fg='white', font=('Courier', 12, 'bold')).pack()

    # Carregar a imagem e converter para Tkinter-compatible

    Button(GRADE_1, text=str(F'Entrar na Porta {PORTA}'),width=20,  padx=10, pady=10, bg="green", fg="white", activebackground="orange",
           command=lambda porta=PORTA: start_apps(porta,SCRIPT), font=('Courier', 10)).pack()
    Button(GRADE_1, text="Mais informações:", width=20, padx=10, pady=10, bg="lightblue", fg="blue", cursor="hand2",
           command=abrir_link1, font=('Courier', 10)).pack()
    # Encerrar Servidores
    Button(GRADE_1, text="Encerrar Servidores", command=lambda: threading.Thread(target=fechar_aplicacao, args=(root,)).start(),
           width=20, padx=10, pady=10, bg="red", fg="white", activebackground="orange", font=('Courier', 10)).pack()

    # Mensagem dinâmicax'
    mensagem_label = Label(root, text="", bg="#020239", fg="black", font=('Courier', 10))
    mensagem_label.grid(row=1, column=0, columnspan=3, pady=5)



    root.mainloop()
if __name__ == "__main__":
    main(SCRIPT,PORTA)
