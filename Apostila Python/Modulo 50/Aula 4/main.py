import streamlit as st
from google import genai
from chaves import chave_gemini

# Cria o cliente (uma conexão nova e aberta a cada execução)
modelo_ia = genai.Client(api_key=chave_gemini)

st.write("# Chatbot com IA")

# 1. Histórico de mensagens para a tela do Streamlit
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe as mensagens já enviadas
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    # 2. Mostra e salva a mensagem do usuário
    st.chat_message("user").write(texto_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})

    # 3. Converte a lista para o formato exato que a API do Gemini exige
    # (role: user/model e parts contendo dicionários com {"text": ...})
    historico_gemini = [
        {
            "role": "user" if msg["role"] == "user" else "model",
            "parts": [{"text": msg["content"]}]
        }
        for msg in st.session_state["lista_mensagens"]
    ]

    # 4. Envia o histórico completo para a IA
    with st.spinner("Pensando na resposta..."):
        resposta_ia = modelo_ia.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=historico_gemini
        )
        texto_resposta_ia = resposta_ia.text

    # 5. Mostra e salva a resposta da IA
    st.chat_message("assistant").write(texto_resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta_ia})