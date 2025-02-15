# Abre el archivo de la plantilla de la carta en modo lectura
starting = open("C:/Users/jorge_fqp8p4m/PycharmProjects/Mail_Merge_Project/Input/Letters/starting_letter.txt", "r")
# Abre el archivo que contiene los nombres de los destinatarios en modo lectura
n = open("C:/Users/jorge_fqp8p4m/PycharmProjects/Mail_Merge_Project/Input/Names/invited_names.txt", "r")

# Lee todas las líneas del archivo de nombres y las almacena en una lista
names = n.readlines()
# Lee el contenido completo de la plantilla de la carta
original_text = starting.read()

# Itera sobre cada nombre en la lista de nombres
for name in names:
    # Elimina los espacios y saltos de línea del nombre (por ejemplo, "\n")
    clean_name = name.strip()
    # Reemplaza el marcador "[]" en la plantilla con el nombre actual
    new_name = original_text.replace("[]", f"{clean_name}")
    # Crea un nuevo archivo para cada nombre, con un nombre único basado en el nombre del destinatario
    with open(f"C:/Users/jorge_fqp8p4m/PycharmProjects/Mail_Merge_Project/Output/ReadyToSend/letter_for_{clean_name}.docx", "w") as new_letter:
        # Escribe el contenido modificado en el nuevo archivo
        new_letter.write(new_name)

starting.close()
n.close()











#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp