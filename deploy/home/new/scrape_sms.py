#!/usr/bin/python2.7
import cmgpy
at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

sms_file = open('sms_history.txt', 'a') # append all SMS to file

result = icon322.AT(at.cmgl(stat="ALL"))
messages = result.messageList
for message in messages:
    # {'date': '13/02/23,13:05:54-24', 'cmgl': '1', 'stat': 'REC READ', 'message': 'Str: blather!', 'da': '+19082165058'}
    formatted_message_string = message['date'] + ";" + 
                               message['da'] + ";\"" +
                               message['message'] + "\""
    formatted_message_string = formatted_message_string.replace('\n','^n')
    formatted_message_string = formatted_message_string.replace('\r','^r')
    sms_file.write(formatted_message_string+'\n')


# could be moved before loop
icon322.AT(at.cmgd(index=0, flag=4)) # delete ALL SMS with flag=4

