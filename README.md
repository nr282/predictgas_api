# PredictGas API

PredictGas API aims to predict Natural Gas Consumption State By State using (1) professional grade weather data and (2) our own mathematical, scientific theory developed for the prediction of Natural Gas Consumption. 

 A Historical Benchmark achieves around a 9% prediction error on unseen Natural Gas Consumption reports. The Benchmark is discussed and laid out in the white paper.
 
 Our API has a 4% prediction error. Our claim is that we have 9% - 4% = 5% skill. 

 This is likely more competetive in accuracy than the competitors 

# API Documentation

The API simply calculates Residential Consumption of Natural Gas on a state-by-state basis from start date to end date. Start and End Date can found in the code. The API returns Spectral Technologies's best estimate for a particular date.

If the date is in the past, best estimate will use EIA data and historical weather data. If the date is in the near future, the best estimate will use near term weather forecast. If it is in the far future, it will use average historical weather data in combination with 
any methodology to increase accuracy for that day's weather forecast. 



The API returns values in the MMCF. The API is based around: (1) a professional weather data provider and (2) EIA Natural Gas Consumption Reports found for example here for California: 
https://www.eia.gov/dnav/ng/hist/n3010ca2M.htm

# Feature Requests

## Use Fast Disaggregation in Time Technology (FDTT). Creation of a daily model. 

Currently, $\alpha_{u}(t)$ the sensitivity to weather is time-dependent, where the $u$ represents uniform. It is constructed as a monthly function, ie $\alpha_{u}(t) = \alpha_{m}$, where $m = 1...12$. This leads to the situation where the sensitivity is not smooth in time, this represents a uniform disaggregation in time. This leads us the desire to smooth $\alpha_{u}(t)$ using another of Spectral Technologies' technology FDTT. FDTT can be viewed as a mathematical functional $u_{c}(t) = FDTT(\alpha_{u}(t))$. Using $u_{c}(t)$ will be useful in cleaning up and improving the calculation. 

Empirically, I expect to clean up the results significantly. There is a 2X variation found in $\alpha_{u}(t)$
##























