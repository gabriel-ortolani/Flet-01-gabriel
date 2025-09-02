# Aprendizagem flet

Este repositório contém exemplos, desafios e projetos de programação mobile utilizando [Flet](https://flet.dev/), uma biblioteca Python para criação de interfaces gráficas modernas e multiplataforma.

## Sobre

Aqui você encontra códigos de estudo e prática, incluindo:

- Primeiros passos com Flet
- Layouts básicos e avançados
- Componentes interativos (botões, campos de texto, listas, etc)
- Aplicativos de exemplo: calculadora, loja virtual, zoológico virtual, painel de configuração, entre outros
- Exercícios e desafios para fixação dos conceitos

## Criação de um arquivo flet do zero
1. **Crie a pasta .venv**
   ```bash
   python -m venv .venv
   ```
3. **ative a pasta .venv**
   ```bash
   .venv\Scripts\activate
   ```
4.  **Instale o flet**
```bash
pip install flet-desktop
```
4. **Executar o arquivo**
```bash
flet run --web Nome_do_arquivo.py
```
---

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Flet-01-gabriel.git
   cd Flet-01-gabriel
   ```

2. **Instale o Flet:**
   ```bash
   pip install flet
   ```

3. **Execute qualquer arquivo de exemplo:**
   ```bash
   python nome_do_arquivo.py
   ```
   Exemplo:
   ```bash
   python 1_primeiro_app.py
   ```

## Estrutura

- `1_primeiro_app.py` — Seu primeiro app Flet<br>
  <img width="378" height="119" alt="image" src="https://github.com/user-attachments/assets/bef9f884-0169-4ee5-adb8-bdc83470d114" /><br>
  Neste primeiro site/aplicativo foi comprenedido o basico da inserção de texto com flet
- `2_botao_simples.py` — Exemplo de botão interativo<br>
<img width="170" height="77" alt="image" src="https://github.com/user-attachments/assets/28b05841-2967-4038-8f6c-2c9418333556" /><br>
Nesta aplicação foi aprendido a criação de botões e a criação de eventos quando o botão é apertado acime pode se ver o botão antes de ser apertado e abaixo a troca do texto que ocorre quando aperta o botão<br>
<img width="157" height="77" alt="image" src="https://github.com/user-attachments/assets/e3e51b74-e050-4cd2-8dcb-349be044bae2" /><br>


- `3_campo_texto.py` — Campo de texto e resposta dinâmica<br>
<img width="239" height="107" alt="image" src="https://github.com/user-attachments/assets/38edf486-a56d-4622-bbb0-9202c4b943d3" /><br>
Nesta aplicação foi desenvolvido à aplicação das caixas de texto que são preenchidas pelo usuario(inputs), na imagem acima é mostrado o site ao iniciar onde podemos colocar nosso nome e logo apos ao apertar o botão aparece uma mensagem prazer em conhece-lo como mostrado na imagem abaixo <br>
<img width="248" height="138" alt="image" src="https://github.com/user-attachments/assets/d23b4786-e8f7-48ae-b249-aec0d623c486" /><br>



- `4_lista_cores.py` — Seletor de cores<br>
<img width="290" height="179" alt="image" src="https://github.com/user-attachments/assets/03306a56-fab9-4999-ab81-59e0690cdaf6" /><br>
Neste arquivo foi aprendido a capacidade de alterar elementos visuais de acordo com a seleção de cores, como na imagem acima que mostra o site ao seriniciado que vem com uma cor padrão branca e ao escolher uma cor essa cor branca muda para a cor corresposdente como na imagem abaixo.<br>
<img width="281" height="186" alt="image" src="https://github.com/user-attachments/assets/1c2e392a-35bb-4ebd-b8bb-09c001434922" /><br>
- `5_layout_basico.py` — Layouts com Row e Column<br>
<img width="388" height="302" alt="image" src="https://github.com/user-attachments/assets/bb655a37-b30b-4983-93d1-3a56e06bc0ae" /><br>
Nesta aplicação foi encinado como organizar os itens no site como feito em html usando o display flex<br>

- `5a_desafio1.py` — Desafio: Criador de Perfil<br>
<img width="320" height="275" alt="image" src="https://github.com/user-attachments/assets/7a968e05-8150-45f2-8393-006485e57e09" /><br>
Neste site foi desenvolvido um tipo de formulario como um formulario de cadastro/login com flet como mostrado na imagem acime e o login efetuado na imagem abaixo <br>
<img width="323" height="457" alt="image" src="https://github.com/user-attachments/assets/14bc53be-f974-4c18-a054-a31baab54645" /><br>

- `6_contador.py` — Contador completo<br>
<img width="150" height="200" alt="image" src="https://github.com/user-attachments/assets/f0a16f82-6b0a-47b5-9556-06ef810bcc35" /><br>
Nesta aplicação foi feito um tipo de contador como mostrado na imagem acima e caso você aperte um dos botões aumente ou diminua o contado como mostrado nas imagem abaixo<br>
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/f8a6b907-0f09-4851-b4ec-208c4761714e" /> <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/7c0ca4e5-d016-45eb-ad3f-599a119daa43" /><br>



- `7_calculadora.py` — Calculadora simples<br>
<img width="350" height="400" alt="image" src="https://github.com/user-attachments/assets/588daf2a-28ba-4174-a99d-2356e26e1f87" /><br>
Neste site foi feito uma calculadora como na imagem acima e apos colocar os numero e a operação desejáda e apertar o botão a conta é realizada<br>
<img width="350" height="400" alt="image" src="https://github.com/user-attachments/assets/8093b0ec-8767-4547-b098-4edfa3029ba9" /><br>

- `8_painel_conf.py` — Painel de configuração de texto<br>
<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/3408ce38-283d-42f3-9059-b3ff49a70386" /><br>
Nesta aplicação foi feito uma especie de editor de texto na primeira imagem o site ao iniciar e na imagem abaixo o texto editado<br>
<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/da752c83-bfd6-4703-b193-f3503af876f9" /><br>

- `9_galeria_cards.py` — Galeria de animais com filtros<br>
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/2382d6da-e93c-4298-a0c7-3bacec88835a" /><br>
Neste site foi feito um tipo de catalogo de dinossauros com mecanismo de busca na imagem acima o site ao iniciar e na abaixo a pesquisa por nome<br>
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/898a2b6c-0c25-4fb2-979e-94f8278c6589" /><br>

- `10_app_multipagina.py` — App multipágina com navegação<br>
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/4652d98b-7657-4eb6-9845-b157ef190bb5" /><br>
Nesta aplicação mostra uma página de aplicativo mobile com opções como perfil, sobre e etc, na imagem acima o aplicativo ao iniciar e abaixo uma das abas que se pode entrar<br>
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/6458e09e-9af5-44ef-9245-9bc3a2218938" /><br>

- `10a_desafio2.py` — Desafio: Loja virtual mini<br>
Nesta site é uma loja virtual em que você pode adicionar produtos ao carrinho e mostra abaixo no carrinho seus produtos e o preço da compra<br>
<img width="350" height="250" alt="image" src="https://github.com/user-attachments/assets/67050a0a-2020-49da-b887-4e86393c52df" /><br>
<img width="350" height="250" alt="image" src="https://github.com/user-attachments/assets/a5edd75e-d603-40c2-a31d-d69f214e9228" /><br>



