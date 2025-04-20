from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Dict, Any, List, Optional


class MongoDBBase:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str) -> Collection:
        return self.db[collection_name]

    def find_one_data(self, collection_name: str, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        collection = self.get_collection(collection_name)
        return collection.find_one(query)

    def find_data(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        collection = self.get_collection(collection_name)
        return list(collection.find(query))

    def update_data(self, collection_name: str, query: Dict[str, Any], update: Dict[str, Any]) -> Any:
        collection = self.get_collection(collection_name)
        return collection.update_many(query, {"$set": update})

    def update_one_data(self, collection_name: str, query: Dict[str, Any], update: Dict[str, Any]) -> Any:
        collection = self.get_collection(collection_name)
        return collection.update_one(query, {"$set": update})

    def delete_one_data(self, collection_name: str, query: Dict[str, Any]) -> Any:
        collection = self.get_collection(collection_name)
        return collection.delete_one(query)
