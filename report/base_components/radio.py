from .base_component import BaseComponent
from fasthtml.common import Input, Label, Div

class Radio(BaseComponent):

    def __init__(self, values, name, hx_get="", hx_target="", selected=""):
        self.values = values
        self.name = name
        self.hx_get=hx_get
        self.hx_target=hx_target
        self.selected=selected


    def build_component(self, entity_id, model):

        children = []
        for value in self.values:
            # Build kwargs for Input, only include checked if this value should be checked
            input_kwargs = {
                'type': "radio",
                'id': value.lower(),
                'name': self.name,
                'value': value,
                'hx_get': self.hx_get,
                'hx_target': self.hx_target
            }
            
            # Only add checked attribute if this option should be checked
            if value == model.name.title():
                input_kwargs['checked'] = True
            
            input_child = Input(**input_kwargs)
            label_child = Label(value, _for=value.lower())
            children.append(input_child)
            children.append(label_child)

        return children
    
    def outer_div(self, component):
        return Div(
            *component
        )