from utils import smooth, BaseState


class StateNormal(BaseState): # N

    def __init__(self, context):
        super().__init__(context)
        self.c = context
    
    def on_left_click(self, event): # A
        # Left
        self.c.bt_left.update(event.value)

    def on_down_click(self, event): # B
        if event.value == 1: # +B
            self.c.set_state(self.c.state_B)
    
    def on_up_click(self, event): # C
        self.c.bt_right.update(event.value)

    def on_right_click(self, event): # D
        if event.value == 1: # +D
            # Move to browser state
            self.c.set_state(self.c.state_D)
    
    def on_move_rel_x(self, event):
        # Horizontal movement
        self.c.bt_rel_x.update(smooth(event.value))

    def on_move_rel_y(self, event):
        # Vertical movement
        self.c.bt_rel_y.update(smooth(event.value))


class StateB(BaseState):

    def __init__(self, context):
        super().__init__(context)
        self.c = context
        self.clean = True
    
    def on_activate(self):
        self.clean = True
    
    def on_left_click(self, event): # A
        self.clean = False
        if event.value == 1:
            self.c.on_switch_windows(False)

    def on_down_click(self, event): # B
        if event.value == 0:
            if self.clean:
                self.c.key_back.press()
                self.c.key_back.release()
            
            self.c.set_state(self.c.state_N)
    
    def on_up_click(self, event): # C
        self.clean = False
        self.c.key_forward.update(event.value)

    def on_right_click(self, event): # D
        self.clean = False
        if event.value == 1:
            self.c.on_switch_windows(True)
    
    def on_move_rel_x(self, event):
        # Horizontal movement
        self.clean = False
        self.c.bt_wheel_h.update(event.value * 20)

    def on_move_rel_y(self, event):
        # Vertical movement
        self.clean = False
        self.c.bt_wheel_v.update(-event.value * 10)


class StateD(BaseState):

    def __init__(self, context):
        super().__init__(context)
        self.c = context
        self.clean = True
    
    def on_activate(self):
        self.clean = True
    
    def on_left_click(self, event): # A
        self.clean = False
        if event.value == 1:
            self.c.key_leftctrl.press()
            self.c.bt_left.press()
        else:
            self.c.bt_left.release()
            self.c.key_leftctrl.release()

    def on_down_click(self, event): # B
        self.clean = False

        if event.value == 1:
            self.c.key_leftctrl.press()
            self.c.key_w.press()
        else:
            self.c.key_w.release()
            self.c.key_leftctrl.release()
    
    def on_up_click(self, event): # C
        self.clean = False

        if event.value == 1:
            self.c.key_leftalt.press()
            self.c.key_f4.press()
        else:
            self.c.key_f4.release()
            self.c.key_leftalt.release()

    def on_right_click(self, event): # D
        if event.value == 0:
            if self.clean:
                self.c.bt_middle.press()
                self.c.bt_middle.release()
            self.c.set_state(self.c.state_N)
    
    def on_move_rel_x(self, event):
        self.clean = False
        # Horizontal movement
        # self.clean = False
        # self.c.key_tabs.update(event.value)

    def on_move_rel_y(self, event):
        # Vertical movement
        self.clean = False
        self.c.key_tabs.update(-event.value * 5)