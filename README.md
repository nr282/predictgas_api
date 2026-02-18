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

## Why are Spectral Technologies' Forecasts better? 

Spectral Technologies discovered and solved the "Weather Aggregation" problem, making our techniques/forecasts significantly better

The "Weather Aggregation Problem" is the observation that many hedge fund anlaysts aggregate (a) daily weather to a monthly value by taking the average of daily weather data. This reduces the amount of information in the dataset by a factor of 1/30. Hence the aggregating the weather data throws out 97% of the information that is contained in the weather dataset. Often hedge funds will spend between 50k-100k per annum to acquire the weather dataset, only to then toss out not less than 97% of the information by taking the average. This is equivalent to wasting between 0.97 * 50k = 48.5k to 0.97 * 100k = 97k for no reason outside of just having slopping not well thought out theory. 

## PredictGas ROI 

PredictGas saves the Natural Gas Trader on average 50k as PredictGas increases informational efficiency.






























