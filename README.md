# Ponderada Semana 3

O **Slack** é uma plataforma de comunicação para equipes que permite troca de mensagens em tempo real, colaboração por meio de canais organizados e compartilhamento de arquivos. Ele é amplamente utilizado em ambientes corporativos para comunicação eficiente. Este repositório contém **testes automatizados** para validar **requisitos funcionais e não funcionais** relacionados ao envio, edição e exclusão de mensagens no Slack.

## Requisitos Testados

#### Funcionais

- **Envio de mensagens** - O usuário pode enviar mensagens para um canal.  
- **Edição de mensagens** - O usuário pode editar uma mensagem já enviada.  
- **Formatar mensagens com Markdown** - O Slack renderiza corretamente mensagens formatadas.  
- **Exclusão de mensagens** - Apenas o autor pode excluir sua própria mensagem.  
- **Envio de arquivos** - O Slack impõe um limite de tamanho para arquivos enviados.  

#### Não Funcionais

- **Baixa latência no envio de mensagens** - As mensagens devem ser entregues em menos de 200ms.  
- **Baixa latência na edição de mensagens** - Edições devem ser processadas em menos de 150ms.  
- **Baixa latência na exibição de mensagens recebidas** - Mensagens devem aparecer na interface em menos de 50ms.  
- **Controle de permissões** - O Slack deve impedir o envio de mensagens em canais privados sem autorização.  
- **Conectividade** - O Slack deve detectar quando não há conexão à internet e impedir o envio de mensagens.  
- **Limitação de edição** - O Slack deve impedir edições após 30 minutos.  
- **Restrição de tamanho de arquivos** - Arquivos maiores que 100MB não devem ser aceitos.  

## Como Rodar os Testes

Primeiro, instale a depêndencia com `pip install -r requirements.txt` e depois rode os testes com `behave`
