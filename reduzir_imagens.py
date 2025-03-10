import os
from PIL import Image

# Diretório onde estão as imagens
pasta_origem = "/home/alexandro/spatial-db2/images"
pasta_saida = "/home/alexandro/spatial-db2/images2"

# Criar a pasta de saída, se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Qualidade da compressão (1-100, sendo 100 a melhor qualidade)
qualidade = 75  

# Percorre todas as imagens na pasta
for arquivo in os.listdir(pasta_origem):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        caminho_imagem = os.path.join(pasta_origem, arquivo)
        caminho_saida = os.path.join(pasta_saida, arquivo)

        try:
            with Image.open(caminho_imagem) as img:
                img = img.convert("RGB")  # Para evitar problemas com transparência
                img.save(caminho_saida, "JPEG", quality=qualidade, optimize=True)
                print(f"Imagem comprimida: {arquivo}")
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

print("Processo concluído!")
