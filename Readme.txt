##################################
# This project is created by:-   #
# Shivanand Nalgire (IIT Bombay) #
##################################

The idea of the project is -
1) First we capture the background which is displayed when we have cloak on ourself. We capture the background images 50 times. (Higher the number, better will be the result)
2) Create a mask for cloak with HSV (Hue, Saturation and Value) for seperating the cloak part here by checking if there is any part from lower red to upper red.
3) We create the second mask for having everything except the cloak part using bitwise NOT.

Feel free to use and share this project for your application.
Thank you.