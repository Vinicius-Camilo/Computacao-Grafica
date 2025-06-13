# Projeto Contador de Objetos

Este projeto implementa um algoritmo aprimorado de detecção e contagem de objetos usando Python e OpenCV. O foco principal é identificar e contar objetos em imagens com precisão, reduzindo falsos positivos. O projeto utiliza técnicas avançadas de segmentação, incluindo o algoritmo watershed, para aprimorar o processo de detecção.

## Melhorias Realizadas

1. **Técnicas Avançadas de Segmentação**: Implementação do algoritmo watershed para separar melhor objetos sobrepostos, melhorando a precisão da detecção.
2. **Pré-processamento Aprimorado**: Ajuste de parâmetros para binarização e operações morfológicas para criar uma máscara mais limpa, reduzindo ruídos e melhorando a detecção de objetos.
3. **Filtragem de Contornos**: Adição de filtros para ignorar pequenos contornos que provavelmente são ruídos, garantindo que apenas objetos significativos sejam contados.
4. **Saída Visual**: A imagem final de saída exibe os contornos detectados e a contagem total de objetos diretamente na imagem, proporcionando feedback visual imediato.
5. **Salvamento da Imagem**: A imagem processada com contornos e contagem é salva em disco para análise ou relatório posterior.

## Estrutura do Projeto

```
object-counter
├── src
│   ├── main.py        # Script principal para detecção e contagem de objetos
│   └── utils.py       # Funções utilitárias para processamento de imagens
├── images
│   ├── chocolates.jpg  # Imagem de entrada para detecção
│   ├── seeds.png       # Segunda imagem de entrada para testes
│   └── mask.png        # Máscara gerada durante o processamento
├── requirements.txt    # Lista de dependências
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivos a serem ignorados pelo Git
```

## Requisitos

Para executar este projeto, é necessário ter Python 3.x instalado juntamente com as bibliotecas requeridas. Você pode instalar as dependências usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando o Código

Para executar o algoritmo de detecção e contagem de objetos, rode o script principal:

```bash
python src/main.py
```

Isso irá processar as imagens localizadas no diretório `images` e exibir os resultados. A imagem de saída com os contornos detectados e a contagem será salva no diretório `images` como `mask.png`.

## Informações Adicionais

Sinta-se à vontade para explorar o arquivo `src/utils.py` para funções utilitárias que dão suporte ao algoritmo principal. O projeto pode ser estendido com recursos adicionais, como suporte a diferentes formatos de imagem ou integração com uma interface de usuário.

## Licença

Este projeto é open-source e está disponível para modificação e distribuição sob a Licença MIT.