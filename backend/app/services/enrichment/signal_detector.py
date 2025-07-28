import logging
import openai
import os
from typing import List, Dict, Optional

class SignalDetector:
    """
    Uses GPT-4 to extract sales signals (funding, leadership changes, tech adoption, etc.) from unstructured text.
    Returns a list of detected signals, each with type, value, and confidence.
    Handles API errors and logs all actions.
    """
    def __init__(self, openai_api_key: Optional[str] = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.openai_api_key

    def detect_signals(self, text: str) -> List[Dict[str, str]]:
        prompt = (
            """
            Extract all critical sales signals from the following text. 
            For each signal, return a JSON list of objects with these fields: 
            - type (e.g., 'funding', 'leadership_change', 'tech_adoption')
            - value (e.g., '$50M Series B', 'New CTO: Jane Doe', 'Adopted Snowflake')
            - confidence (High, Medium, Low)
            Only include signals that are relevant for B2B sales intelligence. 
            Text:
            """
            f"{text}\n\nJSON:"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.2,
            )
            import json
            content = response.choices[0].message["content"].strip()
            # Try to parse the first JSON list in the response
            start = content.find('[')
            end = content.rfind(']')
            if start != -1 and end != -1:
                signals = json.loads(content[start:end+1])
                self.logger.info(f"Extracted {len(signals)} signals.")
                return signals
            else:
                self.logger.warning("No signals found in response.")
                return []
        except openai.RateLimitError as e:
            self.logger.error(f"OpenAI rate limit error: {e}")
            return []
        except openai.OpenAIError as e:
            self.logger.error(f"OpenAI API error: {e}")
            return []
        except Exception as e:
            self.logger.error(f"Unexpected error during signal detection: {e}")
            return []

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    detector = SignalDetector()
    sample_text = (
        "Acme Corp announced a $25M Series A funding round led by Sequoia. "
        "Jane Doe was appointed as the new CTO. The company recently migrated to Snowflake for data warehousing."
    )
    signals = detector.detect_signals(sample_text)
    print("Detected signals:")
    for signal in signals:
        print(signal) 