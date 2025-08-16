import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from models.handshakeModels import HandshakeRequest


class HandshakeService:
    def __init__(self, sessions_file_path: str = "sessions.json"):
        self.sessions_file_path = Path(sessions_file_path)
        self.sessions_file_path.parent.mkdir(exist_ok=True)
    
    def _load_sessions(self) -> Dict[str, Any]:
        if not self.sessions_file_path.exists():
            return {}
        
        try:
            with open(self.sessions_file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    
    def _save_sessions(self, sessions: Dict[str, Any]) -> None:
        
        with open(self.sessions_file_path, 'w') as f:
            json.dump(sessions, f, indent=4)
    
    # Create a new session based on the handshake request
    def create_session(self, handshake_data: HandshakeRequest) -> str:
       
        session_id = f"session_{uuid.uuid4().hex[:8]}"
      
        sessions = self._load_sessions()
    
        session_data = {
            "session_id": session_id,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "data": handshake_data.model_dump()
        }
      
        sessions[session_id] = session_data
        
        self._save_sessions(sessions)
        
        return session_id
    


