# Gerador de QRCode

Este é um aplicativo simples para gerar e salvar códigos QR a partir de links. O aplicativo foi criado utilizando Python e as bibliotecas `tkinter`, `qrcode`, `PIL`, `ttkbootstrap` e `io`.

## Funcionalidades

- **Geração de QRCode**: O aplicativo gera códigos QR a partir de um link fornecido.
- **Validação de Link**: Verifica se o link fornecido começa com "https://".
- **Exibição do QRCode**: Mostra o QRCode gerado dentro da interface gráfica do aplicativo.
- **Salvar QRCode**: Permite salvar o QRCode gerado como um arquivo PNG.
- **Interface Estilizada**: Utiliza a biblioteca `ttkbootstrap` para uma interface gráfica mais elegante.
- **Centralização da Janela**: A janela do aplicativo é centralizada na tela do usuário.

## Bibliotecas Necessárias

- `tkinter`
- `qrcode`
- `PIL`
- `ttkbootstrap`
- `io`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/jgafarias/Gen-QRCode.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Gen-QRCode
    ```

3. Instale as bibliotecas necessárias:
    ```bash
    pip install tkinter qrcode pillow ttkbootstrap
    ```

## Uso

1. Execute o aplicativo:
    ```bash
    python gerador_qrcode.py
    ```

2. Insira o link que deseja converter em QRCode no campo de entrada.

3. Clique em "Gerar" para criar o QRCode.

4. Para salvar o QRCode como um arquivo PNG, clique em "Salvar".

## Requisitos
- Python 3.x

## Contato

Para mais informações, entre em contato com o autor:

- **Nome:** João Gabriel
- **GitHub:** [jgafarias](https://github.com/jgafarias)
