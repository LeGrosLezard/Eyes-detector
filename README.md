# Eyes-detector in progress

  Hello my name's Jb i've 25 years old, barely graduate of OpenClassrooms on web developpement, computer enthusiast I tried to make an eyes tracking.

Here we detect if the person gets up, bends down, backs up, looks up, down, right, left, also top right, top left, bottom ... if the person gets up or down we recalculate then the position; focus on the code. In order to do this we must take into account the position of the eyes on the x and y axis.



# --version 2--- In progress

# Initialization

First we need to pass an

![b-ConvertImage](https://user-images.githubusercontent.com/54853371/64929242-fb1dcd00-d823-11e9-98bf-3d8347006d32.jpg)

# The head position 

Second we need to verify thead position (personn moves to left or top or bot or right ?) for a re initialization. Indeed, the crop position isn't valid anymore in this case

![a-ConvertImage](https://user-images.githubusercontent.com/54853371/64929226-a5492500-d823-11e9-8222-0101e9da7395.jpg)













![dada](https://user-images.githubusercontent.com/54853371/64900015-a137ce80-d68e-11e9-91d6-7136854f8b1a.png)



# Concretely what is that for ? 

But that can serve more than anything else! Mr Hawkins, one of the most brilliant physicists of our century and Physic, needed it to be able to communicate. We were able to find out how a user could look at a web page for example and what information to put on such a site.

Did you know PNL ? it's a theory on the visual fields and the gaze associate to our things

![images](https://user-images.githubusercontent.com/54853371/64900590-3ab4af80-d692-11e9-9dd9-9b7df461077c.jpg)

For our personal project, use this to be able to say what a user thinks in conversation through this process

From my 17 years old i try and try to match Patrick Jane or Spencer Ried. SPOILER, beginner pay attention to what is said, may be strange.


# Library


# Architecture


# How it works ?

We take in the initialization the points of the detection of the eyes. 

We then make it by the average of the points previously recovered to make some crop cut areas. By this we avoid detection jumps

In these cut areas we try to make an automatic thresold that only detects the eye. the threshold converted the image is in black or white color according to a certain threshold it is this threshold that we try to detect automatically. we are satisfied once we have found an area of 1240.

Then we leave the eye with a findcontour and take the coordinates of the center of these areas


Then we take the position of these centers at each moment to know if the eye goes in one direction or not taking into account the movements of the head of the user by a face detection by haarcascade. (in course)


# How improve ?

Ia 

# Limit

Tt depends a lot on the threshold, the hair is a source of false detection, it depends on the detection of the eyes during initialization.




<br><br><br><br><br><br>

# ---Version 1--

At first we need to do an initialization who will calculate the position of the eyes

![uno](https://user-images.githubusercontent.com/54853371/64900188-c0832b80-d68f-11e9-820d-2dc774c932ab.png)

Secondly

![dadada-ConvertImage](https://user-images.githubusercontent.com/54853371/64900396-42c01f80-d691-11e9-90d2-63795ba31673.jpg)

<em>A fringe can change everything.... Did you know that appearance can increase your salary and the look of others? no ? https://myprofilmypollution.herokuapp.com</em>


![sa](https://user-images.githubusercontent.com/54853371/64900447-7b5ff900-d691-11e9-80d3-930fbe4172b5.png)




# Library

 Python 3.x
 
 pip
 
 python-opencv



# Architecture

A main.py file (where we lunch the program) who depends of image_processing.py. 

image_processing.py who dependance of haarcascade form the haar folder

# How improve ?

Ia 

# Limit

course this is a limit in case the personn is too agitated, all depend on a face detection. 

There are so many false detections. We need to put out the hair.

We cannot make for example the personn look up on the left.

