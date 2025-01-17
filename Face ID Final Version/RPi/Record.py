from picamera import PiCamera
from time import sleep
import serial
import os
from Myservo2 import Myservo

check = 1
loop = 0
ser = serial.Serial(port='/dev/ttyACM1',baudrate=115200,timeout=1)
servopin = 17

while True:
          if check == 1:
                    print('Listening on /dev/ttyACM1...')
                    check = 0
                    
          msg = ser.readline()
          smsg = msg.decode('utf-8').strip()
          if smsg is '1':
              
                    check = 1
                    result1 = os.popen('rm -rf /home/pi/video.h264')
                    print(result1.read())
                    result2 = os.popen('rm -rf /home/pi/video.mp4')
                    print(result2.read())
                    
                    print('RX:{}\nRecording'.format(smsg))
                    
                    if loop == 0:
                        camera = PiCamera()
                        
                    camera.resolution = (640,480)
                    camera.framerate = 15
                    camera.start_preview()
                    camera.start_recording('/home/pi/video.h264')
                    sleep(4)
                    camera.stop_recording()
                    camera.stop_preview()
                    check = 1
                    loop = 1
                    result3 = os.popen('MP4Box -add video.h264 video.mp4')
                    print(result3.read())
                    print('Converted')
                    
                    servopin1 = 17
                    servopin2 = 27

                    ser2 = serial.Serial(port='/dev/ttyACM1',baudrate=115200,timeout=1)

                    while True:
                                        
                              msg2 = ser2.readline()
                              smsg2 = msg2.decode('utf-8').strip()
                              if len(smsg2)>0 and smsg2 != '1':
                                  
                                  #print(smsg2)
                                  if smsg2 is '2':
                                      Myservo(servopin1, servopin2)
                                      print('Door is open')
                                      break
                                  if smsg2 is '3':
                                      print('Locked')
                                      break
                                      
