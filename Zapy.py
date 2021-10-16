### Zapy

import pywhatkit as WhatsApp

### Horário de entrega
TriggerH = 04
TriggerM = 20

### Lista de contatos
Contacts = ["+5511912345678", "+5611912345678", "+5711912345678", "+5811912345678", "+5911912345678", "+6011912345678"]

### Enviar mensagens para multiplos contatos
for PhoneNumber in Contacts:
    Message = "Aqui uma mensagem customizada que será enviada para cada contato na matriz Contacts"
    WhatsApp.sendwhatmsg(PhoneNumber, Message, TriggerH, TriggerM)

### Desmarque o comentário nas linhas abaixo para enviar mensagem a somente um contato
# PhoneNumber = ""
# Message = "Aqui uma mensagem customizada que será enviada para cada contato guardado na variável PhoneNumber"
# WhatsApp.sendwhatmsg(PhoneNumber, Message, TriggerH, TriggerM)
