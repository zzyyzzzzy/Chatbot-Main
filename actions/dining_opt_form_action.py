from pickle import NONE
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action, ValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


DINING_IN = ["for here", "dining in", "dine in", "table for", "table"]
TO_GO = ["to go", "take away"]
# dining option form class
class AcitonSubmitDiningOpt(Action):
    def name(self) -> Text:
        return "action_submit_dining_option"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        
        dining_opt = tracker.get_slot("dining_option")
        # Could potentially connected with the "avaiable tables" database
        if dining_opt == "dine in":
            dispatcher.utter_message(text="Please give me a minute. Our server will be with you shortly.")
            return [SlotSet("dining_option", None), SlotSet("num_people", None), SlotSet("num_pizza", None), SlotSet("num_drink", None)]
        return []
    
class ValidateDiningOptForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_dining_opt_form"

    def validate_dining_option(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        ask_again_text = "I didn't get that, can you repeat again?"
        if slot_value.lower() in DINING_IN:
            return {"dining_option": "dine in"}
        elif slot_value.lower() in TO_GO:
            return {"dining_option": "to go", "num_people": 0}
        else:
            dispatcher.utter_message(text=ask_again_text)
            return {"dining_option": None}