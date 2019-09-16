# Eyes-detector

  Hello my name's Jb i've 25 years old, barely graduate of OpenClassrooms on web developpement, computer enthusiast I tried to make an eyes tracking.

Here we detect if the person gets up, bends down, backs up, looks up, down, right, left, also top right, top left, bottom ... if the person gets up or down we recalculate then the position; focus on the code. In order to do this we must take into account the position of the eyes on the x and y axis.


# How it works ?

We can detect the position of the eyes and we make a threshold in this region that we put in a loop, 
that we automatically adjust until the detection of an air that we hope is our eye. Then we return each position in a list, a container.

We then compare the current position with the old position. 

This is sensitive to false detections. We do this on the x and y axis.

In addition, we check that both eyes have detected this and we display a message (reduce false detection). 

We also make a list of the position of the head and check his position at each moment to deduce a possible movement 

(for example a verbal slap (head movement right or left) but it will be in another program, verbal evasion(for a bot movement or right or left ect...), emotional heaviness(for a bot movement) or a bloating.)


<br><br>
# --version 2---


# The head position 

Here we detecte head movement who hasnt effect on the position of eyes.

![a-ConvertImage](https://user-images.githubusercontent.com/54853371/64929226-a5492500-d823-11e9-8222-0101e9da7395.jpg)

We recover at every moment the detection of the head. We thus compare the position of a second ago that is t -1 with the current position t. <em>Note that the use of the notion t allows us to give a scientific dimension</em>


# Eyes detection

![c](https://user-images.githubusercontent.com/54853371/64973475-5fd03a80-d8ab-11e9-92d8-7451f364d452.png)

Now we apply a gray filter (we render the image with only one channel, there is blue and green red, we render 3 channels to one) then a blurring of our two eyes averaging areas . In addition we apply a threshold filter. We are binarizing the image. We make the pixels either white or black according to a threshold. In order to determine this threshold, we make a loop which at the detection of an area stops the automation because we our eye become black then.

In the case where we only detect one eye we apply the same threshold as the other, if we do not find any of the two eyes we start again the last process


# In FINE

We take center of our area and compare it with last data (placed in list). Course it could detect the return of the eye.


# LIMIT

distance beetween user and camera, hairs or something who can delete a good detection of eyes, size of the file and time loop execution... (in course)



# Concretely what is that for ? 

But that can serve more than anything else! Mr Hawkins, one of the most brilliant physicists of our century and Physic, needed it to be able to communicate. We were able to find out how a user could look at a web page for example and what information to put on such a site.

Did you know PNL ? it's a theory on the visual fields and the gaze associate to our things

![images](https://user-images.githubusercontent.com/54853371/64900590-3ab4af80-d692-11e9-9dd9-9b7df461077c.jpg)

<strong>VC</strong> Visual built
<strong>VR</strong> visual rememor
<strong>AC</strong> auditive built
<strong>AR</strong> auditory  recalled
<strong>K</strong> knesthetic
<strong>id</strong> Internal dialogue

<em>well on a theory can be built and deconstructed, CARE left is right for our views</em>

For our personal project, use this to be able to say what a user thinks in conversation through this process. imagine that everyone can understand each other and that there is no quiproco, that there is no more secret, that acceptable taboo today becomes understandable (taboo of the kind why I have curly and not smooth hair).


From my 17 years old i try and try to match Patrick Jane or Spencer Ried. SPOILER, beginner pay attention to what is said, may be strange.




# Library

 Python 3.x
 
 pip
 
 python-opencv

# Architecture

A main file .py composed by:

- eyes function (detecting eyes)

- automatic tresh function (ajusting threshold)

- center_detection function (detecting center of area detected by automatic tresh)

- head_movement function (detecting movement of head)

- dectetion_message (if right and left eye have the same position display a message)

- video_capture (lunching video capture (camera) and all functions)








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

