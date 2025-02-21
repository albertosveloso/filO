import os
import shutil

folder = r"C://Users\Alber\Desktop"

files_moved = 0
errors = 0

for file in os.listdir(folder):
    try:
        filename, file_extension = os.path.splitext(file)
        
        # Ignora pastas para evitar recursão infinita
        if not file_extension:
            continue
        
        file_extension = file_extension[1:]  # Remove o ponto do formato .jpg, .png, etc.
        folder_to_organize_file = os.path.join(folder, file_extension)

        # Cria a pasta se não existir
        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

        # Move o arquivo
        shutil.move(os.path.join(folder, file), os.path.join(folder_to_organize_file, file))
        files_moved += 1
        print(f"✅ '{file}' movido para '{file_extension}'")

    except Exception as e:
        errors += 1
        print(f"❌ Erro ao mover '{file}': {e}")

# Feedback final
print("\n--- Relatório de Organização ---")
print(f"Arquivos movidos com sucesso: {files_moved}")
print(f"Arquivos com erro: {errors}")

if errors == 0:
    print("🎉 Organização concluída com sucesso!")
else:
    print("⚠️ Organização concluída, mas com alguns erros.")