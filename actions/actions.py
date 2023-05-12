from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayFood(Action):

    def name(self) -> Text:
        return "action_say_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = tracker.get_slot("food")
        flavor = tracker.get_slot("flavor")
        size = tracker.get_slot("size")

        if not food:
            dispatcher.utter_message(text="Você ainda não realizou um pedido.")
        else:
            dispatcher.utter_message(text=f"Seu pedido: {food} {size} de {flavor}!")
        return []
