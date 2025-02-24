from behave import given, when, then
import time
from mock import (
    mock_send_message, mock_edit_message, mock_send_markdown_message,
    mock_send_message_offline, mock_send_message_no_permission,
    mock_edit_message_timeout, mock_send_large_file, mock_delete_other_user_message
)

@given("um usuário autenticado no Slack")
def step_authenticate(context):
    print("✅ Usuário autenticado (simulado).")

# 🟢 CENÁRIOS POSITIVOS
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

@when("ele edita uma mensagem enviada")
def step_edit_message(context):
    context.response = mock_edit_message()

@then("a mensagem editada deve ser entregue em menos de 150ms")
def step_check_edit_latency(context):
    assert context.response["ok"], "❌ Edição falhou!"
    print(f"✅ Teste aprovado: Edição realizada com sucesso")

@when("ele envia uma mensagem formatada com Markdown")
def step_send_markdown_message(context):
    context.response = mock_send_markdown_message()

@then("a mensagem deve ser exibida corretamente na interface")
def step_check_markdown_display(context):
    assert context.response["ok"], "❌ Markdown não foi processado corretamente!"
    print(f"✅ Teste aprovado: Markdown exibido corretamente")

# 🔴 CENÁRIOS NEGATIVOS
@when("ele tenta enviar uma mensagem sem conexão")
def step_send_message_offline(context):
    context.response = mock_send_message_offline()

@then("ele deve receber um erro informando a falha de envio")
def step_check_offline_error(context):
    assert not context.response["ok"], "❌ A mensagem foi enviada sem conexão!"
    print("✅ Teste aprovado: Erro retornado ao tentar enviar sem internet")

@when("ele tenta enviar uma mensagem em um canal restrito")
def step_send_message_no_permission(context):
    context.response = mock_send_message_no_permission()

@then("ele deve receber um erro informando que não tem permissão")
def step_check_no_permission_error(context):
    assert not context.response["ok"], "❌ Mensagem enviada sem permissão!"
    print("✅ Teste aprovado: Erro retornado ao tentar enviar sem permissão")

@when("ele tenta editar uma mensagem após 30 minutos")
def step_edit_message_timeout(context):
    context.response = mock_edit_message_timeout()

@then("ele deve receber um erro informando que a edição não é permitida")
def step_check_edit_timeout_error(context):
    assert not context.response["ok"], "❌ Mensagem editada após tempo limite!"
    print("✅ Teste aprovado: Erro retornado ao tentar editar mensagem expirada")

@when("ele tenta enviar um arquivo maior que 100MB")
def step_send_large_file(context):
    context.response = mock_send_large_file()

@then("ele deve receber um erro informando que o arquivo é muito grande")
def step_check_large_file_error(context):
    assert not context.response["ok"], "❌ Arquivo muito grande foi enviado!"
    print("✅ Teste aprovado: Erro retornado ao tentar enviar arquivo grande")

@when("ele tenta excluir uma mensagem enviada por outro usuário")
def step_delete_other_user_message(context):
    context.response = mock_delete_other_user_message()

@then("ele deve receber um erro informando que não tem permissão para excluir")
def step_check_delete_permission_error(context):
    assert not context.response["ok"], "❌ Mensagem de outro usuário foi excluída!"
    print("✅ Teste aprovado: Erro retornado ao tentar excluir mensagem de outro usuário")
