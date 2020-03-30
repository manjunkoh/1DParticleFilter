# 1DParticleFilter
This repository contains source codes and a Jupyter Notebook tutorial for 1 dimensional particle filter for estimating or tracking. 

The tutorial estimates the system below:

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%24%24x_%7Bk&plus;1%7D%20%3D%20f%20%5B%20k%20%2C%20x_k%20%2C%20v_k%20%5D%20%3D%202%20%5Coperatorname%20%7B%20atan%20%7D%20%5B%20x_k%20%5D%20&plus;%200.5%20*%20%5Ccos%20%28%20%5Cpi%20k%20/%203%20%29%20&plus;%20v_k%24%24%5C%5C%20%24%24z_k%20%3D%20h%20%5B%20k%20%2C%20x_k%20%5D%20&plus;%20w_k%20%3D%20x_k%20&plus;%20x_k%20%5E%20%7B%202%20%7D%20&plus;%20x_k%20%5E%20%7B%203%20%7D%20&plus;%20w_k%24%24%5C%5C%20%24%24E%20%5C%7B%20v_k%20%5C%7D%20%3D%200%20%2C%20E%20%5C%7B%20v_k%20v_j%20%5C%7D%20%3D%20%5Cdelta%20_%20%7B%20j%20k%20%7D%20Q_k%5C%20where%5C%20Q_k%20%3D%201%24%24%5C%5C%20%24%24E%20%5C%7B%20w_k%20%5C%7D%20%3D%200%20%2C%20E%20%5C%7B%20w_k%20w_j%20%5C%7D%20%3D%20%5Cdelta%20_%20%7B%20j%20k%20%7D%20R_k%5C%20where%5C%20R_k%3D%200.25%24%24%5C%5C%20%24%24%5Cquad%20%5Chat%20%7B%20x%20%7D_0%20%3D%204%20%2C%20P_0%20%3D%202%24%24)

I got this example from a class taught by Dr. Psiaki. But one can solve other 1D systems they want and modifying in the source codes. The prerequisites to fully understand this document Bayesian Statistics and Kalman Filter.  

NOTE: The tutorial is currently unfinished because the latter part needs to be more polished (classic botching the end to submit the project on time). May or may not add some about Kalman Filter as well. <br/>
Also there is an issue where some of the Latex-formatted equations are not rendering properly and pictures aren't showing on github, so I highly recommend running on your local jupyer notebook if you have it.    

# Acknowledgement 
I would like to thank Drs. Heng Xiao and Mark L. Psiaki for allowing me to take their courses as an undergrad; it led me to have a passion for this field and dothis semester project. <br/>
I would also like to thank my good friend Matt Marti for the guidance along the way. 

To Wi, 

Feels like yesterday when we talked about this at Sharkey's about how you were very excited to see this project finish. I will regret forever not finishing sooner. <br/>
To so many people you brought happiness beyond measure, colors we didn't see before, and personality warmer than a fireplace on rainy days. <br/>
Your kind spirit will echo through all of us in eternity. <br/>
Fly high brother. 


