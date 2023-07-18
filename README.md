# unipolar_steppermotor_MD5HD-HD14
In this project I am controlling 5phase unipolar stepper motor (model A2K-S544) using Autonics motor driver ( model MD5-HD14)) and raspberry pi. Also I have incorporated two photomicro sensors (model EE-SX672A) to limit the rotation angle of my stepper motor.
Initial program rotates the motor in a clockwise direction until the right sensor is interrupted, then stop for a few seconds then start rotating counter clockwise direction until the left sensor is interrupted where it stops.
