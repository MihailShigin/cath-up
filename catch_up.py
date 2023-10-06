from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (700, 500))

window.blit(background,(0,0))


#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)
x_s1, y_s1 = 100, 100
sprite2 = transform.scale(
    image.load('sprite2.png'),
    (101, 101)
)
x_s2, y_s2 = 200, 200

clock = time.Clock()
FPS = 60


#обработай событие «клик по кнопке "Закрыть окно"»
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False 

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y_s1 > 5:
        y_s1 -= 10
    if keys_pressed[K_DOWN] and y_s1 < 400:
        y_s1 += 10
    if keys_pressed[K_LEFT] and x_s1 > 5:
        x_s1 -= 10
    if keys_pressed[K_RIGHT] and y_s1 < 595:
        x_s1 += 10
    if keys_pressed[K_s] and y_s2 < 400:
        y_s2 += 10
    if keys_pressed[K_w] and y_s2 > 5:
        y_s2 -= 10
    if keys_pressed[K_a] and x_s2 > 5:
        x_s2 -= 10
    if keys_pressed[K_d] and x_s2 < 595:
        x_s2 += 10

    window.blit(background, (0,0))
    window.blit(sprite1, (x_s1, y_s1))
    window.blit(sprite2, (x_s2, y_s2))

    clock.tick(FPS)
    display.update()