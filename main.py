import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))

def dua_game():
    pass


def main_game():
    menu.clear()
    menu.add_selector('Đường đua: ',[('số 1',1),('số 2',2),('số 3',3)],onchange=duong_dua)
    menu.add_selector('Xe:', [(' số 1', 1), (' số 2', 2),(' số 3',3),(' số 4',4),(' số 5',5)], onchange=so_xe)
    menu.add_button('OK',dua_game)
    menu.add_button('Quay lại',start_the_game)



def duong_dua(value,Đườngđua):
    pass
    

def nap_game():
    pass

def so_xe(value,Xe):
    pass

def load_game():
    pass

def start_the_game():
    menu.clear()
    menu.add_text_input('Tên người chơi :', default=' ')
    menu.add_button('Bắt đầu', main_game)
    menu.add_button('Quay lại', main_menu)


def help_game():
    menu.clear()
    menu.add_button('Quay lại', main_menu)


def main_menu():
    menu.clear()
    menu.add_button('Chơi mới', start_the_game)
    menu.add_button('Chơi tiếp', load_game)
    menu.add_button('Giúp đỡ', help_game)
    menu.add_button('Thoát', pygame_menu.events.EXIT)


menu = pygame_menu.Menu(600, 800, 'Chào mừng đến với ??? ',
                       theme=pygame_menu.themes.THEME_ORANGE)
main_menu()


menu.mainloop(surface)
