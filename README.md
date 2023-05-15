# AimBooster AimBot

## Project Details

This project is an AimBot for [AimBooster](www.aimbooster.com/). The code takes a screenshot, finds the targets, moves the cursor and clicks. Currently it can handle over 50 targets/sec.

## Instructions

Enter [AimBooster.com](www.aimbooster.com/). Change the settings to the following:

![Settings](https://raw.githubusercontent.com/X10KND/AimBooster-AimBot/main/Settings.png)

Change the values in code if required.  
X_OFFSET is the X position of the top-left corner and Y_OFFSET is the Y position of the top-left corner.

```python
X_OFFSET = 585
Y_OFFSET = 440

WIDTH = 750
HEIGHT = 525
```

Once the code is running, you have 2 seconds to switch to AimBooster and hit start.

## Requirements

`pip install numpy`  
`pip install mss`  
`pip install mouse`

## WARNING

This code currently has no fail-safe. It takes complete control over all mouse movements as long as the colour <html><span style="background-color:#00FF00; border-radius: 50%; height: 12px; width: 12px; display: inline-block;"></span></html>`#00FF00` is on screen.

## Note

I have found it performs better on the Chrome browser compared to Firefox. This might be a limitation of the AimBooster site.