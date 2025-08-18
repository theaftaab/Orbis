import json 
from pathlib import Path
from typing import Dict, Any, List

from models.registerDriversModels import Drivers

class RegisterDriversService:
    def __init__(self, drivers_file_path: str = "drivers.json"):
        self.drivers_file_path = Path(drivers_file_path)
        self.drivers_file_path.parent.mkdir(exist_ok=True)

    def _load_drivers(self) -> Dict[Drivers , Any]:
        if not self.drivers_file_path.exists():
            return {"drivers": [],}  
        
        try:
            with open(self.drivers_file_path, 'r') as f:
                data = json.load(f)
                if not isinstance(data, list) or "drivers" not in data:
                    return {"drivers": [],}  
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return {"drivers": []}  

    def _save_drivers(self, drivers: Dict[str,Any]) -> None:
        with open(self.drivers_file_path, 'w') as f:
            json.dump(drivers, f, indent=4)

    def register_drivers(self, request: Drivers) -> List[str]:
        drivers = self._load_drivers()
        drivers_map = {}
        for driver_item in drivers:
            if isinstance(driver_item, dict) and 'driver_id' in driver_item:
                drivers_map[driver_item['driver_id']] = driver_item

        upserted_ids: List[str] = []
        
        # Iterate through the list of driver objects from the request
        for driver in request:
            driver_dict = driver.model_dump()
            driver_id = driver_dict["driver_id"]
            
            # Add or update the driver in our map
            drivers_map[driver_id] = driver_dict
            upserted_ids.append(driver_id)
            
        # Convert the map's values back to a list for saving
        updated_drivers_list = list(drivers_map.values())
        
        # Save the complete, updated list
        self._save_drivers(updated_drivers_list)
        return upserted_ids