import pygame ,random,time
WHITE=(255,255,255)
pad_width=960
pad_height=960
player_width = 60
player_height = 60
TEXTCOLOR=(255,255,255)

#함수 선언구간

def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))

def player_(x,y):
    global gamepad, player
    gamepad.blit(player,(x,y))

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x, y))

def textObj(text,font):
    textSurface=font.render(text,True,(0,0,0))
    return textSurface,textSurface.get_rect()

def dispMessage(text):
    global gamepad

    largeText=pygame.font.Font('malgun.ttf',115)
    TextSurf, TextRect=textObj(text,largeText)
    TextRect.center=((pad_width/2),(pad_height/2))
    gamepad.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    runGame(jk)

def bulco(text):
    global gamepad
    norText = pygame.font.Font('malgun.ttf', 35)
    TextSurf, TextRect = textObj(text, norText)
    TextRect.center = ((pad_width / 40), (pad_height / 10))
    gamepad.blit(TextSurf, TextRect)


def numc1():
    global gamepad
    am= random.randrange(-15, 15)
    bm = random.randrange(-15, 15)
    while (am==0 and bm==0 or (abs(am)+abs(bm)<=15)):
        am = random.randrange(-15, 15)
        bm = random.randrange(-15, 15)
    return am,bm


def intro1():
    global gamepad, a, b, c, clock
    cre=False
    while not cre:
        a=3
        b=2
        c=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cre = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return c

                if event.key == pygame.K_2:
                    return b

                if event.key == pygame.K_3:
                    return a
        drawObject(intro, 0, 0)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

#본진함수

def runGame(j):
    global gamepad, clock, player, background, ema, emb, emc, emd
    global bullet,bullet2,embulx1,embuly1,embulx2,embuly2,score1
    global score2, score3, score4, pyshot,emeblo1_xy,emeblo2_xy
    global emeblo3_xy, emeblo4_xy,dam, shot_sound

#리스트,변수 선언구간
    bullet_xy = []
    back_xy=[]
    right_xy=[]
    left_xy=[]
    emeblo1_xy=[]
    emeblo2_xy=[]
    emeblo3_xy=[]
    emeblo4_xy=[]
    crashed = False
    isshot1=False
    isshot2 = False
    isshot3 = False
    isshot4 = False
    score1=0
    score2=0
    score3 = 0
    score4 = 0
    dorl1=True
    dorl2=True
    dorl3=True
    dorl4=True
    pyshot=False
    dam=0
    sit=True
    sita=True
    bul=40

    # 유저 위치 선언

    x = pad_width * 0.55
    y = pad_height * 0.45
    x_change = 0
    y_change = 0
    background_x = 0

    # 적 위치 지정구간

    embulx1 = pad_width * 0.55
    embuly1 = pad_height * 0.16

    embulx2 = pad_width * 0.85
    embuly2 = pad_height * 0.47

    embulx3 = pad_width * 0.2
    embuly3 = pad_height * 0.47

    embulx4 = pad_width * 0.55
    embuly4 = pad_height * 0.9

    embulx5 = pad_width * 0.55
    embuly5 = pad_height * 0.16

    embulx6 = pad_width * 0.85
    embuly6 = pad_height * 0.47

    embulx7 = pad_width * 0.2
    embuly7 = pad_height * 0.47

    embulx8 = pad_width * 0.55
    embuly8 = pad_height * 0.9

    # 적 총알 무작위 숫자

    iax =  0
    iay =  -10

    ibx ,iby =numc1()

    icx ,icy = numc1()

    idx,idy = numc1()

    iex,iey = numc1()

    ifx,ify = numc1()

    igx,igy = numc1()

    ihx,ihy = numc1()

#본진 루프 함수

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
#키보드 입력 사항 구간
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=5
                elif event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key == pygame.K_RIGHT:
                    x_change =5
                if sit:
                    if event.key == pygame.K_w:
                        pygame.mixer.Sound.play(shot_sound)
                        sit=False
                        bul-=1
                        bullet_x = x + player_width/2
                        bullet_y = y + player_height
                        bullet_xy.append([bullet_x, bullet_y])
                    elif event.key == pygame.K_s:
                        pygame.mixer.Sound.play(shot_sound)
                        sit = False
                        bul -= 1
                        back_x = x + player_width/2
                        back_y = y + player_height
                        back_xy.append([back_x, back_y])
                if sita:
                    if event.key == pygame.K_d:
                        pygame.mixer.Sound.play(shot_sound)
                        sita = False
                        bul -= 1
                        right_x = x + player_width
                        right_y = y + player_height / 2
                        right_xy.append([right_x, right_y])
                    elif event.key == pygame.K_a:
                        pygame.mixer.Sound.play(shot_sound)
                        sita = False
                        bul -= 1
                        left_x = x + player_width
                        left_y = y + player_height / 2
                        left_xy.append([left_x, left_y])

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0
                elif event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        y+=y_change
        x+=x_change
        buli=str(bul)
        bulco(buli)
        bulco("                        발 남았습니다.")

#장외 방지 구간

        if y < 0:
            y_change = 0
            sit = True
        elif y > 875:
            y_change = 0
            sit = True
        elif x < 0:
            x_change = 0
            sit = True
        elif x > 850:
            x_change = 0
            sit = True

#적 총알 무작위 조준구간
        if dorl1==True:
            embulx1-=iax
            embuly1-=iay
            if embulx1<=0 or embuly1<=0 or embulx1>=pad_width or embuly1>=pad_height:
                iax, iay = numc1()
                embulx1 =pad_width*0.55
                embuly1 =pad_height*0.16
            elif x < pad_width * 0.55 + 100 and x > pad_width * 0.55 or \
                 y < pad_height * 0.45 + 100 and y > pad_height * 0.45:
                iax, iay = 0,-15
        else:

            embulx1=-100
            embuly1=-100


        if dorl2==True:
            embulx2-=ibx
            embuly2-=iby
            if embulx2<=0 or embuly2<=0 or embulx2>=pad_width or embuly2>=pad_height:
                ibx, iby = numc1()
                embulx2 =pad_width*0.85
                embuly2 =pad_height*0.47
            elif x < pad_width * 0.55 + 100 and x > pad_width * 0.55 or \
                 y < pad_height * 0.45 + 100 and y > pad_height * 0.45:
                ibx, iby = 15,0
        else:

            embulx2=-100
            embuly2=-100

        if dorl3==True:
            embulx3 -= icx
            embuly3 -= icy
            if embulx3<=0 or embuly3<=0 or embulx3>=pad_width or embuly3>=pad_height:
                icx, icy = numc1()
                embulx3 = pad_width*0.2
                embuly3 = pad_height*0.47
            elif x < pad_width * 0.55+100 and x > pad_width * 0.55 or \
                                    y < pad_height * 0.45 + 100 and y > pad_height * 0.45:
                icx, icy = -15,0
        else:

            embulx3=-100
            embuly3=-100

        if dorl4==True:
            embulx4 -= idx
            embuly4 -= idy
            if embulx4<=0 or embuly4<=0 or embulx4>=pad_width or embuly4>=pad_height:
                idx, idy = numc1()
                embulx4 = pad_width*0.55
                embuly4 = pad_height*0.9
            elif x < pad_width * 0.55 + 100 and x > pad_width * 0.55 or \
                 y < pad_height * 0.45 + 100 and y > pad_height * 0.45:
                idx, idy = 0,15
        else:

            embulx4 = -100
            embuly4 = -100

        if j>1:
            if dorl1 == True:
                embulx5 -= iex
                embuly5 -= iey
                if embulx5 <= 0 or embuly5 <= 0 or embulx5 >= pad_width or embuly5 >= pad_height:
                    iex, iey = numc1()
                    embulx5 = pad_width * 0.55
                    embuly5 = pad_height * 0.16
            else:

                embulx5 = -100
                embuly5 = -100

            if dorl2 == True:
                embulx6 -= ifx
                embuly6 -= ify
                if embulx6 <= 0 or embuly6 <= 0 or embulx6 >= pad_width or embuly6 >= pad_height:
                    ifx, ify = numc1()
                    embulx6 = pad_width * 0.85
                    embuly6 = pad_height * 0.47
            else:

                embulx6 = -100
                embuly6 = -100
            if j>2:
                if dorl3 == True:
                    embulx7 -= igx
                    embuly7 -= igy
                    if embulx7 <= 0 or embuly7 <= 0 or embulx7 >= pad_width or embuly7 >= pad_height:
                        igx, igy = numc1()
                        embulx7 = pad_width * 0.2
                        embuly7 = pad_height * 0.47
                else:

                    embulx7 = -100
                    embuly7 = -100

                if dorl4 == True:
                    embulx8 -= ihx
                    embuly8 -= ihy
                    if embulx8 <= 0 or embuly8 <= 0 or embulx8 >= pad_width or embuly8 >= pad_height:
                        ihx, ihy = numc1()
                        embulx8 = pad_width * 0.55
                        embuly8 = pad_height * 0.9
                else:

                    embulx8 = -100
                    embuly8 = -100



# 적->아군 공격 판단 구간
        if x+100>embulx1 and x<embulx1+35:
            if y+100>embuly1 and y<embuly1+35:
                pyshot=True
                embulx1 = pad_width * 0.55
                embuly1 = pad_height * 0.16
        if x+100 > embulx2 and x < embulx2+35:
            if y+100 > embuly2 and y< embuly2+35:
                pyshot = True
                embulx2 = pad_width * 0.85
                embuly2 = pad_height * 0.47
        if x+100 > embulx3 and x < embulx3+35:
            if y+100 > embuly3 and y < embuly3+35:
                pyshot = True
                embulx3 = pad_width * 0.2
                embuly3 = pad_height * 0.47
        if x+100 > embulx4 and x < embulx4+35:
            if y+100 > embuly4 and y < embuly4+35:
                pyshot = True
                embulx4 = pad_width * 0.55
                embuly4 = pad_height * 0.9
        if j>1:
            if x + 100 > embulx5 and x < embulx5 + 35:
                if y + 100 > embuly5 and y < embuly5 + 35:
                    pyshot = True
                    embulx5 = pad_width * 0.55
                    embuly5 = pad_height * 0.16
            if x + 100 > embulx6 and x < embulx6 + 35:
                if y + 100 > embuly6 and y < embuly6 + 35:
                    pyshot = True
                    embulx6 = pad_width * 0.85
                    embuly6 = pad_height * 0.47
            if j>2:
                if x + 100 > embulx7 and x < embulx7 + 35:
                    if y + 100 > embuly7 and y < embuly7 + 35:
                        pyshot = True
                        embulx7 = pad_width * 0.2
                        embuly7 = pad_height * 0.47
                if x + 100 > embulx8 and x < embulx8 + 35:
                    if y + 100 > embuly8 and y < embuly8 + 35:
                        pyshot = True
                        embulx8 = pad_width * 0.55
                        embuly8 = pad_height * 0.9


        #아군->적 공격 판단 구간
        if len(bullet_xy) != 0:
            for i, axy in enumerate(bullet_xy):
                axy[1] -= 15
                bullet_xy[i][1] = axy[1]
                if axy[0]>((pad_width*0.43)-20) and (axy[0]<(pad_width*0.43)+180):
                    if axy[1]>((pad_height*0.06)-25) and  (axy[1]<(pad_height*0.06)+120):
                        isshot1=True
                        sit = True
                        bullet_xy.remove(axy)
                if axy[0]>((pad_width*0.73)-20) and axy[0]<((pad_width*0.73)+180):
                    if axy[1]>((pad_height*0.37)-25) and  axy[1]<((pad_height*0.37)+120):
                        isshot2=True
                        sit = True
                        bullet_xy.remove(axy)
                if axy[0]>((pad_width*0.08)-20) and axy[0]<((pad_width*0.08)+180):
                    if axy[1]>((pad_height*0.37)-25) and  axy[1]<((pad_height*0.37)+120):
                        isshot3=True
                        sit = True
                        bullet_xy.remove(axy)
                if axy[0]>((pad_width*0.43)-20) and axy[0]<((pad_width*0.43)+180):
                    if axy[1]>((pad_height*0.8)-25) and  (axy[1]<(pad_height*0.8)+120):
                        isshot4=True
                        sit = True
                        bullet_xy.remove(axy)
                if axy [0] >= pad_width or axy [0] <= 0 or axy [1] >= pad_height or axy [1] <= 0:
                    try:
                        sit = True
                        bullet_xy.remove(axy)
                    except:
                        pass
        if len(bullet_xy) !=0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)

        if len(back_xy) != 0:
            for i, bxy in enumerate(back_xy):
                bxy[1] += 15
                back_xy[i][1] = bxy[1]
                if bxy[0] > ((pad_width * 0.43)-20) and bxy[0] < (pad_width * 0.43) +180:
                    if bxy[1] > ((pad_height * 0.06) -25) and bxy[1] < (pad_height * 0.06) + 120:
                        isshot1 = True
                        sit = True
                        back_xy.remove(bxy)
                if bxy[0] > ((pad_width * 0.73)-20) and bxy[0] < (pad_width * 0.73) +180:
                    if bxy[1] > ((pad_height * 0.37) -25) and bxy[1] < (pad_height * 0.37) + 120:
                        isshot2 = True
                        sit = True
                        back_xy.remove(bxy)
                if bxy[0] > ((pad_width * 0.08)-20) and bxy[0] < (pad_width * 0.08) +180:
                    if bxy[1] > ((pad_height * 0.37) -25) and bxy[1] < (pad_height * 0.37) + 120:
                        isshot3 = True
                        sit = True
                        back_xy.remove(bxy)
                if bxy[0] > ((pad_width * 0.43)-20) and bxy[0] < (pad_width * 0.43) +180:
                    if bxy[1] > ((pad_height * 0.8) -25) and bxy[1] < (pad_height * 0.8) + 120:
                        isshot4 = True
                        sit = True
                        back_xy.remove(bxy)
                if bxy[0] >= pad_width or bxy[0] <= 0 or bxy[1] >= pad_height or bxy[1] <= 0:
                    try:
                        sit = True
                        back_xy.remove(bxy)
                    except:
                        pass
        if len(back_xy) != 0:
            for bx, by in back_xy:
                drawObject(bullet, bx, by)

        if len(right_xy) != 0:
            for i, cxy in enumerate(right_xy):
                cxy[0] += 15
                right_xy[i][0] = cxy[0]
                if cxy[0] > ((pad_width * 0.43)-20) and cxy[0] < (pad_width * 0.43) +180:
                    if cxy[1] > ((pad_height * 0.1) -25) and cxy[1] < (pad_height * 0.1) + 120:
                        isshot1 = True
                        sita = True
                        right_xy.remove(cxy)
                if cxy[0] > ((pad_width * 0.73)-20) and cxy[0] < (pad_width * 0.73) +180:
                    if cxy[1] > ((pad_height * 0.37) -25) and cxy[1] < (pad_height * 0.37) + 120:
                        isshot2 = True
                        sita = True
                        right_xy.remove(cxy)
                if cxy[0] > ((pad_width * 0.08)-20) and cxy[0] < (pad_width * 0.08) +180:
                    if cxy[1] > ((pad_height * 0.37) -25) and cxy[1] < (pad_height * 0.37) + 120:
                        isshot3 = True
                        sita = True
                        right_xy.remove(cxy)
                if cxy[0] > ((pad_width * 0.43)-20) and cxy[0] < (pad_width * 0.43) +180:
                    if cxy[1] > ((pad_height * 0.8) -25) and cxy[1] < (pad_height * 0.8) + 120:
                        isshot4 = True
                        sita = True
                        right_xy.remove(cxy)
                if cxy[0] >= pad_width or cxy[0] <= 0 or cxy[1] >= pad_height or cxy[1] <= 0:
                    try:
                        sita = True
                        right_xy.remove(cxy)
                    except:
                        pass
        if len(right_xy) != 0:
            for bx, by in right_xy:
                drawObject(bullet, bx, by)

        if len(left_xy) != 0:
            for i, dxy in enumerate(left_xy):
                dxy[0] -= 15
                left_xy[i][0] = dxy[0]
                if dxy[0] > ((pad_width * 0.43)-20) and dxy[0] < (pad_width * 0.43) +180:
                    if dxy[1] > ((pad_height * 0.06)-25) and dxy[1] < ((pad_height * 0.06) + 120):
                        isshot1 = True
                        sita = True
                        left_xy.remove(dxy)
                if dxy[0] > (pad_width * 0.73-20) and dxy[0] < (pad_width * 0.73) +180:
                    if dxy[1] > ((pad_height * 0.37) -25) and dxy[1] < (pad_height * 0.37) + 120:
                        isshot2 = True
                        sita = True
                        left_xy.remove(dxy)
                if dxy[0] > ((pad_width * 0.08)-20) and dxy[0] < (pad_width * 0.08) +180:
                    if dxy[1] > ((pad_height * 0.37) -25) and dxy[1] < (pad_height * 0.37) + 120:
                        isshot3 = True
                        sita = True
                        left_xy.remove(dxy)
                if dxy[0] > ((pad_width * 0.43)-20) and dxy[0] < (pad_width * 0.43) +180:
                    if dxy[1] > ((pad_height * 0.8) -25) and dxy[1] < (pad_height * 0.8) + 120:
                        isshot4 = True
                        sita = True
                        left_xy.remove(dxy)
                if dxy[0] >= pad_width or dxy[0] <= 0 or dxy[1] >= pad_height or dxy[1] <= 0:
                    try:
                        sita = True
                        left_xy.remove(dxy)
                    except:
                        pass
        if len(left_xy) != 0:
            for bx, by in left_xy:
                drawObject(bullet, bx, by)
        #적군->아군 반응 함수
        if pyshot:
            dam+=1
            pyshot=False

        #아군->적군 반응 함수
        if isshot1:
            score1+=1
            isshot1=False

        if isshot2:
            score2+=1
            isshot2 = False

        if isshot3:
            score3+=1
            isshot3 = False

        if isshot4:
            score4+=1
            isshot4 = False

        drawObject(eme, pad_width * 0.45, pad_height * 0.06)
        drawObject(eme, pad_width * 0.75, pad_height * 0.37)
        drawObject(eme, pad_width * 0.1, pad_height * 0.37)
        drawObject(eme, pad_width * 0.45, pad_height * 0.8)

        #피통구현
        if dam==1:
            drawObject(pyblo1,pad_width*0.02, pad_height*0.02)
        elif dam==2:
            drawObject(pyblo2,pad_width*0.02, pad_height*0.02)
        elif dam == 3:
            drawObject(pyblo3, pad_width * 0.02, pad_height * 0.02)
        elif dam==4:
            drawObject(pyblo4,pad_width*0.02, pad_height*0.02)
        elif dam==5:
            drawObject(pyblo5,pad_width*0.02, pad_height*0.02)
        elif dam==6:
            drawObject(pyblo6,pad_width*0.02, pad_height*0.02)
        elif dam==7:
            drawObject(pyblo7,pad_width*0.02, pad_height*0.02)
        elif dam==8:
            drawObject(pyblo8,pad_width*0.02, pad_height*0.02)
        elif dam==9:
            drawObject(pyblo9,pad_width*0.02, pad_height*0.02)
        elif dam==10:
            drawObject(pyblo10,pad_width*0.02, pad_height*0.02)
            pygame.mixer.Sound.play(lose_sound)
            dispMessage("You Lose!!")
        if bul==0:
            pygame.mixer.Sound.play(lose_sound)
            dispMessage("You Lose!!")

        if score1==1:
            drawObject(emeblo1, pad_width*0.42, pad_height*0.21)
        elif score1==2:
            drawObject(emeblo2,pad_width*0.42, pad_height*0.21)
        elif score1==3:
            drawObject(emeblo3,pad_width*0.42, pad_height*0.20)
        elif score1==4:
            drawObject(emeblo4,pad_width*0.42, pad_height*0.21)
        elif score1==5:
            drawObject(emeblo5,pad_width*0.42, pad_height*0.20)
            drawObject(impact, pad_width * 0.45, pad_height * 0.06)
            if dorl1==True:
                pygame.mixer.Sound.play(explosion_sound)
            dorl1=False
        elif score1>5:
            drawObject(emeblo5, pad_width * 0.42, pad_height * 0.20)
            drawObject(impact, pad_width * 0.45, pad_height * 0.06)
            dorl1 = False


        if score2==1:
            drawObject(emeblo1,pad_width*0.72, pad_height*0.52 )
        elif score2==2:
            drawObject(emeblo2,pad_width*0.72, pad_height*0.52)
        elif score2==3:
            drawObject(emeblo3,pad_width*0.72, pad_height*0.51)
        elif score2==4:
            drawObject(emeblo4,pad_width*0.72, pad_height*0.52)
        elif score2==5:
            drawObject(emeblo5,pad_width*0.72, pad_height*0.51)
            drawObject(impact, pad_width * 0.75, pad_height * 0.37)
            if dorl2 == True:
                pygame.mixer.Sound.play(explosion_sound)
            dorl2=False
        elif score2>5:
            drawObject(emeblo5, pad_width * 0.72, pad_height * 0.51)
            drawObject(impact, pad_width * 0.75, pad_height * 0.37)
            dorl2 = False

        if score3==1:
            drawObject(emeblo1, pad_width*0.07, pad_height*0.52)
        elif score3==2:
            drawObject(emeblo2,pad_width*0.07, pad_height*0.52)
        elif score3==3:
            drawObject(emeblo3,pad_width*0.07, pad_height*0.51)
        elif score3==4:
            drawObject(emeblo4,pad_width*0.07, pad_height*0.52)
        elif score3==5:
            drawObject(emeblo5,pad_width*0.07, pad_height*0.51)
            drawObject(impact, pad_width * 0.1, pad_height * 0.37)
            if dorl3 == True:
                pygame.mixer.Sound.play(explosion_sound)
            dorl3=False
        elif score3>5:
            drawObject(emeblo5, pad_width * 0.07, pad_height * 0.51)
            drawObject(impact, pad_width * 0.1, pad_height * 0.37)
            dorl3 = False

        if score4==1:
            drawObject(emeblo1, pad_width*0.42, pad_height*0.95)
        elif score4==2:
            drawObject(emeblo2,pad_width*0.42, pad_height*0.95)
        elif score4==3:
            drawObject(emeblo3,pad_width*0.42, pad_height*0.94)
        elif score4==4:
            drawObject(emeblo4,pad_width*0.42, pad_height*0.95)
        elif score4==5:
            drawObject(emeblo5,pad_width*0.42, pad_height*0.94)
            drawObject(impact, pad_width * 0.45, pad_height * 0.8)
            if dorl4 == True:
                pygame.mixer.Sound.play(explosion_sound)
            dorl4=False
        elif score4>5:
            drawObject(emeblo5, pad_width * 0.42, pad_height * 0.94)
            drawObject(impact, pad_width * 0.45, pad_height * 0.8)
            dorl4 = False


        if score1>=5 and score2>=5 and score3>=5 and score4>=5:
            pygame.mixer.Sound.play(win_sound)
            dispMessage("You Win!!")


        drawObject(player, x, y)
        drawObject(emebul1,embulx1,embuly1)
        drawObject(emebul2, embulx2, embuly2)
        drawObject(emebul3, embulx3, embuly3)
        drawObject(emebul4, embulx4, embuly4)
        if j>1:
            drawObject(emebul5, embulx5, embuly5)
            drawObject(emebul6, embulx6, embuly6)
            if j>2:
                drawObject(emebul7, embulx7, embuly7)
                drawObject(emebul8, embulx8, embuly8)
        drawObject(empblo, pad_width*0.42, pad_height*0.17)
        drawObject(empblo, pad_width*0.72, pad_height*0.48)
        drawObject(empblo, pad_width*0.07, pad_height*0.48)
        drawObject(empblo, pad_width*0.42, pad_height*0.91)
        drawObject(pyembl, pad_width*0.02, pad_height*0.02)

        pygame.display.update()
        gamepad.fill(WHITE)
        back(background_x,0)
        clock.tick(60)

    pygame.quit()
    quit()

#콘텐츠 관리 구간

def initGame():
    global gamepad,clock,player,background,emebul5,emebul6,emebul7,emebul8
    global eme, bullet,bullet2, bullet3, emebul1
    global bullet4,impact,emeblo1,empblo,plyblo,emeblo2
    global emeblo3,emeblo4, emeblo5,pyembl, pyblo10
    global pyblo1,pyblo2,pyblo3,pyblo4,pyblo5,pyblo6,pyblo7,pyblo8,pyblo9
    global shot_sound, explosion_sound,win_sound,lose_sound
    global emebul2,emebul3,emebul4,BIGFONT,BASICFONT,intro,jk

    pygame.init()
    BIGFONT = pygame.font.Font("malgun.ttf", 100)
    BASICFONT = pygame.font.Font("malgun.ttf", 18)
    gamepad=pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption("엄마의 점심시간")
    player = pygame.image.load("KakaoTalk_20170601_203042782.png")
    background = pygame.image.load("KakaoTalk_20170601_214031696.jpg")
    eme=pygame.image.load("KakaoTalk_20170601_210156741.png")
    bullet = pygame.image.load("KakaoTalk_20170601_203051304.png")
    impact = pygame.image.load("KakaoTalk_20170601_211919913.png")
    emebul1= pygame.image.load("aa1.png")
    emebul2 = pygame.image.load("aa2.png")
    emebul3 = pygame.image.load("aa3.png")
    emebul4 = pygame.image.load("aa4.png")
    emebul5 = pygame.image.load("aa1.png")
    emebul6 = pygame.image.load("aa2.png")
    emebul7 = pygame.image.load("aa3.png")
    emebul8 = pygame.image.load("aa4.png")
    empblo= pygame.image.load("피통2.png")
    emeblo1= pygame.image.load("피통1_1.png")
    plyblo= pygame.image.load("피통3.png")
    emeblo2= pygame.image.load("피통1_2.png")
    emeblo3= pygame.image.load("피통1_3.png")
    emeblo4= pygame.image.load("피통1_4.png")
    emeblo5= pygame.image.load("피통1_5.png")
    pyembl=pygame.image.load("아군 피통.png")
    pyblo1=pygame.image.load("아군 피통1.png")
    pyblo2 = pygame.image.load("아군 피통2.png")
    pyblo3 = pygame.image.load("아군 피통3.png")
    pyblo4 = pygame.image.load("아군 피통4.png")
    pyblo5 = pygame.image.load("아군 피통5.png")
    pyblo6 = pygame.image.load("아군 피통6.png")
    pyblo7 = pygame.image.load("아군 피통7.png")
    pyblo8 = pygame.image.load("아군 피통8.png")
    pyblo9 = pygame.image.load("아군 피통9.png")
    pyblo10 = pygame.image.load("아군 피통10.png")
    intro = pygame.image.load("8.png")


    shot_sound = pygame.mixer.Sound("SINGLE-SHOT2.wav")
    explosion_sound = pygame.mixer.Sound("baby.wav")
    pygame.mixer.music.load("DangerousEscpae-Everyday2.wav")
    pygame.mixer.music.play(-1)
    win_sound=pygame.mixer.Sound("win2.wav")
    lose_sound=pygame.mixer.Sound("lose2.wav")
    count = pygame.mixer.Sound("321.wav")
    clock = pygame.time.Clock()
    jk=intro1()
    pygame.mixer.Sound.play(count)
    time.sleep(3)
    runGame(jk)


initGame()