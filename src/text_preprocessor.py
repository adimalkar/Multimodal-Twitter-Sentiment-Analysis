import re
import string
from typing import List, Dict, Any, Optional

class TweetPreprocessor:
    """
    Advanced text preprocessing and normalization pipeline tailored for 
    multimodal Twitter sentiment analysis models (e.g., BART, BERT, RoBERTa).
    
    Handles Twitter-specific artifacts (handles, URLs, hashtags, emojis) 
    while preserving sentiment-bearing signals.
    """
    
    def __init__(self, preserve_hashtags: bool = True, lowercase: bool = True):
        self.preserve_hashtags = preserve_hashtags
        self.lowercase = lowercase
        
        # Regex patterns for Twitter-specific tokens
        self.url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self.mention_pattern = re.compile(r'@\w+')
        self.hashtag_pattern = re.compile(r'#(\w+)')
        self.whitespace_pattern = re.compile(r'\s+')

    def clean_text(self, text: str) -> str:
        """
        Cleans and normalizes raw tweet string for NLP embeddings.
        
        Args:
            text (str): Raw tweet content
            
        Returns:
            str: Cleaned text suitable for tokenizer ingestion
        """
        if not isinstance(text, str):
            return ""
            
        # 1. Remove URLs
        cleaned = self.url_pattern.sub('', text)
        
        # 2. Remove User Mentions (@user)
        cleaned = self.mention_pattern.sub('', cleaned)
        
        # 3. Handle Hashtags (#happy -> happy)
        if self.preserve_hashtags:
            cleaned = self.hashtag_pattern.sub(r'\1', cleaned)
        else:
            cleaned = self.hashtag_pattern.sub('', cleaned)
            
        # 4. Optional lowercasing
        if self.lowercase:
            cleaned = cleaned.lower()
            
        # 5. Remove redundant whitespace / newlines
        cleaned = self.whitespace_pattern.sub(' ', cleaned).strip()
        
        return cleaned

    def batch_process(self, tweets: List[str]) -> List[str]:
        """Processes a list of tweet strings in sequence."""
        return [self.clean_text(tweet) for tweet in tweets if tweet]

    def extract_features(self, text: str) -> Dict[str, Any]:
        """
        Extracts structural sentiment cues before cleaning.
        
        Returns:
            Dict: Contains counts of exclamation marks, uppercase words, hashtags
        """
        if not isinstance(text, str):
            return {"caps_ratio": 0.0, "exclamations": 0, "hashtags": []}
            
        words = text.split()
        caps_count = sum(1 for w in words if w.isupper() and len(w) > 1)
        caps_ratio = round(caps_count / max(len(words), 1), 4)
        exclamations = text.count('!')
        hashtags = self.hashtag_pattern.findall(text)
        
        return {
            "caps_ratio": caps_ratio,
            "exclamation_count": exclamations,
            "hashtags": hashtags,
            "cleaned_text": self.clean_text(text)
        }
