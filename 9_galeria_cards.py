# Galeria de Animais com Filtros usando Flet
# Este script cria uma interface gráfica que exibe uma galeria de animais em cards,

# Importa a biblioteca Flet para criar interfaces gráficas
import flet as ft

def criar_card_animal(nome, emoji, descricao, cor):
    """
    Função que cria um card (cartão) visual para cada animal.
    """
    return ft.Container(
        content=ft.Column([
            # Emoji grande no topo do card
            ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
            # Nome do animal em negrito e branco
            ft.Text(nome, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            # Descrição menor e com transparência
            ft.Text(descricao, size=12, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza tudo horizontalmente
        spacing=8  # Espaço de 8 pixels entre cada elemento
        ),
        bgcolor=cor,  # Cor de fundo do card (varia por animal)
        padding=10,   # Espaçamento interno de 20 pixels
        border_radius=15,  # Bordas arredondadas
        width=400,    # Largura fixa do card
        height=900,   # Altura fixa do card
        # Sombra para dar efeito de profundidade
        shadow=ft.BoxShadow(
            spread_radius=1,  # Expansão da sombra
            blur_radius=8,    # Intensidade do desfoque
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)  # Cor preta com 30% de transparência
        )
    )

def main(page: ft.Page):
    """
    Função principal que define toda a interface do aplicativo.
    Esta função é chamada quando o app inicia.
    """
    
    # Configurações básicas da página/janela
    page.title = "Galeria com Filtros"  # Título que aparece na aba do navegador
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)  # Margem interna da página
    page.scroll = ft.ScrollMode.AUTO  # Permite rolagem quando o conteúdo não cabe na tela
    
    # Lista com todos os dados dos animais
    # Cada animal é um dicionário (como uma ficha) com suas características
    animais = [
        {
            "nome": "Tiranossauro", 
            "emoji": "🦖", 
            "descricao": "Carnívoro, bípede, dentes afiados e visão apurada", 
            "cor": ft.Colors.BROWN_400, 
            "categoria": "Carnívoro", 
            "tamanho": "Grande",
            "sociável": "Antissocial"
        },
        {
            "nome": "Espinossauro", 
            "emoji": "🦖", 
            "descricao": "Maior carnívoro terrestre", 
            "cor": ft.Colors.GREEN_700, 
            "categoria": "Carnívoro", 
            "tamanho": "Grande",
            "sociável": "Antissocial"
        },
        {
            "nome": "Estegossauro", 
            "emoji": "🦕", 
            "descricao": "Herbívoro com placas ósseas nas costas", 
            "cor": ft.Colors.GREEN_400, 
            "categoria": "Herbívoro", 
            "tamanho": "Médio",
            "sociável": "Sociável"
        },
        {
            "nome": "Velociraptor", 
            "emoji": "🦖", 
            "descricao": "Inteligente e caçava em grupo.", 
            "cor": ft.Colors.ORANGE_400, 
            "categoria": "Carnívoro", 
            "tamanho": "Pequeno",
            "sociável": "Sociável"
        },
        {
            "nome": "Braquiossauro", 
            "emoji": "🦕", 
            "descricao": "Herbívoro gigante com pescoço longo", 
            "cor": ft.Colors.BLUE_200, 
            "categoria": "Herbívoro", 
            "tamanho": "Grande",
            "sociável": "Sociável"
        },
        {
            "nome": "Tricerátopo", 
            "emoji": "🦕", 
            "descricao": "Herbívoro com três chifres", 
            "cor": ft.Colors.LIME_700, 
            "categoria": "Herbívoro", 
            "tamanho": "Médio",
            "sociável": "Sociável"
        },
        {
            "nome": "Anquilossauro", 
            "emoji": "🦕", 
            "descricao": "Herbívoro blindado", 
            "cor": ft.Colors.GREY_600, 
            "categoria": "Herbívoro", 
            "tamanho": "Médio",
            "sociável": "Sociável"
        }
    ]
    
    # Criação dos elementos visuais da interface
    
    # GridView = uma grade que organiza os cards em colunas e linhas automaticamente
    area_cards = ft.GridView(
        expand=1,              # Ocupa todo o espaço disponível
        runs_count=2,          # 2 colunas de cards
        max_extent=180,        # Largura máxima de cada card
        child_aspect_ratio=1.0, # Proporção altura/largura (1.0 = quadrado)
        spacing=15,            # Espaço horizontal entre cards
        run_spacing=15         # Espaço vertical entre cards
    )
    
    # Dropdown = menu suspenso para escolher categoria
    filtro_categoria = ft.Dropdown(
        label="Categoria",  # Texto que aparece acima do menu
        width=150,          # Largura do menu
        value="Todos",      # Valor selecionado inicialmente
        options=[           # Lista de opções disponíveis
            ft.dropdown.Option("Todos"), 
            ft.dropdown.Option("Carnívoro"), 
            ft.dropdown.Option("Herbívoro")
        ]
    )
    
    # Dropdown para filtrar por tamanho
    filtro_tamanho = ft.Dropdown(
        label="Tamanho", 
        width=150, 
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"), 
            ft.dropdown.Option("Pequeno"), 
            ft.dropdown.Option("Médio"), 
            ft.dropdown.Option("Grande")
        ]
    )
    filtro_Social = ft.Dropdown(
        label="Social", 
        width=150, 
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"), 
            ft.dropdown.Option("Sociável"), 
            ft.dropdown.Option("Antissocial")
        ]
    )
    
    # Campo de texto para buscar animais por nome
    campo_busca = ft.TextField(
        label="Buscar",                    # Texto de ajuda que aparece no campo
        width=150,                         # Largura do campo
        prefix_icon=ft.Icons.SEARCH        # Ícone de lupa no início do campo
    )
    
    # Texto que mostra quantos animais estão sendo exibidos
    contador = ft.Text(
        "",                                # Texto vazio inicialmente
        size=14, 
        color=ft.Colors.GREY_600, 
        text_align=ft.TextAlign.CENTER
    )
    
    def carregar_cards(e=None):
        """
        Função que carrega e exibe os cards dos animais aplicando os filtros.
        
        Parâmetro 'e' é o evento (quando o usuário muda algo), mas não usamos aqui.
        O '=None' significa que o parâmetro é opcional.
        """
        
        # Primeiro, limpa todos os cards que estão sendo mostrados
        area_cards.controls.clear()
        
        # Pega os valores atuais dos filtros
        categoria = filtro_categoria.value
        tamanho = filtro_tamanho.value
        social = filtro_Social.value
        busca = (campo_busca.value or "").lower()  # Converte para minúscula para comparar melhor
        
        # Filtra os animais usando list comprehension (uma forma compacta de filtrar listas)
        # Para cada animal 'a' na lista 'animais', inclui apenas se:
        filtrados = [a for a in animais 
                    if (categoria == "Todos" or a["categoria"] == categoria) and      # Categoria bate OU é "Todos"
                       (tamanho == "Todos" or a["tamanho"] == tamanho) and          # Tamanho bate OU é "Todos"
                        (social == "Todos" or a["sociável"] == social) and          # Social bate OU é "Todos"
                       (not busca or busca in a["nome"].lower())]                   # Não há busca OU nome contém o texto buscado
        
        # Para cada animal que passou pelos filtros, cria um card e adiciona na grade
        for animal in filtrados:
            # Chama a função que criamos lá em cima para fazer o card
            card_do_animal = criar_card_animal(
                animal["nome"], 
                animal["emoji"], 
                animal["descricao"], 
                animal["cor"]
            )
            # Adiciona o card na área de exibição
            area_cards.controls.append(card_do_animal)
        
        # Atualiza o contador mostrando quantos animais estão visíveis
        total_filtrados = len(filtrados)  # Quantos animais passaram pelos filtros
        total_geral = len(animais)        # Total de animais no sistema
        
        if total_filtrados == total_geral:
            # Se está mostrando todos, escreve uma mensagem
            contador.value = f"Mostrando todos os {total_filtrados} animais"
        else:
            # Se está filtrado, mostra quantos foram encontrados
            contador.value = f"Encontrados {total_filtrados} de {total_geral} animais"
        
        # Atualiza a tela para mostrar as mudanças
        page.update()
    
    def limpar_filtros(e):
        """
        Função que limpa todos os filtros e volta ao estado inicial.
        
        Parâmetro 'e' é o evento do clique no botão.
        """
        # Volta todos os filtros para "Todos"
        filtro_categoria.value = "Todos"
        filtro_tamanho.value = "Todos"
        filtro_Social.value = "Todos"
        # Limpa o campo de busca
        campo_busca.value = ""
        # Recarrega os cards (agora sem filtros)
        carregar_cards()
    
    # Conecta os eventos: quando o usuário mudar qualquer filtro, chama carregar_cards()
    for controle in [filtro_categoria, filtro_tamanho, campo_busca, filtro_Social]:
        controle.on_change = carregar_cards  # 'on_change' = quando mudar
    
    # Carrega os cards pela primeira vez (quando o app abre)
    carregar_cards()
    
    # Constrói a interface visual adicionando todos os elementos à página
    page.add(
        ft.Column([  # Coluna = organiza elementos um embaixo do outro
            
            # Título principal do app
            ft.Text(
                "🦁 Zoológico Virtual", 
                size=24, 
                weight=ft.FontWeight.BOLD, 
                text_align=ft.TextAlign.CENTER
            ),
            
            # Subtítulo explicativo
            ft.Text(
                "Explore diferentes categorias de animais", 
                size=14, 
                color=ft.Colors.GREY_600, 
                text_align=ft.TextAlign.CENTER
            ),
            
            # Primeira linha de filtros: categoria, tamanho e social lado a lado
            ft.Row([filtro_categoria, filtro_tamanho, filtro_Social], 
                  alignment=ft.MainAxisAlignment.CENTER,  # Centraliza na tela
                  spacing=20  # 20 pixels de espaço entre eles
            ),
            
            # Segunda linha: campo de busca e botão de limpar
            ft.Row([
                campo_busca, 
                ft.ElevatedButton(
                    "🧹 Limpar",           # Texto do botão com emoji
                    on_click=limpar_filtros,  # Função a chamar quando clicado
                    bgcolor=ft.Colors.GREY_400,  # Cor de fundo
                    color=ft.Colors.WHITE        # Cor do texto
                )
            ], 
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=20
            ),
            
            # Contador de resultados
            contador,
            
            # Container = caixa que contém a grade de animais
            ft.Container(
                content=area_cards,      # A grade que criamos
                height=400,              # Altura fixa de 400 pixels
                border=ft.border.all(1, ft.Colors.GREY_300),  # Borda cinza de 1 pixel
                border_radius=10,        # Bordas arredondadas
                padding=10               # Espaçamento interno
            )
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza tudo horizontalmente
        spacing=15  # 15 pixels de espaço entre cada seção
        )
    )

# Inicia o aplicativo Flet chamando a função main
ft.app(target=main)