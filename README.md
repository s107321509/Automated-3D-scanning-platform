# Automatic shooting platform for 3D modeling


## Table of Contents

- [Background](#Background)
- [Install](#Install)
- [Usage](#Usage)


## Background

`3D modeling platform`The 3D platform is used to rotate the specimen to capture images from different angles of the specimen to complete the prior work required for 3D modeling. However, although there are many ready-made 3D scanners on the market that can be purchased by the public, they are expensive and cost tens of thousands of yuan. Our two-dimensional platform is composed of 3D printing components and stepping motors, and its cost is relatively low. And easy to get.

This github provides the code for the control platform.


There are several things you must prepare before using this program：

1. Rasberry pi
2. 3 stepping motors
3. camera
4. Motor drive
5. Download the platform architecture model from [Openscan] (https://www.thingiverse.com/thing:3050437) and print it out using 3D printing

## Install

This project uses gphoto2 to control the camera to take pictures. Please make sure that this software is installed before use.

```sh
$ sudo apt-get install gphoto2
```
Please make sure to install python2.7 before use.

```sh
$ sudo apt-get install python2.7
```

##  Usage

The specimen shooting process can be roughly divided into the following steps：

1.The user can define any number of tilt angles and the number of steps of a horizontal rotation in the `tilting.py`, as follows, which is defined as the horizontal turntable shooting 40 surround images per revolution, and the tilt axis moves 300 microsteps each time, divided into three Shoot from different angles.

```sh
panning_step = [40,40,40]
tilting_step = [300,300,300]
```
2.Use `start.py` to control the movement of the stacking platform to find the clear range of the front and back focus of the subject. Use the method of reading the keyboard keys to define w as forward, s as backward, a and d to define the shooting start and end positions, and finally press the q key to complete the parameters set up.

3.After each step of the horizontal turntable, the stacking program is called. After each step of the stack, the camera program is executed to automatically control the camera to shoot the specimen.

4.Repeat step (3) until the horizontal turntable completes one revolution.

5.Move the tilt axis to the next angle and repeat steps (3) (4) until all the tilt angles are taken. 

6.After the shooting is completed, the three-axis platform returns to the initial position.
