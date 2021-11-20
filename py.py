from os import stat
import random
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import statistics

df = pd.read_csv("Stud.csv")

#Lists

gender_list = df["gender"].to_list()
race_list = df["race/ethnicity"].to_list()
pEducation_list = df["parental level of education"].to_list()
lunch_list = df["lunch"].to_list()
tPC_list = df["test preparation course"].to_list()
mathScore_list = df["math score"].to_list()
readingScore_list = df["reading score"].to_list()
writingScore_list = df["writing score"].to_list()

#mean for data.

gender_mean = statistics.mean(gender_list)
race_mean = statistics.mean(race_list)
pEducation_mean = statistics.mean(pEducation_list)
lunch_mean = statistics.mean(lunch_list)
tPC_mean = statistics.mean(tPC_list)
mathScore_mean = statistics.mean(mathScore_list)
readingScore_mean = statistics.mean(readingScore_list)
writingScore_mean = statistics.mean(writingScore_list)
print("Mean of the stats in the data".format(gender_mean, race_mean, pEducation_mean, lunch_mean, tPC_mean, mathScore_mean, readingScore_mean, writingScore_mean))
print(gender_mean, race_mean, pEducation_mean, lunch_mean, tPC_mean, mathScore_mean, readingScore_mean, writingScore_mean)

#median for data.

gender_median = statistics.median(gender_list)
race_median = statistics.median(race_list)
pEducation_median = statistics.median(pEducation_list)
lunch_median = statistics.median(lunch_list)
tPC_median = statistics.median(tPC_list)
mathScore_median = statistics.median(mathScore_list)
readingScore_median = statistics.median(readingScore_list)
writingScore_median = statistics.median(writingScore_list)
print("Median of the stats in the data".format(gender_mean, race_mean, pEducation_mean, lunch_mean, tPC_mean, mathScore_mean, readingScore_mean, writingScore_mean))
print(gender_median, race_median, pEducation_median, lunch_median, tPC_median, mathScore_median, readingScore_median, writingScore_median)

#mode for data.

gender_mode = statistics.mode(gender_list)
race_mode = statistics.mode(race_list)
pEducation_mode = statistics.mode(pEducation_list)
lunch_mode = statistics.mode(lunch_list)
tPC_mode = statistics.mode(tPC_list)
mathScore_mode = statistics.mode(mathScore_list)
readingScore_mode = statistics.mode(readingScore_list)
writingScore_mode = statistics.mode(writingScore_list)
print("Mode of the stats in the data".format(gender_mean, race_mean, pEducation_mean, lunch_mean, tPC_mean, mathScore_mean, readingScore_mean, writingScore_mean))
print(gender_mode, race_mode, pEducation_mode, lunch_mode, tPC_mode, mathScore_mode, readingScore_mode, writingScore_mode)

fig = ff.create_distplot([mathScore_mean], ["Math Grades"], show_hist=False)
fig.show()