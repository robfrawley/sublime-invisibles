import sublime
import sublime_plugin

class ToggleInvisiblesCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        white_space = "selection" if settings.get("draw_white_space", "selection") != "selection" else "all"
        settings.set("draw_white_space", white_space)
        sublime.save_settings("Preferences.sublime-settings")
        return "off" if white_space == "selection" else "on"

    def is_checked(self):
    	settings = sublime.load_settings("Preferences.sublime-settings")
        return settings.get("draw_white_space", "selection") != "selection"