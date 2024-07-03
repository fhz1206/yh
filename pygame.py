import pygame, sys
import random, time
#用户严禁修改（1～行）
#函数作用：初始化
def pygame_screen_init(width, height, classname, icon, text_size):
    pygame.init()
    font = pygame.font.Font('fonts/font.ttf', text_size)
    screen = pygame.display.set_mode((width, height))
    if classname == '':
        pygame.display.set_caption('pygame')
    else:
        pygame.display.set_caption(str(classname))
    if icon == '':
        pygame.display.set_icon(pygame.image.load('pygame_logo'))
    else:
        pygame.display.set_icon(icon)
        
    clock = pygame.time.Clock()
    clock.tick(24)
            
#函数作用：重新绘制
def pygame_screen_for_draw():
    pygame.display.flip()
    pygame.display.update()
    
def pygame_key_a():
    return event.key == pygame.K_a
    
def pygame_key_b():
    return event.key == pygame.K_b
        
def pygame_key_c():
    return event.key == pygame.K_c
    
def pygame_key_d():
    return event.key == pygame.K_d

def pygame_key_e():
    return event.key == pygame.K_e
    
def pygame_key_f():
    return event.key == pygame.K_f

def pygame_key_g():
    return event.key == pygame.K_g

def pygame_key_h():
    return event.key == pygame.K_h
    
def pygame_key_i():
    return event.key == pygame.K_i

def pygame_key_j():
    return event.key == pygame.K_j

def pygame_key_k():
    return event.key == pygame.K_k

def pygame_key_l():
    return event.key == pygame.K_l

def pygame_key_m():
    return event.key == pygame.K_m

def pygame_key_n():
    return event.key == pygame.K_n

def pygame_key_o():
    return event.key == pygame.K_o

def pygame_key_p():
    return event.key == pygame.K_p
    
def pygame_key_q():
    return event.key == pygame.K_q

def pygame_key_r():
    return event.key == pygame.K_r

def pygame_key_s():
    return event.key == pygame.K_s

def pygame_key_t():
    return event.key == pygame.K_t

def pygame_key_u():
    return event.key == pygame.K_u

def pygame_key_v():
    return event.key == pygame.K_v

def pygame_key_w():
    return event.key == pygame.K_w

def pygame_key_x():
    return event.key == pygame.K_x

def pygame_key_y():
    return event.key == pygame.K_y

def pygame_key_z():
    return event.key == pygame.K_z

def pygame_key_up():
    return event.key == pygame.K_UP

def pygame_key_down():
    return event.key == pygame.K_DOWN

def pygame_key_left():
    return event.key == pygame.K_LEFT
    
def pygame_key_right():
    return event.key == pygame.K_RIGHT

def pygame_img_upload(imgname, sizewidth, sizeheight):
    img_upload = pygame.image.load(imgname)convert_alpha()
    img_upload = pygame.transform.scale(img_upload, sizewidth, sizeheight)
        
def pygame_screen_img(img, x, y):
    img_draw = img
    screen.blit(img_draw, (x, y))

def pygame_screen_font(string, x, y, rgb):
    render = pygame.render(string, True, rgb)
    screen.blit(render, (x, y))

def pygame_screen_collidemouse(name1):
    return name1.rect.collidepoint(pygame.mouse.get_pos())
    
def pygame_screen_collide(name1, name2):
    return name1.rect.colliderect(name2.rect)

state = 1 # 状态（用户可修改）
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.'QUIT':
            running = False
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEDOWN: # 
            pass
            
pygame.quit()
sys.exit()