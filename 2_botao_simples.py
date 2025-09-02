import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro btn"
    page.padding = 20

    #criando um texto que será modificado pelo btn
    mensagem = ft.Text(
        value="clique no botão abaixo!",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """python
        Esta função será executada sempre que o btn for clicado o perâmetro 'evento' contém informações sobre o clique.
        """
        #mudando o texto da msg
        mensagem.value = "vc caiu no bait"
        mensagem.color = ft.Colors.RED

        #importante: sempre que uma propriedade de um controle for alterada, é necessário chamar o método page.update() para que as mudanças apareçam na tela
        page.update()

    #criando nosso btn
    meu_btn = ft.ElevatedButton(
        text="Clique aqui",
        on_click=botao_clicado,
        width=200,
        height=50,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    #adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_btn)

ft.app(target=main)