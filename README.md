# 1DParticleFilter
This repository contains source codes and a Jupyter Notebook tutorial for 1 dimensional particle filter for estimating or tracking. 

**Best way is to download the Jupyter Notebook to see the tutorial**

The tutorial estimates the system below:

    "\n",
    "$$x_{k+1} = f [ k , x_k , v_k ] = 2 \\operatorname { atan } [ x_k ] + 0.5 * \\cos ( \\pi k / 3 ) + v_k$$\n",
    "\n",
    "$$z_k = h [ k , x_k ] + w_k = x_k + x_k ^ { 2 } + x_k ^ { 3 } + w_k$$\n",
    "\n",
    "$$E \\{ v_k \\} = 0 , E \\{ v_k v_j \\} = \\delta _ { j k } Q_k\\ where\\ Q_k = 1$$\n",
    "\n",
    "$$E \\{ w_k \\} = 0 , E \\{ w_k w_j \\} = \\delta _ { j k } R_k\\ where\\ R_k= 0.25$$\n",
    "\n",
    "$$\\quad \\hat { x }_0 = 4 , P_0 = 2$$\n",
    "\n",
    
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


