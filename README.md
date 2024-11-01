# Carbon-Footprint

This repository provides insights and tools to understand and reduce the carbon footprint associated with technology, particularly focusing on cloud computing and AI model training. It includes scripts to fetch real-time carbon intensity data, calculate carbon emissions, and set up environmentally efficient model training on Google Cloud's Vertex AI.

More about it: https://medium.com/@teendifferent/green-computing-harnessing-ai-for-a-sustainable-future-0626cc94efaa

## Features

- **Carbon Intensity Data Fetching:** Retrieve real-time carbon intensity data using the Electricity Map API.
- **Energy Consumption Calculation:** Calculate energy usage and corresponding carbon emissions.
- **Environmentally Efficient Model Training:** Set up and run ML model training jobs on Google Cloud's Vertex AI, selecting regions with low carbon intensity.
- **Carbon Footprint Analysis:** Analyze the carbon footprint of your Google Cloud usage through BigQuery.

## Requirements

- Python 3.x
- Libraries: `requests`, `json`, `google-cloud`, `pandas`
- Google Cloud account and credentials
- Electricity Map API key

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Carbon-Footprint-Tech.git
    cd Carbon-Footprint-Tech
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables for Google Cloud credentials and Electricity Map API key.

4. Run the script to fetch carbon intensity data:
    ```bash
    python electricity_map_api.py
    ```

5. Run the script to train a model on Vertex AI:
    ```bash
    python vertex_ai_training.py
    ```

## Reference
- [DeepLearning.AI Short Course: Carbon-Aware Computing for GenAI Developers](https://www.deeplearning.ai/short-courses/carbon-aware-computing-for-genai-developers/).
