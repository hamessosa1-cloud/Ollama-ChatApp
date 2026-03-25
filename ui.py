import tkinter as tk
from app.llm_client import consultar_modelo

def iniciar_ui():
    def enviar():
        prompt = entrada.get()

        if prompt == "":
            return

        chat.insert(tk.END, "Tú: " + prompt + "\n")

        respuesta, tiempo = consultar_modelo(prompt)

        chat.insert(tk.END, f"IA ({tiempo}s): {respuesta}\n\n")

        entrada.delete(0, tk.END)

    ventana = tk.Tk()
    ventana.title("Chat IA Local - Gemma 2B")

    chat = tk.Text(ventana, height=20, width=60)
    chat.pack()

    entrada = tk.Entry(ventana, width=50)
    entrada.pack()

    boton = tk.Button(ventana, text="Enviar", command=enviar)
    boton.pack()

    ventana.mainloop()