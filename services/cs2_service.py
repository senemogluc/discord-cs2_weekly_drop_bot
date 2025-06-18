from datetime import datetime, timedelta
import pytz


RESET_WEEKDAY = 2  # Wednesday (Monday=0)
RESET_HOUR_UTC = 0  # 00:00 UTC corresponds to 03:00 Istanbul time
RESET_MINUTE = 0

def _format_timedelta(td: timedelta) -> str:
    """Helper function to format a timedelta into a human-readable string."""
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes = remainder // 60

    # Handle pluralization for a cleaner output
    day_str = f"{days} day{'s' if days != 1 else ''}"
    hour_str = f"{hours} hour{'s' if hours != 1 else ''}"
    minute_str = f"{minutes} minute{'s' if minutes != 1 else ''}"

    return f"{day_str}, {hour_str}, and {minute_str} left until the next CS2 reset."

def cs2_weekly_reset_countdown(timezone_str: str = "Europe/Istanbul") -> str:
    """
    Calculates the time remaining until the next CS2 weekly reset.

    The reset happens every Wednesday at 00:00 UTC (which is 03:00 in Istanbul local time).

    Args:
        timezone_str (str): The user's timezone in pytz format (default is Europe/Istanbul).

    Returns:
        str: A human-readable string showing days, hours, and minutes left until reset.
    """
    # Current time in user's timezone
    user_tz = pytz.timezone(timezone_str)
    now_local = datetime.now(user_tz)

    # Current time in UTC
    now_utc = datetime.now(pytz.utc)
    weekday_utc = now_utc.weekday()

    # Calculate days until next reset day (Wednesday)
    days_until_reset = (RESET_WEEKDAY - weekday_utc) % 7
    # If today is reset day but reset hour has passed, schedule for next week
    if days_until_reset == 0 and now_utc.hour >= RESET_HOUR_UTC:
        days_until_reset = 7

    # Next reset time in UTC
    next_reset_utc = (now_utc + timedelta(days=days_until_reset)).replace(
        hour=RESET_HOUR_UTC, minute=RESET_MINUTE, second=0, microsecond=0
    )

    # Convert reset time to user's local timezone
    next_reset_local = next_reset_utc.astimezone(user_tz)

    # Calculate remaining time until reset
    time_left = next_reset_local - now_local

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes = remainder // 60

    return _format_timedelta(time_left)
