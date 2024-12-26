from tkinter import Tk, Frame, StringVar, Label, IntVar
from tkinter.ttk import Progressbar
import threading
import time

class Application:
    def __init__(self, master: Tk = None):
        self.master = master

        self.master.overrideredirect(True) # Remove a barra superior
        self.master.title("Ultron") # Altera o título da janela

        self.load_screen = Frame(self.master)
        self.load_screen.pack(padx=5, pady=5)
        self.label01_text = StringVar(value="Carregando, por favor aguarde...")
        self.label01 = Label(self.load_screen, textvariable=self.label01_text)
        self.label01.pack()
        self.percent = IntVar(value=0)
        self.progress_bar = Progressbar(self.load_screen, variable=self.percent)
        self.progress_bar.config(orient="horizontal")
        self.progress_bar.config(mode="determinate")
        self.progress_bar.config(length=250)
        self.progress_bar.pack()

        # Cria uma Thread para executar o carregamento simultaneamente
        threading.Thread(target=self.load_main_screen, daemon=True).start()
        """
            O parâmetro 'daemon' faz com que a Thread seja encerrada 
            automaticamente quando a Thread principal é fechada.
        """

    # Função que realiza o carregamento das informações da janela
    def load_main_screen(self):
        time.sleep(1)
        qtt_operation = range(100)
        for i, _ in enumerate(qtt_operation, start=1):
            self.percent.set(i)
            time.sleep(0.1)
        time.sleep(1)
        self.master.withdraw() # Esconde a janela
        self.master.overrideredirect(False) # Devolve a barra superior
        self.load_screen.destroy()
        self.init_main_screen()

    # Função que inicializa a janela principal após o carregamento
    def init_main_screen(self):
        self.master.resizable(False, False) # Desabilita o redimensionamento da janela

        self.main_screen = Frame(self.master)
        self.main_screen.pack(padx=5, pady=5)

        self.container_header = Frame(self.main_screen)
        self.container_header.pack()
        self.label_title_text = StringVar(value="Inventário de máquina")
        self.label_title = Label(self.container_header, textvariable=self.label_title_text)
        self.label_title.config(font=("Segoe UI", "10", "bold"))
        self.label_title.pack()

        self.container_main = Frame(self.main_screen)
        self.container_main.pack(padx=100)

        self.container_footer = Frame(self.main_screen)
        self.container_footer.pack()
        self.label_foot_text = StringVar(value="Desenvolvido por Derik B. Pimentel")
        self.label_foot = Label(self.container_footer, textvariable=self.label_foot_text)
        self.label_foot.pack()

        self.master.deiconify() # Mostra a janela novamente

if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()