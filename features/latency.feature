Feature: Testes de mensagens no Slack

  Como um usuário do Slack
  Quero enviar, editar e excluir mensagens corretamente
  Para garantir uma comunicação eficiente e confiável

  # 🟢 CENÁRIOS POSITIVOS
  Scenario: Enviar uma mensagem e verificar o tempo de entrega
    Given um usuário autenticado no Slack
    When ele envia uma mensagem para um canal
    Then a mensagem deve ser entregue em menos de 200ms

  Scenario: Mensagem editada deve ser entregue rapidamente
    Given um usuário autenticado no Slack
    When ele edita uma mensagem enviada
    Then a mensagem editada deve ser entregue em menos de 150ms

  Scenario: Enviar mensagem com formatação Markdown
    Given um usuário autenticado no Slack
    When ele envia uma mensagem formatada com Markdown
    Then a mensagem deve ser exibida corretamente na interface

  # 🔴 CENÁRIOS NEGATIVOS
  Scenario: Tentar enviar uma mensagem sem conexão à internet
    Given um usuário autenticado no Slack
    When ele tenta enviar uma mensagem sem conexão
    Then ele deve receber um erro informando a falha de envio

  Scenario: Tentar enviar uma mensagem sem permissão
    Given um usuário autenticado no Slack
    When ele tenta enviar uma mensagem em um canal restrito
    Then ele deve receber um erro informando que não tem permissão

  Scenario: Tentar editar uma mensagem após tempo limite
    Given um usuário autenticado no Slack
    When ele tenta editar uma mensagem após 30 minutos
    Then ele deve receber um erro informando que a edição não é permitida

  Scenario: Tentar enviar um arquivo muito grande
    Given um usuário autenticado no Slack
    When ele tenta enviar um arquivo maior que 100MB
    Then ele deve receber um erro informando que o arquivo é muito grande

  Scenario: Tentar excluir mensagem de outro usuário
    Given um usuário autenticado no Slack
    When ele tenta excluir uma mensagem enviada por outro usuário
    Then ele deve receber um erro informando que não tem permissão para excluir
