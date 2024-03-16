# Natural language processing course 2023/24: `Towards Generalizable NLP Models: A Prompt-Guided Inference Dataset with Integrated Reasoning Rules`



## Project Team

* Blaž Lipar (Student of Digital Linguistics at University of Ljubljana)
* Meta Kokalj (Student of Digital Linguistics at University of Ljubljana)


## Project Overview

This project aims to construct a comprehensive inference dataset for training NLP models. The dataset will focus on promoting model generalizability by incorporating diverse scenario categories and prompt-driven generation.

## Key Objectives

* Create a high-quality dataset encompassing various reasoning modes.
* Ensure dataset diversity through multiple scenario categories.
* Construct effective and adaptable prompts for inference pair generation by combining reasoning rules, factual grounding, heuristic flexibility, Chain of Thought (CoT), and Tree of Thought (ToT).

## Methodology
The methodology involves two key steps: scenario generation and inference pair generation using reasoning rules, Chain of Thought (CoT), and Tree of Thought (ToT) techniques.

### Scenario Generation

This section addresses challenges of natural text-based datasets:
* Citation Management
* Authorship Attribution Difficulties

Prompt-driven scenarios enhance control over information and mitigate bias.

#### Scenario Categories

* Historical Events (causal reasoning, temporal reasoning, counterfactuals)
* Scientific Explanations (deductive reasoning)
* Everyday Situations (inductive reasoning, analogical reasoning)
* News Reports (critical reasoning)
* Fictional Stories (narrative reasoning, social reasoning)

### Inference Pair Generation


**Reasoning Guided Prompt Engineering**

In this phase, we adopt a multifaceted approach to prompt design, drawing upon established reasoning principles alongside heuristic strategies and factual hints. Our goal is to craft prompts that effectively guide the model towards desired inferences while preserving adaptability to diverse scenarios encountered in natural language.

We will examine NLP datasets (SNLI, MNLI) to refine prompt structure.

**Chain of Thought Reasoning (CoT)**

CoT allows us to gain insights into the model's reasoning steps for prompt refinement. By analyzing the CoT output, we can identify:

* Areas where the model's reasoning diverges from the intended path.
* Weaknesses in the prompt or areas where the model lacks understanding.
* Potential biases in the model's reasoning process.

Benefits of CoT:
* Provides deeper understanding of the model's thought process.
* Enables debugging and improvement of prompts.
* Helps identify and mitigate model biases.

**Tree of Thought (ToT) Technique**

This technique encourages the model to explore different reasoning paths and evaluate them before arriving at a conclusion.

Benefits of ToT in addition to CoT:
* Reveals reasoning patterns beyond established rules encoded in prompts.
* Helps identify complex reasoning processes used by the model.
* Enables generating more diverse inference pairs.


**Integrating Reasoning Rules with CoT and ToT:**

In inference pair generation, we will combine reasoning rules with CoT and ToT techniques. Firstly, the reasoning rules will guide the initial generation of inference pairs based on the prompts. Then, CoT will provide insights into the model's reasoning process, allowing us to refine and improve the prompts based on observed deviations or weaknesses. Finally, ToT will complement CoT by exploring additional reasoning paths and enriching the diversity of generated inference pairs.

## Expected Outcomes

* A well-structured inference dataset for NLP training.
* Enhanced model generalizability in reasoning tasks.
* Improved understanding of prompt-based scenario generation for NLP datasets.


## Further Exploration

* Develop an automated pipeline for prompt generation and scenario creation.
* Investigate transfer learning techniques for applying the dataset to various NLP tasks.
* Analyze the impact of dataset diversity on model performance across reasoning modes.


