with open("Input/Letters/starting_letter.txt", "r") as file:
    template = file.read()
with open("Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
for name in names:
    mail = template.replace("[name]", name.strip())
    with open(f"Output/ReadyToSend/Letter_for_{name.strip()}", "w") as output:
        output.write(mail)