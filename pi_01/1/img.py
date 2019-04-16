
def getImage(response, path):
    formato = response.url[-3:]
    if formato == "jpg" or formato == "gif" or formato == "png":
        file_to_open = path + "imagem"
        open("imagem.jpg", 'wb').write(response.content)
        return True
        
    return False