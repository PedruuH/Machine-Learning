import pyscreenshot as ImageGrab

if __name__ == "__main__":
    imagem = ImageGrab.grab()
    imagem.show()
    imagem.save('screenShot2.jpg', 'jpeg')

