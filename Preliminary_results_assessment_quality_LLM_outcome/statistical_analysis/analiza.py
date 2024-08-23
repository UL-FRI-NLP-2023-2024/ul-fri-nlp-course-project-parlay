import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Your data
chat_scores = [37.99, 42.50, 44.00, 48.95, 45.00, 50.00, 46.00, 43.03, 44.80, 44.00]
gemini_scores = [37.66, 39.54, 41.00, 49.50, 43.75, 48.00, 45.42, 42.75, 42.00, 42.75]

# Create DataFrame
df = pd.DataFrame({
    'Chat Scores': chat_scores,
    'Gemini Scores': gemini_scores
})

# Descriptive Statistics
descriptive_stats = df.describe()

# T-test
t_stat, p_value = ttest_ind(chat_scores, gemini_scores)

# Add T-test results to a DataFrame
t_test_results = pd.DataFrame({
    't-statistic': [t_stat],
    'p-value': [p_value]
})

# Save to Excel
with pd.ExcelWriter('Chat_Gemini_Analysis.xlsx') as writer:
    df.to_excel(writer, sheet_name='Scores', index=False)
    descriptive_stats.to_excel(writer, sheet_name='Descriptive Statistics')
    t_test_results.to_excel(writer, sheet_name='T-test Results')

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot([chat_scores, gemini_scores], labels=['Chat Scores', 'Gemini Scores'])
plt.title('Box Plot of Scores')

plt.subplot(1, 2, 2)
plt.hist(chat_scores, alpha=0.5, label='Chat Scores', bins=5)
plt.hist(gemini_scores, alpha=0.5, label='Gemini Scores', bins=5)
plt.title('Histogram of Scores')
plt.legend()

plt.tight_layout()
plt.savefig('Chat_Gemini_Analysis.png')
plt.show()

