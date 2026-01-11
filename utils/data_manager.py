from config.apps_config import APPS

def get_all_apps():
    """Returns all apps"""
    return APPS

def get_app_by_id(app_id):
    """Returns a specific app by ID"""
    for app in APPS:
        if app['id'] == app_id:
            return app
    return None
