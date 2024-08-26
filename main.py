def replace_letter(file_path, original_letter, new_letter):
    text = ""
    # file = open(file_path, 'r')
    # file.close()
    with open(file_path, 'r') as file:
        text = file.read()
        text = text.replace(original_letter, new_letter)
    
    with open(file_path, 'w') as file:
        file.write(text)

replace_letter("c:/Users/Probook/Desktop/Python/1-day/nom.txt", "b", "e")