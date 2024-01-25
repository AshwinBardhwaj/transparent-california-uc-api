# Transparent California API

A REST api that retrieves salary and occupation data for all UC employees using information retrieved in 2022.

In 1968, California passed the California Public Records Act (CPRA) which required government records to be made public.
Naturally, this includes all employees of the Univeristy of California system.

## How It Works

To collect data from the [Transparent California](https://transparentcalifornia.com/) website, a web scraper iterated over the pages to retrieve 
the data of each UC Employee.
This data was then compiled into a CSV and SQL database. Cleaning was preformed for the data for missing entires and incorrect inputs.
The api was created over the Django REST framework.
