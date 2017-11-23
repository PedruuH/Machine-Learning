import pyscreenshot as ImageGrab

if __name__ == "__main__":
    imagem = ImageGrab.grab()
    imagem.save('screenShot2.jpg', 'jpeg')

