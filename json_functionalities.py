import os
import json
from pathlib import Path
from typing import NoReturn

class JsonFile:
    @staticmethod
    def read(directory, filename):
        data: dict = {}
        full_path: str = JsonFile.get_full_file_path(
            directory, filename
        )
        try:
            with open(full_path, 'r') as json_file:
                data = json.load(json_file)
        except Exception as err:
            print(f"error {err}")
        finally:
            return data
    
    @staticmethod
    def write(directory: str, filename: str, data) -> NoReturn:
        full_path: str = JsonFile.get_full_file_path(
            directory, filename
        )
        try:
            with open(full_path, 'w') as json_file:
                json.dump(data, json_file)
        except Exception as err:
            print(f"error {err}")
        else:
            print(f"successfully added data to {filename}")
    
    @staticmethod
    def append(directory: str, filename: str, new_data:dict) -> NoReturn:
        old_data: list = JsonFile.read(directory, filename)
        if isinstance(old_data, list):
            old_data.append(new_data)
        JsonFile.write(directory, filename, old_data)
    
    @staticmethod
    def is_file_exists(_path: str) -> bool:
        """Checks if a file exists"""
        _file = Path(_path)
        if not _file.is_file():
            return False
        return True
    
    @staticmethod
    def get_full_file_path(directory: str, filename: str) -> str:
        full_path: str = os.path.join(directory, filename)
        file_exists: bool = JsonFile.is_file_exists(full_path)
        if not file_exists:
            raise ValueError(" File not found")
        return full_path