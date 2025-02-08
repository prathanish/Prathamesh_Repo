import pygame   
from sys import exit
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 =  pygame.image.load('astronaut_walk_1.png').convert_alpha()
        player_walk_2 =  pygame.image.load('astronaut_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('astronaut_jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('pygame_study\jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity =- 20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0 
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
    

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
    
        if type =='fly':
            fly_1 = pygame.image.load('pygame_study\Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('pygame_study\Fly2.png').convert_alpha()
            self.frames = [ fly_1,fly_2]
            y_pos = 210
            self.animation_speed = 0.2
        else: 
            snail_1 = pygame.image.load('pygame_study\snail1.png').convert_alpha()
            snail_2 = pygame.image.load('pygame_study\snail2.png').convert_alpha()
            self.frames = [snail_1,snail_2]
            y_pos = 300
            self.animation_speed = 0.05
        self.animation_index = 0 
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100),y_pos))

    def animation_state(self):
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.frames): self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    
    

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = score_font.render(f'Score: {current_time}',False,('White'))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
                

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -110]

        return obstacle_list
    else: 
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): 
                collision_sound.play()
                return False
    return True

pygame.mixer.init()
collision_sound = pygame.mixer.Sound('pygame_study\collision_sound.mp3')
collision_sound.set_volume(2)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        collision_sound.play()
        obstacle_group.empty()
        return False
    else: return True

pygame.init() #opposite of pygame.quit and initializes pygame
screen = pygame.display.set_mode((800,400)) #screen made also specified size in pixels
pygame.display.set_caption('Pygame runner') #game name
clock = pygame.time.Clock() #frame rate setter
#surface positions like (x,y) in graph except y is inverted and origin(0,0) point point is top left
score_font = pygame.font.Font('pygame_study\Pixeltype.ttf', 50) #specify font type and size while making font and only ttf(true type font) files work

game_active = False
start_time = 0
score = 0 

bg_music = pygame.mixer.Sound('pygame_study\music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()



background_surface = pygame.image.load('pygame_study\space_backgorund.png').convert() #single quotes needed to convert and load image properly

scaled_version = pygame.transform.scale(background_surface,(800,500))
ground_surface = pygame.image.load('pygame_study\ground.png').convert()

# score_surf = score_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

#Obstacles

#Snail
snail_frame1 = pygame.image.load('pygame_study\snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('pygame_study\snail2.png').convert_alpha()
snail_frames = [snail_frame1,snail_frame2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]


#Fly
fly_frame1 = pygame.image.load('pygame_study\Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('pygame_study\Fly2.png').convert_alpha()
fly_frames = [fly_frame1,fly_frame2]
fly_frame_index= 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 =  pygame.image.load('astronaut_walk_1.png').convert_alpha()
player_walk_2 =  pygame.image.load('astronaut_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('astronaut_jump.png').convert_alpha()



player_surf = player_walk[player_index]
player_rect = player_walk_1.get_rect(midbottom = (80,300)) # creating a rectangle to have more control over the player surface
player_gravity = 0

# Default screen
player_stand = pygame.image.load('astronaut_standing.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = score_font.render('Lost in an awkward place',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = score_font.render('Press space to start',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,320))


#Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

# snail_animation_timer = pygame.USEREVENT + 2 
# pygame.time.set_timer(snail_animation_timer,500)

# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer,100)


while True:
    for event in pygame.event.get(): #
        if event.type == pygame.QUIT: #code to close window of game
            pygame.quit()
            exit() #to close the while loop
            
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity =-20    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity =-20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)


        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly','snail','snail','snail'])))
                # if random.randint(0,2):
                #     obstacle_rect_list.append(snail_frame1.get_rect(midbottom = (random.randint(900,1100),300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(midbottom = (random.randint(900,1100),210)))
            
            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0: 
            #         snail_frame_index = 1
            #     else: 
            #         snail_frame_index = 0
            #     snail_surf = snail_frames[snail_frame_index]

            # elif event.type == fly_animation_timer:
            #     if fly_frame_index == 0: 
            #         fly_frame_index = 1
            #     else: 
            #         fly_frame_index = 0
            #     fly_surf = fly_frames[fly_frame_index]

            

    if game_active: # actual game
        screen.blit(scaled_version,(0,0)) #putting surface on screen by specifying coordinates
        screen.blit(ground_surface,(0,300))

        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)    
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # snail_rect.x -= 5
        # if snail_rect.right < -100: snail_rect.left = 800
        # screen.blit(snail_frame1,snail_rect)

        #Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        
        #Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # #Collisions
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player.sprite.rect.midbottom = (80,300)
        player.sprite.gravity = 0
        
        score_message = score_font.render(f'Last score: {score}',False,('White'))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60) #max frame rate

