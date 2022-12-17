from spike import Motor, DistanceSensor, PrimeHub, MotorPair, ColorSensor
from spike.control import wait_for_seconds, Timer
import random

# Initialize the Hub
hub = PrimeHub()
hub.speaker.set_volume(100)
hub.light_matrix.show_image('CHESSBOARD')

# Initialize the Distance Sensor and motor
motors = MotorPair('C', 'D')
motorC = Motor('C')
motorD = Motor('D')
colorA = ColorSensor('A')
colorB = ColorSensor('B')


# Set default speed
current_speed = 25

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

def secondsToMinutes(seconds):
    #Convert to minutes and round down
    minutes = seconds // 60

    #Get remaining seconds
    remaining_seconds = seconds % 60

    #Format the seconds to have a leading zero
    formatted_seconds = "{:02d}".format(remaining_seconds)

    #Return formatted string with minutes and seconds
    return "{}:{}".format(minutes, formatted_seconds)

def randomAction():
    global current_speed
    num = random.randint(0, 4) # However many different actions we want!

    if num == 0:
        #Spin in place
        print("Spin")
        matrixSpin()
        motorC.start(80)
        motorD.start(80)
        #motors.start_tank_at_power(-80, 80)
        wait_for_seconds(2)
        # Return to normal speed
        #motors.start(current_speed)
        motorC.start(-current_speed)
        motorD.start(current_speed)
    elif num == 1:
        #Speed up for 1 second
        print("Temporary Speed Up")
        matrixSpeedUpTemp()
        if current_speed < 85:
            motorC.start(-current_speed-15)
            motorD.start(current_speed+15)
            #motors.start(current_speed + 15)
            print("Temporary Speed: " + str(current_speed + 15))
        else:
            motorC.start(-100)
            motorD.start(100)
            #motors.start(100)
            print("Temporary Speed: 100")
        wait_for_seconds(1)
        motors.start(current_speed)
    elif num == 2:
        #Slow down for 1 second
        print("Temporary Slow Down")
        matrixSlowDownTemp()
        if current_speed > 15:
            motorC.start(-current_speed+15)
            motorD.start(current_speed-15)
            #motors.start(current_speed - 15)
            print("Temporary Speed: " + str(current_speed - 15))
        else:
            motorC.start(-5)
            motorD.start(5)
            #motors.start(5)
            print("Temporary Speed: 5")
        wait_for_seconds(1)
        motorC.start(-current_speed)
        motorD.start(current_speed)
        #motors.start(current_speed)
    elif num == 3:
        #Speed up permanently
        print("Permanent Speed Up")
        matrixSpeedUpPerm()
        current_speed = current_speed + 5
        motorC.start(-current_speed)
        motorD.start(current_speed)
        #motors.start(current_speed)
        print("New Speed: " + str(current_speed))
    elif num == 4:
        #Slow down permanently
        print("Permanent Slow Down")
        matrixSlowDownPerm()
        current_speed = current_speed - 5
        motorC.start(-current_speed)
        motorD.start(current_speed)
        #motors.start(current_speed)
        print("New Speed: " + str(current_speed))

def race():
    global current_speed
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

    while(colorA.get_color() != 'red'):
        #Line following
        if colorA.get_color() == 'black':
            motorC.start(-current_speed)
            motorD.start(10)
            wait_for_seconds(0.5)
        elif colorB.get_color() == 'black':
            motorD.start(current_speed)
            motorC.start(-10)
            wait_for_seconds(0.5)
        else:
            motorC.start(-current_speed)
            motorD.start(current_speed)
        #Powerup detection
        if colorA.get_color() == 'green':
            print("Powerup Detected")
            randomAction()
            hub.light_matrix.show_image('ARROW_N')
        
    #Stop the robot when the finish line is detected
    motors.stop()

    #Format and print the total time
    totalTime = secondsToMinutes(timer.now())
    print("Total Time: " + totalTime)

    hub.light_matrix.show_image('CHESSBOARD')
    hub.speaker.beep(60, 0.2)
    hub.speaker.beep(65, 0.3)
    hub.speaker.beep(70, 0.2)
    hub.speaker.beep(75, 0.3)

    #Display the total time on the matrix
    hub.light_matrix.off()
    while True:
        hub.light_matrix.write(totalTime)

#Start race
race()