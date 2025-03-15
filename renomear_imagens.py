import os

# Diretório onde estão as imagens
caminho_das_imagens = "/home/alexandro/spatial-db2b/cap6"

# Verifica se o diretório existe
if not os.path.exists(caminho_das_imagens):
    print(f"❌ Erro: O diretório {caminho_das_imagens} não foi encontrado.")
    exit(1)

# Listar os arquivos no diretório
arquivos = os.listdir(caminho_das_imagens)

# Percorrer os arquivos e renomear aqueles que começam com "6_"
for arquivo in arquivos:
    if arquivo.startswith("6_"):
        novo_nome = "fig" + arquivo  # Adiciona "fig" antes do nome atual
        caminho_antigo = os.path.join(caminho_das_imagens, arquivo)
        caminho_novo = os.path.join(caminho_das_imagens, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"✅ Renomeado: {arquivo} → {novo_nome}")

print("🎉 Todos os arquivos foram renomeados com sucesso!")
