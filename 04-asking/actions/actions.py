from typing import Dict, Text, List

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action


class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_last_name"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        first_name = tracker.get_slot("first_name")
        dispatcher.utter_message(text=f"So {first_name}, what is your last name?")
        return []
