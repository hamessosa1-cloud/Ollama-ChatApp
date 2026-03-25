import requests
import time

# URL de la API de Ollama
URL = "http://localhost:11434/api/generate"

def consultar_modelo(prompt, modelo="llama3.2:3b"):
    """
    Envía un prompt al modelo de Ollama y devuelve la respuesta + tiempo
    """

    data = {
        "model": modelo,
        "prompt": prompt,
        "stream": False
    }

    try:
        inicio = time.time()

        response = requests.post(URL, json=data, timeout=120)

        tiempo = round(time.time() - inicio, 2)

        if response.status_code == 200:
            respuesta = response.json()["response"]
            return respuesta, tiempo
        else:
            return f"Error HTTP: {response.status_code}", tiempo

    except requests.exceptions.ConnectionError:
        return "Error: Ollama no está corriendo", 0

    except requests.exceptions.Timeout:
        return "Error: tiempo de espera agotado", 0

    except Exception as e:
        return f"Error inesperado: {str(e)}", 0