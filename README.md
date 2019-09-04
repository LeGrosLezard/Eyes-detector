# Eyes-detector

<em>status: <strong>need a code review and translation</strong></em><br><br>


Computer vision/haarcascade

<em>here is a project where we can detect eyes and know their movements</em>

We propose to do an initialization or we detect the eyes of the person. We fill a list of the top 50 positions. Then we propose to say where the eyes move. For this we perform an average of the initialization and check the position by contribution to this average. If the person goes down, or heads up, we do a new initialization.




VIDEO qui montre




CV2 -> pip install opencv-python (real time image processing)

numpy -> pip install numpy (make array object)






Explication
