import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

movie = pygame.movie.Movie("your_video.mp4")
movie.set_display(screen, rect=screen.get_rect())
movie.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
