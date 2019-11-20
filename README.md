# VanHackathon 2019
### Prediction of best talent for available jobs at VanHack Community.

**Business Scenario:** Finding the best candidates for a job is a really hard task and demands a lot of time from the recruiters because each candidate must be evaluated manually. VanHack has over 100,000 candidates in our platform, and it is quite impossible to assess each candidate individually. With this in mind, they are looking for a way to determine which candidates have the highest chance of getting hired. Vanhack already has its own matching algorithm that makes matching easier, but they are looking for a more accurate solution that will ultimately result in more hires. 

**Problem:**

**Methodology:**

1. Prepare Data
2. Build Features
3. Train ML Models
4. Pre-Process Test Data
5. Results

 **Project File Structure** :
```
├── README.md                    <- The top-level README for developers using this project.
├── data
│    ├── AvailableCandidates.csv <- All available candidates data(To.   
│    ├── HiredCandidates.csv     <- All hired candidated data.
│    ├── HiredJobDetails.csv     <- All hired jobs data.
│    └── JobsToPredict.csv       <- Data of jobs to predict candidates for.
│
├── src
│    ├── VanHack_main.ipynb       <- Jupyter Notebook file where the entire project resides. 
│    └── app.py                   <- Streamlit app for accessing prediction results on GUI app.

```
1. **Prepare Data:**

   Training data - Prepared hired dataset from hired candidates and jobs data to learn the features of candidates and jobs that leads to getting hired. 

   In order to accommodate for the missing data of candidates who were not hired, a random sample of available candidates(AvailableCandidates.csv) matching the number of hired candidates was used as proxy for users who were likely not hired. A random sample from 10,000 candidates was chosen to minimize selection bias and skewness in data.

2. **Build Features:**

   The following features were built to give the model more features to learn from:

   position_match - Similarity between Job position and Candidate position

   common_skills - Skills common to the Job requirement and Candidate skillset

   common_skills_no - # Skills common to the Job requirement and Candidate skillset

   common_skills_ratio - # common_skills_no/ # Skills in Job requirement

   other_skills_ratio - # other skills/ # Candidate skills

   

3. **Train ML Models:**

   Tree based algorithm, Light GBM was used to train the model and find Feature Importance

4. **Pre-Process Test Data:**

   Test data id prepared by combining all available candidates with the jobs for which best candidates must be selected for. Necessary features are added to the test data

5. **Results:**

6. **Area of Improvements:**
