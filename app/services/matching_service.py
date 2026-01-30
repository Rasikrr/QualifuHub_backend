import json
from typing import List
from openai import OpenAI
from app.core.config import settings
from app.models.domain import Vacancy, CV

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def rank_cvs_for_vacancy(vacancy: Vacancy, cvs: List[CV]) -> List[CV]:
    if not cvs:
        return []

    # Prepare data for OpenAI
    vacancy_info = {
        "title": vacancy.title,
        "description": vacancy.description,
        "required_skills": [s.name for s in vacancy.required_skills],
        "category": vacancy.category
    }

    candidates_info = []
    for cv in cvs:
        candidates_info.append({
            "id": str(cv.id),
            "full_name": cv.full_name,
            "summary": cv.summary,
            "experience_level": cv.experience_level,
            "skills": [{"name": s.name, "verified": s.is_verified} for s in cv.skills]
        })

    prompt = f"""
    You are a professional HR recruiter. Rank the following candidates for the given job vacancy.
    Return only a JSON list of candidate IDs in order from best match to worst match.
    Top 10 candidates only.

    Vacancy:
    {json.dumps(vacancy_info, indent=2)}

    Candidates:
    {json.dumps(candidates_info, indent=2)}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-5.2", # or gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant that ranks job candidates."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"} if "gpt-4" in "gpt-3.5-turbo" else None # Adjusted check
        )
        
        # Note: gpt-3.5-turbo-1106 and later support json_object
        # For simplicity in MVP, we'll parse the content
        content = response.choices[0].message.content
        # Expecting something like {"ranked_ids": ["uuid1", "uuid2", ...]}
        # We need to be careful with parsing
        try:
            data = json.loads(content)
            if isinstance(data, list):
                ranked_ids = data
            elif isinstance(data, dict):
                # Try to find a list in the dict
                ranked_ids = next((v for v in data.values() if isinstance(v, list)), [])
            else:
                ranked_ids = []
        except:
            ranked_ids = []

        # Map back to CV objects
        cv_map = {str(cv.id): cv for cv in cvs}
        ranked_cvs = [cv_map[cid] for cid in ranked_ids if cid in cv_map]
        
        return ranked_cvs[:10]
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        # Fallback to simple matching or just returning first 10
        return cvs[:10]
