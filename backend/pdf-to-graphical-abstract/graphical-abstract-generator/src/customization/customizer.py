class Customizer:
    def __init__(self):
        self.color_scheme = 'light'
        self.layout = 'vertical'
        self.design_type = 'text-heavy'

    def set_color_scheme(self, scheme):
        valid_schemes = ['dark', 'light', 'custom']
        if scheme in valid_schemes:
            self.color_scheme = scheme
        else:
            raise ValueError(f"Invalid color scheme. Choose from {valid_schemes}.")

    def set_layout(self, layout_style):
        valid_layouts = ['vertical', 'horizontal', 'mind-map']
        if layout_style in valid_layouts:
            self.layout = layout_style
        else:
            raise ValueError(f"Invalid layout style. Choose from {valid_layouts}.")

    def set_design_type(self, design):
        valid_designs = ['icon-based', 'text-heavy']
        if design in valid_designs:
            self.design_type = design
        else:
            raise ValueError(f"Invalid design type. Choose from {valid_designs}.")