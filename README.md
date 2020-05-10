# Project: Churn Fortuneteller - machine learning model to predict customer churn.


**Summary**
The Telecommunication industry mostly depends on subscription-based services. The profitability of the Organization mainly depends on its market share or its customer base. The customer acquisition and retention are two important factors that will directly impact the organization’s profitability [2]. 
Churn rates depict the rate at which customer base shrink over a measured period and are often used to indicate the strength of a company’s customer service division and its overall growth prospects. Lower churn rates suggest a company is in a stronger and competitive state. Customer loss impacts carriers significantly as they often make a significant investment to acquire customers. The ability to identify customers who will abandon services, while there is still time to do something about it, represents a huge additional potential revenue source for every online business. Furthermore, it is always more difficult and expensive to acquire a new customer than it is to retain a current paying customer.
Achieving right balance between customer acquisition and retention is not easy task. Statistics suggests that acquiring new customer is 5 times costlier than retaining the customer. Due to this, many companies are spending hugely to identify those customers who are likely to churn and taking the necessary steps to retain them and reduce the churn rate. Therefore, this project's aim to finding vital factors that increase customer churn is important to take necessary actions to reduce this churn.

**Objective**




Our team aims to create an efficient and accurate algorithm to identify the most prominent reasons for customer churn. The algorithm considers many factors such as customer's demographic, subscribed services and usage details. The prediction model assists the Telecom company to predict their customers who are more likely stop using their services. The prediction model developed in this work uses machine learning technique.

Building a machine learning model using the past customer churn data and their characteristics & behavior. The customer churn prediction model which assists telecom operators to predict customers who are most likely subject to churn based on various attributes related to demographics of customer, facilities offered, customer tenure and their charges. This machine learning project embodied in advanced analytics that leverage the existing customer's data to reveal hidden patterns and new insights that will enable the business users to take better decisions.

The supervised tree-based machine learning model will predict the response for existing customers. Upon completion of data analysis and feature engineering using if-else rules, we build tree-based machine learning methods and algorithms for predicting the customer churn. We have analyzed and implemented the Random Forest and Extreme Gradient Boost (XGBoost) tree-based models to build the predictive model. 

We used the IBM telecom dataset available from [kaggle.com](https://www.kaggle.com/blastchar/telco-customer-churn). The raw data contained 7043 rows (customers) and 21 columns (features). 


**Method**
Develope accurate and effective predictive model using machine learning techniques to predict the customer churn well in advance. Refer the details below.

Supervised Machine Learning Models Implemented in Churn Fortuneteller
•	Random Forest Classifier (bagging) – Sum of individual decision trees and averaging over independent subsets of data (sampled with replacement)
•	XGBoost Classifier (boosting) - Each decision tree learns from errors from previous learners which are assigned higher weights, sequential learners, optimization over error function
•	Chosen Model: Random Forest (Lower false negatives, higher F1-score and accuracy)
Random Search Optimization 
•	Begin by selecting certain hyperparameter search space
•	Randomness or probability (typically in the form of a pseudorandom number generator) in its methodology. 
•	The random element may be introduced through sampling specifications of the algorithm, or through noise in the function observation
•	Finally, the outcome is given by optimal result for a given hyperparameter of a model to maximize it’s predictive power
•	Randomized Search Cross-Validation (CV) API in python scikit learn
Unsupervised K-Means Clustering
•	Initialize k number of clusters and initial centroids randomly assigned
•	Each instances assigned to nearest centroid which varies but eventually converges 
•	Euclidean distance used to measure and keep track of each dataset instance to shifting nearest centroids

**Solutions To Reduce Churn Rate**
Acquiring a customer is far more costly than keeping a customer. Any company that wants to retain its customers should find some value in analysing and lowering down the churn rate. Even emerging markets, which witnessed high growth in the past, are now looking to consolidate their customer base and differentiate themselves from their peers to reduce churn rates.

Telecom players use a variety of different metrics to determine when customers are about to leave. It is profitable for companies to explore the reasons why customers are leaving, and then target at risk customers with enticing offers. There are several different tactics companies use to maintain their customer bases [1]
- One of the most important is simply providing efficient customer service. Providing clients with an easy way to get questions answered and issues handled is the key to maintaining cellular clients.

- Value- added services serve as a subscriber retention tool, especially for established players. While for newer entrants, it will become a part of the marketing strategy to attract customers. If VAS providers leverage the opportunities to tie up with operators, there could be a major increase in the uptake of their services.

- Offer upgrades on the client’s existing account. Expanding on services offered and giving better rates or discounts to the client often improves customer retention rates.

- Another tactic is offering free access or reduced rates on smartphone applications. The increasing regular use by customers of cell-phone applications makes free access to such applications an enticing bonus for many customers.

- Competing cellular providers aggressively market special deals to churn customers away from their current provider. Common practices include offering free phones and buying out any existing service contract. The cellular service business is highly competitive and will likely remain so; therefore, churn rates will continue to be an important focus for cellular providers.

- Fighting wireless churn with trendy smartphones and fast data network

- One-on-one marketing campaigns is one of the best tactics to reduce churn rate. Make sure that customers are communicated the new services offering based on their usage analysis and trends and should be given proactive information on the plans which will benefit the customer.
