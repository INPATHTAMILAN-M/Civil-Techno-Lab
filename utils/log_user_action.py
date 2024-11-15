from account.models import UserActivity

def log_user_activity(user, action, details=None):
    UserActivity.objects.create(
        user=user,
        action=action,
        details=details
    )
