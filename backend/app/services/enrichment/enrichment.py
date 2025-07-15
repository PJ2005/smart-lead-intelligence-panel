import logging
from typing import Dict, Any
from .summarizer import SummarizerService
from .scoring import LeadScoringEngine
import os

"""
EnrichmentService: Enriches company data using Apollo API and generates a GPT-4 summary via SummarizerService. Adds a lead score via LeadScoringEngine.
"""
class EnrichmentService:
    """
    Enriches company data using Apollo API only and generates a GPT-4 summary.
    Adds funding, tech stack, employee count, and more. Calculates a lead score.
    """
    def __init__(self, apollo_enrichment_api_key: str = None, openai_api_key: str = None, scoring_config: Dict[str, Any] = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.apollo_enrichment_api_key = apollo_enrichment_api_key
        self.summarizer = SummarizerService(openai_api_key=openai_api_key or os.environ.get("OPENAI_API_KEY"))
        self.scorer = LeadScoringEngine(config=scoring_config)

    def enrich(self, company: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enrich the company dict with additional data from Apollo API, add a GPT-4 summary, and calculate a lead score.
        Returns a new dict with enrichment fields added.
        """
        enriched = company.copy()
        self.logger.info(f"Starting enrichment for {company.get('company_name')}")
        apollo_data = self._enrich_with_apollo(company)
        if apollo_data:
            self.logger.info("Apollo enrichment successful.")
            enriched.update(apollo_data)
        else:
            self.logger.error("Apollo enrichment failed. Returning original data.")
        # Summarize company description
        description = enriched.get("description")
        if description:
            summary = self.summarizer.summarize(description)
            if summary:
                enriched["summary"] = summary
            else:
                self.logger.error("Summarization failed. No summary added.")
        else:
            self.logger.warning("No description found to summarize.")
        # Score the lead
        score = self.scorer.score(enriched)
        enriched["score"] = score
        return enriched

    def _enrich_with_apollo(self, company: Dict[str, Any]) -> Dict[str, Any]:
        """
        Stub: Simulate Apollo enrichment. Replace with real API call.
        """
        if company.get("company_name") == "Anthropic":
            return {
                "funding": "$1.5B",
                "tech_stack": ["Go", "PyTorch"],
                "employee_count": 150,
                "domain": "anthropic.com"
            }
        # Simulate failure for other companies
        return {}

# Testability: Run independently
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    service = EnrichmentService()
    test_companies = [
        {"company_name": "Anthropic"},
        {"company_name": "UnknownCo"}
    ]
    for c in test_companies:
        enriched = service.enrich(c)
        print(f"\nEnriched data for {c['company_name']}:")
        for k, v in enriched.items():
            print(f"  {k}: {v}") 