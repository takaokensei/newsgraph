import json
import logging
from typing import List, Dict, Any, Optional
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prompt Template for Triple Extraction
TRIPLET_EXTRACTION_TEMPLATE = """
You are an expert AI Knowledge Engineer. Your task is to extract meaningful Entities and Relationships from the given news text to build a Knowledge Graph.

**Input Text (Category: {category}):**
"{text}"

**Instructions:**
1. Identify key **Entities** (Person, Organization, Concept, Location, Technology, etc.).
2. Identify **Relationships** between these entities. Use precise verbs (e.g., "LOCATED_IN", "DEVELOPS", "INVESTS_IN", "PART_OF").
3. Output the result ONLY in strict JSON format.
4. Do NOT add any conversational text or markdown code blocks (like ```json). Just the raw JSON.

**JSON Schema:**
{{
    "entities": [
        {{"name": "Entity Name", "type": "Type"}},
        ...
    ],
    "relationships": [
        {{"source": "Entity Name", "target": "Entity Name", "relation": "RELATION_TYPE"}},
        ...
    ]
}}

**Example Output:**
{{
    "entities": [
        {{"name": "Petrobras", "type": "Organization"}},
        {{"name": "Energia Eólica", "type": "Concept"}}
    ],
    "relationships": [
        {{"source": "Petrobras", "target": "Energia Eólica", "relation": "INVESTS_IN"}}
    ]
}}
"""

class LLMExtractor:
    def __init__(self, provider="ollama", model_name=OLLAMA_MODEL):
        self.provider = provider
        self.model_name = model_name
        self.llm = self._initialize_llm()
        self.prompt = PromptTemplate(
            input_variables=["text", "category"],
            template=TRIPLET_EXTRACTION_TEMPLATE
        )

    def _initialize_llm(self):
        if self.provider == "ollama":
            logger.info(f"Initializing Ollama LLM with model: {self.model_name}")
            return Ollama(base_url=OLLAMA_BASE_URL, model=self.model_name)
        else:
            # Placeholder for other providers
            raise ValueError(f"Provider {self.provider} not yet implemented.")

    def extract_triplets(self, text: str, category: str) -> Dict[str, Any]:
        """
        Extract entities and relationships from text using LLM.
        """
        try:
            formatted_prompt = self.prompt.format(text=text, category=category)
            logger.info(f"Sending request to LLM (Length: {len(text)} chars)...")
            
            response = self.llm.invoke(formatted_prompt)
            
            # Clean response (robust JSON extraction)
            clean_response = response.strip()
            # Try to find JSON object
            start_idx = clean_response.find('{')
            end_idx = clean_response.rfind('}')
            
            if start_idx != -1 and end_idx != -1:
                clean_response = clean_response[start_idx:end_idx+1]
            
            data = json.loads(clean_response)
            return data
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            print(f"❌ RAW RESPONSE: {response}") # Debug print
            logger.debug(f"Raw Response: {response}")
            return {"entities": [], "relationships": []}
        except Exception as e:
            logger.error(f"LLM Extraction failed: {e}")
            return {"entities": [], "relationships": []}

# Mock implementation for verification if LLM is down
class MockExtractor:
    def extract_triplets(self, text: str, category: str) -> Dict[str, Any]:
        logger.info("Using Mock Extractor")
        return {
            "entities": [
                {"name": "Brasil", "type": "Location"},
                {"name": "Economia", "type": "Concept"}
            ],
            "relationships": [
                {"source": "Brasil", "target": "Economia", "relation": "HAS_SECTOR"}
            ]
        }
