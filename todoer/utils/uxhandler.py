from todoer.utils.pages import Pages
from todoer.utils.messages import Messages
from todoer.utils.steps import UserSteps


class UXNode:
    def __init__(
        self,
        step: str,
        parent: "UXNode" = None,
        trigger: str = None,
        keyboard: list = None,
        description: str = "",
        required_permission: int = 1,
    ):
        self.step = step
        self.trigger = trigger
        self.keyboard = keyboard
        self.required_permission = required_permission
        self.description = description
        self.parent = None
        if parent:
            self.set_parent(parent)
        self.children = set()

    def set_parent(self, parent: "UXNode"):
        self.parent = parent
        parent.children.add(self)

    def __repr__(self):
        return str(
            {
                "step": self.step,
                "trigger": self.trigger,
                "required_permission": self.required_permission,
            }
        )


class UXTree:
    nodes = {}
    # ----------------- START -----------------
    nodes[UserSteps.START.value] = UXNode(
        UserSteps.START.value,
        keyboard=Pages.HOME.value,
        description=Messages.START_TEXT.value,
        trigger=Messages.START_TRIGGER.value,
    )
