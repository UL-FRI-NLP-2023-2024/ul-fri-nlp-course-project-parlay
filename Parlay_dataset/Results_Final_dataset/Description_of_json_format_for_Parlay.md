# Description of JSON Format for NLI Dataset

Our dataset, constructed in JSON format, exemplifies principles of structured and systematic organization. This format was chosen to enhance both human and machine interaction with the data, thereby supporting advanced NLP tasks.

## JSON Structure Overview

At the root level, each of the five categories contains nested objects representing the scenarios that serve as premises. Each scenario is uniquely identified by a key (e.g., `"Scenario 2"`), representing distinct instances used for the NLI tasks.

### Key Components

- **OQACM Score:** An additional quantitative measure provided for each scenario, serving as an indicator of its quality or relevance. This score aids in the assessment and selection process for research and practical applications.
  
- **Labels:** Within each scenario object, the structure is subdivided into three labels:
  - **Entailment**
  - **Contradiction**
  - **Neutral**

### Subobject Structure

Each subobject (Entailment, Contradiction, Neutral) contains the following keys:
  
- **Scenario:** Sets the context for the NLI task.
- **Hypothesis:** Represents the hypothesis related to the scenario.
- **Explanation:** Provides an explanation for the inferential relationship between the scenario and the hypothesis.

## Benefits of This Structure

This tripartite division ensures clarity and specificity, allowing for precise categorization and analysis of the inferential relationships.

