Feature: Latência da Mensagem no Slack

  Como um usuário do Slack
  Quero que minhas mensagens sejam entregues rapidamente
  Para garantir uma comunicação eficiente

  Scenario: Enviar uma mensagem e verificar o tempo de entrega
    Given um usuário autenticado no Slack
    When ele envia uma mensagem para um canal
    Then a mensagem deve ser entregue em menos de 200ms

  Scenario: Mensagem com anexo deve ser entregue em tempo aceitável
    Given um usuário autenticado no Slack
    When ele envia uma mensagem com um anexo de até 1MB
    Then a mensagem deve ser entregue em menos de 300ms

  Scenario: Mensagem recebida deve aparecer instantaneamente
    Given um usuário autenticado no Slack
    When outro usuário envia uma mensagem para ele
    Then a mensagem deve aparecer na interface em menos de 50ms
