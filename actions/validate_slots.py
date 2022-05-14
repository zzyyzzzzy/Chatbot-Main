from pickle import NONE
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action, ValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidatePredefinedSlots(ValidationAction):
    def name(self) -> Text:
        return "action_validate_slot_mappings"
    def validate_num_pizza(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate location value."""
        pizza_type_set = tracker.get_slot("pizza_type")
        if tracker.get_intent_of_latest_message() != "buy_pizza" and not pizza_type_set:
            return {"num_pizza": None}
    
    def validate_num_drink(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate location value."""
        drink_type_set = tracker.get_slot("drink_type")
        if tracker.get_intent_of_latest_message() != "buy_drink" and not drink_type_set:
            return {"num_drink": None}
    
    def validate_num_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        dining_opt_set = tracker.get_slot("dining_option")
        if tracker.get_intent_of_latest_message() != "choose_dining_opt" and not dining_opt_set:
            return {"num_people": None}
        if dining_opt_set  == "to go":
            return {"num_people": None}
        
    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        pizza_type_set = tracker.get_slot("pizza_type")
        if tracker.get_intent_of_latest_message() != "buy_pizza" and not pizza_type_set:
            return {"pizza_size": None}
        
    def validate_drink_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        drink_type_set = tracker.get_slot("drink_type")
        if tracker.get_intent_of_latest_message() != "buy_drink" and not drink_type_set:
            return {"drink_size": None}