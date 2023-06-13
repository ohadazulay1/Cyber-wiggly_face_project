from enum import Enum

class commonUtils:

    PositionLeftRight = Enum("PositionLeftRight", ["LEFT", "RIGHT"])

    #הופך את השיא מהדאטאבייס (פלואוט) לסטרינג קריא
    @staticmethod
    def get_time_str(score: float) -> str:
        minutes = int(score // 60)
        seconds = int(score % 60)
        milliseconds = int((score % 1) * 1000)
        time_text = f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        return time_text


