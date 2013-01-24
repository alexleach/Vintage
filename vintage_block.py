from vintage import expand_to_block

class ViReverseBlockSelectionsDirection(sublime_plugin.TextCommand):
    def run(self, edit):
        x0, y0 = self.view._block_begin
        xf, yf = self.view._block_end
        self.view._block_begin = (x0, yf)
        self.view._block_end = (xf, y0)

        new_sels = []
        for s in self.view.sel():
            new_sels.append(sublime.Region(s.b, s.a))
        self.view.sel().clear()
        for s in new_sels:
            self.view.sel().add(s)

