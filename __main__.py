import tkinter as tk
from tkinter import ttk
import random

class SmartBinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Monitoramento - Lixeira Inteligente")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f5f5f5")

        # Cabeçalho
        header = tk.Frame(root, bg="#2e7d32", height=70)
        header.pack(fill="x")

        tk.Label(
            header,
            text="LIXEIRA INTELIGENTE - CIDADE LIMPA",
            bg="#2e7d32",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        # Painel principal
        main = tk.Frame(root, bg="#f5f5f5")
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # Menu lateral
        sidebar = tk.Frame(main, bg="#263238", width=220)
        sidebar.pack(side="left", fill="y")

        tk.Label(
            sidebar,
            text="MENU",
            bg="#263238",
            fg="white",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        botoes = [
            "Dashboard",
            "Mapa",
            "Lixeiras",
            "Alertas",
            "Relatórios",
            "Configurações"
        ]

        for item in botoes:
            tk.Button(
                sidebar,
                text=item,
                width=20,
                bg="#37474f",
                fg="white",
                relief="flat"
            ).pack(pady=5)

        # Área central
        content = tk.Frame(main, bg="#f5f5f5")
        content.pack(side="right", fill="both", expand=True)

        # Cards superiores
        cards = tk.Frame(content, bg="#f5f5f5")
        cards.pack(fill="x")

        self.card_total = self.criar_card(cards, "Lixeiras Ativas", "156")
        self.card_cheias = self.criar_card(cards, "Quase Cheias", "23")
        self.card_alertas = self.criar_card(cards, "Alertas", "5")
        self.card_online = self.criar_card(cards, "Conectadas", "98%")

        # Área principal
        area = tk.Frame(content, bg="#f5f5f5")
        area.pack(fill="both", expand=True, pady=10)

        # Lista de lixeiras
        frame_lista = tk.LabelFrame(
            area,
            text="Lixeiras Monitoradas",
            padx=10,
            pady=10
        )
        frame_lista.pack(side="left", fill="y", padx=5)

        self.lista = tk.Listbox(frame_lista, width=25, height=20)
        self.lista.pack()

        for i in range(1, 11):
            self.lista.insert("end", f"Lixeira #{i}")

        self.lista.bind("<<ListboxSelect>>", self.atualizar_detalhes)

        # Painel de detalhes
        detalhes = tk.LabelFrame(
            area,
            text="Status da Lixeira",
            padx=20,
            pady=20
        )
        detalhes.pack(side="right", fill="both", expand=True, padx=5)

        self.nome = tk.Label(
            detalhes,
            text="Selecione uma lixeira",
            font=("Arial", 18, "bold")
        )
        self.nome.pack(pady=10)

        tk.Label(
            detalhes,
            text="Nível de preenchimento"
        ).pack()

        self.progress = ttk.Progressbar(
            detalhes,
            length=400,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        self.lbl_nivel = tk.Label(
            detalhes,
            text="0%"
        )
        self.lbl_nivel.pack()

        self.lbl_peso = tk.Label(
            detalhes,
            text="Peso: 0 kg",
            font=("Arial", 12)
        )
        self.lbl_peso.pack(pady=5)

        self.lbl_bateria = tk.Label(
            detalhes,
            text="Bateria: 100%",
            font=("Arial", 12)
        )
        self.lbl_bateria.pack(pady=5)

        self.lbl_status = tk.Label(
            detalhes,
            text="Status: Normal",
            font=("Arial", 12, "bold"),
            fg="green"
        )
        self.lbl_status.pack(pady=15)

        tk.Button(
            detalhes,
            text="Atualizar Dados",
            bg="#2e7d32",
            fg="white",
            font=("Arial", 12),
            command=self.simular_dados
        ).pack(pady=15)

    def criar_card(self, parent, titulo, valor):
        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        frame.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        tk.Label(
            frame,
            text=titulo,
            bg="white",
            font=("Arial", 11)
        ).pack(pady=5)

        tk.Label(
            frame,
            text=valor,
            bg="white",
            fg="#2e7d32",
            font=("Arial", 18, "bold")
        ).pack(pady=5)

        return frame

    def atualizar_detalhes(self, event):
        self.simular_dados()

    def simular_dados(self):
        try:
            indice = self.lista.curselection()[0] + 1
        except:
            indice = 1

        nivel = random.randint(10, 100)
        peso = random.randint(5, 50)
        bateria = random.randint(40, 100)

        self.nome.config(text=f"Lixeira #{indice}")

        self.progress["value"] = nivel
        self.lbl_nivel.config(text=f"{nivel}%")

        self.lbl_peso.config(
            text=f"Peso: {peso} kg"
        )

        self.lbl_bateria.config(
            text=f"Bateria: {bateria}%"
        )

        if nivel >= 80:
            self.lbl_status.config(
                text="Status: Coleta Necessária",
                fg="red"
            )
        elif nivel >= 60:
            self.lbl_status.config(
                text="Status: Atenção",
                fg="orange"
            )
        else:
            self.lbl_status.config(
                text="Status: Normal",
                fg="green"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartBinApp(root)
    root.mainloop()