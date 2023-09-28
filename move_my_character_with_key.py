from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Move.png')

def handle_events():
    global running, dir, dir2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 1
            elif event.key == SDLK_LEFT:
                dir = -1
            elif event.key == SDLK_UP:
                dir2 = 1
            elif event.key == SDLK_DOWN:
                dir2 = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = 0
            elif event.key == SDLK_LEFT:
                dir = 0
            elif event.key == SDLK_UP:
                dir2 = 0
            elif event.key == SDLK_DOWN:
                dir2 = 0


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
dir2 = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir == 0 and dir2 == 0:
        character.clip_draw(0, 192, 64, 64, x, y)
    elif dir == 1:
        character.clip_draw(frame * 64, 64, 64, 64, x, y)
    elif dir == -1:
        character.clip_draw(frame * 64, 128, 64, 64, x, y)
    elif dir2 == 1:
        character.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif dir2 == -1:
        character.clip_draw(frame * 64, 192, 64, 64, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH

    x += dir * 5

    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT

    y += dir2 * 5
    delay(0.05)

close_canvas()

