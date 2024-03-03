# Assignment

Group:

- Magnus
- Peter
- Yusuf

## Questions

- Which machine learning methods did you choose to apply in the application?

In Supervised Learning, we used **Random Forest Classifier**, **Bernoulli Naive Bayes** and **Voting Classifier**

In Unsupervised Learning, we used **K-Means**

- How accurate is your solution of prediction?

Our highest accuracy was Random Forest Classifier with an accuracy of between 85,5% and 88%

Closely followed by Voting Classifer of 84 to 85% and 80,95% for Naive Bayes

- Which are the most decisive factors for quitting a job?

The highest correlation we found was OverTime_Yes (24,6%), MaritalStatus_Single (17,54%), JobRole_Sales Representative (15,72%) and BusinessTravel_Travel_Frequently (11,51%) which all had a correlation of over 10%

- Which work positions and departments are in higher risk of losing employees?

| Department             | Quitting Rate | Percentage |
| ---------------------- | ------------- | ---------- |
| Human Resources        | 12/63         | (19.05%)   |
| Research & Development | 133/961       | (13.84%)   |
| Sales                  | 92/446        | (20.63%)   |

| JobRole                   | Quitting Rate | Percentage |
| ------------------------- | ------------- | ---------- |
| Healthcare Representative | 9/131         | (6.87%)    |
| Human Resources           | 12/52         | (23.08%)   |
| Laboratory Technician     | 62/259        | (23.94%)   |
| Manager                   | 5/102         | (4.90%)    |
| Manufacturing Director    | 10/145        | (6.90%)    |
| Research Director         | 2/80          | (2.50%)    |
| Research Scientist        | 47/292        | (16.10%)   |
| Sales Executive           | 57/326        | (17.48%)   |
| Sales Representative      | 33/83         | (39.76%)   |

- Are employees of different gender paid equally in all departments?

| Department             | Gender | MonthlyIncome |
| ---------------------- | ------ | ------------- |
| Human Resources        | Female | 7264.000000   |
| Human Resources        | Male   | 6371.023256   |
| Research & Development | Female | 6513.691293   |
| Research & Development | Male   | 6129.888316   |
| Sales                  | Female | 6972.126984   |
| Sales                  | Male   | 6949.645914   |

- Do the family status and the distance from work influence the work-life balance?

We weren't entirely sure what the question was asking, so we decided to check for the correlation between the variables.

| Variable               | Correlation to WorkLifeBalance |
| ---------------------- | ------------------------------ |
| MaritalStatus_Single   | 0.014921                       |
| MaritalStatus_Married  | -0.006388                      |
| MaritalStatus_Divorced | -0.009080                      |
| DistanceFromHome       | -0.026556                      |

- Does education make people happy (satisfied from the work)?

As we can see from the tables below, the higher the education, the lower the job satisfaction, and the same can be seen as the job satisfaction increases, the education decreases.

Which might be because the higher the education, the person might have higher expectations for the job, and therefore be less satisfied with the job.

| Education | JobSatisfaction |
| --------- | --------------- |
| 1         | 2.800000        |
| 2         | 2.769504        |
| 3         | 2.652098        |
| 4         | 2.786432        |
| 5         | 2.666667        |

| JobSatisfaction | Education |
| --------------- | --------- |
| 1               | 2.944637  |
| 2               | 2.896429  |
| 3               | 2.914027  |
| 4               | 2.901961  |

- Which were the challenges in the project development?

When making the unsupervised models a bad result was returned. This caused confusion since a better result was expected, but after having spent time looking at both the input data and the output, a conclusion was made that the data just didn't fit the type of model. There was also the challenge of setting up the Streamlit application as it is a new library for the team. This required some experimenting which ultimately led to a better understanding of BI application development.
