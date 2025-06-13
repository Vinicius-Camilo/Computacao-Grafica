# Steganography Web App

Este projeto é uma aplicação web que permite aos usuários ocultar e extrair mensagens secretas em imagens digitais utilizando a técnica de esteganografia de Menor Bit Significativo (LSB). A aplicação é construída com um backend Flask e um frontend simples em HTML/CSS/JavaScript.

## Funcionalidades

- **Inserir Mensagem em Imagem**: Usuários podem fazer upload de uma imagem PNG e embutir uma mensagem secreta nela.
- **Ler Mensagem de Imagem**: Usuários podem fazer upload de uma imagem que pode conter uma mensagem oculta e extraí-la.

## Estrutura do Projeto

```
steganography-web-app
├── backend
│   ├── app.py                # Ponto de entrada principal para a aplicação Flask
│   ├── steganography.py      # Lógica para técnicas de esteganografia LSB
│   └── requirements.txt      # Dependências do backend
├── frontend
│   ├── index.html            # Documento HTML principal da aplicação web
│   ├── styles.css            # Estilos para a aplicação web
│   └── script.js             # JavaScript para lidar com interações do usuário
├── README.md                 # Documentação do projeto
└── .gitignore                # Arquivos e diretórios ignorados pelo Git
```

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python com Flask

## Instruções de Configuração

1. **Clone o repositório**:
   ```
   git clone <repository-url>
   cd steganography-web-app
   ```

2. **Configure o backend**:
   - Navegue até o diretório `backend`.
   - Instale as dependências necessárias:
     ```
     pip install -r requirements.txt
     ```

3. **Execute a aplicação Flask**:
   ```
   python app.py
   ```

4. **Acesse a aplicação**:
   - Abra seu navegador e vá para `http://127.0.0.1:5000`.

## Uso

### Para Inserir uma Mensagem em uma Imagem

1. Vá até a seção "Inserir mensagem em imagem".
2. Faça upload de uma imagem PNG.
3. Digite sua mensagem secreta no campo de texto.
4. Clique no botão para codificar a mensagem e gerar a nova imagem.
5. Baixe a imagem com a mensagem embutida.

### Para Ler uma Mensagem de uma Imagem

1. Vá até a seção "Ler mensagem de imagem".
2. Faça upload de uma imagem que possa conter uma mensagem oculta.
3. Clique no botão para extrair e exibir a mensagem oculta.
