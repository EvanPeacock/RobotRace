from spike import Motor, DistanceSensor, PrimeHub, MotorPair, ColorSensor
from spike.control import wait_for_seconds, Timer
import random

# Initialize the Hub
hub = PrimeHub()
hub.speaker.set_volume(100)
hub.light_matrix.show_image('CHESSBOARD')

#Initialize the Distance Sensor and motor
motors = MotorPair('C', 'D')
col_sensor_A = ColorSensor('A')
col_sensor_B = ColorSensor('B')


def matrixSpin():
    hub.light_matrix.off()
    hub.light_matrix.set_pixel(1, 0)
    hub.light_matrix.set_pixel(0, 1)
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(0, 3)
    hub.light_matrix.set_pixel(1, 4)
    hub.light_matrix.set_pixel(2, 4)
    hub.light_matrix.set_pixel(3, 4)
    hub.light_matrix.set_pixel(4, 2)
    hub.light_matrix.set_pixel(4, 3)
    hub.light_matrix.set_pixel(3, 1)
    hub.light_matrix.set_pixel(2, 2)
    hub.speaker.beep(75, 0.2)
    hub.speaker.beep(60, 0.2)
    hub.speaker.beep(75, 0.2)
    hub.speaker.beep(60, 0.2)

def matrixSpeedUpTemp():
    hub.light_matrix.off()
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(1, 1)
    hub.light_matrix.set_pixel(2, 0)
    hub.light_matrix.set_pixel(3, 1)
    hub.light_matrix.set_pixel(4, 2)

    hub.light_matrix.set_pixel(1, 4)
    hub.light_matrix.set_pixel(2, 3)
    hub.light_matrix.set_pixel(3, 4)
    hub.speaker.beep(60, 0.3)
    hub.speaker.beep(70, 0.3)
    hub.speaker.beep(80, 0.3)
    hub.speaker.beep(90, 0.3)

def matrixSlowDownTemp():
    hub.light_matrix.off()
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(1, 3)
    hub.light_matrix.set_pixel(2, 4)
    hub.light_matrix.set_pixel(3, 3)
    hub.light_matrix.set_pixel(4, 2)

    hub.light_matrix.set_pixel(1, 0)
    hub.light_matrix.set_pixel(2, 1)
    hub.light_matrix.set_pixel(3, 0)
    hub.speaker.beep(90, 0.3)
    hub.speaker.beep(80, 0.3)
    hub.speaker.beep(70, 0.3)
    hub.speaker.beep(60, 0.3)

def matrixSpeedUpPerm():
    hub.light_matrix.off()
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(1, 1)
    hub.light_matrix.set_pixel(2, 0)
    hub.light_matrix.set_pixel(3, 1)
    hub.light_matrix.set_pixel(4, 2)
    hub.speaker.beep(60, 0.3)
    hub.speaker.beep(75, 0.3)
    hub.speaker.beep(90, 0.3)

def matrixSlowDownPerm():
    hub.light_matrix.off()
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(1, 3)
    hub.light_matrix.set_pixel(2, 4)
    hub.light_matrix.set_pixel(3, 3)
    hub.light_matrix.set_pixel(4, 2)
    hub.speaker.beep(90, 0.3)
    hub.speaker.beep(75, 0.3)
    hub.speaker.beep(60, 0.3)

def randomAction():
    num = random.randint(0, 4) # However many different actions we want!

    if num == 0:
        #Spin in place
        print("Spin")
        matrixSpin()
        motors.start(20, -20)
        wait_for_seconds(2)
        motors.start()
    elif num == 1:
        #Speed up for 2 seconds
        print("Temporary Speed Up")
        matrixSpeedUpTemp()
        motors.start(30)
        wait_for_seconds(2)
        motors.start()
    elif num == 2:
        #Slow down for 2 seconds
        print("Temporary Slow Down")
        matrixSlowDownTemp()
        motors.start(10)
        wait_for_seconds(2)
        motors.start()
    elif num == 3:
        #Speed up permanently
        print("Permanent Speed Up")
        matrixSpeedUpPerm()
        motors.start(30)
    elif num == 4:
        #Slow down permanently
        print("Permanent Slow Down")
        matrixSlowDownPerm()
        motors.start(10)

def race():
    #Press the left button to start
    while True:
        if hub.left_button.was_pressed():
            hub.speaker.beep(60, 0.3)
            wait_for_seconds(0.8)
            hub.speaker.beep(60, 0.3)
            wait_for_seconds(0.8)
            hub.speaker.beep(60, 0.3)
            wait_for_seconds(0.8)
            hub.speaker.beep(75, 0.3)
            hub.light_matrix.show_image('ARROW_N')
            timer = Timer()
            print("Timer Started")
            break

    while(col_sensor_A.get_color() != 'red'):
        #Line following
        if col_sensor_A.get_color() == 'black':
            motors.start(20, 15)
        elif col_sensor_B.get_color() == 'black':
            motors.start(-15)
        else:
            motors.start()

        #Powerup detection
        if col_sensor_A.get_color() == 'green':
            print("Powerup Detected")
            randomAction()
            hub.light_matrix.show_image('ARROW_N')

    #Stop the robot when the finish line is detected
    motors.stop()
    hub.light_matrix.show_image('CHESSBOARD')
    print("Total Time: " + str(timer.now()) + " seconds")
    hub.speaker.beep(60, 0.2)
    hub.speaker.beep(65, 0.3)
    hub.speaker.beep(70, 0.2)
    hub.speaker.beep(75, 0.3)

race()