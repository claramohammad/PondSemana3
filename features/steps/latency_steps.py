from behave import given, when, then
import time
from mock import mock_send_message, mock_send_message_with_attachment, mock_receive_message

@given("um usuário autenticado no Slack")
def step_authenticate(context):
    print("✅ Usuário autenticado (simulado).")

@when("ele envia uma mensagem para um canal")
def step_send_message(context):
    context.start_time = time.time()
    response = mock_send_message()
    context.end_time = time.time()
    context.response = response

@then("a mensagem deve ser entregue em menos de 200ms")
def step_check_latency(context):
    elapsed_time = context.response["latency"]
    assert elapsed_time < 200, f"❌ Latência de {elapsed_time:.2f}ms excedeu 200ms"
    print(f"✅ Teste aprovado: Mensagem entregue em {elapsed_time:.2f}ms")

@when("ele envia uma mensagem com um anexo de até 1MB")
def step_send_message_with_attachment(context):
    context.start_time = time.time()
    response = mock_send_message_with_attachment()
    context.end_time = time.time()
    context.response = response

@then("a mensagem deve ser entregue em menos de 300ms")
def step_check_attachment_latency(context):
    elapsed_time = context.response["latency"]
    assert elapsed_time < 300, f"❌ Latência de {elapsed_time:.2f}ms excedeu 300ms"
    print(f"✅ Teste aprovado: Mensagem com anexo entregue em {elapsed_time:.2f}ms")

@when("outro usuário envia uma mensagem para ele")
def step_receive_message(context):
    context.start_time = time.time()
    response = mock_receive_message()
    context.end_time = time.time()
    context.response = response

@then("a mensagem deve aparecer na interface em menos de 50ms")
def step_check_display_latency(context):
    elapsed_time = context.response["latency"]
    assert elapsed_time < 50, f"❌ Tempo de exibição foi {elapsed_time:.2f}ms, acima do esperado"
    print(f"✅ Teste aprovado: Mensagem exibida em {elapsed_time:.2f}ms")
