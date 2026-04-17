# ATS9-Testes-APIs
Este projeto realiza testes de performance em uma API construída com FastAPI, simulando múltiplas requisições simultâneas ao endpoint /processar.

Os testes utilizam pytest, pytest-asyncio e httpx para validar o comportamento assíncrono da aplicação, garantindo que:

Todas as requisições retornam status 200;
A resposta está correta (pagamento_aprovado);
O tempo total de execução permanece abaixo de 3,5 segundos, mesmo com alta concorrência (até 50 requisições simultâneas).

O objetivo é demonstrar a eficiência do processamento assíncrono e a capacidade da API de lidar com múltiplos acessos ao mesmo tempo.
