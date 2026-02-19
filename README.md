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

Spectral Technologies discovered and solved the "Weather Aggregation" problem, making our techniques/forecasts significantly better. The theory that allowed us to solve said problem is attached in the white paper called: "Residential Commercial Modelling of Natural Gas Consumption"

Futhermore, Spectral Technologies leverages our own FDTT technology to solve critical issues at the intersection of (1) daily and (2) monthly frequency data. Code to FDTT can be found here: https://github.com/nr282/FDTT

## PredictGas ROI 

PredictGas leverages weather data much more effectively.



































