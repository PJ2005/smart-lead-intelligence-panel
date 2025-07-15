"""
SummarizerService: Uses OpenAI GPT-4 to generate concise company summaries. Handles API errors and rate limits gracefully.
"""
import logging
import openai
import os
from typing import Optional

class SummarizerService:
    """
    Uses GPT-4 to generate a concise 1-2 line summary for a company.
    Handles API errors and rate limits gracefully.
    """
    def __init__(self, openai_api_key: Optional[str] = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.openai_api_key

    def summarize(self, company_text: str) -> Optional[str]:
        prompt = (
            "Summarize the following company description in 1-2 concise, business-focused sentences:\n"
            f"{company_text}"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=80,
                temperature=0.7,
            )
            summary = response.choices[0].message["content"].strip()
            return summary
        except openai.RateLimitError as e:
            self.logger.error(f"OpenAI rate limit error: {e}")
            return None
        except openai.OpenAIError as e:
            self.logger.error(f"OpenAI API error: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error during summarization: {e}")
            return None 