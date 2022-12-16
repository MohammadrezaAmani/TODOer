import enum

class Messages(enum.Enum):
    """Enum class for messages to be displayed to the user."""
    TASK = "Task"
    REMINDER = "Reminder"
    MY_PROFILE = "My Profile"
    PLOT = "Plot"
    # ------------------------- start ---------------------------------
    START_TEXT = "welcome to todoer bot."
    START_TRIGGER = "/start"