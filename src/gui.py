""" @package gui
    @author: Tadeas Vintrlik <xvintr04>
    Documentation for main GUI package
"""
from gi.repository import Gtk, Gdk
from gi.repository import Pango


def main():
    """ @brief Main gui function
        Start the cycle for gui drawing
    """
    builder = Gtk.Builder()
    builder.add_from_file("../gui/prototype1.glade")
    window = builder.get_object("window1")
    change_fonts(builder)
    connect_signals(builder)
    window.show_all()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()


def user_input(self, entry):
    """ @brief inputs the desired symbol into the entry
        @param self the caller of the function
        @param entry the entry where to add the new symbol
    """
    entry.set_text(entry.get_text() + self.get_label())


def user_result(self, entry):
    """ @brief calculates the result from the entry
        @param *self the caller of the function
        @param entry the entry where to show the result
    """
    del self  # Unused for now
    entry.set_text("This should show the result")


def rem_char(self, entry):
    """ @brief removes last character from entry
        @param *self the caller of the function
        @param entry the entry where to remove the character
    """
    del self  # Unused for now
    text = entry.get_text()
    entry.set_text(text[:-1])


def clear(self, entry):
    """ @brief clears the entry
        @param *self the caller of the function
        @param entry the entry which to clear
    """
    del self  # Unused for now
    entry.set_text("")


def change_fonts(builder):
    """ @brief change fonts of all elements
        @param builder builder class for making gui from glade
    """
    font = Pango.FontDescription('Sans Bold 18')
    change_font_grid(builder, 'numbers', font, 4, 3)
    change_font_grid(builder, 'operators', font, 5, 2)
    entry = builder.get_object('entry')
    entry.modify_font(font)
    entry.set_alignment(1)


def on_key_pressed(widget, event, entry):
    """ @brief handler for key-press-event
        @param widget widget active when key press occured
        @param event type of event that occured
        @param entry entry filed to modify
    """
    inputables = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                  "+", "-", "/", "*", "!", "^"]
    if event.keyval == Gdk.KEY_Return or chr(event.keyval) == "=":
        user_result(widget, entry)
    elif event.keyval == Gdk.KEY_c:
        clear(widget, entry)
    elif event.keyval == Gdk.KEY_BackSpace:
        rem_char(widget, entry)
    elif event.keyval == Gdk.KEY_s:
        entry.set_text(entry.get_text() + "√")
    elif event.keyval == Gdk.KEY_r:
        entry.set_text(entry.get_text() + "n√")
    elif chr(event.keyval) in inputables:
        entry.set_text(entry.get_text() + chr(event.keyval))


def connect_signals(builder):
    """ @brief connect signals to all buttons
        @param builder builder class for making gui from glade
    """
    connect_signal_grid(builder, 'numbers', 4, 3)
    connect_signal_grid(builder, 'operators', 5, 2)
    entry = builder.get_object('entry')
    builder.get_object('equals').connect("clicked", user_result, entry)
    builder.get_object('rem').connect("clicked", rem_char, entry)
    builder.get_object('clr').connect("clicked", clear, entry)
    window = builder.get_object("window1")
    window.connect("key-press-event", on_key_pressed, entry)


def connect_signal_grid(builder, grid_name, rows, columns):
    """ @brief connect all buttons in grid to callbacks
        @param builder builder class for making gui from glade
        @param grid_name name of the grid to use
        @param rows number of rows of the grid
        @param columns number of coulmns of the grid
    """
    exceptions = ["=", "REM", "CLR"]
    entry = builder.get_object("entry")
    grid = builder.get_object(grid_name)
    for i in range(0, columns):
        for j in range(0, rows):
            button = grid.get_child_at(i, j)
            if button.get_label() in exceptions:
                continue
            button.connect("clicked", user_input, entry)


def change_font_grid(builder, grid_name, font, rows, columns):
    """ @brief change fonts in a grid
        Change fonts of all children in the GtkGrid element
        @param builder builder class for making gui from glade
        @param grid_name name of the grid to use
        @param font font to change it to
        @param rows number of rows of the grid
        @param columns number of coulmns of the grid
    """
    grid = builder.get_object(grid_name)
    for i in range(0, columns):
        for j in range(0, rows):
            button = grid.get_child_at(i, j)
            button.modify_font(font)


if __name__ == "__main__":
    APP = Gtk.Application(application_id='Calc')
    APP.connect('activate', main)
    APP.run(None)
    main()
