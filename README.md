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
│    ├── app.py                   <- Demo app for accessing prediction results on GUI.
|    ├── df.csv                   <- Test dataset
|    ├── result.csv               <- Final results dataset with best 10 talents for each job available.
│    └── VanHack_main.ipynb       <- Jupyter Notebook file where the entire project resides. 

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
     Tree based algorithm, Light GBM was used to train the model and find Feature Importance. I chose LGB because it is fast, uses less   memory and is one of the best performing classification algorithms. 
   
   Since, the training data had only ~400 data points while, the test data has around ~100,000 data points the predicting power of the algorithm was not too good. Hence, to counter that I used the Feature importance from the trained model which was a very good predictor in predicting if a candidate would be hired or not. 
   
   The feature importance obtained from the model:
   ![Feature Importance](https://github.com/anishjoni/VanHackathon/raw/master/src/feature_imp.png)
  
 
4. **Pre-Process Test Data:**

   Test data is prepared by combining all available candidates with jobs for which best candidates must be selected for. Necessary features are added to the test data and a match score is calculated based on the weights from the model for the most important features.

5. **Results:**
   `Results.csv` contains top 10 predictions made for each job role that needs to be filled. As seen in feature importance, this prediction is made from the trained model with `position_match` being the most prominent feature in matching the candidate to the job followed by `common_skills_ratio` and `other_skills_ration`.
   
   The best way to view the results is through the streamlit app that I created with the results that allows you to select any of the available jobs in the market and shows the top 10 candidates matching the role based on the match score as you can see below:
   ![Top 10 Candidates](https://github.com/anishjoni/VanHackathon/raw/master/src/top_10_talent.png)
   
6. **Area of Improvements:**
                   - Collecting data of Candidates who were not selected for specific roles after applying for them would help make the training more accurate.

  - Increasing the number of data points in the training dataset.
  - Creating categories/buckets for Candidate positions to reduce redundancies of position names

