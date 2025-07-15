# Company Data Enrichment Module

**Note:** The enrichment pipeline now includes AI-powered summarization using GPT-4. The output will include a `summary` field if a description is present and summarization succeeds.

## Table of Contents
- Overview
- Usage
- SummarizerService Usage
- Troubleshooting Summarization
- OpenAI API Key Configuration
- Summarization Integration
- Extending Summarization
- Testing Summarization Independently
- Logging and Monitoring
- Value of Summarization
- Limitations and Future Improvements
- Changelog

## Overview
The `EnrichmentService` enriches normalized company data with additional information such as funding, tech stack, employee count, and more, using third-party APIs (Apollo, etc.).

Now also includes **AI-powered company summarization** using GPT-4 via the `SummarizerService`.

- **Primary API:** Apollo (stubbed)
- **Summarization:** GPT-4 (OpenAI)
- **OOP, modular, and independently testable**

## Usage

### 1. Import and Initialize
```python
from enrichment import EnrichmentService
service = EnrichmentService(
    apollo_enrichment_api_key="...",
    openai_api_key="..."  # or set OPENAI_API_KEY in your environment
)
```

### 2. Enrich Company Data (with Summary)
```python
company = {"company_name": "OpenAI", "description": "OpenAI is a leading company in AI research and deployment."}
enriched = service.enrich(company)
print(enriched)
```

### 3. Example Output
```
{
  'company_name': 'OpenAI',
  'description': 'OpenAI is a leading company in AI research and deployment.',
  'summary': 'OpenAI is a leading company in AI research and deployment, focused on advancing artificial intelligence in a safe and beneficial manner.',
  'funding': '$11B',
  'tech_stack': ['Python', 'TensorFlow', 'Kubernetes'],
  'employee_count': 375,
  'domain': 'openai.com'
}
```

## API Details (Stubbed)
- **Apollo:** Adds funding, tech stack, employee count, domain (stubbed logic for demo)
- **GPT-4:** Generates a 1-2 line summary from the company description

## Error Handling
- If the OpenAI API returns an error or rate limit, the error is logged and no summary is added.
- The enrichment pipeline continues even if summarization fails.

## Integration
Call `EnrichmentService.enrich(company_dict)` after normalization in any scraper, before caching or storage. The output will include a `summary` field if a description is present and summarization succeeds.

## Extending
- Replace stub methods with real API calls as needed.
- Add more enrichment providers or summarization options as desired. 

## SummarizerService Usage

The `SummarizerService` can be used independently to generate a summary from any company description text:

```python
from enrichment.summarizer import SummarizerService
summarizer = SummarizerService(openai_api_key="...")
summary = summarizer.summarize("OpenAI is a leading company in AI research and deployment.")
print(summary)
``` 

## Troubleshooting Summarization
- If the `summary` field is missing, check that the company data includes a `description` and that your OpenAI API key is set.
- If you see errors about rate limits or API failures, check your OpenAI usage and logs for details. 

## OpenAI API Key Configuration
- Set your OpenAI API key in the environment variable `OPENAI_API_KEY` or pass it directly to `SummarizerService` or `EnrichmentService`.
- Example `.env` entry:
  ```env
  OPENAI_API_KEY=your_openai_key_here
  ``` 

## Summarization Integration
- After enrichment, the pipeline generates a summary from the company description using GPT-4.
- The summary is added as a `summary` field in the output dict.
- This makes the output more readable and useful for dashboards, lead cards, and analytics. 

## Extending Summarization
- You can customize the prompt in `SummarizerService` for different summary styles.
- You can use other OpenAI models by changing the `model` parameter.
- You can add fallback logic or additional summarization providers as needed. 

## Testing Summarization Independently
- You can test the summarizer directly by running:
  ```python
  from enrichment.summarizer import SummarizerService
  summarizer = SummarizerService(openai_api_key="...")
  print(summarizer.summarize("OpenAI is a leading company in AI research and deployment."))
  ``` 

## Logging and Monitoring
- All summarization attempts, errors, and rate limits are logged via the standard logger.
- Check your logs for details if summaries are missing or errors occur. 

## Value of Summarization
- Summaries provide a quick, digestible overview of each company for business users.
- They improve the user experience in dashboards, lead cards, and analytics by surfacing key information at a glance. 

## Limitations and Future Improvements
- Summarization depends on the quality and length of the input description.
- OpenAI API usage may incur costs and is subject to rate limits.
- Future: Add caching for summaries, support for multi-language, and more robust error handling. 

## Changelog
- 2025-07-15: Added AI-powered company summarization using GPT-4 (SummarizerService) and integrated it into the enrichment pipeline. 

## LeadScoringEngine Usage

The `LeadScoringEngine` calculates a 0-100 score for each company using rule-based logic (and future ML/LLM support).

### Example
```python
from enrichment.scoring import LeadScoringEngine
scorer = LeadScoringEngine()
score = scorer.score(company_dict)
print(score)
```

### Configuration
You can customize scoring weights by passing a config dict:
```python
config = {"funding_weight": 0.3, "employee_count_weight": 0.1, ...}
scorer = LeadScoringEngine(config=config)
```

### Integration
The enrichment pipeline automatically adds a `score` field to each company dict.

### Example Output
```
{
  'company_name': 'OpenAI',
  'description': 'OpenAI is a leading company in AI research and deployment.',
  'summary': 'OpenAI is a leading company in AI research and deployment, focused on advancing artificial intelligence in a safe and beneficial manner.',
  'funding': '$11B',
  'tech_stack': ['Python', 'TensorFlow', 'Kubernetes'],
  'employee_count': 375,
  'domain': 'openai.com',
  'score': 80
}
``` 

## Extending Lead Scoring
- The `score_with_ml` method is a stub for future ML/LLM-based scoring.
- Replace with a real model or API as needed. 

## Bug Fix: OpenAI Error Handling (2025-07-15, updated)
- Now uses openai.RateLimitError and openai.OpenAIError directly for SDK >=1.0.0.
- Ensures compatibility with latest OpenAI Python SDK and robust error handling in the pipeline. 