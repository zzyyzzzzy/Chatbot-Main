from pickle import NONE
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# order form 
class AskOrderDone(Action):
    def name(self) -> Text:
        return "action_ask_order_done"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        
        if tracker.get_slot("first_time_order"):
            dispatcher.utter_message(text="What can i get for you?")
        else:
            dispatcher.utter_message(
                text="Anything elese I can get for you?")
        return [SlotSet("first_time_order", False)]

class ActionSubmitOrderForm(Action):
    def name(self) -> Text:
        return "action_submit_order_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text=f"Your order have been placed. We’re on it. Please head to the register and pay.")
        return [SlotSet("first_time_order", True), SlotSet("dining_option", None),SlotSet("order_done", None)]
    
class ValidateOrderForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_order_form"

    def validate_order_done(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""
        
        if not slot_value:
            return {"order_done": None}
        return {"order_done": True}