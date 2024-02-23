from PIL import Image
import os

# Pasta contendo os arquivos JPEG
pasta_jpeg = r'<pasta com as fotos>'

# Pasta de saída para os arquivos PNG
pasta_png = r'<pasta destino>'

# Certifique-se de que a pasta de saída exista, se não, crie-a
if not os.path.exists(pasta_png):
    os.makedirs(pasta_png)

# Lista todos os arquivos na pasta JPEG
arquivos_jpeg = os.listdir(pasta_jpeg)

# Itera sobre cada arquivo JPEG na pasta
for arquivo_jpeg in arquivos_jpeg:
    # Constrói o caminho completo para o arquivo JPEG
    caminho_jpeg = os.path.join(pasta_jpeg, arquivo_jpeg)

    # Abre a imagem JPEG usando o Pillow
    imagem = Image.open(caminho_jpeg)

    # Constrói o caminho completo para o arquivo PNG de saída
    caminho_png = os.path.join(pasta_png, os.path.splitext(arquivo_jpeg)[0] + '.png')

    # Salva a imagem no formato PNG
    imagem.save(caminho_png, 'PNG')

print('Conversão concluída.')