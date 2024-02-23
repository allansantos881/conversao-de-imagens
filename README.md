# Instruções de Uso:


#1 Instale as dependências necessárias executando o seguinte comando:
!pip install Pillow

#2 Modifique as variáveis pasta_jpeg e pasta_png no script para os caminhos reais das suas pastas de origem (JPEG) e destino (PNG).

#3 Execute o script utilizando o seguinte comando no terminal:
python converter_jpeg_para_png.py

Observações:

Certifique-se de que todas as imagens na pasta JPEG são válidas e podem ser abertas pelo Pillow.
O script cria automaticamente a pasta de destino se ela não existir.
Requisitos:

Python 3.x
Pillow (instalado via pip)

# Conversor JPEG para PNG

Este script em Python utiliza a biblioteca Pillow para converter imagens JPEG para o formato PNG. A conversão é útil para cenários que exigem transparência ou compressão sem perda de qualidade.

## Instruções de Uso

Após a instalação, basta colocar o diretório de sua pasta aonde contém as fotos e o diretório aonde vai sair as imgens convertidas:

# Pasta contendo os arquivos JPEG
pasta_jpeg = r'<pasta com as fotos>'

# Pasta de saída para os arquivos PNG
pasta_png = r'<pasta destino>'

Basta executar o programa e pronto! Simples assim.

