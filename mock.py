def mock_send_message():
    return {"ok": True, "latency": 180}

def mock_edit_message():
    return {"ok": True, "latency": 120}

def mock_send_markdown_message():
    return {"ok": True}

def mock_send_message_offline():
    return {"ok": False, "error": "Sem conexão"}

def mock_send_message_no_permission():
    return {"ok": False, "error": "Sem permissão"}

def mock_edit_message_timeout():
    return {"ok": False, "error": "Edição não permitida"}

def mock_send_large_file():
    return {"ok": False, "error": "Arquivo muito grande"}

def mock_delete_other_user_message():
    return {"ok": False, "error": "Sem permissão"}
