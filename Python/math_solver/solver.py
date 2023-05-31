from tkinter import *
from math import log

#Functions

def create_menu():
    title_img_label.place_forget()
    title_exit_btn.place_forget()
    title_start_btn.place_forget()
    title_text_label.place_forget()
    menu_label.place(anchor='center', x=250, y=50)
    menu_exit_btn.place(anchor='se', x=490, y=590)
    perc_icon_label.place(anchor='center', x=100, y=150)
    perc_text_label.place(anchor='center', x=100, y=200)
    perc_btn.place(anchor='center', x=100, y=240)
    power_icon_label.place(anchor='center', x=375, y=150)
    power_text_label.place(anchor='center', x=375, y=200)
    power_btn.place(anchor='center', x=375, y=240)
    figures_icon_label.place(anchor='center', x=100, y=370)
    figures_text_label.place(anchor='center', x=100, y=420)
    figures_btn.place(anchor='center', x=100, y=460)
    dst_icon_label.place(anchor='center', x=375, y=370)
    dst_text_label.place(anchor='center', x=375, y=420)
    dst_btn.place(anchor='center', x=375, y=460)

def create_DST_window():

    def select():
        choice = find_choise.get()
        if choice == 1:
            dist_field.delete(0, END)
            dist_field.configure(state='disabled')
            speed_field.configure(state='normal')
            time_field.configure(state='normal')
        elif choice == 2:
            time_field.delete(0, END)
            time_field.configure(state='disabled')
            speed_field.configure(state='normal')
            dist_field.configure(state='normal')
        elif choice == 3:
            speed_field.delete(0, END)
            speed_field.configure(state='disabled')
            dist_field.configure(state='normal')
            time_field.configure(state='normal')

    def calc():
        choice = find_choise.get()
        d = dist_field.get()
        t = time_field.get()
        s = speed_field.get()
        if choice == 1:
            try:
                dist_field.configure(fg='#000000')
                s = float(s)
                t = float(t)
                if s > 0 and t > 0:
                    dist_field.configure(state='normal')
                    dist_field.delete(0, END)
                    d = s * t
                    dist_field.insert(0, d)
                    dist_field.configure(state='disabled')
                else:
                    dist_field.configure(state='normal')
                    dist_field.delete(0, END)
                    dist_field.configure(fg='red')
                    dist_field.insert(0, 'ERROR')
                    dist_field.configure(state='disabled')
            except:
                dist_field.configure(state='normal')
                dist_field.delete(0, END)
                dist_field.configure(fg='red')
                dist_field.insert(0, 'ERROR')
                dist_field.configure(state='disabled')
        elif choice == 2:
            try:
                time_field.configure(fg='#000000')
                s = float(s)
                d = float(d)
                if s > 0 and d > 0:
                    time_field.configure(state='normal')
                    time_field.delete(0, END)
                    t = d / s
                    time_field.insert(0, t)
                    time_field.configure(state='disabled')
                else:
                    time_field.configure(state='normal')
                    time_field.delete(0, END)
                    time_field.configure(fg='red')
                    time_field.insert(0, 'ERROR')
                    time_field.configure(state='disabled')
            except:
                time_field.configure(state='normal')
                time_field.delete(0, END)
                time_field.configure(fg='red')
                time_field.insert(0, 'ERROR')
                time_field.configure(state='disabled')
        elif choice == 3:
            try:
                speed_field.configure(fg='#000000')
                t = float(t)
                d = float(d)
                if t > 0 and d > 0:
                    speed_field.configure(state='normal')
                    speed_field.delete(0, END)
                    s = d / t
                    speed_field.insert(0, s)
                    speed_field.configure(state='disabled')
                else:
                    speed_field.configure(state='normal')
                    speed_field.delete(0, END)
                    speed_field.configure(fg='red')
                    speed_field.insert(0, 'ERROR')
                    speed_field.configure(state='disabled')
            except:
                speed_field.configure(state='normal')
                speed_field.delete(0, END)
                speed_field.configure(fg='red')
                speed_field.insert(0, 'ERROR')
                speed_field.configure(state='disabled')








    bg_dst = '#4287f5'
    fg_dst = '#d0d9db'
    dst_window = Toplevel(root)
    dst_window.title('Distance, Speed & Time')
    dst_window.geometry('500x320')
    dst_window.resizable(False, False)
    dst_window.configure(background=bg_dst)

    dst_pic = PhotoImage(file="SpeedDistanceTime.png")
    dst_pic_label = Label(dst_window, image=dst_pic, bg=bg_dst, fg=fg_color)
    dst_pic_label.place(anchor='center', x=250, y=70)

    find_label = Label(dst_window, text='To find:', font=my_font, bg=bg_dst, fg=fg_dst)
    find_label.place(anchor='center', x=50, y=180)

    find_choise = IntVar()

    dist_radio = Radiobutton(dst_window, font=my_font, bg=bg_dst, fg=fg_dst, text = 'Distance', value=1, variable=find_choise, activebackground=bg_dst, command=select)
    dist_radio.place(anchor='w', x=10, y=210)

    time_radio = Radiobutton(dst_window, font=my_font, bg=bg_dst, fg=fg_dst, text = 'Time', value=2, variable=find_choise, activebackground=bg_dst, command=select)
    time_radio.place(anchor='w', x=10, y=240)

    speed_radio = Radiobutton(dst_window, font=my_font, bg=bg_dst, fg=fg_dst, text = 'Speed', value=3, variable=find_choise, activebackground=bg_dst, command=select)
    speed_radio.place(anchor='w', x=10, y=270)

    dist_label = Label(dst_window, text='Distance', font=my_font, bg=bg_dst, fg=fg_dst)
    dist_label.place(anchor='center', x=230, y=160)
    dist_field = Entry(dst_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    dist_field.place(anchor='center', x=230, y=185)


    time_label = Label(dst_window, text='Time', font=my_font, bg=bg_dst, fg=fg_dst)
    time_label.place(anchor='center', x=330, y=160)
    time_field = Entry(dst_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    time_field.place(anchor='center', x=330, y=185)

    speed_label = Label(dst_window, text='Speed', font=my_font, bg=bg_dst, fg=fg_dst)
    speed_label.place(anchor='center', x=430, y=160)
    speed_field = Entry(dst_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    speed_field.place(anchor='center', x=430, y=185)

    calc_button = Button(dst_window, text='CALC', width=8, height=1, font=my_font, bg='#00b300', fg=fg_color, relief = my_relief, command=calc).place(anchor='center', x=330, y=240)



    dst_window.mainloop()






def create_figures_window():

    def calc_triangle():
        triangle_field_p.configure(fg='#000000')
        triangle_field_s.configure(fg='#000000')
        try:
            a = float(triangle_field_a.get())
            b = float(triangle_field_b.get())
            c = float(triangle_field_c.get())
            if (a>=b+c) or (c>=b+a) or (b>=a+c):
                triangle_field_p.delete(0, END)
                triangle_field_s.delete(0, END)
                triangle_field_p.configure(fg='red')
                triangle_field_s.configure(fg='red')
                triangle_field_p.insert(0, 'ERROR')
                triangle_field_s.insert(0, 'ERROR')
            else:
                p = a + b + c
                p_half = p/2
                s = (p_half*(p_half-a)*(p_half-b)*(p_half-c))**0.5
                triangle_field_p.delete(0, END)
                triangle_field_s.delete(0, END)
                triangle_field_p.insert(0, round(p, 3))
                triangle_field_s.insert(0, round(s, 3))
        except:
            triangle_field_p.delete(0, END)
            triangle_field_s.delete(0, END)
            triangle_field_p.configure(fg='red')
            triangle_field_s.configure(fg='red')
            triangle_field_p.insert(0, 'ERROR')
            triangle_field_s.insert(0, 'ERROR')

    def calc_rectangle():
        rectangle_field_p.configure(fg='#000000')
        rectangle_field_s.configure(fg='#000000')
        try:
            a = float(rectangle_field_a.get())
            b = float(rectangle_field_b.get())
            if a<=0 or b<=0:
                rectangle_field_p.delete(0, END)
                rectangle_field_s.delete(0, END)
                rectangle_field_p.configure(fg='red')
                rectangle_field_s.configure(fg='red')
                rectangle_field_p.insert(0, 'ERROR')
                rectangle_field_s.insert(0, 'ERROR')
            else:
                p = (a + b) * 2
                s = a * b
                rectangle_field_p.delete(0, END)
                rectangle_field_s.delete(0, END)
                rectangle_field_p.insert(0, round(p, 3))
                rectangle_field_s.insert(0, round(s, 3))
        except:
            rectangle_field_p.delete(0, END)
            rectangle_field_s.delete(0, END)
            rectangle_field_p.configure(fg='red')
            rectangle_field_s.configure(fg='red')
            rectangle_field_p.insert(0, 'ERROR')
            rectangle_field_s.insert(0, 'ERROR')

    def calc_circle():
        circle_field_l.configure(fg='#000000')
        circle_field_s.configure(fg='#000000')
        try:
            r = float(circle_field_r.get())
            if r <= 0:
                circle_field_l.delete(0, END)
                circle_field_s.delete(0, END)
                circle_field_l.configure(fg='red')
                circle_field_s.configure(fg='red')
                circle_field_l.insert(0, 'ERROR')
                circle_field_s.insert(0, 'ERROR')
            else:
                l = 2*3.14*r
                s = 3.14*r**2
                circle_field_l.delete(0, END)
                circle_field_s.delete(0, END)
                circle_field_l.insert(0, round(l, 3))
                circle_field_s.insert(0, round(s, 3))
        except:
            circle_field_l.delete(0, END)
            circle_field_s.delete(0, END)
            circle_field_l.configure(fg='red')
            circle_field_s.configure(fg='red')
            circle_field_l.insert(0, 'ERROR')
            circle_field_s.insert(0, 'ERROR')


    bg_fig = '#d9aae3'
    fig_window = Toplevel(root)
    fig_window.title('Perimeter & Square')
    fig_window.geometry('600x450')
    fig_window.resizable(False, False)
    fig_window.configure(background=bg_fig)

    triangle_pic = PhotoImage(file="triangle.png")
    triangle_pic_label = Label(fig_window, image=triangle_pic, bg=bg_fig, fg=fg_color)
    triangle_pic_label.place(anchor='w', x=30, y=80)

    triangle_label_a = Label(fig_window, text='side a:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=40, y=200)
    triangle_field_a = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    triangle_field_a.place(anchor='center', x=125, y=200)

    triangle_label_b = Label(fig_window, text='side b:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=40, y=230)
    triangle_field_b = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    triangle_field_b.place(anchor='center', x=125, y=230)

    triangle_label_c = Label(fig_window, text='side c:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=40, y=260)
    triangle_field_c = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    triangle_field_c.place(anchor='center', x=125, y=260)

    triangle_calc = Button(fig_window, text='CALC', width=7, height=1, font=my_font, bg='#00b300', fg=fg_color, relief = my_relief, command=calc_triangle).place(anchor='center', x=80, y=310)

    triangle_label_p = Label(fig_window, text='P =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=40, y=360)
    triangle_field_p = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    triangle_field_p.place(anchor='center', x=120, y=360)

    triangle_label_s = Label(fig_window, text='S =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=40, y=390)
    triangle_field_s = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    triangle_field_s.place(anchor='center', x=120, y=390)


    rectangle_pic = PhotoImage(file="rectangle.png")
    rectangle_pic_label = Label(fig_window, image=rectangle_pic, bg=bg_fig)
    rectangle_pic_label.place(anchor='center', x=300, y=80)

    rectangle_label_a = Label(fig_window, text='side a:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=260, y=200)
    rectangle_field_a = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    rectangle_field_a.place(anchor='center', x=345, y=200)

    rectangle_label_b = Label(fig_window, text='side b:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=260, y=230)
    rectangle_field_b = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    rectangle_field_b.place(anchor='center', x=345, y=230)

    rectangle_calc = Button(fig_window, text='CALC', width=7, height=1, font=my_font, bg='#00b300', fg=fg_color, relief = my_relief, command=calc_rectangle).place(anchor='center', x=300, y=310)

    rectangle_label_p = Label(fig_window, text='P =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=260, y=360)
    rectangle_field_p = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    rectangle_field_p.place(anchor='center', x=340, y=360)

    rectangle_label_s = Label(fig_window, text='S =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=260, y=390)
    rectangle_field_s = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    rectangle_field_s.place(anchor='center', x=340, y=390)

    circle_pic = PhotoImage(file="circle.png")
    circle_pic_label = Label(fig_window, image=circle_pic, bg=bg_fig)
    circle_pic_label.place(anchor='e', x=570, y=80)

    circle_label_r = Label(fig_window, text='radius:', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=460, y=200)
    circle_field_r = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    circle_field_r.place(anchor='center', x=545, y=200)

    circle_calc = Button(fig_window, text='CALC', width=7, height=1, font=my_font, bg='#00b300', fg=fg_color, relief = my_relief, command=calc_circle).place(anchor='center', x=500, y=310)

    circle_label_l = Label(fig_window, text='L =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=460, y=360)
    circle_field_l = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    circle_field_l.place(anchor='center', x=540, y=360)

    circle_label_s = Label(fig_window, text='S =', font=my_font, bg=bg_fig, fg=fg_color).place(anchor='center', x=460, y=390)
    circle_field_s = Entry(fig_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')
    circle_field_s.place(anchor='center', x=540, y=390)

    fig_window.mainloop()


def create_power_window():

    def select():
        option =  function_type.get()
        widget = [power_base_field, power_index_field, equal_mark, answer_mark, root_mark, root_index_field,
                  root_number_field, log_mark, log_base_field, log_number_field, calc_button]
        for i in widget:
            i.place_forget()
        calc_button.place(anchor='center', x=225, y=160)
        answer_mark.configure(text='?')
        for i in [power_base_field, power_index_field, root_index_field, root_number_field, log_base_field, log_number_field]:
            i.delete(0, END)
        if option == 1:
            power_index_field.place(anchor='center', x=175, y=85)
            power_base_field.place(anchor='center', x=150, y=110)
            answer_mark.place(anchor='center', x=335, y=110)
            equal_mark.place(anchor='center', x=220, y=110)
        elif option == 2:
            equal_mark.place(anchor='center', x=260, y=110)
            answer_mark.place(anchor='center', x=335, y=110)
            root_number_field.place(anchor='center', x=220, y=110)
            root_index_field.place(anchor='center', x=170, y=81)
            root_mark.place(anchor='center', x=180, y=110)
        elif option == 3:
            equal_mark.place(anchor='center', x=285, y=95)
            answer_mark.place(anchor='center', x=335, y=95)
            log_number_field.place(anchor='center', x=240, y=95)
            log_base_field.place(anchor='center', x=200, y=110)
            log_mark.place(anchor='center', x=160, y=95)

    def calc_power():
        try:
            base = float(power_base_field.get())
            index = float(power_index_field.get())
            res = base ** index
            res = round(res, 2)
        except:
            res = "ERROR"
        return res
    def calc_root():
        try:
            number = float(root_number_field.get())
            index = float(root_index_field.get())
            if index != 0:
                res = number ** (1/index)
                res = round(res, 2)
            else:
                res = "ERROR"
        except:
            res = "ERROR"
        return res
    def calc_log():
        try:
            base = float(log_base_field.get())
            number = float(log_number_field.get())
            res = log(numder, base)
            res = round(res, 2)
        except:
            res = "ERROR"
        return res
    def calc():
        option = function_type.get()
        if option == 1:
            answer = calc_power()
        elif option == 2:
            answer = calc_root()
        elif option == 3:
            answer = calc_log()
        answer_mark.configure(text = answer)






    bg_power = '#fcd15b'
    fg_power = '#3d3f40'
    power_window = Toplevel(root)
    power_window.title('Power, Root & Log')
    power_window.geometry('450x200')
    power_window.resizable(False, False)
    power_window.configure(background=bg_power)

    function_type = IntVar()

    power_button = Radiobutton(power_window, font=my_font, bg=bg_power, fg=fg_power, text = 'Power', value=1, variable=function_type, command=select)
    power_button.place(anchor='w', x=50, y=30)

    Root_button = Radiobutton(power_window, font=my_font, bg=bg_power, fg=fg_power, text = 'Root', value=2, variable=function_type, command=select)
    Root_button.place(anchor='center', x=225, y=30)

    Log_button = Radiobutton(power_window, font=my_font, bg=bg_power, fg=fg_power, text = 'Log', value=3, variable=function_type, command=select)
    Log_button.place(anchor='e', x=400, y=30)

    equal_mark = Label(power_window, text='=', font=('Courier New', 22), bg=bg_power, fg=fg_power)
    answer_mark = Label(power_window, text='?', font=('Courier New', 22), bg=bg_power, fg=fg_power)
    calc_button = Button(power_window, text='CALC', width=6, height=1, font=my_font, bg='#00b300', fg=fg_power, relief = my_relief, comman=calc)

    power_base_field = Entry(power_window, width=4, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')

    power_index_field = Entry(power_window, width=3, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')

    # ---------------------------------------------------------------------------------------------------------------------------
    root_mark = Label(power_window, text='√', font=('Courier New', 42), bg=bg_power, fg=fg_power)

    root_index_field = Entry(power_window, width=2, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')


    root_number_field = Entry(power_window, width=4, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')

    # ---------------------------------------------------------------------------------------------------------------------------
    log_mark = Label(power_window, text='log', font=('Courier New', 22), bg=bg_power, fg=fg_power)


    log_base_field = Entry(power_window, width=2, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')


    log_number_field = Entry(power_window, width=4, fg=fg_power, relief=my_relief, font=my_font, justify='center', highlightthickness=0.1, highlightbackground='#000000')



def create_percent_window():


    def r_select():
        perc_f = function_type.get()
        find_number_field.configure(state='normal')
        find_percent_field.configure(state='normal')
        percent_100_field.configure(state='normal')
        find_number_field.delete(0, END)
        find_percent_field.delete(0, END)
        percent_100_field.delete(0, END)
        find_number_field.configure(state='disabled')
        find_percent_field.configure(state='disabled')
        percent_100_field.configure(state='disabled')
        if perc_f == 1:
            find_number_field.configure(state='disabled')
            find_percent_field.configure(state='normal')
            percent_100_field.configure(state='normal')
        elif perc_f == 2:
            find_number_field.configure(state='normal')
            find_percent_field.configure(state='disabled')
            percent_100_field.configure(state='normal')
        elif perc_f == 3:
            find_number_field.configure(state='normal')
            find_percent_field.configure(state='normal')
            percent_100_field.configure(state='disabled')




    def calc():
        perc_f = function_type.get()
        if perc_f == 1:
            try:
                find_number_field.configure(state='normal')
                find_number_field.delete(0, END)
                find_number_field.configure(state='disabled')
                fpf = float(find_percent_field.get())
                p100f = float(percent_100_field.get())
                answer = p100f/100*fpf
                answer = round(answer, 3)
                find_number_field.configure(state='normal')
                find_number_field.insert(0, answer)
                find_number_field.configure(state='disabled')
            except:
                find_number_field.configure(state='normal')
                find_number_field.insert(0, 'ERROR')
                find_number_field.configure(state='disabled')
        elif perc_f == 2:
            try:
                find_percent_field.configure(state='normal')
                find_percent_field.delete(0, END)
                find_percent_field.configure(state='disabled')
                fnf = float(find_number_field.get())
                p100f = float(percent_100_field.get())
                answer = fnf/(p100f/100)
                answer = round(answer, 3)
                answer = str(answer) + '%'
                find_percent_field.configure(state='normal')
                find_percent_field.insert(0, answer)
                find_percent_field.configure(state='disabled')
            except:
                find_percent_field.configure(state='normal')
                find_percent_field.insert(0, 'ERROR')
                find_percent_field.configure(state='disabled')
        elif perc_f == 3:
            try:
                percent_100_field.configure(state='normal')
                percent_100_field.delete(0, END)
                percent_100_field.configure(state='disabled')
                fnf = float(find_number_field.get())
                fpf = float(find_percent_field.get())
                answer = fnf/fpf*100
                answer = round(answer, 3)
                percent_100_field.configure(state='normal')
                percent_100_field.insert(0, answer)
                percent_100_field.configure(state='disabled')
            except:
                percent_100_field.configure(state='normal')
                percent_100_field.insert(0, 'ERROR')
                percent_100_field.configure(state='disabled')


















    bg_percent = '#c564e8'
    fg_percent = '#3d3f40'
    percent_window = Toplevel(root)
    percent_window.title('Percent & etc.')
    percent_window.geometry('500x250')
    percent_window.resizable(False, False)
    percent_window.configure(background=bg_percent)


    function_type = IntVar()

    find_number_button = Radiobutton(percent_window, font=my_font, bg=bg_percent, fg=fg_percent, text = 'Number', value=1, variable=function_type, command=r_select)
    find_number_button.place(anchor='w', x=10, y=90)

    find_percent_button = Radiobutton(percent_window, font=my_font, bg=bg_percent, fg=fg_percent, text = 'Percent', value=2, variable=function_type, command=r_select)
    find_percent_button.place(anchor='w', x=10, y=130)

    find_100percent_button = Radiobutton(percent_window, font=my_font, bg=bg_percent, fg=fg_percent, text = '100 percents', value=3, variable=function_type, command=r_select)
    find_100percent_button.place(anchor='w', x=10, y=170)

    log_mark = Label(percent_window, text='Find:', font=('Courier New', 22), bg=bg_percent, fg=fg_percent)
    log_mark.place(anchor='w', x=20, y=35)

    find_number_field = Entry(percent_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    find_number_field.place(anchor='center', x=260, y=90)

    find_percent_field = Entry(percent_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    find_percent_field.place(anchor='center', x=430, y=90)

    percent_100_field = Entry(percent_window, width=8, relief=my_relief, font=my_font, justify='center', highlightthickness=0.6, highlightbackground='#000000', state='disabled')
    percent_100_field.place(anchor='center', x=260, y=150)

    p100_mark = Label(percent_window, text='100%', font=('Courier New', 22), bg=bg_percent, fg=fg_percent)
    p100_mark.place(anchor='center', x=430, y=150)

    fn_fp_mark = Label(percent_window, text='-', font=('Courier New', 32), bg=bg_percent, fg=fg_percent)
    fn_fp_mark.place(anchor='center', x=345, y=90)

    p100_p100m_mark = Label(percent_window, text='-', font=('Courier New', 32), bg=bg_percent, fg=fg_percent)
    p100_p100m_mark.place(anchor='center', x=345, y=150)

    calc_button = Button(percent_window, text='CALC', width=6, height=1, font=my_font, bg='#00b300', fg=fg_percent, relief = my_relief, command=calc)
    calc_button.place(anchor='center', x=345, y=210)












    percent_window.mainloop()






#UI Design
bg_color = '#008ae6'
fg_color = '#ffffff'
my_font = ('Courier New', 14)
my_relief = 'raised'

#Start Window


root = Tk()
root.title('Math Solver Ultra Extra Pro')
root.geometry('500x600+300+100')
root.resizable(False, False)
root.configure(background=bg_color)
root.iconbitmap('lock.ico')

title_image = PhotoImage(file="math.png")
title_img_label = Label(root, image=title_image, bg=bg_color)
title_img_label.place(anchor='center', x=250, y=80)

title_text_label = Label(root, text='Hello!\nYou are in Math Solver\nIt will help with math.\nGood luck!', font=my_font, bg=bg_color, fg=fg_color)
title_text_label.place(anchor='center', x=250, y=280)

title_start_btn = Button(root, text='START', width=10, height=2, font=my_font, bg='#00b300', fg=fg_color, relief = my_relief, command=create_menu)
title_start_btn.place(anchor='center', x=160, y=400)

title_exit_btn = Button(root, text='EXIT', width=10, height=2, font=my_font, bg='#ff1a1a', fg=fg_color, relief = my_relief, command=root.destroy)
title_exit_btn.place(anchor='center', x=360, y=400)

#Menu Window

menu_label = Label(root, text='Choose', font=('Courier New', 20), bg=bg_color, fg=fg_color)

menu_exit_btn = Button(root, text='EXIT', font=my_font, bg='#ff1a1a', fg=fg_color, relief = my_relief, command=root.destroy)

perc_icon = PhotoImage(file="percent.png")
perc_icon_label = Label(root, image=perc_icon, bg=bg_color)
perc_text_label = Label(root, text='Percent & etc.', font=my_font, bg=bg_color, fg=fg_color)
perc_btn = Button(root, width=10, height=1, text='START', font=my_font, bg='#f5ad42', fg=fg_color, relief = my_relief, command=create_percent_window)

power_icon = PhotoImage(file="root.png")
power_icon_label = Label(root, image=power_icon, bg=bg_color)
power_text_label = Label(root, text='Power, Root & Log', font=my_font, bg=bg_color, fg=fg_color)
power_btn = Button(root, width=10, height=1, text='START', font=my_font, bg='#f5ad42', fg=fg_color, relief = my_relief, command=create_power_window)

figures_icon = PhotoImage(file="figures.png")
figures_icon_label = Label(root, image=figures_icon, bg=bg_color)
figures_text_label = Label(root, text='Perimeter & Square', font=my_font, bg=bg_color, fg=fg_color)
figures_btn = Button(root, width=10, height=1, text='START', font=my_font, bg='#f5ad42', fg=fg_color, relief = my_relief, command=create_figures_window)

dst_icon = PhotoImage(file="dst.png")
dst_icon_label = Label(root, image=dst_icon, bg=bg_color)
dst_text_label = Label(root, text='Distance, Speed & Time', font=my_font, bg=bg_color, fg=fg_color)
dst_btn = Button(root, width=10, height=1, text='START', font=my_font, bg='#f5ad42', fg=fg_color, relief = my_relief, command=create_DST_window)

root.mainloop()
