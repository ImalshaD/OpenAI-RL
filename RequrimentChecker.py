import subprocess
lgym=True
lnumpy=True
lpygame=True
lmatplotlib=True
try:
    import gym
    print("Gym installed properly")
    lgym=False
except:
    print("gym not installed properly")
try:
    import numpy
    print("numpy installed properly")
    lnumpy=False
except:
    print("numpy not installed properly")
try:
    import pygame
    print("pygame installed properly")
    lpygame=False
except:
    print("pygame not installed properly")
try:
    import matplotlib
    print("matplotlib installed properly")
    lmatplotlib=False
except:
    print("matplotlib not installed properly")

if (lgym or lnumpy or lpygame or lmatplotlib):
    print("Installing libraries")
    subprocess.call([r'runMeFirst.bat'])
else:
    print("All set to go")