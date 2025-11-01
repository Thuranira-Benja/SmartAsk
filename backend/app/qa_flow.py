from typing import Optional

qa_map = {
    "what are the admission requirements?": "Admission requirements include a KCSE certificate, a completed application form, and copy of ID.",
    "how do i apply for a transcript?": "To apply for a transcript, visit the registrar's office or use the online portal and submit the transcript request form.",
}

def check_hardcoded(question: str) -> Optional[str]:
    q = question.lower().strip()
    return qa_map.get(q)
