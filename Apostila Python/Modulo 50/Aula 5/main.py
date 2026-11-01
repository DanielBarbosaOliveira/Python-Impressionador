# Hashzap
# Botao de iniciar chat
# popup para entrar no chat
# Quando entra no chat: (aparece para todo mundo)
    # Mensagem de que você entrou no chat
    # Campo e botao de enviar mensagem
# A cada mensagem enviada: (aparece para todo mundo)
    # Nome: Texto da Mensagem

import flet as ft

def main(page: ft.Page):
    texto = ft.Text("Hashzap")
    
    chat = ft.Column(expand=True, width= float("inf") ,horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=10)
    
    nome_usuario = ft.TextField(
        label="Digite seu nome de usuário",)
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem['texto']
            usuario_mensagem = mensagem['usuario']
            # Pegar mensagem e adicionar no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.Colors.BLUE_200))
        page.update()
    
    page.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        page.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        page.update()
    
    campo_mensagem = ft.TextField(label="Digite sua mensagem", expand=True, on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.Button("Enviar", on_click=enviar_mensagem)
    
    def entrar_popup(evento):
        page.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        page.add(chat)
        # fechar o popup
        page.pop_dialog()
        # remover botao iniciar chat
        page.remove(botao_iniciar)
        page.remove(texto)
        # criar campo de mensagem do usuário e botão de enviar mensagem
        page.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        
        page.update()
    
    popup = ft.AlertDialog(
        modal=True,
        title=ft.Text("Bem-vindo ao Hashzap!"),
        content=nome_usuario,
        actions=[ft.Button("Entrar", on_click=entrar_popup)]
    )
    
    def entra_chat(evento):
        page.show_dialog(popup)

    botao_iniciar = ft.Button("Iniciar Chat", on_click=entra_chat)
    
    page.add(texto, botao_iniciar)

ft.run(main)