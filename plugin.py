import sublime, sublime_plugin
class TemplatePluginCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Hello world")
        self.view.insert(edit, 0, "Hello, World!")