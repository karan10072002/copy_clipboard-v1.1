# copy_clipboard-v1.1
This program saves your last 10 copied items and makes them available to you through very easily accessible shortcut keys which saves a lot of time and effort while copying multiple items of different kinds from different sources. 

To provide refference for your last 10 copied items the console shows them with their respective indexing.

copy_clipboard cheet sheet ( shortcut keys ):

    ctrl + c  -----  copies the text
    shift + x  -----  copies the files and folders
    ctrl + v + int( 1 - 9) -----  pastes the copied item at the respective index
    ctrl + v + int( 1 - 9) + int( 1 - 9 ) ---- pastes the copied item at the respective nested index
  
Modules required are:

    pyautogui    installation---->    pip install pyautogui
    
    pynput       installation---->    pip install pynput
    
setting up the programm.
    
press shift and right click on a file or folder and take a screen shot and crop the image for only "copy as path" in the right click       dropdown box and save the cropped image in the folder of copy_clipboard programm. Save al least 2 such images there with the names:
    
    Screenshot (1).png
    Screenshot (2).png
    
    DELETE the existing .png files in the folder (these are for example).
    
And the programm is ready for use.
