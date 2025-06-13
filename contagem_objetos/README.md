# Projeto Contador de Objetos

Este projeto implementa um algoritmo de detecção e contagem de objetos usando Python e OpenCV. O objetivo é identificar e contar objetos em imagens com precisão, utilizando técnicas de segmentação, operações morfológicas e o algoritmo watershed.

## Funcionalidades

- **Segmentação Avançada:** Utiliza o algoritmo watershed para separar objetos sobrepostos.
- **Pré-processamento:** Conversão para tons de cinza, binarização (Otsu invertida) e operações morfológicas para remoção de ruídos.
- **Contagem de Objetos:** Conta objetos significativos na imagem, ignorando pequenos ruídos.
- **Saída Visual:** Exibe e salva a imagem final com os contornos dos objetos detectados e a contagem total sobreposta.
- **Salvamento de Resultado:** A imagem processada é salva no diretório `images` como `mask.png`.

## Estrutura do Projeto

```
contagem_objetos
├── src
│   ├── main.py        # Script principal para detecção e contagem de objetos
│   └── utils.py       # Funções utilitárias para processamento de imagens
├── images
│   ├── chocolates.jpg  # Imagem de entrada para detecção
│   ├── seeds.png       # Outra imagem de entrada para testes
│   ├── mask.png        # Imagem de saída gerada pelo processamento
│   ├── moedas.jpg      # Outras imagens de exemplo
│   ├── moedas.png
│   ├── gems.jpg
├── requirements.txt    # Lista de dependências
├── dependencias.txt    # Instruções para instalação das dependências
├── README.md           # Documentação do projeto
```

## Requisitos

- Python 3.12
- As bibliotecas listadas em `requirements.txt`

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Executando o Código

Para rodar o algoritmo de detecção e contagem de objetos, execute o script principal:

```bash
python src/main.py
```

O script irá processar a imagem `images/chocolates.jpg` (ou outra imagem definida no código), exibir os resultados em janelas e salvar a imagem final com os contornos e a contagem em `images/mask.png`.

## Observações

- Para testar com outras imagens, substitua o caminho da imagem em `src/main.py`.
- O resultado será exibido em janelas do OpenCV e salvo automaticamente.
- O código pode ser adaptado para diferentes tipos de imagens ajustando os parâmetros de segmentação e morfologia.