🔒 Gerador de Senhas Premium (Python + Flask)

Um gerador de senhas web altamente seguro e responsivo, desenvolvido com Python e Flask. A interface utiliza um design moderno com efeito Glassmorphism (Dark Mode), inspirado em padrões de UI premium.

Diferente de geradores comuns que utilizam geração pseudoaleatória, este projeto utiliza a biblioteca secrets nativa do Python, garantindo segurança de nível criptográfico na criação de cada senha.

🚀 Funcionalidades

Geração Segura: Utiliza o módulo secrets do Python para entropia criptográfica.

Customização Total: Escolha entre 8 e 32 caracteres via slider dinâmico.

Filtros Precisos: Switches para incluir/excluir Maiúsculas, Minúsculas, Números e Símbolos.

UI/UX Premium: Design responsivo, botões interativos e feedback visual (Toast Notification) ao copiar a senha.

Privacidade: Geração feita 100% no servidor local/backend, sem retenção de dados ou rastreamento.

🛠️ Tecnologias Utilizadas

Backend: Python 3.12, Flask

Frontend: HTML5, CSS3 (Variáveis, Flexbox, Media Queries), JavaScript (para o botão de copiar)

Ícones: FontAwesome

📂 Estrutura do Projeto

/gerador-de-senhas
 ┣ 📂 static/
 ┃ ┗ 📜 style.css       # Estilização completa e Dark Mode
 ┣ 📂 templates/
 ┃ ┗ 📜 index.html      # Estrutura da interface
 ┗ 📜 app.py            # Lógica de rotas e segurança em Python


⚙️ Como executar localmente

Certifique-se de ter o Python instalado na sua máquina.

Clone este repositório:

git clone https://github.com/SEU-USUARIO/gerador-de-senhas.git


Acesse a pasta do projeto:

cd gerador-de-senhas


Instale o Flask:

pip install flask


Execute o servidor:

python app.py


Abra o navegador e acesse: http://127.0.0.1:5000
