from typing import TypedDict, Dict, Any, List, Optional
from sqlalchemy.orm import Session


class AgentState(TypedDict):
    db:Session

    user_input: str
    user_id:int

    messages: List[Dict[str, str]]

    context: Dict[str, Any]

    action: Optional[str]

    params: Dict[str, Any]

    result: Optional[Dict[str, Any]]

    response: Optional[str]