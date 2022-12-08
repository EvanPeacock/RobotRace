from spike import Motor, DistanceSensor, PrimeHub, MotorPair, ColorSensor
from spike.control import wait_for_seconds, Timer

# Initialize the Hub
hub = PrimeHub()
hub.speaker.set_volume(100)
hub.light_matrix.show_image('CHESSBOARD')

#Initialize the Distance Sensor and motor
motors = MotorPair('C', 'D')
col_sensor_A = ColorSensor('A')
col_sensor_B = ColorSensor('B')

def race():
    running = False
    #Press the left button to start
    while True:
        if hub.left_button.was_pressed():
            running = True
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
            hub.light_matrix.show_image('DIAMOND')
            print("Powerup Detected")
            hub.speaker.beep(55, 0.2)
            hub.speaker.beep(65, 0.3)
            hub.speaker.beep(55, 0.2)
            hub.light_matrix.show_image('ARROW_N')

    #Stop the robot when the finish line is detected        
    motors.stop()
    running = False
    hub.light_matrix.show_image('CHESSBOARD')
    print("Total Time: " + str(timer.now()) + " seconds")
    hub.speaker.beep(60, 0.2)
    hub.speaker.beep(65, 0.3)
    hub.speaker.beep(70, 0.2)
    hub.speaker.beep(75, 0.3)



race()
