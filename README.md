# Sentiment Analysis Command Line Tool
### IDS706 Project Number 3: this project is a combination of threes together
* Project #7: Create Data Engineering Command-line Tool [General]
* Project #9: Publish Python Command-line Tool or Library to Python Package Repository [Advanced]

### Goal:
* Evaluate whether a sentence entered by the user is positive or negative.

### Dataset:
* Goodreads book review (3GB)
* Source: https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/reviews
* Credit to:
  * Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.  [bibtex]
  * Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19. [bibtex]

### Pipeline
![image](https://user-images.githubusercontent.com/43796329/137572854-21320154-8d6c-4c68-835c-c7f3977970cd.png)

### Project Replication Instruction:
* Data Generation:
 * Go to source link above download and unzip data
 * Move the json into the data folder.
 * Run the Dataset Truncate.ipynb notebook to generate smaller datasets (runtime: 20 minutes)
 * Warnings! Do not push datasets to GitHub!
