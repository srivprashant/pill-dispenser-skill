from mycroft import MycroftSkill, intent_file_handler


class PillDispenser(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dispenser.pill.intent')
    def handle_dispenser_pill(self, message):
        self.speak_dialog('dispenser.pill')


def create_skill():
    return PillDispenser()

