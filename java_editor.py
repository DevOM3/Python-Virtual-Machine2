from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox
import os
import subprocess
import tkinter.font as tkf

fontoption = "lucida"
fontstyle = "normal"
fontsize = 12

def font():
    font_ls = list(tkf.families())

    def set_op():
        textarea.config(font=f"{font_ls[font.curselection()[0]]} {fontsize} {fontstyle}")

    font_root = Toplevel(root)
    font_root.title("Font")
    font_root.geometry("250x300")

    font_label = Label(font_root, text="Font\n\n", font="ariel 21")
    font_label.place(x=21, y=3)

    scroll_y = Scrollbar(font_root)
    font = Listbox(font_root, font="lucida 11", yscrollcommand=scroll_y.set)
    font.place(x=21, y=51)
    scroll_y.pack(fill=Y, side=RIGHT)
    scroll_y.config(command=font.yview)

    for i in tkf.families():
        font.insert(END, i)

    Button(font_root, text="Ok", font="lucida 11", command=set_op, width=7).place(x=111, y=251)

    font_root.mainloop()

def new():
    textarea.delete(1.0, END)

def style():
    style_ls = ["normal", "bold", "italic", "roman", "underline"]

    def set_style():
        textarea.config(font=f"{fontstyle} {fontsize} {style_ls[style.curselection()[0]]}")

    style_root = Toplevel(root)
    style_root.title("Style")
    style_root.geometry("250x300")

    style_label = Label(style_root, text="Font Style\n\n", font="ariel 21")
    style_label.place(x=21, y=3)

    style = Listbox(style_root, font="lucida 11")
    style.place(x=21, y=51)

    style.insert(END, "normal")
    style.insert(END, "bold")
    style.insert(END, "italic")
    style.insert(END, "roman")
    style.insert(END, "underline")

    Button(style_root, text="Ok", font="lucida 11", command=set_style, width=7).place(x=111, y=251)
    style_root.mainloop()


def size():
    size_ls = list(range(8, 73))

    def set_size():
        textarea.config(font=f"{fontoption} {size_ls[size.curselection()[0]]} {fontstyle}")

    size_root = Toplevel(root)
    size_root.title("Size")
    size_root.geometry("250x360")

    size_label = Label(size_root, text="Font Size\n\n", font="ariel 21")
    size_label.place(x=21, y=3)

    scroll_y = Scrollbar(size_root)
    size = Listbox(size_root, font="lucida 11", yscrollcommand=scroll_y.set)
    size.place(x=21, y=51)
    scroll_y.pack(fill=Y, side=RIGHT)
    scroll_y.config(command=size.yview)

    for i in range(8, 73):
        size.insert(END, i)

    Button(size_root, text="Ok", font="lucida 11", command=set_size, width=7).place(x=111, y=251)
    size_root.mainloop()


def f_help():
    messagebox.showinfo("JAVA Editor",
                 "1) You can Write the Java program in the text area \n"
                 "2) The option to Save , Make new file is available in the File menu section \n"
                 "3) You can Exit whenever you want to Exit and we will ask you if any problem or warning is there \n"
                 "4) Fonts option is also available in th is Version to personalize the Editor settings \n"
                 "5) If you have some queries Visit Contact Us section in the Help menu\n")


def contact():
    messagebox.showinfo("C Editor",
                 "Creator : Om Londhe, Ajay Rathod\n"
                 "Contact no. : 7276594467\n7972526888\n"
                 "E-mail id : oplondhe@gmaiil.com, rathodajay1202@gmail.com\n")


def about():
    messagebox.showinfo("JAVA Editor",
                 "This is the JAVA editor .\n"
                 "It is made by Om Londhe and Ajay Rathod using the tKinter package in the Python for Graphical User "
                 "Interface(GUI) purpose......\n"
                 "The version of Python used is the Python 3.7.4 and 3.8.0\n")


def save():
    global file_name, s, o, parent


    if file_name is None:
        ls = [('Java Files', '*.java')]
        file_name = asksaveasfilename(initialdir="C:\\PythonProject\\JavaEditor\\", initialfile="Untitled",
                                      filetypes=ls,
                                      defaultextension=ls)
        if file_name == "":
            file_name = None
        else:
            f = open(file_name, "w")
            f.write(textarea.get(1.0, END))
            f.close()
    else:
        f = open(file_name, "w")
        f.write(textarea.get(1.0, END))
        f.close()

    s = str(file_name).split(".")
    f = str(s[0])
    o = f[f.rfind("/"):][1:]

def saveas():
    file_name = "Untitled"
    file_name = asksaveasfilename(initialfile=f"{file}", filetypes=[("C programming file", "*.c")],
                             defaultextension=".c")
    ls = [('Java Files', '*.java')]
    file_name = asksaveasfilename(initialdir="C:\\PythonProject\\JavaEditor\\", initialfile="Untitled", filetypes=ls,
                                  defaultextension=ls)
    f = open(file, "w")
    f.write(textarea.get(1.0, END))
    f.close()

    s = str(file_name).split(".")
    f = str(s[0])
    o = f[f.rfind("/"):][1:]

def save1():
    f = open(file_name, "w")
    st = textarea.get(0.0, END)
    f.write(st)
    f.close()

def open():
    ls = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt'), ('Java Files', '*.java')]
    fil = askopenfilename(initialdir="C:\\PythonProject\\JavaEditor\\", filetypes=ls, defaultextension='.java')
    sop = open(fil, "r")
    textarea.delete(0.0, END)
    textarea.insert(0.0, sop.read())

def class1():
    textarea.tag_config('key', foreground="Purple")
    textarea.insert(INSERT, "class ", 'key')
    # textarea.insert(INSERT, f'{o}\n' + "{\n\t")
    textarea.insert(INSERT,"\n\t")
    textarea.insert(INSERT, "public static void ", 'key')
    textarea.insert(INSERT, "main(String []args)\n\t{\n\t\t\n\t}\n}\n")
    # textarea.insert(INSERT, f'class {o}\n' + "{\n\tpublic static void main(String []args)\n\t{\n\t\t\n\t}\n}\n")

def new_window():
    subprocess.call(['python', 'editor1.py'])
global i
i = 0


def dark():
    global i
    i=i+1
    if i % 2 != 0:
        root.config(bg="black")
        textarea.config(fg="white",bg="gray")
        m.config(fg="blue",bg="gray")

    elif i % 2 == 0:
        textarea.config(fg="black",bg="white")


def undo():
    textarea.event_generate("<<Undo>>")


def redo():
    try:
        textarea.edit_redo()
    except:
        pass

def stop():
    global file
    if file is None:
        e = messagebox.askyesno("Exit ", "Do you want to Save you File ?")
        if e == YES:
            save()
            exit()
        else:
            exit()
    else:
        exit()


def f_print():
    os.startfile(textarea, "print")

def delete():
    textarea.delete(1.0, END)

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def select():
    textarea.tag_add("sel", '1.0', 'end')

def Deselect():
    textarea.tag_remove("sel", '1.0', 'end')

def compile():
    save1
    os.system(f'start cmd /c "javac {file_name}"')
def run():
    f = str(s[0])
    o = f[:f.rfind("/")]
    a = f[f.rfind("/"):]
    fi = a[1:]
    path = o[2:]
    os.system(f'start cmd /k "C: & cd{path} & java {fi}"')


def rightclick(eve):
    popup = Menu(root, tearoff=0)
    popup.add_command(label="Undo", command=undo)
    popup.add_command(label="cut", command=cut)
    popup.add_command(label="copy", command= copy)
    popup.add_command(label="paste", command=paste)
    popup.add_command(label="Delete", command=delete)
    popup.add_command(label="Select All", command=select)
    popup.add_command(label="Compile", command=compile)
    popup.add_command(label="Run", command=run)
    try:
        popup.tk_popup(300, 300, 1)
    finally:
        popup.grab_release()


def edit(event):
    textarea.tag_config('key', foreground="Purple")
    ls=textarea.index(INSERT)
    if textarea.get("%s - 2c" %ls , ls) == "im":
        print("Enter")
        popup = Menu(root, tearoff=0)
        popup.add_command(label="import", command=lambda: text("import"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s-5c" %ls , ls) == 'java.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="util", command=lambda: text("util"))
        popup.add_command(label="io", command=lambda: text("io"))
        popup.add_command(label="sql", command=lambda: text("sql"))
        popup.add_command(label="awt", command=lambda: text("awt"))
        popup.add_command(label="applet", command=lambda: text("applet"))
        popup.add_command(label="beans", command=lambda: text("beans"))
        popup.add_command(label="math", command=lambda: text("math"))
        popup.add_command(label="net", command=lambda: text("net"))
        popup.add_command(label="nio", command=lambda: text("nio"))
        popup.add_command(label="rmi", command=lambda: text("rmi"))
        popup.add_command(label="security", command=lambda: text("security"))
        popup.add_command(label="text", command=lambda: text("text"))
        popup.add_command(label="time", command=lambda: text("time"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s-12c" %ls , ls) == 'java.applet.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="Applet", command=lambda: text("Applet"))
        popup.add_command(label="AppletContext", command=lambda: text("AppletContext"))
        popup.add_command(label="AppletStub", command=lambda: text("AppletStub"))
        popup.add_command(label="AudioClip", command=lambda: text("AudioClip"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()
    if textarea.get("%s-2c" %ls,ls) == 'ne':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="new", command=lambda: text("new"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()
    if textarea.get("%s-15c" %ls , ls) == 'java.awt.event.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="ActionListener", command=lambda: text("ActionListener"))
        popup.add_command(label="ActionEvent", command=lambda: text("ActionEvent"))
        popup.add_command(label="ComponentAdapter", command=lambda: text("ComponentAdapter"))
        popup.add_command(label="ComponentEvent", command=lambda: text("ComponentEvent"))
        popup.add_command(label="ComponentListener", command=lambda: text("ComponentListener"))
        popup.add_command(label="ContainerAdapter", command=lambda: text("ContainerAdapter"))
        popup.add_command(label="ContainerEvent", command=lambda: text("ContainerEvent"))
        popup.add_command(label="ContainerListener", command=lambda: text("ContainerListener"))
        popup.add_command(label="FocusAdapter", command=lambda: text("FocusAdapter"))
        popup.add_command(label="FocusListener", command=lambda: text("FocusListener"))
        popup.add_command(label="FocusEvent", command=lambda: text("FocusEvent"))
        popup.add_command(label="ItemEvent", command=lambda: text("ItemEvent"))
        popup.add_command(label="ItemListener", command=lambda: text("ItemListener"))
        popup.add_command(label="KeyAdapter", command=lambda: text("KeyAdapter"))
        popup.add_command(label="KeyEvent", command=lambda: text("KeyEvent"))
        popup.add_command(label="KeyListener", command=lambda: text("KeyListener"))
        popup.add_command(label="MouseAdapter", command=lambda: text("MouseAdapter"))
        popup.add_command(label="MouseEvent", command=lambda: text("MouseEvent"))
        popup.add_command(label="MouseListener", command=lambda: text("MouseListener"))
        popup.add_command(label="PaintEvent", command=lambda: text("PaintEvent"))
        popup.add_command(label="MouseMotionListener", command=lambda: text("MouseMotionListener"))
        popup.add_command(label="TextEvent", command=lambda: text("TextEvent"))
        popup.add_command(label="TextListener", command=lambda: text("TextListener"))
        popup.add_command(label="WindowAdapter", command=lambda: text("WindowAdapter"))
        popup.add_command(label="WindowEvent", command=lambda: text("WindowEvent"))
        popup.add_command(label="WindowFocusListener", command=lambda: text("WindowFocusListener"))
        popup.add_command(label="WindowListener", command=lambda: text("WindowListener"))
        popup.add_command(label="WindowStateListener", command=lambda: text("WindowStateListener"))

        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()
    if textarea.get("%s-7c" %ls , ls) == 'System.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="in", command=lambda: text("in"))
        popup.add_command(label="out", command=lambda: text("out"))
        popup.add_command(label="err", command=lambda: text("err"))
        popup.add_command(label="exit", command=lambda: text("exit"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()
    if textarea.get("%s-11c" % ls, ls) == 'System.out.'or textarea.get("%s-11c" % ls, ls) == 'System.err.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="print", command=lambda: text("print"))
        popup.add_command(label="println", command=lambda: text("println"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s-8c" %ls , ls) == 'java.io.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="BufferedInputStream", command=lambda: text("BufferedInputStream"))
        popup.add_command(label="BufferedOutputStream", command=lambda: text("BufferedOutputStream"))
        popup.add_command(label="DataInputStream", command=lambda: text("DataInputStream"))
        popup.add_command(label="InputStreamReader", command=lambda: text("InputStreamReader"))
        popup.add_command(label="File", command=lambda: text("File"))
        popup.add_command(label="IOException", command=lambda: text("IOException"))
        popup.add_command(label="FileReader", command=lambda: text("FileReader"))
        popup.add_command(label="FileWriter", command=lambda: text("Filewriter"))
        popup.add_command(label="PrintReader", command=lambda: text("PrintReader"))
        popup.add_command(label="PrintWriter", command=lambda: text("PrintWriter"))
        popup.add_command(label="Reader", command=lambda: text("Reader"))
        popup.add_command(label="Writer", command=lambda: text("Writer"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s-3c" % ls, ls) == 'sop':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="event", command=lambda :text("SOP"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()


    if textarea.get("%s-9c" %ls , ls) == 'java.awt.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="event", command=lambda: text("event"))
        popup.add_command(label="Button", command=lambda: text("Button"))
        popup.add_command(label="Canvas", command=lambda: text("Canvas"))
        popup.add_command(label="CheckBox", command=lambda: text("CheckBox"))
        popup.add_command(label="CheckBoxMenuItem", command=lambda: text("CheckBoxMenuItem"))
        popup.add_command(label="Choice", command=lambda: text("Choice"))
        popup.add_command(label="Color", command=lambda: text("Color"))
        popup.add_command(label="Component", command=lambda: text("Component"))
        popup.add_command(label="Container", command=lambda: text("Container"))
        popup.add_command(label="Dialog", command=lambda: text("Dialog"))
        popup.add_command(label="FlowLayout", command=lambda: text("FlowLayout"))
        popup.add_command(label="Font", command=lambda: text("Font"))
        popup.add_command(label="Frame", command=lambda: text("Frame"))
        popup.add_command(label="Graphics", command=lambda: text("Graphics"))
        popup.add_command(label="Image", command=lambda: text("Image"))
        popup.add_command(label="Label", command=lambda: text("Label"))
        popup.add_command(label="List", command=lambda: text("List"))
        popup.add_command(label="Menu", command=lambda: text("Menu"))
        popup.add_command(label="MenuBar", command=lambda: text("MenuBar"))
        popup.add_command(label="MenuItem", command=lambda: text("MenuItem"))
        popup.add_command(label="Paint", command=lambda: text("Paint"))
        popup.add_command(label="Panel", command=lambda: text("Panel"))
        popup.add_command(label="Polygon", command=lambda: text("Polygon"))
        popup.add_command(label="PopupMenu", command=lambda: text("PopupMenu"))
        popup.add_command(label="Rectangle", command=lambda: text("Rectangle"))
        popup.add_command(label="ScrollBar", command=lambda: text("ScrollBar"))
        popup.add_command(label="ScrollPane", command=lambda: text("ScrollPane"))
        popup.add_command(label="Shape", command=lambda: text("Shape"))
        popup.add_command(label="Stroke", command=lambda: text("Stroke"))
        popup.add_command(label="TextArea", command=lambda: text("TextArea"))
        popup.add_command(label="TextField", command=lambda: text("TextField"))
        popup.add_command(label="ToolKit", command=lambda: text("ToolKit"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s-10c" %ls , ls) == 'java.util.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="Calendar", command=lambda: text("Calendar"))
        popup.add_command(label="Collection", command=lambda: text("Collection"))
        popup.add_command(label="Collections", command=lambda: text("Collections"))
        popup.add_command(label="Date", command=lambda: text("Date"))
        popup.add_command(label="Dictionary", command=lambda: text("Dictionary"))
        popup.add_command(label="Enumeration", command=lambda: text("Enumeration"))
        popup.add_command(label="EnumMap", command=lambda: text("EnumMap"))
        popup.add_command(label="EnumSet", command=lambda: text("EnumSet"))
        popup.add_command(label="HashMap", command=lambda: text("HashMap"))
        popup.add_command(label="HashSet", command=lambda: text("HashSet"))
        popup.add_command(label="HashTable", command=lambda: text("HashTable"))
        popup.add_command(label="LinkedHashMap", command=lambda: text("LinkedHashMap"))
        popup.add_command(label="LinkedHashSet", command=lambda: text("LinkedHashSet"))
        popup.add_command(label="LinkedList", command=lambda: text("LinkedList"))
        popup.add_command(label="List", command=lambda: text("List"))
        popup.add_command(label="Map", command=lambda: text("Map"))
        popup.add_command(label="Objects", command=lambda: text("Objects"))
        popup.add_command(label="Queue", command=lambda: text("Queue"))
        popup.add_command(label="Random", command=lambda: text("Random"))
        popup.add_command(label="Scanner", command=lambda: text("Scanner"))
        popup.add_command(label="Set", command=lambda: text("Set"))
        popup.add_command(label="Stack", command=lambda: text("Stack"))
        popup.add_command(label="TimeZone", command=lambda: text("TimeZone"))
        popup.add_command(label="Vector", command=lambda: text("Vector"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s - 6c" %ls , ls) == 'javax.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="swing", command=lambda: text("swing"))
        popup.add_command(label="accessibility", command=lambda: text("accessibility"))
        popup.add_command(label="annotation", command=lambda: text("annotation"))
        popup.add_command(label="imageio", command=lambda: text("imageio"))
        popup.add_command(label="lang", command=lambda: text("lang"))
        popup.add_command(label="management", command=lambda: text("management"))
        popup.add_command(label="naming", command=lambda: text("naming"))
        popup.add_command(label="print", command=lambda: text("print"))
        popup.add_command(label="rmi", command=lambda: text("rmi"))
        popup.add_command(label="script", command=lambda: text("script"))
        popup.add_command(label="security", command=lambda: text("security"))
        popup.add_command(label="sound", command=lambda: text("sound"))
        popup.add_command(label="sql", command=lambda: text("sql"))
        popup.add_command(label="tools", command=lambda: text("tools"))
        popup.add_command(label="xml", command=lambda: text("xml"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s - 12c" %ls , ls) == 'javax.swing.':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="JApplet", command=lambda: text("JApplet"))
        popup.add_command(label="JButton", command=lambda: text("JButton"))
        popup.add_command(label="JCheckBox", command=lambda: text("JCheckBox"))
        popup.add_command(label="JCheckBoxMenuItem", command=lambda: text("JCheckBoxMenuItem"))
        popup.add_command(label="JColorChooser", command=lambda: text("JColorChooser"))
        popup.add_command(label="JComboBox", command=lambda: text("JComboBox"))
        popup.add_command(label="JComponent", command=lambda: text("JComponent"))
        popup.add_command(label="JDesktoPane", command=lambda: text("JDesktoPane"))
        popup.add_command(label="JDialog", command=lambda: text("JDialog"))
        popup.add_command(label="JEditorPane", command=lambda: text("JEditorPane"))
        popup.add_command(label="JFileChooser", command=lambda: text("JFileChooser"))
        popup.add_command(label="JFormattedTextField", command=lambda: text("JFormattedTextField"))
        popup.add_command(label="JFrame", command=lambda: text("JFrame"))
        popup.add_command(label="JInternalFrame", command=lambda: text("JInternalFrame"))
        popup.add_command(label="JLabel", command=lambda: text("JLabel"))
        popup.add_command(label="JLayer", command=lambda: text("JLayer"))
        popup.add_command(label="JLayeredPane", command=lambda: text("JLayeredPane"))
        popup.add_command(label="JList", command=lambda: text("JList"))
        popup.add_command(label="JMenu", command=lambda: text("JMenu"))
        popup.add_command(label="JMenuBar", command=lambda: text("JMenuBar"))
        popup.add_command(label="JMenuItem", command=lambda: text("JMenuItem"))
        popup.add_command(label="JOptionPane", command=lambda: text("JOptionPane"))
        popup.add_command(label="JPanel", command=lambda: text("JPanel"))
        popup.add_command(label="JPasswordField", command=lambda: text("JPasswordField"))
        popup.add_command(label="JPopupMenu", command=lambda: text("JPopupMenu"))
        popup.add_command(label="JProgressBar", command=lambda: text("JProgressBar"))
        popup.add_command(label="JRadioButton", command=lambda: text("JRadioButton"))
        popup.add_command(label="JRadioButtonMenuItem", command=lambda: text("JRadioButtonMenuItem"))
        popup.add_command(label="JRootPane", command=lambda: text("JRootPane"))
        popup.add_command(label="JScrollBar", command=lambda: text("JScrollBar"))
        popup.add_command(label="JSeparator", command=lambda: text("JSeparator"))
        popup.add_command(label="JSlider", command=lambda: text("JSlider"))
        popup.add_command(label="JSpinner", command=lambda: text("JSpinner"))
        popup.add_command(label="JSplitPane", command=lambda: text("JSplitPane"))
        popup.add_command(label="JTabbedPane", command=lambda: text("JTabbedPane"))
        popup.add_command(label="JTextArea", command=lambda: text("JTextArea"))
        popup.add_command(label="JTextField", command=lambda: text("JTextField"))
        popup.add_command(label="JToolBar", command=lambda: text("JToolBar"))
        popup.add_command(label="JTree", command=lambda: text("JTree"))
        popup.add_command(label="JToolTip", command=lambda: text("JToolTip"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s - 2c" % ls, ls) == 'if':
        popup = Menu(root, tearoff=0)
        popup.add_command(label="if..", command=lambda: text("if.."))
        popup.add_command(label="if..else", command=lambda: text("if..else"))
        popup.add_command(label="if.else.if", command=lambda: text("if.else.if"))
        popup.add_command(label="if.if", command=lambda: text("if.if"))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    # if textarea.__getitem__().__contains__("public"):
    #     textarea.tag_config('keyword',foreground='purple')

    if textarea.get("%s - 3c" %ls , ls) == "for":
        popup = Menu(root, tearoff=0)
        popup.add_command(label="for", command=lambda: text("for"))
        popup.add_command(label="for..", command=lambda: text("for.."))
        try:
            popup.tk_popup(event.x_root, event.y_root, 1)
        finally:
            popup.grab_release()

    if textarea.get("%s - 5c" %ls , ls) == "while":
            popup = Menu(root, tearoff=0)
            popup.add_command(label="while..", command=lambda: text("while.."))
            try:
                popup.tk_popup(event.x_root, event.y_root, 1)
            finally:
                popup.grab_release()

    if textarea.get("%s - 2c" %ls , ls) == "do":
            popup = Menu(root, tearoff=0)
            popup.add_command(label="do..while", command=lambda: text("do..while"))
            try:
                popup.tk_popup(event.x_root, event.y_root, 1)
            finally:
                popup.grab_release()
    if textarea.get("%s - 5c" %ls , ls) == "class":
            popup = Menu(root, tearoff=0)
            popup.add_command(label="class..", command=lambda: text("class.."))
            try:
                popup.tk_popup(event.x_root, event.y_root, 1)
            finally:
                popup.grab_release()
    if textarea.get("%s-6c" % ls, ls) == "static":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "static", 'key')
    if textarea.get("%s-6c" % ls, ls) == "return":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "return", 'key')
    if textarea.get("%s-6c" % ls, ls) == "double":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "double", 'key')
    if textarea.get("%s-6c" % ls, ls) == "native":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "native", 'key')
    if textarea.get("%s-3c" % ls, ls) == "int":
        textarea.delete("%s-3c" % ls, ls)
        textarea.insert(INSERT, "int", 'key')
    if textarea.get("%s-4c" % ls, ls) == "byte":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "byte", 'key')
    if textarea.get("%s-5c" % ls, ls) == "short":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "short", 'key')
    if textarea.get("%s-4c" % ls, ls) == "long":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "long", 'key')
    if textarea.get("%s-5c" % ls, ls) == "float":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "float", 'key')
    if textarea.get("%s-4c" % ls, ls) == "char":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "char", 'key')
    if textarea.get("%s-6c" % ls, ls) == "throws":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "throws", 'key')
    if textarea.get("%s-5c" % ls, ls) == "final":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "final", 'key')
    if textarea.get("%s-5c" % ls, ls) == "class":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "class", 'key')
    if textarea.get("%s-6c" % ls, ls) == "public":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "public", 'key')
    if textarea.get("%s-4c" % ls, ls) == "void":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "void", 'key')
    if textarea.get("%s-7c" % ls, ls) == "private":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "private", 'key')
    if textarea.get("%s-9c" % ls, ls) == "protected":
        textarea.delete("%s-9c" % ls, ls)
        textarea.insert(INSERT, "protected", 'key')
    if textarea.get("%s-7c" % ls, ls) == "extends":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "extends", 'key')
    if textarea.get("%s-10c" % ls, ls) == "implements":
        textarea.delete("%s-10c" % ls, ls)
        textarea.insert(INSERT, "implements", 'key')
    if textarea.get("%s-9c" % ls, ls) == "interface":
        textarea.delete("%s-9c" % ls, ls)
        textarea.insert(INSERT, "interface", 'key')
    if textarea.get("%s-3c" % ls, ls) == "for":
        textarea.delete("%s-3c" % ls, ls)
        textarea.insert(INSERT, "for", 'key')
    if textarea.get("%s-2c" % ls, ls) == "do":
        textarea.delete("%s-2c" % ls, ls)
        textarea.insert(INSERT, "do", 'key')
    if textarea.get("%s-6c" % ls, ls) == "switch":
        textarea.delete("%s-6c" % ls, ls)
        textarea.insert(INSERT, "switch", 'key')
    if textarea.get("%s-4c" % ls, ls) == "case":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "case", 'key')
    if textarea.get("%s-5c" % ls, ls) == "while":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "while", 'key')
    if textarea.get("%s-2c" % ls, ls) == "if":
        textarea.delete("%s-2c" % ls, ls)
        textarea.insert(INSERT, "if", 'key')
    if textarea.get("%s-4c" % ls, ls) == "else":
        textarea.delete("%s-4c" % ls, ls)
        textarea.insert(INSERT, "else", 'key')
    if textarea.get("%s-7c" % ls, ls) == "default":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "default", 'key')
    if textarea.get("%s-8c" % ls, ls) == "abstract":
        textarea.delete("%s-8c" % ls, ls)
        textarea.insert(INSERT, "abstract", 'key')
    if textarea.get("%s-8c" % ls, ls) == "strictfp":
        textarea.delete("%s-8c" % ls, ls)
        textarea.insert(INSERT, "strictfp", 'key')
    if textarea.get("%s-12c" % ls, ls) == "synchronised":
        textarea.delete("%s-12c" % ls, ls)
        textarea.insert(INSERT, "synchronised", 'key')
    if textarea.get("%s-7c" % ls, ls) == "package":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "package", 'key')
    if textarea.get("%s-7c" % ls, ls) == "boolean":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "boolean", 'key')
    if textarea.get("%s-5c" % ls, ls) == "break":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "break", 'key')
    if textarea.get("%s-8c" % ls, ls) == "continue":
        textarea.delete("%s-8c" % ls, ls)
        textarea.insert(INSERT, "continue", 'key')
    if textarea.get("%s-5c" % ls, ls) == "catch":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "catch", 'key')
    if textarea.get("%s-7c" % ls, ls) == "finally":
        textarea.delete("%s-7c" % ls, ls)
        textarea.insert(INSERT, "finally", 'key')
    if textarea.get("%s-10c" % ls, ls) == "instanceof":
        textarea.delete("%s-10c" % ls, ls)
        textarea.insert(INSERT, "instanceof", 'key')

    if textarea.get("%s-5c" % ls, ls) == "super":
        textarea.delete("%s-5c" % ls, ls)
        textarea.insert(INSERT, "super", 'key')



    def text(eve):
        # textarea.tag_config('keyword', foreground="Purple")
        # textarea.tag_config('key', foreground="Blue")
        textarea.tag_config('key', foreground="Purple")
        ls = textarea.index(INSERT)
        if eve == "new":
            textarea.delete("%s-2c" % ls, ls)
            textarea.insert(INSERT, "new", 'key')
        if eve == "import":
            textarea.delete("%s-3c"%ls,ls)
            textarea.insert(INSERT, "import",'key')
        if eve == "util":
            textarea.insert(INSERT, "util")

        if eve == "swing":
            textarea.insert(INSERT, "swing")
        if eve=="print":
            textarea.insert(INSERT,"print(" ");")
        if eve=="println":
            textarea.insert(INSERT,"println(" ");")
        if eve=="exit":
            textarea.insert(INSERT,"exit()")
        if eve == "io":
            textarea.insert(INSERT, "io")
        if eve == "sql":
            textarea.insert(INSERT, "sql")
        if eve == "awt":
            textarea.insert(INSERT, "awt")
        if eve == "beans":
            textarea.insert(INSERT, "beans")
        if eve == "math":
            textarea.insert(INSERT, "math")
        if eve == "text":
            textarea.insert(INSERT, "text")
        if eve == "rmi":
            textarea.insert(INSERT, "rmi")
        if eve == "security":
            textarea.insert(INSERT, "security")
        if eve == "nio":
            textarea.insert(INSERT, "nio")
        if eve == "applet":
            textarea.insert(INSERT, "applet")
        if eve == "net":
            textarea.insert(INSERT, "net")
        if eve == "time":
            textarea.insert(INSERT, "time")
        if eve == "BufferedInputStream":
            textarea.insert(INSERT, "BufferedInputStream")
        if eve == "BufferedOutputStream":
            textarea.insert(INSERT, "BufferedOutputStream")
        if eve == "DataInputStream":
            textarea.insert(INSERT, "DataInputStream")
        if eve == "InputStreamReader":
            textarea.insert(INSERT, "InputStreamReader")
        if eve == "File":
            textarea.insert(INSERT, "File")
        if eve == "IOException":
            textarea.insert(INSERT, "IOException")
        if eve == "FileReader":
            textarea.insert(INSERT, "FileReader")
        if eve == "FileWriter":
            textarea.insert(INSERT, "FileWriter")
        if eve == "PrintReader":
            textarea.insert(INSERT, "PrintReader")
        if eve == "PrintWriter":
            textarea.insert(INSERT, "PrintWriter")
        if eve == "Reader":
            textarea.insert(INSERT, "Reader")
        if eve == "Writer":
            textarea.insert(INSERT, "Writer")
        if eve == "event":
            textarea.insert(INSERT, "event")
        if eve == "Button":
            textarea.insert(INSERT, "Button")
        if eve == "Canvas":
            textarea.insert(INSERT, "Canvas")
        if eve == "CheckBox":
            textarea.insert(INSERT, "CheckBox")
        if eve == "CheckBoxMenuItem":
            textarea.insert(INSERT, "CheckBoxMenuItem")
        if eve == "Choice":
            textarea.insert(INSERT, "Choice")
        if eve == "Color":
            textarea.insert(INSERT, "Color")
        if eve == "Component":
            textarea.insert(INSERT, "Component")
        if eve == "Container":
            textarea.insert(INSERT, "Container")
        if eve == "Dialog":
            textarea.insert(INSERT, "Dialog")
        if eve == "FlowLayout":
            textarea.insert(INSERT, "FlowLayout")
        if eve == "Font":
            textarea.insert(INSERT, "Font")
        if eve == "Frame":
            textarea.insert(INSERT, "Frame")
        if eve == "Graphics":
            textarea.insert(INSERT, "Graphics")
        if eve == "Image":
            textarea.insert(INSERT, "Image")
        if eve == "Label":
            textarea.insert(INSERT, "Label")
        if eve == "List":
            textarea.insert(INSERT, "List")
        if eve == "Menu":
            textarea.insert(INSERT, "Menu")
        if eve == "MenuBar":
            textarea.insert(INSERT, "MenuBar")
        if eve == "MenuItem":
            textarea.insert(INSERT, "MenuItem")
        if eve == "Paint":
            textarea.insert(INSERT, "Paint")
        if eve == "Panel":
            textarea.insert(INSERT, "Panel")
        if eve == "Polygon":
            textarea.insert(INSERT, "Polygon")
        if eve == "PopupMenu":
            textarea.insert(INSERT, "PopupMenu")
        if eve == "Rectangle":
            textarea.insert(INSERT, "Rectangle")
        if eve == "ScrollBar":
            textarea.insert(INSERT, "ScrollBar")
        if eve == "ScrollPane":
            textarea.insert(INSERT, "ScrollPane")
        if eve == "Shape":
            textarea.insert(INSERT, "Shape")
        if eve == "Stroke":
            textarea.insert(INSERT, "Stroke")
        if eve == "TextArea":
            textarea.insert(INSERT, "TextArea")
        if eve == "TextField":
            textarea.insert(INSERT, "TextField")
        if eve == "ToolKit":
            textarea.insert(INSERT, "ToolKit")
        if eve == "Calendar":
            textarea.insert(INSERT, "Calendar")
        if eve == "Collection":
            textarea.insert(INSERT, "Collection")
        if eve == "Collections":
            textarea.insert(INSERT, "Collections")
        if eve == "Date":
            textarea.insert(INSERT, "Date")
        if eve == "Dictionary":
            textarea.insert(INSERT, "Dictionary")
        if eve == "Enumeration":
            textarea.insert(INSERT, "Enumeration")
        if eve == "EnumMap":
            textarea.insert(INSERT, "EnumMap")
        if eve == "EnumSet":
            textarea.insert(INSERT, "EnumSet")
        if eve == "HashMap":
            textarea.insert(INSERT, "HashMap")
        if eve == "HashSet":
            textarea.insert(INSERT, "HashSet")
        if eve == "HashTable":
            textarea.insert(INSERT, "HashTable")
        if eve == "LinkedHashMap":
            textarea.insert(INSERT, "LinkedHashMap")
        if eve == "LinkedHashSet":
            textarea.insert(INSERT, "LinkedHashSet")
        if eve == "LinkedList":
            textarea.insert(INSERT, "LinkedList")
        if eve == "List":
            textarea.insert(INSERT, "List")
        if eve == "Map":
            textarea.insert(INSERT, "Map")
        if eve == "Objects":
            textarea.insert(INSERT, "Objects")
        if eve == "Queue":
            textarea.insert(INSERT, "Queue")
        if eve == "Random":
            textarea.insert(INSERT, "Random")
        if eve == "Scanner":
            textarea.insert(INSERT, "Scanner")
        if eve == "Set":
            textarea.insert(INSERT, "Set")
        if eve == "Stack":
            textarea.insert(INSERT, "Stack")
        if eve == "TimeZone":
            textarea.insert(INSERT, "TimeZone")
        if eve == "Vector":
            textarea.insert(INSERT, "Vector")
        if eve == "accessibility":
            textarea.insert(INSERT, "accessibility")
        if eve == "annotation":
            textarea.insert(INSERT, "annotation")
        if eve == "imageio":
            textarea.insert(INSERT, "imageio")
        if eve == "lang":
            textarea.insert(INSERT, "lang")
        if eve == "management":
            textarea.insert(INSERT, "management")
        if eve == "naming":
            textarea.insert(INSERT, "naming")
        if eve == "print":
            textarea.insert(INSERT, "print")
        if eve == "script":
            textarea.insert(INSERT, "script")
        if eve == "sound":
            textarea.insert(INSERT, "sound")
        if eve == "tools":
            textarea.insert(INSERT, "tools")
        if eve == "xml":
            textarea.insert(INSERT, "xml")
        if eve == "JApplet":
            textarea.insert(INSERT, "JApplet")
        if eve == "JButton":
            textarea.insert(INSERT, "JButton")
        if eve == "JCheckBox":
            textarea.insert(INSERT, "JCheckBox")
        if eve == "JCheckBoxMenuItem":
            textarea.insert(INSERT, "JCheckBoxMenuItem")
        if eve == "JColorChooser":
            textarea.insert(INSERT, "JColorChooser")
        if eve == "JComboBox":
            textarea.insert(INSERT, "JComboBox")
        if eve == "JComponent":
            textarea.insert(INSERT, "JComponent")
        if eve == "JDesktoPane":
            textarea.insert(INSERT, "JDesktoPane")
        if eve == "JDialog":
            textarea.insert(INSERT, "JDialog")
        if eve == "JEditorPane":
            textarea.insert(INSERT, "JEditorPane")
        if eve == "JFileChooser":
            textarea.insert(INSERT, "JFileChooser")
        if eve == "JFormattedTextField":
            textarea.insert(INSERT, "JFormattedTextField")
        if eve == "JFrame":
            textarea.insert(INSERT, "JFrame")
        if eve == "JInternalFrame":
            textarea.insert(INSERT, "JInternalFrame")
        if eve == "JLabel":
            textarea.insert(INSERT, "JLabel")
        if eve == "JLayer":
            textarea.insert(INSERT, "JLayer")
        if eve == "JLayeredPane":
            textarea.insert(INSERT, "JLayeredPane")
        if eve == "JList":
            textarea.insert(INSERT, "JList")
        if eve == "JMenu":
            textarea.insert(INSERT, "JMenu")
        if eve == "JMenuBar":
            textarea.insert(INSERT, "JMenuBar")
        if eve == "JMenuItem":
            textarea.insert(INSERT, "JMenuItem")
        if eve == "JOptionPane":
            textarea.insert(INSERT, "JOptionPane")
        if eve == "JPanel":
            textarea.insert(INSERT, "JPanel")
        if eve == "JPasswordField":
            textarea.insert(INSERT, "JPasswordField")
        if eve == "JPopupMenu":
            textarea.insert(INSERT, "JPopupMenu")
        if eve == "JProgressBar":
            textarea.insert(INSERT, "JProgressBar")
        if eve == "JRadioButton":
            textarea.insert(INSERT, "JRadioButton")
        if eve == "JRadioButtonMenuItem":
            textarea.insert(INSERT, "JRadioButtonMenuItem")
        if eve == "JRootPane":
            textarea.insert(INSERT, "JRootPane")
        if eve == "JScrollBar":
            textarea.insert(INSERT, "JScrollBar")
        if eve == "JSeparator":
            textarea.insert(INSERT, "JSeparator")
        if eve == "JSlider":
            textarea.insert(INSERT, "JSlider")
        if eve == "JSpinner":
            textarea.insert(INSERT, "JSpinner")
        if eve == "JSplitPane":
            textarea.insert(INSERT, "JSplitPane")
        if eve == "JTabbedPane":
            textarea.insert(INSERT, "JTabbedPane")
        if eve == "JTextArea":
            textarea.insert(INSERT, "JTextArea")
        if eve == "JTextField":
            textarea.insert(INSERT, "JTextField")
        if eve == "JToolBar":
            textarea.insert(INSERT, "JToolBar")
        if eve == "JTree":
            textarea.insert(INSERT, "JTree")
        if eve == "JToolTip":
            textarea.insert(INSERT, "JToolTip")
        if eve == "Applet":
            textarea.insert(INSERT, "Applet")
        if eve == "AppletContext":
            textarea.insert(INSERT, "AppletContext")
        if eve == "AppletStub":
            textarea.insert(INSERT, "AppletStub")
        if eve == "AudioClip":
            textarea.insert(INSERT, "AudioClip")
        if eve == "in":
            textarea.insert(INSERT, "in")
        if eve == "out":
            textarea.insert(INSERT, "out")
        if eve == "err":
            textarea.insert(INSERT, "err")
        if eve == "ActionListener":
            textarea.insert(INSERT, "ActionListener")
        if eve == "ActionEvent":
            textarea.insert(INSERT, "ActionEvent")
        if eve == "ComponentAdapter":
            textarea.insert(INSERT, "ComponentAdapter")
        if eve == "ComponentEvent":
            textarea.insert(INSERT, "ComponentEvent")
        if eve == "ComponentListener":
            textarea.insert(INSERT, "ComponentListener")
        if eve == "ContainerAdapter":
            textarea.insert(INSERT, "ContainerAdapter")
        if eve == "ContainerEvent":
            textarea.insert(INSERT, "ContainerEvent")
        if eve == "ContainerListener":
            textarea.insert(INSERT, "ContainerListener")
        if eve == "FocusAdapter":
            textarea.insert(INSERT, "FocusAdapter")
        if eve == "FocusListener":
            textarea.insert(INSERT, "FocusListener")
        if eve == "FocusEvent":
            textarea.insert(INSERT, "FocusEvent")
        if eve == "ItemEvent":
            textarea.insert(INSERT, "ItemEvent")
        if eve == "ItemListener":
            textarea.insert(INSERT, "ItemListener")
        if eve == "KeyAdapter":
            textarea.insert(INSERT, "KeyAdapter")
        if eve == "KeyEvent":
            textarea.insert(INSERT, "KeyEvent")
        if eve == "KeyListener":
            textarea.insert(INSERT, "KeyListener")
        if eve == "MouseAdapter":
            textarea.insert(INSERT, "MouseAdapter")
        if eve == "MouseEvent":
            textarea.insert(INSERT, "MouseEvent")
        if eve == "MouseListener":
            textarea.insert(INSERT, "MouseListener")
        if eve == "PaintEvent":
            textarea.insert(INSERT, "PaintEvent")
        if eve == "MouseMotionListener":
            textarea.insert(INSERT, "MouseMotionListener")
        if eve == "TextEvent":
            textarea.insert(INSERT, "TextEvent")
        if eve == "TextListener":
            textarea.insert(INSERT, "TextListener")
        if eve == "WindowAdapter":
            textarea.insert(INSERT, "WindowAdapter")
        if eve == "WindowEvent":
            textarea.insert(INSERT, "WindowEvent")
        if eve == "WindowFocusListener":
            textarea.insert(INSERT, "WindowFocusListener")
        if eve == "WindowListener":
            textarea.insert(INSERT, "WindowListener")
        if eve == "WindowStateListener":
            textarea.insert(INSERT, "WindowStateListener")


        if eve == "SOP":
            textarea.delete("%s-3c"%ls,ls)
            textarea.insert(INSERT, "System.out.println(" ");")
        if eve == "if..":
            textarea.insert(INSERT, "(condition)\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve == "if..else":
            textarea.insert(INSERT, "(condition)\n\t\t{\n\t\t\n\t\t}\n\t\t")
            textarea.insert(INSERT,"else",'key')
            textarea.insert(INSERT,"\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve == "if.else.if":
            textarea.insert(INSERT, "(condition-1)\n\t\t{\n\t\t\n\t\t}\n\t\t")
            textarea.insert(INSERT,"else",'key')
            textarea.insert(INSERT,"if",'key')
            textarea.insert(INSERT,"(condition-2)\n\t\t{\n\t\t\n\t\t}\n\t\t")
            textarea.insert(INSERT,"else",'key')
            textarea.insert(INSERT,"\n\t\t{\n\t\t}\n\t\t")
        if eve == "if.if":
            textarea.insert(INSERT, "(condition-1)\n\t\t{\n\t\t\n\t\t}\n\t\t")
            textarea.insert(INSERT,"if",'key')
            textarea.insert(INSERT,"(condition-2)\n\t\t{\n\t\t\n\t\t}\n\t\t")
            textarea.insert(INSERT,"if",'key')
            textarea.insert("(condition)\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve=="for":
            textarea.insert(INSERT,"(initialization;condition;increment/decrement)\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve == "for..":
            textarea.insert(INSERT, "(var:collection)\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve == "while..":
            textarea.insert(INSERT, "(condition)\n\t\t{\n\t\t\n\t\tincrement/decrement\n\t\t}\n\t\t")
        if eve == "do..while":
            textarea.insert(INSERT, "\n\t\t{\n\t\t\n\t\tincrement/decrement\n\t\t}\n\t\t")
            textarea.insert(INSERT,"while",'key')
            textarea.insert(INSERT,"(condition);\n\t\t")
        if eve == "class..":
            textarea.insert(INSERT, "\n\t\t{\n\t\t\n\t\t}\n\t\t")
        if eve=="public":
            textarea.delete("%s-3c"%ls,ls)
            textarea.insert(INSERT,"public",'key')



root=Tk()
root.geometry("800x700")
textarea=Text(root,state='normal')
# root.config(title=(o+".java"))
class1()

m = Menu(root)
m1 = Menu(m, tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="New Window", command=new_window)
m1.add_separator()
m1.add_command(label="Open", command=open)
m1.add_separator()
m1.add_command(label="Save", command=save1)
m1.add_command(label="Save as", command=saveas)
m1.add_command(label="Print", command=f_print)
m1.add_separator()
m1.add_command(label="Exit", command=stop)
root.config(menu=m)
m.add_cascade(label="File", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="Undo", command=undo)
m1.add_command(label="Redo", command=redo)
m1.add_command(label="Select all", command=select)
m1.add_separator()
m1.add_command(label="Cut", command=cut)
m1.add_command(label="Copy", command=copy)
m1.add_command(label="Paste", command=paste)
m1.add_command(label="Delete", command=delete)
root.config(menu=m)
m.add_cascade(label="Edit", menu=m1)


m1 = Menu(m, tearoff=0)
m1.add_command(label="Compile", command=compile)
m1.add_command(label="Run", command=run)
root.config(menu=m)
m.add_cascade(label="Build", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_checkbutton(label="Dark Mode",command=dark)
fm = Menu(m1, tearoff=0)
fm.add_command(label="Font", command=font)
fm.add_command(label="Font Style", command=style)
fm.add_command(label="Text Size", command=size)
m1.add_cascade(label="Font", menu=fm)
root.config(menu=m)
m.add_cascade(label="Format", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="View Help", command=f_help)
m1.add_command(label="Contact Us", command=contact)
m1.add_separator()
m1.add_command(label="About", command=about)
root.config(menu=m)
m.add_cascade(label="Help", menu=m1)

textarea.bind('<KeyRelease>',edit)
textarea.bind('<Button-3>',rightclick)
textarea.pack(fill='both',expand=True)
root.mainloop()
