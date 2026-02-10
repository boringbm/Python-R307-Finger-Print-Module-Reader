# R307 Finger Print Module
Reads and returns fingerprint template in JSON format using R307 fingerprint modules attached to USB to TTL cable on the computer.

## Hardware Used
-   RoboThings R307 Finger Print Sensor Module (https://amzn.to/4bRn7sl)
-   USB to TTL Converter Module (https://amzn.to/4qqRoBC)

## Initial Setup
-   Activate virtual environment
-   Install required dependencies from requirements.txt file
-   Change "/dev/ttyUSB0" in this line to reflect your actual port where the USB to TTL converter module is connected:<br>
    ``f = PyFingerprint("/dev/ttyUSB0", 57600)``
-   Run the application:<br>
```bash
    uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
