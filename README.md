# Project Traffic

Predict the impact a traffic accident will have on traffic flow.

### Project Description

There are hundreds of thousands of vehicle accidents in Texas and California, some traffic incidents have greater impacts on traffic flow than others. Many factors may contribute to the impact a traffic accident may have on traffic flow to include specific locations, features of the road, and/or weather conditions. If the impact of traffic accidents can be predictable based on these features then local authorities may have a better idea on where to place emergency resources and how to plan road renovations.

### Project Goal

* Discover what drives the impact on traffic flow from accidents
* Use drivers to develop a machine learning model to predict severity
* This information could be used to further our understanding of traffic flow

### Initial Thoughts

My initial hypothesis is that drivers of severity will be most strongly associated with zip codes and weather conditions.

## The Plan

* Acquire data from kaggle.com
  * Create a dataframe from the csv I downloaded from kaggle.com
* Prepare data
  * Create Engineered columns from existing data
  * Get rid of columns that probably don't have significant impact on severity
  * Dealt with null values
* Explore data in search of drivers of severity
  * Answer the following initial questions
    * Is there a correlation between temperature and severity?
    * Is there a correlation pressure and severity?
    * Is there a correlation between windspeed and severity?
    * Is there a correlation between severity between duration?
* Develop a Model to predict property value
  * Use drivers identified in explore to help build predictive models of different types
  * Evaluate models on train and validate data
  * Select the best model based on $RMSE$ and $R^2$
  * Evaluate the best model on test data
* Draw conclusions

## Data Dictionary

| Original                     | Feature        | Definition                                              |
| :--------------------------- | :---------     | :------------------------------------------------------ |
| ID                           | Identification | This is a unique identifier of the accident record.     |
| Source                       | Source         | Source of raw accident data                             |
| Severity (Target)            | severity rank  | Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay: 1)|        
| temp                         | °F             |  Outdoor Temperature for during the accident| 
| humidity                     | %              | Value of Relative Humidity for the during the accident|
| wind_direction               | ° Compass      | The average (arithmetic mean) value of Wind Direction for the accident|
| wind_speed                   | mi/h           | value of Wind Speed during the accident| 
| month                        | Month          | The month of the accident took place|
| temp_mean                    | °F             | The value of Outdoor Temperature for the day|
| humidity_mean                | %              | The value of Relative Humidity for the day|
| wind_direction_mean          | ° Compass      | The value of Wind Direction for the day |
| wind_speed_mean              | Knots          | The value of Wind Speed for the day|
| month                        | Month          | The month of the the accident occurred represented by 1-12|                
| city                         | City           | City in which the accident occurred|                 
| county                       | County         | County in which accident occurred|         
| state                        | State          | State in which accident occurred|                   
| zipcode                      | Zipcode        | Zipcode in which accident occurred|               
| pressure                     | Atm            | barometric pressure in weather at the time of the accident|                  
| visibility                   | Mi             | miles of visibility|              
| weather_condition            | Weather condition | general weather condition|                   
| sunrise_sunset               | Night/Day      | day or nich |                
| day_of_week                  | Day of the week | day of week 0=sunday, 6=Saturday |                 
| season                       | Season of accident | Winter, Spring, Summer, Fall |             
| duration                     | minuts/hours of accidents | how long the traffic flow was impacted|  

## Steps to Reproduce

1) Clone this repo
2) If you have access to kaggle datesets:
   - Save dataset
   - Run notebook
3) If you don't have access:
   - Request access from Codeup
   - Do step 2

# Conclusions


### Takeaways and Key Findings
- Individual features may have a relationsip with severity but non strong enough to act as strong indicators

### Recommendations and Next Steps
- If environmental factors don't play a significant role in severity, I think that classification features such as location, terrain, and road features would act as great indicators so would be worth exploring.