import pandas as pd

# Data for Chat outcomes
chat_data = {
    "Example": ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3", "EXAMPLE 4", "EXAMPLE 5",
                "EXAMPLE 6", "EXAMPLE 7", "EXAMPLE 8", "EXAMPLE 9", "EXAMPLE 10"],
    "Total Score": [42.66, 45.00, 50.00, 43.66, 39.17, 40.66, 44.17, 42.67, 42.17, 43.50]
}

# Data for Gemini outcomes
gemini_data = {
    "Example": ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3", "EXAMPLE 4", "EXAMPLE 5",
                "EXAMPLE 6", "EXAMPLE 7", "EXAMPLE 8", "EXAMPLE 9", "EXAMPLE 10"],
    "Total Score": [45.17, 45.66, 40.34, 36.33, 47, 38.83, 45.16, 32.01, 39.17, 43.67]
}

# Convert data to DataFrames
chat_df = pd.DataFrame(chat_data)
gemini_df = pd.DataFrame(gemini_data)

# Calculate descriptive statistics for Chat outcomes
chat_desc_stats = chat_df["Total Score"].describe()

# Calculate descriptive statistics for Gemini outcomes
gemini_desc_stats = gemini_df["Total Score"].describe()

# Perform a t-test to compare the means of Chat and Gemini outcomes
from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(chat_df["Total Score"], gemini_df["Total Score"])

# Display the results
print("Descriptive Statistics for Chat Outcomes:")
print(chat_desc_stats)
print("\nDescriptive Statistics for Gemini Outcomes:")
print(gemini_desc_stats)
print("\nT-test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
