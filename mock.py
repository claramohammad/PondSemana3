import time
import random

def mock_send_message():
    """Simula o envio de uma mensagem no Slack, retornando um tempo aleatório."""
    simulated_latency = random.uniform(50, 180)  # Simula uma latência entre 50ms e 180ms
    time.sleep(simulated_latency / 1000)  # Converte para segundos
    print(f"📩 Mensagem enviada (simulada) em {simulated_latency:.2f}ms")
    return {"ok": True, "latency": simulated_latency}

def mock_send_message_with_attachment():
    """Simula o envio de uma mensagem com anexo."""
    simulated_latency = random.uniform(100, 250)  # Simula latência entre 100ms e 250ms
    time.sleep(simulated_latency / 1000)
    print(f"📎 Mensagem com anexo enviada (simulada) em {simulated_latency:.2f}ms")
    return {"ok": True, "latency": simulated_latency}

def mock_receive_message():
    """Simula o recebimento de uma mensagem no Slack."""
    simulated_latency = random.uniform(10, 40)  # Simula latência entre 10ms e 40ms
    time.sleep(simulated_latency / 1000)
    print(f"📥 Mensagem recebida e renderizada em {simulated_latency:.2f}ms")
    return {"ok": True, "latency": simulated_latency}
