# Tocando uma música com pygame
import pygame
import time

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("PythonExercicios/ex021.mp3")

# Inicia a reprodução do arquivo MP3
pygame.mixer.music.play()

# Mantém o script em execução enquanto a música está tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)
