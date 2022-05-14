from pickle import NONE
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


ALLOWED_SIZES = ["small", "medium", "large", "extra-large", "extra large", "s", "m", "l", "xl"]
ALLOWED_DRINK_TYPES = ["sprite", "fanta", "coke"]

# drink form
class ValidateDrinkForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_drink_form"

    def validate_drink_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""

        if slot_value.lower() not in ALLOWED_SIZES:
            dispatcher.utter_message(text=f"We only accept drink sizes: s/m/l/xl.")
            return {"drink_size": None}
        # dispatcher.utter_message(text=f"OK! You want to have a {slot_value} drink.")
        return {"drink_size": slot_value}

    def validate_drink_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `drink_type` value."""

        if slot_value.lower() not in ALLOWED_DRINK_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that drink. We serve {'/'.join(ALLOWED_DRINK_TYPES)}.")
            return {"drink_type": None}
        # dispatcher.utter_message(text=f"OK! You want to have a {slot_value}.")
        return {"drink_type": slot_value}

class AcitonSubmitDrink(Action):
    def name(self) -> Text:
        return "action_submit_drink"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
       
        dispatcher.utter_message(text="Drink order submited")
        return [SlotSet("drink_size", None), SlotSet("drink_type", None), SlotSet("num_drink", None), 
                SlotSet("pizza_size", None), SlotSet("num_pizza", None), SlotSet("first_time_order", False)]