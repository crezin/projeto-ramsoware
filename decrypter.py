import os 
import pyaes 


## abrir o arquivo criptografado
file_name = "teste.txt.ransowaretroll"
file = open(file_name, "rb") 
file_data = file.read()
file.close()


##chave da criptografia 

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

##remover o arquivos criptografados
os.remove(file_name)

## criar um novo arquivo criptografado 

new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()


