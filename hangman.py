import pygame,random
pygame.init()
w,h=800,600
WINDOW=pygame.display.set_mode((w,h))
pygame.display.set_caption("HANGMAN")
hang_0=pygame.image.load("hangman #0.png")
hang_1=pygame.image.load("hangman #1.png")
hang_2=pygame.image.load("hangman #2.png")
hang_3=pygame.image.load("hangman #3.png")
hang_4=pygame.image.load("hangman #4.png")
hang_5=pygame.image.load("hangman #5.png")
hang_last=pygame.image.load("hangman #6.png")
blank=pygame.image.load("blank.png")

#Random Words

sentences=["fat","nikal"]#it shoudl be less than 8
choosed=random.choice(sentences).lower()
lenght_of_words=len(choosed)
########Fade############
def fade(width, height):

    fade = pygame.Surface((width, height))
    fade.fill((255,255,255))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        WINDOW.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawWindow():
    WINDOW.fill((0,0,0))


t_font=pygame.font.SysFont("Arial",100)
t_2_font=pygame.font.SysFont("Arial",50)
def text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    WINDOW.blit(img,(x,y))




def main():
    width_for_incorrect_words=320
    correct_words=set()
    incorrect_words=set()
    c_worsd=[]



    WINDOW.blit(hang_0,(0,0))
    width=10
    blank_resized=pygame.transform.scale(blank,(90,90))


    for i in range(lenght_of_words):
        WINDOW.blit(blank_resized,(width,490))
        width+=100


    run=True
    clock=pygame.time.Clock()
    hang_numbers = 1
    while run:



        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.KEYDOWN:  # i got that from stackoverflow
                key_pressed = pygame.key.name(event.key)




        #TYPE_-______________________________________FROM TOMORROW
                if key_pressed in choosed:
                    correct_words.add(key_pressed)
                    s=choosed.find(key_pressed)
                    if len(choosed) ==3:

                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                    if len(choosed) == 4:
                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                        if s == 3:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 310, 480)
                    if len(choosed) == 5:
                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                        if s == 3:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 310, 480)
                        if s == 4:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 410, 480)
                    if len(choosed) == 6:
                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                        if s == 3:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 310, 480)
                        if s == 4:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 410, 480)
                        if s == 5:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 510, 480)
                    if len(choosed) == 7:
                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                        if s == 3:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 310, 480)
                        if s == 4:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 410, 480)
                        if s == 5:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 510, 480)
                        if s == 6:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 610, 480)
                    if len(choosed) == 8:
                        if s ==0:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 10, 480)
                        if s ==1:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 110, 480)
                        if s ==2:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 210, 480)
                        if s == 3:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 310, 480)
                        if s == 4:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 410, 480)
                        if s == 5:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 510, 480)
                        if s == 6:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 610, 480)
                        if s == 7:
                            text(f"{key_pressed}", t_font, (0, 0, 0), 710, 480)




                else:

                    if hang_numbers <=6:

                        damn=f"hangman #{int(hang_numbers)}.png"
                        WINDOW.blit(pygame.image.load(damn),(0,0))
                        incorrect_words.add(f"{key_pressed}")
                        hang_numbers+=1
                        text("incorrect Guesses :<",t_2_font,(0,0,0),300,200)
                        for i, letter in enumerate(incorrect_words):
                            text(letter, t_2_font, (255, 0, 0), 300 + i * 30, 300)

                        # for i in incorrect_words:
                        #     text(f"{i} ",t_2_font,(255, 0, 0),width_for_incorrect_words,200)
                        #     width_for_incorrect_words+=10



                    else:
                        WINDOW.fill((255, 0, 0))
                        text("YOU LOOSE!", t_font, (0, 0, 0), 150, 200)

                if len(set(correct_words)) == len(set(choosed)):
                    WINDOW.fill((0,255,0))
                    text("YOU WIN!", t_font, (0, 0, 0),150, 200)
                else:
                    pass



        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    fade(800,600)
    main()