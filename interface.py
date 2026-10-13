import streamlit as st
import requests

URL = "http://localhost:11434/api/chat"
MODELO = "llama3.2"
SISTEMA = (
    "Converse de forma natural e casual, em português, "
    "com respostas curtas e diretas."
)

st.set_page_config(page_title="Aurora", page_icon="💬")
st.title("Aurora")

# Guarda o histórico da conversa enquanto a página estiver aberta
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Mostra as mensagens anteriores (ficam entre o título e a caixa de texto)
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Caixa de texto fixa embaixo, com botão de enviar ao lado
pergunta = st.chat_input("Escreva sua mensagem...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.write(pergunta)

    dados = {
        "model": MODELO,
        "messages": [{"role": "system", "content": SISTEMA}]
        + st.session_state.mensagens,
        "stream": False,
    }

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta = requests.post(URL, json=dados, timeout=300)
                resposta.raise_for_status()
                texto = resposta.json()["message"]["content"]
            except requests.exceptions.RequestException:
                texto = "Não consegui falar com o Ollama. Ele está rodando?"
        st.write(texto)

    st.session_state.mensagens.append({"role": "assistant", "content": texto})