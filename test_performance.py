import asyncio
import time

import httpx
import pytest
import pytest_asyncio
from httpx import ASGITransport

from api_pagamentos import app


@pytest.mark.asyncio
@pytest.mark.parametrize("num_requisicoes", [5, 20, 50])
async def test_performance_pagamento(num_requisicoes):
    """
    Testa o endpoint /processar com múltiplas requisições simultâneas.
    Valida que todas retornam status 200 e que o tempo total é < 3.5s.
    """
    transport = ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:

        async def fazer_requisicao():
            response = await client.get("/processar")
            return response

        inicio = time.monotonic()

        respostas = await asyncio.gather(
            *[fazer_requisicao() for _ in range(num_requisicoes)]
        )

        tempo_total = time.monotonic() - inicio

    # Valida que todas as respostas têm status 200
    status_codes = [r.status_code for r in respostas]
    assert all(code == 200 for code in status_codes), (
        f"Nem todas as respostas foram 200. Recebidos: {status_codes}"
    )

    # Valida que o corpo da resposta está correto
    for resposta in respostas:
        assert resposta.json() == {"status": "pagamento_aprovado"}

    # Valida que o tempo total foi menor que 3.5 segundos
    assert tempo_total < 3.5, (
        f"Tempo total de {tempo_total:.2f}s excedeu o limite de 3.5s "
        f"para {num_requisicoes} requisições simultâneas."
    )

    print(
        f"\n✅ {num_requisicoes} requisições concluídas em {tempo_total:.2f}s"
    )
