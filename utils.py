def validar_lista_tarefas(response):
    """
    Valida que a resposta HTTP contém uma lista de tarefas e que
    pelo menos uma delas possui a chave 'completed'.
    """
    body = response.json()

    assert isinstance(body, list), (
        f"Esperava uma lista, mas recebeu: {type(body).__name__}"
    )

    assert len(body) > 0, "A lista de tarefas está vazia."

    tem_completed = any("completed" in tarefa for tarefa in body)
    assert tem_completed, (
        "Nenhuma tarefa na lista contém a chave 'completed'."
    )
