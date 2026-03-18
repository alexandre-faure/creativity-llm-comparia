# **Measuring Creativity in Large Language Models (LLMs)**

_A Comparative Study Using Real-World Data from compar:IA_

**Master 2 Project – CentraleSupélec, Artificial Intelligence Specialization**

## **Project Overview**

This repository contains the code, analysis, and deliverables for our **Master 2 project** at CentraleSupélec, focusing on **measuring the creativity of Large Language Models (LLMs)** using real-world user data from the **compar:IA** platform (Ministry of Culture, France).

### **Key Objectives**

1. **Define and justify** a rigorous framework of quantitative metrics to evaluate LLM creativity.
2. **Apply the Bradley-Terry model** to rank models based on pairwise user preferences.
3. **Identify and correct** systematic biases in the compar:IA dataset.
4. **Validate construct validity** to ensure the "creativity" label truly measures creativity.

## Datasets

We use three open datasets from **compar:IA** (Ministry of Culture, France), available on Hugging Face:

| Dataset                    | Description                                                                                                                                 | Size          | Hugging Face Link                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------- |
| **comparia-conversations** | Full conversations (prompts + model responses) with metadata (categories, keywords, energy consumption, tokens)                             | 472k entries  | [Link](https://huggingface.co/datasets/ministere-culture/comparia-conversations) |
| **comparia-votes**         | User preferences at the conversation level (votes for Model A, B, or tie) with qualitative labels (e.g., `creative`, `useful`, `incorrect`) | 157k entries  | [Link](https://huggingface.co/datasets/ministere-culture/comparia-votes)         |
| **comparia-reactions**     | User reactions at the message level (thumbs up/down, labels like `creative`, `useful`, `superficial`)                                       | 94.3k entries | [Link](https://huggingface.co/datasets/ministere-culture/comparia-reactions)     |

**Note:** All datasets are under the **Etalab 2.0 license** and have been anonymized for privacy.

## Setup & Installation

### Prerequisites

- Python 3.11+
- Git
- Hugging Face account (for dataset access)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alexandre-faure/creativity-llm-comparia.git
   cd creativity-llm-comparia
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   pyenv virtualenv 3.11 creativity-llm
   pyenv activate creativity-llm
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download datasets:**
   - Accept the terms of use on [Hugging Face](https://huggingface.co/collections/comparIA/jeux-de-donnees-compar-ia).
   - Place the datasets in the `data/` folder.

---

## Key Deliverables

| Deliverable | Description | Format |
| ----------- | ----------- | ------ |
|             |             |        |

_To complete_

---

## Methodology Highlights

_To complete_

## References

- [compar:IA Platform](https://comparia.beta.gouv.fr/)
- [Franceschelli & Musolesi (2023) - On the Creativity of LLMs](https://arxiv.org/abs/2304.00008)
- [Bradley & Terry (1952) - Rank Analysis](https://www.jstor.org/stable/2334029)
- [Davidson (1970) - Extending Bradley-Terry for Ties](https://www.jstor.org/stable/2283595)

## License

This project is under the GNU General Public License v3.0 (GPL-3.0). See [LICENSE](LICENSE) for details.

Any use of the dataset must comply with the Etalab 2.0 license terms. See [compar:IA License](https://alliance.numerique.gouv.fr/licence-ouverte-open-licence/) for more information.
