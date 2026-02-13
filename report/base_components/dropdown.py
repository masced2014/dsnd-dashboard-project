from .base_component import BaseComponent
from fasthtml.common import Select, Label, Div, Option

class Dropdown(BaseComponent):


    def __init__(self, id="selector", name="entity-selection", label=""):
        self.id = id
        self.name = name
        self.label = label

    def build_component(self, entity_id, model):
        options = []
        data_items = self.component_data(entity_id, model)
        for idx, (text, value) in enumerate(data_items):
            # Select first option if entity_id is None, otherwise match entity_id
            is_selected = (entity_id is None and idx == 0) or (str(value) == entity_id)
            
            # Build option kwargs conditionally
            option_kwargs = {'value': value}
            if is_selected:
                option_kwargs['selected'] = True
            
            option = Option(text, **option_kwargs)
            options.append(option)


        dropdown_settings = {
            'name': self.name
            }
        
        # if model.name:
        #     dropdown_settings['disabled'] = 'disabled'

        selector = Select(
            *options,
            **dropdown_settings
            )
        
        return selector
    
    def outer_div(self, child):

        return Div(
            Label(self.label, _for=self.id),
            child,
            id=self.id,
        )
    