import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Chess Mind Map")
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)


        # PAGE 0

        self.page0 = Gtk.Box()
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.page0.pack_start(listbox, True, True, 0)



        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l3 = Gtk.Label("Squares it protected/protecting", xalign=0)
        vbox.pack_start(l3, True, True, 0)

        self.s3 = Gtk.Switch()
        self.s3.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s3, False, True, 0)

        listbox.add(row)

        # row = Gtk.ListBoxRow()
        # hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        # row.add(hbox)
        # vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # hbox.pack_start(vbox, True, True, 0)
        #
        # l4 = Gtk.Label("Squares it protects now", xalign=0)
        # vbox.pack_start(l4, True, True, 0)
        #
        # self.s4 = Gtk.Switch()
        # self.s4.props.valign = Gtk.Align.CENTER
        # hbox.pack_start(self.s4, False, True, 0)
        #
        # listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l99 = Gtk.Label("Closed/opened lines", xalign=0)
        vbox.pack_start(l99, True, True, 0)

        self.s99 = Gtk.Switch()
        self.s99.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s99, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l2 = Gtk.Label("Enemy intention (profylaxis)", xalign=0)
        vbox.pack_start(l2, True, True, 0)

        self.s2 = Gtk.Switch()
        self.s2.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s2, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l5 = Gtk.Label("Find tactical weaknesses", xalign=0)
        vbox.pack_start(l5, True, True, 0)

        self.s5 = Gtk.Switch()
        self.s5.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s5, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l6 = Gtk.Label("Find candidate moves", xalign=0)
        vbox.pack_start(l6, True, True, 0)

        self.s6 = Gtk.Switch()
        self.s6.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s6, False, True, 0)

        listbox.add(row)


        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l7 = Gtk.Label("Imagine possible answer and calculate", xalign=0)
        vbox.pack_start(l7, True, True, 0)

        self.s7 = Gtk.Switch()
        self.s7.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s7, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        l11 = Gtk.Label("Imagine drawbacks of enemy answer", xalign=0)
        vbox.pack_start(l11, True, True, 0)

        self.s11 = Gtk.Switch()
        self.s11.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.s11, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        self.zero_next_button = Gtk.Button(label="Done")
        self.zero_next_button.connect("clicked", self.zero_button_clicked)
        hbox.pack_start(self.zero_next_button, True, True, 0)

        listbox.add(row)

        self.page0.set_border_width(10)
        self.notebook.append_page(self.page0, Gtk.Label('Move'))

        # PAGE 1

        self.page1 = Gtk.Box()
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.page1.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label("King's Position", xalign=0)
        vbox.pack_start(label1, True, True, 0)

        self.switch1 = Gtk.Switch()
        self.switch1.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch1, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Unprotected Pieces", xalign=0)

        self.switch2 = Gtk.Switch()
        self.switch2.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch2, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Alignments & Pins", xalign=0)

        self.switch3 = Gtk.Switch()
        self.switch3.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch3, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Knight Fork Distance", xalign=0)

        self.switch4 = Gtk.Switch()
        self.switch4.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch4, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Trapped Pieces", xalign=0)

        self.switch5 = Gtk.Switch()
        self.switch5.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch5, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Overloaded Defenders", xalign=0)

        self.switch6 = Gtk.Switch()
        self.switch6.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch6, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Defence Too Far Away", xalign=0)

        self.switch7 = Gtk.Switch()
        self.switch7.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch7, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        self.first_next_button = Gtk.Button(label="Done")
        self.first_next_button.connect("clicked", self.first_button_clicked)
        hbox.pack_start(self.first_next_button, True, True, 0)

        listbox.add(row)

        self.page1.set_border_width(10)
        self.notebook.append_page(self.page1, Gtk.Label('Tactical Analysis'))

        # SECOND TAB

        self.page2 = Gtk.Box()
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.page2.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_1 = Gtk.Label("Material Advantage", xalign=0)
        vbox.pack_start(label_1, True, True, 0)

        self.switch_1 = Gtk.Switch()
        self.switch_1.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_1, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_2 = Gtk.Label("Imminent Threats", xalign=0)
        vbox.pack_start(label_2, True, True, 0)

        self.switch_2 = Gtk.Switch()
        self.switch_2.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_2, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_3 = Gtk.Label("Kings Position and Safety", xalign=0)
        vbox.pack_start(label_3, True, True, 0)

        self.switch_3 = Gtk.Switch()
        self.switch_3.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_3, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_4 = Gtk.Label("Open Lines Control", xalign=0)
        vbox.pack_start(label_4, True, True, 0)

        self.switch_4 = Gtk.Switch()
        self.switch_4.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_4, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_5 = Gtk.Label("Pawn Structures", xalign=0)
        vbox.pack_start(label_5, True, True, 0)

        self.switch_5 = Gtk.Switch()
        self.switch_5.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_5, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_6 = Gtk.Label("Piece Development & Place", xalign=0)
        vbox.pack_start(label_6, True, True, 0)

        self.switch_6 = Gtk.Switch()
        self.switch_6.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_6, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label_7 = Gtk.Label("Center & Space", xalign=0)
        vbox.pack_start(label_7, True, True, 0)

        self.switch_7 = Gtk.Switch()
        self.switch_7.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switch_7, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        self.second_next_button = Gtk.Button(label="Done")
        self.second_next_button.connect("clicked", self.second_button_clicked)
        hbox.pack_start(self.second_next_button, True, True, 0)

        listbox.add(row)

        self.page2.set_border_width(10)
        self.notebook.append_page(self.page2, Gtk.Label('Strategical Analysis'))

        # FORK TAB

        self.page3 = Gtk.Box()
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.page3.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        labell1 = Gtk.Label("Fork square protected", xalign=0)
        vbox.pack_start(labell1, True, True, 0)

        self.switchh1 = Gtk.Switch()
        self.switchh1.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.switchh1, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Protecting piece constrained", xalign=0)

        self.switchh2 = Gtk.Switch()
        self.switchh2.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh2, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Protecting piece can be captured", xalign=0)

        self.switchh3 = Gtk.Switch()
        self.switchh3.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh3, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Protecting piece guards smth else", xalign=0)

        self.switchh4 = Gtk.Switch()
        self.switchh4.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh4, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Captured fork opens lines/possibilities", xalign=0)

        self.switchh5 = Gtk.Switch()
        self.switchh5.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh5, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Check that moves the king/pieces to fork", xalign=0)

        self.switchh6 = Gtk.Switch()
        self.switchh6.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh6, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Exchange piece that defends fork", xalign=0)

        self.switchh7 = Gtk.Switch()
        self.switchh7.props.valign = Gtk.Align.CENTER

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switchh7, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        self.fork_done_button = Gtk.Button(label="Done")
        self.fork_done_button.connect("clicked", self.fork_done_button_clicked)
        hbox.pack_start(self.fork_done_button, True, True, 0)

        listbox.add(row)

        self.page3.set_border_width(10)
        self.notebook.append_page(self.page3, Gtk.Label('Fork'))

    def zero_button_clicked(self, widget):
        # self.s1.set_state(0)
        self.s2.set_state(0)
        self.s3.set_state(0)
        # self.s4.set_state(0)
        self.s5.set_state(0)
        self.s6.set_state(0)
        self.s7.set_state(0)
        self.s99.set_state(0)
        self.s11.set_state(0)
        # self.notebook.set_current_page(1)


    def first_button_clicked(self, widget):
        self.switch1.set_state(0)
        self.switch2.set_state(0)
        self.switch3.set_state(0)
        self.switch4.set_state(0)
        self.switch5.set_state(0)
        self.switch6.set_state(0)
        self.switch7.set_state(0)
        self.notebook.set_current_page(1)

    def second_button_clicked(self, widget):
        self.switch_1.set_state(0)
        self.switch_2.set_state(0)
        self.switch_3.set_state(0)
        self.switch_4.set_state(0)
        self.switch_5.set_state(0)
        self.switch_6.set_state(0)
        self.switch_7.set_state(0)
        self.notebook.set_current_page(0)

    def fork_done_button_clicked(self, widget):
        self.switchh1.set_state(0)
        self.switchh2.set_state(0)
        self.switchh3.set_state(0)
        self.switchh4.set_state(0)
        self.switchh5.set_state(0)
        self.switchh6.set_state(0)
        self.switchh7.set_state(0)
        # self.notebook.set_current_page(1)



win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
# Window Always On Top
win.set_keep_above(True)
Gtk.main()

