import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.padding = 20

    # Título principal
    titulo = ft.Text(
        "👤Crie Seu Perfil",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Subtítulo
    subtitulo = ft.Text(
        "Preencha as informações abaixo",
        size=16,
        text_align=ft.TextAlign.CENTER
    )

    head = ft.Column(
        controls =[titulo, subtitulo],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    inp_name = ft.TextField(
        label="Nome completo",
        width=300,
        border_color=ft.Colors.BLUE,
    )

    inp_idade = ft.TextField(
        label="Idade",
        width=300,
        border_color=ft.Colors.BLUE,
    )

    hobby = ft.Dropdown(
        options=[
            ft.dropdown.Option("Desenhar"),
            ft.dropdown.Option("Fotografia"),
            ft.dropdown.Option("Musica"),
            ft.dropdown.Option("Escrever"),
            ft.dropdown.Option("Ler livros"),
            ft.dropdown.Option("Aprender idiomas"),
            ft.dropdown.Option("Jogos de tabuleiro"),
            ft.dropdown.Option("Academia"),
            ft.dropdown.Option("Caminhar"),
            ft.dropdown.Option("Andar de bicicleta"),
            ft.dropdown.Option("Meditação"),
            ft.dropdown.Option("Jardinagem"),
            ft.dropdown.Option("Cozinhar"),
            ft.dropdown.Option("Assistir séries/filmes"),
            ft.dropdown.Option("Jogar videogame")
        ],
        border_color=ft.Colors.BLUE,
        width=300,
        label="Hobby favorito"
    )
    btn_criar = ft.ElevatedButton(
        text="📝Criar Perfil",
        width=150,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    btn_limpar = ft.ElevatedButton(
        text="🧹Limpar",
        width=150,
        bgcolor=ft.Colors.GREY,
        color=ft.Colors.WHITE
    )

    btn = ft.Row(
        controls=[btn_criar, btn_limpar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    inp = ft.Column(
        controls=[inp_name, inp_idade, hobby, btn],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina = ft.Column(
        controls=[head, inp],
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Cartão de perfil (inicialmente oculto)
    cartao_perfil = ft.Container(
        content=ft.Text("Preencha as informações acima para criar seu perfil."),
        bgcolor=ft.Colors.GREY_100,
        padding=20,
        border_radius=15,
        width=350,
        visible=False
    )

    # Função para mostrar mensagem de erro
    def mostrar_erro(msg):
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text(msg, color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        cartao_perfil.bgcolor = ft.Colors.RED_50
        cartao_perfil.visible = True
        page.update()

    # Função para criar o cartão de perfil
    def criar_perfil(e):
        nome = inp_name.value.strip()
        idade_str = inp_idade.value.strip()
        hobbie = hobby.value

        # Validações
        if not nome or len(nome) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return
        if not idade_str:
            mostrar_erro("Idade é obrigatória")
            return
        try:
            idade = int(idade_str)
            if idade < 1 or idade > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")
            return
        if not hobbie:
            mostrar_erro("Selecione um hobby")
            return

        # Definir categoria de idade
        if idade < 18:
            categoria = "Jovem"
            cor_icone = ft.Colors.GREEN
        elif idade < 60:
            categoria = "Adulto"
            cor_icone = ft.Colors.BLUE
        else:
            categoria = "Experiente"
            cor_icone = ft.Colors.PURPLE

        # Montar cartão visual
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.PERSON, size=60, color=cor_icone),
            ft.Text(nome, size=20, weight=ft.FontWeight.BOLD, color=cor_icone),
            ft.Text(f"{idade} anos - {categoria}", size=14, color=ft.Colors.GREY_600),
            ft.Text(f"Hobby: {hobbie}", size=14, color=ft.Colors.GREY_600),
            ft.Container(
                content=ft.Text("Perfil criado com sucesso! 🎉", color=ft.Colors.WHITE),
                bgcolor=cor_icone,
                padding=10,
                border_radius=20
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        cartao_perfil.bgcolor = ft.Colors.WHITE
        cartao_perfil.visible = True
        page.update()

    # Função para limpar campos
    def limpar_campos(e):
        inp_name.value = ""
        inp_idade.value = ""
        hobby.value = None
        cartao_perfil.visible = False
        page.update()

    # Associar eventos aos botões
    btn_criar.on_click = criar_perfil
    btn_limpar.on_click = limpar_campos

    pagina = ft.Column(
        controls=[head, inp, cartao_perfil],
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(pagina)

ft.app(target=main)