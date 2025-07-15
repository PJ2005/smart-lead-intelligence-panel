import logging
from typing import Dict, Any, Optional

class LeadScoringEngine:
    """
    Calculates a 0-100 lead score using rule-based and (future) AI/ML-based methods.
    Scoring criteria are configurable.
    """
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        # Example default config: weights for each field
        self.config = config or {
            "funding_weight": 0.2,
            "employee_count_weight": 0.2,
            "tech_stack_weight": 0.2,
            "has_summary_weight": 0.1,
            "domain_weight": 0.1,
            "custom_rule_weight": 0.2,
        }

    def score(self, company: Dict[str, Any]) -> int:
        """
        Calculate a 0-100 score for the company using rule-based logic.
        """
        score = 0
        # Example rules (customize as needed):
        if company.get("funding"):
            score += 20 * self.config["funding_weight"]
        if company.get("employee_count", 0) > 100:
            score += 20 * self.config["employee_count_weight"]
        if company.get("tech_stack"):
            score += 20 * self.config["tech_stack_weight"]
        if company.get("summary"):
            score += 10 * self.config["has_summary_weight"]
        if company.get("domain"):
            score += 10 * self.config["domain_weight"]
        # Custom rule: e.g., if 'AI' in summary or tech_stack
        if (company.get("summary") and "AI" in company["summary"]) or \
           (company.get("tech_stack") and any("AI" in t for t in company["tech_stack"])):
            score += 20 * self.config["custom_rule_weight"]
        # Clamp score to 0-100
        score = int(max(0, min(100, score)))
        return score

    def score_with_ml(self, company: Dict[str, Any]) -> int:
        """
        Stub for future ML/LLM-based scoring. Replace with real model.
        """
        # TODO: Integrate ML/LLM model here
        self.logger.info("ML/LLM scoring not implemented. Returning rule-based score.")
        return self.score(company) 