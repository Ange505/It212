import os

# Étape 1 : Création du fichier de base avec 1000 lignes
def create_base_file(filename):
    with open(filename, "w") as file:
        for i in range(1, 1001):  # Créer 1000 lignes
            if i % 2 == 1:  # Ligne impaire
                file.write("A" * 30 + "\n")  # Écrire 30 caractères
            else:  # Ligne paire
                file.write("Ligne paire de contenu\n")

# Étape 2 : Création d'un fichier enfant pour chaque ligne impaire
def create_child_files_for_odd_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    # Extraire et créer un fichier pour chaque ligne impaire
    for index, line in enumerate(lines, start=1):
        if index % 2 == 1:  # Ligne impaire
            child_filename = f"{filename}_odd_line_{index}.txt"
            with open(child_filename, "w") as child_file:
                child_file.write(line)
            print(f"Fichier enfant créé : {child_filename}")

# Paramètres du script
base_filename = "test.txt"  # Nom du fichier de base

# Exécution
create_base_file(base_filename)
create_child_files_for_odd_lines(base_filename)
