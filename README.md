# DSCI560-hw2
## DSCI 560 Data Science Practicum-Homework 2
The purpose of this homework is to get your familiar with FigShare, GitHub, Zenodo, and Jupyter Notebook for 
sharing data science projects and results according to the principles set forth in the Scientific Paper of the Future. 
Three scripts are 
#### random1000.py
generate 1000 random numbers over range 0-100. 
Result can be found at https://figshare.com/articles/dataset/random_x_csv/12981176

#### generatey.py
generate new numbers from the original 1000 using the equation y=3x+6.
Result can be found at https://figshare.com/articles/dataset/output_y_csv/12981173

#### visualization.py
visualize the result. 
Result can be found at https://figshare.com/articles/figure/plot_x_y_png/12981179


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4041266.svg)](https://doi.org/10.5281/zenodo.4041266)

### Instructions to create a virtual environment for the project and run it on your computer

1. Copy this github URL and clone to local repository by executing in command line:  
    `git clone https://github.com/YiLisa/DSCI560-hw2.git`
2. If not already installed, do pip installation of virtualenv package. In command line run:  
    `pip install virtualenv`
3. Go to project folder (DSCI560-hw2) and create new empty environment named dsci560H4 by running:   
On macOS and Linux: `python3 -m venv dsci560H4`  
On Windows: `py -m venv dsci560H4`  
you can changing the last word of the command to name yout environment as you want  
4. Activate the new enviornment by running:  
On Windows:
    `.\dsci560H4\Script\activate`   
On macOS and Linux:
    `source dsci560H4/bin/activate`     
5. Install dependencies by running:  
    `pip install -r requirements.txt`
6. Execute the python scripts by executing in command line:  
    ```
    python random1000.py
    python generatey.py
    python visualization.py
    ```
7. You should get a result as the screenshot shown:
    

You can also execute the HW2 notebook in Binder by clicking the badge:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/YiLisa/DSCI560-hw2/master?filepath=HW2.ipynb)
