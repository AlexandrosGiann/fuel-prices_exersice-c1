# Fuel Prices - Exercise C1 for the Business Programming lectures

#### This is a part of the Business Programming exercise. The exercise is about working with fuel prices data and performing various operations on it.

## Project Structure

Currently, the exercise is structured as follows:
- main.py: The main script that contains the logic for processing fuel prices data. It also contains comments of code that I'm planning to reuse in the near future.
- Test scripts/fuelwide_test.py and Test scripts/openvan-camp_test.py: Test scripts to ensure the correctness of the code in main.py.
- GR_prices: The folder with the fuel prices JSON files.
- .gitignore: A file specifying which files and directories to ignore in the Git repository. GR_prices is currently ignored because it contains JSON files that are not necessary for the exercise.
- README.md: This file, providing an overview of the exercise, where I used AI, its updates and its structure. I put the updates section at the end of the README file to keep track of changes made to the exercise over time.

## Where I used AI:

I used Perplexity AI to find APIs that provide fuel prices data. This is where I found the FuelWide API. The OpenVan API was found by searching on the public-apis repository on GitHub.

## Updates

### Update 24/11/2026

I removed the process of saving the JSON files to disk, because I wanted to make the exercise more focused on the data processing part. I'm planning to recover the saving of JSON files, but for multiple sources. I also added a second source to take the fuel prices data from, which is the FuelWide API.
