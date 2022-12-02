# Clean the environment, set up the working directory:
rm(list=ls())
setwd("~/Desktop/Autumn 2022/I2P/Charts/hate_crime")

# Load library
library(tidyverse)

# Load data
df <- read_csv("hate_crime.csv")

unique(df$BIAS_DESC)

disability <- df %>%
  filter(grepl("Anti-Mental Disability", BIAS_DESC) | 
           grepl("Anti-Physical Disability", BIAS_DESC))

mental <- df %>%
  filter(grepl("Anti-Mental Disability", BIAS_DESC))

physical <- df %>%
  filter(grepl("Anti-Physical Disability", BIAS_DESC))


unique(disability$BIAS_DESC)
unique(disability$OFFENSE_NAME)
unique(disability$VICTIM_COUNT)
unique(disability$VICTIM_TYPES)

disability.groupby(['STATE_ABBR'])['VICTIM_COUNT'].count()

# Export dataframe as csv file

write.csv(disability,"~/Desktop/Autumn 2022/I2P/Charts/hate_crime/disability.csv", row.names = TRUE)

write.csv(mental,"~/Desktop/Autumn 2022/I2P/Charts/hate_crime/mental.csv", row.names = TRUE)

write.csv(physical,"~/Desktop/Autumn 2022/I2P/Charts/hate_crime/physical.csv", row.names = TRUE)