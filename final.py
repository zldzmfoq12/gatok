#!/usr/bin/env python
import vlc,os
import time
import RPi.GPIO as GPIO
import smbus
import time
from ftplib import FTP

ftp=FTP('192.168.0.103','root','raspberry')
ftp.cwd('/norae')
i=0
h=0
nr=[]
titlelist=[]
ftp.retrlines("LIST", nr.append)
while i<len(nr):
  words = nr[i].split(None, 8)
  filename=words[-1].lstrip()
  titlelist.append(filename)
  i+=1
print(titlelist)
while h< len(titlelist):
  local_filename = os.path.join(r"/home/pi/",titlelist[h])
  If=open(local_filename,"wb")
  ftp.retrbinary("RETR "+ titlelist[h], If.write ,8*1024)
  If.close()
  h+=1
print (nr[0])



GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(22,GPIO.IN)

I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor mov e direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)


def main():
  # Main program block
    n=0
    m=0
    print(titlelist[n])
    fulldir="/home/pi/"+titlelist[n]

    instance = vlc.Instance()

    player=instance.media_player_new()

    media =instance.media_new(fulldir)

    player.set_media(media)

    player.play()

    
    lcd_init()

    lcd_string(str(titlelist[0]),LCD_LINE_1)
    lcd_string('playing',LCD_LINE_2)
    time.sleep(1)
    # Initialise display
    
    while True:
        a = player.get_state()
        if a==5:
            break
        elif a==6:
            if n==len(nr)-1:
                n=0
                print(titlelist[n])
                fulldir="/home/pi/"+titlelist[n]
    
                instance = vlc.Instance()
    
                player=instance.media_player_new()

                media =instance.media_new(fulldir) 

                player.set_media(media)
 
                player.play()

                lcd_string(str(titlelist[n]),LCD_LINE_1)
                lcd_string(str(a),LCD_LINE_2)

                time.sleep(1)
                

            else:
                n=n+1
                print(titlelist[n])
                fulldir="/home/pi/"+titlelist[n]

                instance = vlc.Instance()

                player=instance.media_player_new()

                media =instance.media_new(fulldir) 

                player.set_media(media)

                player.play()
                lcd_string(str(titlelist[n]),LCD_LINE_1)
                lcd_string(str(a),LCD_LINE_2)

                time.sleep(1)
            

        if GPIO.input(17) == 0:
            m =m+1
            print("!!!")
            player.pause()
            a=player.get_state
            time.sleep(1)
            lcd_string(str(titlelist[n]),LCD_LINE_1)
            if m %2==0:
              lcd_string('playing',LCD_LINE_2)
            else:
              lcd_string('paused',LCD_LINE_2)
              
           
            


        elif GPIO.input(23) ==0:
            print("!!!!2")
            if(a==3):
                player.stop()
              
            elif(a==4):
              player.stop()
        
                
              
    

        elif GPIO.input(22) ==0:
            if(a==3):
                player.stop()
                print("!!!3")
                n = n+1
                if n==len(nr):
                    n=0
                    print(titlelist[n])
                    fulldir="/home/pi/"+titlelist[n]

                    instance = vlc.Instance()

                    player=instance.media_player_new()

                    media =instance.media_new(fulldir) 

                    player.set_media(media)

                    player.play()
                    lcd_string(str(titlelist[n]),LCD_LINE_1)
                    lcd_string(str(a),LCD_LINE_2)
 

                    time.sleep(1)
                else:
                    print(titlelist[n])
                    fulldir="/home/pi/"+titlelist[n]
                    print(fulldir)

                    instance = vlc.Instance()

                    player=instance.media_player_new()

                    media =instance.media_new(fulldir) 

                    player.set_media(media)

                    player.play()
                    lcd_string(str(titlelist[n]),LCD_LINE_1)
                    lcd_string(str(a),LCD_LINE_2)


                    time.sleep(1)



        elif GPIO.input(18) ==0:
            if(a==3):
                player.stop()
                print("!!!4")
                if n==0:
                    n=len(nr)-1
                    print(titlelist[n])
                    fulldir="/home/pi/"+titlelist[n]

                    instance = vlc.Instance()

                    player=instance.media_player_new()

                    media =instance.media_new(fulldir) 

                    player.set_media(media)

                    player.play()
                    lcd_string(str(titlelist[n]),LCD_LINE_1)
                    lcd_string(str(a),LCD_LINE_2)


                    time.sleep(1)
                else:
                    n=n-1
                    print(titlelist[n])
                    fulldir="/home/pi/"+titlelist[n]

                    instance = vlc.Instance()

                    player=instance.media_player_new()

                    media =instance.media_new(fulldir) 

                    player.set_media(media)

                    player.play()
                    lcd_string(str(titlelist[n]),LCD_LINE_1)
                    lcd_string(str(a),LCD_LINE_2)

                    time.sleep(1)
                    a = player.get_state()

            
                    
if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)


        
main()
