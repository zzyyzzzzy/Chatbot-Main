from pickle import NONE
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action, ValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


ALLOWED_PIZZA_TYPES = ["mozzarella", "mushroom", "veggie", "pepperoni", "hawaii", "cheese", "hawaiian chicken", "hawaii chicken"]
ALLOWED_SIZES = ["small", "medium", "large", "extra-large", "extra large", "s", "m", "l", "xl"]
# pizaa form
class ActionSubmitPizza(Action):
   def name(self) -> Text:
      return "action_submit_pizza"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    dispatcher.utter_message(text="Pizza order submited")
    return [SlotSet("pizza_size", None), SlotSet("pizza_type", None), SlotSet("num_pizza", None),
            SlotSet("drink_size", None), SlotSet("num_drink", None), SlotSet("first_time_order", False)]

class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"

    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""
        p_size = slot_value.lower()
        if p_size not in ALLOWED_SIZES:
            dispatcher.utter_message(text=f"We only accept pizza sizes: s/m/l/xl.")
            return {"pizza_size": None}
        # dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_size": p_size}

    def validate_pizza_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""
        pizza = slot_value.lower()
        if pizza not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"pizza_type": None}
        # dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        if pizza == "hawaii chicken":
            pizza = "hawaiian chicken"
        return {"pizza_type": pizza}