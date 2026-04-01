import pgzrun
import random
WIDTH=800
HEIGHT=600
ship=Actor ('spaceship')
ship.pos=(400,550)
bullets=[]
enemies=[]
score=0
speed=5
bug=Actor('bug')
bug.pos=(random.randint(50,750),-50)
enemies.append('bug')
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullet.pos=(ship.x,ship.y-40)
        bullets.append('bullet')
def update():
    global score
    if keyboard.left:
        ship.x-=10
    if keyboard.right:
        ship.x+=10
    ship.x=max(0,min(WIDTH,ship.x))
    for bullet in bullets:
        bullet.y-=10
        if bullet.y<0:
            bullets.remove(bullet)
    for enemy in enemies:
        enemy.y +=5
        if enemy.y>HEIGHT:
            enemy.y=-50
            enemy.x=(random.randint(50,750))
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullet.remove(bullet)
                enemy.y=-50
                enemy.x=(random.randint(50,750))
                score=score+10
def draw():
    screen.clear()
    screen.fill('pink')
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    screen.draw.text('score:{}'.format(score),topleft=(20,20),color='black',fontsize=20)
pgzrun.go()
    
      

    