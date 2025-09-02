import flet as ft

def main(page: ft.Page):
    page.title = "Campo de texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20) #padding área segura

    #criando um campo onde o usuário pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300,
        border_color=ft.Colors.BLUE,
    )

    #texto que mostrará a resposta
    resposta = ft.Text(
        value="", #inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER,
    )

    def processar_nome(evento):
        """
        Função que pega o textp digitado pelo usuário e faz algo com ele.
        """
        #Pegando o valor digitado no campo
        nome_digitado = campo_nome.value

        #verificando se o usuário realmente digitou algo
        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "por favor, digite seu nome!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "nome muito curto!"
            resposta.color = ft.Colors.RED
        else:
            resposta.value = f"olá, {nome_digitado}! prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN
        
        #Atualizando a interface
        page.update()
    #botao para processar o nome
    botao_ok = ft.ElevatedButton(
        text="confirmar",
        on_click=processar_nome,
        width=150
    )

    #adifionando elementos à página
    page.add(
        ft.Text("Vamos nos conhecer!", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)
