from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import sys


class First_Wind(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.start()
        self.screen()
        self.center()

    def screen(self):
        self.scr = self.palette()
        self.scr.setColor(QPalette.Window, QColor(35, 35, 35))
        self.setPalette(self.scr)
        self.setGeometry(600, 1000, 1000, 600)
        self.setWindowTitle("Название приложения")
        self.center()

    def start(self):
        self.learn = QPushButton(self)
        self.learn.move(490, 200)
        self.learn.resize(200, 100)
        self.learn.setText("Учить формулы")
        self.learn.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
        self.learn.clicked.connect(self.open_choose)

        self.search = QPushButton(self)
        self.search.move(200, 200)
        self.search.resize(200, 100)
        self.search.setText("Искать формулы")
        self.search.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
        self.search.clicked.connect(self.open_search)

        self.intro = QLabel(self)
        self.intro.move(100, 100)
        self.intro.resize(800, 100)
        self.intro.setText(
            "Приветствую! В этом приложении Вы можете найти все формулы \n"
            "из всего классического школьного курса Физики до 9 класса и подготовки к ОГЭ. "
            "\nТакже это приложение поможет Вам найти формулы\n для решения задач "
            "по известным величинам."
        )
        self.intro.setStyleSheet("color: yellow")
        self.intro.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_choose(self):
        self.choose = Choose()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.choose.move(x, y)
        self.choose.resize(w, h)
        self.choose.show()
        self.close()

    def open_search(self):
        self.search = Search_form()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.search.move(x, y)
        self.search.resize(w, h)
        self.search.show()
        self.close()


class Search_form(First_Wind):
    def __init__(self):
        super().__init__()
        self.back()

    def screen(self):
        super().screen()

    def center(self):
        super().center()

    def start(self):
        pass

    def back(self):
        self.back_btn = QPushButton(self)
        self.back_btn.move(10, 10)
        self.back_btn.setText("<--")
        self.back_btn.clicked.connect(self.back_activ)

    def back_activ(self):
        self.close()
        self.first = First_Wind()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.first.move(x, y)
        self.first.resize(w, h)
        self.first.show()


class Choose(First_Wind):
    def __init__(self):
        super().__init__()
        self.main_f()
        self.mechanic()
        self.thermal()
        self.fluctuation()
        self.electicial()
        self.opt()
        self.atom()
        self.back()

    def screen(self):
        super().screen()

    def center(self):
        super().center()

    def start(self):
        pass

    def main_f(self):
        self.themes = QComboBox(self)
        self.themes.setGeometry(70, 230, 230, 70)
        self.themes.move(750, 10)
        self.themes.addItems(
            [
                "-Выберете тему-",
                "Механика;",
                "Тепловые явления;",
                "Электричество и\nмагнетизм;",
                "Колебания и волны;",
                "Оптика;",
                "Атомная и\nядерная физика;",
            ]
        )
        self.themes.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.themes.setStyleSheet(
            "QComboBox {\n"
            "    border: 2px solid #ffff00;\n"
            "    background-color: #555555;\n"
            "    color: white;\n"
            "    padding-left: 35px;\n"
            "}\n"
            "\n"
            "QComboBox QListView {\n"
            "    border: 2px solid #ffff00;\n"
            "    background-color: #555555;\n"
            "    border-radius: 2px;\n"
            "    selection-background-color: #222222;\n"
            "}\n"
            "\n"
        )
        for el in [
            self.hide_mech,
            self.hide_thermal,
            self.hide_elec_magn,
            self.hide_fluct,
            self.hide_optics,
            self.hide_atomic,
        ]:
            self.themes.activated.connect(el)
        self.f_show = QPushButton(self)
        self.f_show.move(20, 530)
        self.f_show.resize(190, 50)
        self.f_show.setText("Показать формулы")
        self.f_show.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.f_show.clicked.connect(self.form_s)

        self.sp_main = [
            self.mechanic,
            self.thermal,
            self.fluctuation,
            self.electicial,
            self.opt,
            self.atom,
        ]

    def mechanic(self):
        self.kinem = QCheckBox(self)
        self.kinem.move(80, 90)
        self.kinem.stateChanged.connect(self.hide_kin)
        self.kinem.setText("Кинематика")

        self.kin_uni_lin_motion = QCheckBox(self)
        self.kin_uni_lin_motion.move(80, 120)
        self.kin_uni_lin_motion.stateChanged.connect(self.hide_kin)
        self.kin_uni_lin_motion.setText(
            "Равномерное прямолинейное движение"
        )  # v = s/t and x = x0 + Vx * t

        self.kin_aver_speed = QCheckBox(self)
        self.kin_aver_speed.move(80, 150)
        self.kin_aver_speed.stateChanged.connect(self.hide_kin)
        self.kin_aver_speed.setText("Средняя и средняя путевая скорость")
        # vсрп = L1 + L2 +... / t1+t2+... and vср = s / t

        self.kin_uni_accel_motion = QCheckBox(self)
        self.kin_uni_accel_motion.move(80, 180)
        self.kin_uni_accel_motion.stateChanged.connect(self.hide_kin)
        self.kin_uni_accel_motion.setText("Равноускоренное прямолинейное движение")
        # a = v - v0 / t; s = v0t + at^2/2; x = x0 + vx0 * t + ax * t^2/2

        self.kin_up = QCheckBox(self)
        self.kin_up.move(80, 210)
        self.kin_up.stateChanged.connect(self.hide_kin)
        self.kin_up.setText("Тело, брошенное вверх")

        self.kin_down = QCheckBox(self)
        self.kin_down.move(80, 240)
        self.kin_down.stateChanged.connect(self.hide_kin)
        self.kin_down.setText("Тело, брошенное вниз")

        self.kin_uni_circ_lab = QLabel(self)
        self.kin_uni_circ_lab.move(80, 285)
        self.kin_uni_circ_lab.setText("Равномерное движение точки по окружности")
        self.kin_uni_circ_lab.setStyleSheet("color: white")
        self.kin_uni_circ_lab.setFont(QtGui.QFont("Times", 9))
        self.kin_uni_circ_lab.adjustSize()
        self.kin_uni_circ_lab.hide()

        self.kin_uc_per = QCheckBox(self)
        self.kin_uc_per.move(80, 310)
        self.kin_uc_per.stateChanged.connect(self.hide_kin)
        self.kin_uc_per.setText("Период")

        self.kin_uc_freq = QCheckBox(self)
        self.kin_uc_freq.move(80, 340)
        self.kin_uc_freq.stateChanged.connect(self.hide_kin)
        self.kin_uc_freq.setText("Частота")

        self.kin_uc_lin = QCheckBox(self)
        self.kin_uc_lin.move(80, 370)
        self.kin_uc_lin.stateChanged.connect(self.hide_kin)
        self.kin_uc_lin.setText("Линейная скорость")

        self.kin_uc_ang = QCheckBox(self)
        self.kin_uc_ang.move(80, 400)
        self.kin_uc_ang.stateChanged.connect(self.hide_kin)
        self.kin_uc_ang.setText("Угловая скорость")

        self.kin_uc_accel = QCheckBox(self)
        self.kin_uc_accel.move(80, 430)
        self.kin_uc_accel.stateChanged.connect(self.hide_kin)
        self.kin_uc_accel.setText("Центростремительное ускорение")

        self.kin_num_rot = QCheckBox(self)
        self.kin_num_rot.move(80, 460)
        self.kin_num_rot.stateChanged.connect(self.hide_kin)
        self.kin_num_rot.setText("Количество оборотов")

        self.sp_kin = [
            self.kin_uni_lin_motion,
            self.kin_aver_speed,
            self.kin_uni_accel_motion,
            self.kin_uc_per,
            self.kin_uc_freq,
            self.kin_uc_lin,
            self.kin_uc_ang,
            self.kin_uc_accel,
            self.kin_up,
            self.kin_down,
            self.kin_num_rot
        ]

        self.dinam = QCheckBox(self)
        self.dinam.move(280, 90)
        self.dinam.stateChanged.connect(self.hide_dinam)
        self.dinam.setText("Динамика")

        self.din_sec_law = QCheckBox(self)
        self.din_sec_law.move(280, 120)
        self.din_sec_law.stateChanged.connect(self.hide_dinam)
        self.din_sec_law.setText("Второй закон Ньютона")

        self.din_elast = QCheckBox(self)
        self.din_elast.move(280, 150)
        self.din_elast.stateChanged.connect(self.hide_dinam)
        self.din_elast.setText("Силы упругости")

        self.din_friction = QCheckBox(self)
        self.din_friction.move(280, 180)
        self.din_friction.stateChanged.connect(self.hide_dinam)
        self.din_friction.setText("Силы трения")

        self.din_label_gravit = QLabel(self)
        self.din_label_gravit.move(280, 225)
        self.din_label_gravit.setText("Гравитационные силы")
        self.din_label_gravit.setStyleSheet("color: white")
        self.din_label_gravit.setFont(QtGui.QFont("Times", 9))
        self.din_label_gravit.adjustSize()
        self.din_label_gravit.hide()

        self.din_law_gravit = QCheckBox(self)
        self.din_law_gravit.move(280, 250)
        self.din_law_gravit.stateChanged.connect(self.hide_dinam)
        self.din_law_gravit.setText("Закон всемирного тяготения и сила тяжести")

        self.din_weight = QCheckBox(self)
        self.din_weight.move(280, 280)
        self.din_weight.stateChanged.connect(self.hide_dinam)
        self.din_weight.setText("Вес")

        self.din_cos_speed = QCheckBox(self)
        self.din_cos_speed.move(280, 310)
        self.din_cos_speed.stateChanged.connect(self.hide_dinam)
        self.din_cos_speed.setText("Космические скорости")

        self.din_label_save = QLabel(self)
        self.din_label_save.move(280, 355)
        self.din_label_save.setText("Механические явления и законы сохранения")
        self.din_label_save.setStyleSheet("color: white")
        self.din_label_save.setFont(QtGui.QFont("Times", 9))
        self.din_label_save.adjustSize()
        self.din_label_save.hide()

        self.din_momentum = QCheckBox(self)
        self.din_momentum.move(280, 380)
        self.din_momentum.stateChanged.connect(self.hide_dinam)
        self.din_momentum.setText("Импульс")

        self.din_work = QCheckBox(self)
        self.din_work.move(280, 410)
        self.din_work.stateChanged.connect(self.hide_dinam)
        self.din_work.setText("Механическая работа и мощность силы. КПД.")

        self.din_ener_kin = QCheckBox(self)
        self.din_ener_kin.move(280, 440)
        self.din_ener_kin.stateChanged.connect(self.hide_dinam)
        self.din_ener_kin.setText("Кинетическая энергия")

        self.din_ener_pot = QCheckBox(self)
        self.din_ener_pot.move(280, 470)
        self.din_ener_pot.stateChanged.connect(self.hide_dinam)
        self.din_ener_pot.setText("Потенциальная энергия")

        self.din_ener_save = QCheckBox(self)
        self.din_ener_save.move(280, 500)
        self.din_ener_save.stateChanged.connect(self.hide_dinam)
        self.din_ener_save.setText("Закон сохранения энергии")

        self.sp_dinam = [
            self.din_sec_law,
            self.din_law_gravit,
            self.din_cos_speed,
            self.din_elast,
            self.din_friction,
            self.din_weight,
            self.din_momentum,
            self.din_work,
            self.din_ener_kin,
            self.din_ener_pot,
            self.din_ener_save,
        ]

        self.stat = QCheckBox(self)
        self.stat.move(480, 90)
        self.stat.setText("Статика")
        self.stat.stateChanged.connect(self.hide_stat)

        self.st_moment = QCheckBox(self)
        self.st_moment.move(480, 120)
        self.st_moment.setText("Момент силы")
        self.st_moment.stateChanged.connect(self.hide_stat)

        self.st_law_bal = QCheckBox(self)
        self.st_law_bal.move(480, 150)
        self.st_law_bal.setText("Правило равновесия рычагов")
        self.st_law_bal.stateChanged.connect(self.hide_stat)

        self.cond = QCheckBox(self)
        self.cond.move(480, 180)
        self.cond.setText("Два условия равновесия тел")

        self.sp_stat = [self.st_moment, self.st_law_bal, self.cond]

        self.base_concept = QCheckBox(self)
        self.base_concept.move(670, 90)
        self.base_concept.stateChanged.connect(self.hide_base_con)
        self.base_concept.setText("Базовые понятия (7 класс)")

        self.bc_press = QCheckBox(self)
        self.bc_press.move(670, 120)
        self.bc_press.setText("Давление")
        self.bc_press.stateChanged.connect(self.hide_base_con)

        self.bc_mass = QCheckBox(self)
        self.bc_mass.move(670, 150)
        self.bc_mass.setText("Масса, объем, плотность")
        self.bc_mass.stateChanged.connect(self.hide_base_con)

        self.sp_bc = [self.bc_press, self.bc_mass]

        self.sp_mech2 = self.sp_kin + self.sp_dinam + self.sp_stat + self.sp_bc
        for i in range(len(self.sp_mech2)):
            self.sp_mech2[i].setStyleSheet("color: gray")
            self.sp_mech2[i].setFont(QtGui.QFont("Times", 10))
            self.sp_mech2[i].adjustSize()
            self.sp_mech2[i].hide()

        self.sp_mech = [self.kinem, self.dinam, self.stat, self.base_concept]
        for i in range(len(self.sp_mech)):
            self.sp_mech[i].setStyleSheet("color: yellow")
            self.sp_mech[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            self.sp_mech[i].adjustSize()
            self.sp_mech[i].hide()

    def thermal(self):
        self.am_of_heat = QCheckBox(self)
        self.am_of_heat.move(100, 80)
        self.am_of_heat.setText("Количество теплоты")

        self.oil = QCheckBox(self)
        self.oil.move(100, 120)
        self.oil.setText("Энергия топлива")

        self.melt = QCheckBox(self)
        self.melt.move(100, 160)
        self.melt.setText('Количество теплоты при плавлении/кристаллизации')

        self.vapo = QCheckBox(self)
        self.vapo.move(100, 200)
        self.vapo.setText('Количество теплоты при парообразовании/конденсации')

        self.sp_thermal = [self.am_of_heat, self.oil, self.melt, self.vapo]
        for i in range(len(self.sp_thermal)):
            self.sp_thermal[i].setStyleSheet("color: yellow")
            self.sp_thermal[i].stateChanged.connect(self.hide_thermal)
            self.sp_thermal[i].setFont(QtGui.QFont("Times", 10))
            self.sp_thermal[i].adjustSize()
            self.sp_thermal[i].hide()

    def electicial(self):
        self.elec = QCheckBox(self)
        self.elec.move(80, 90)
        self.elec.setText('Электрические явления')
        self.elec.stateChanged.connect(self.hide_elec)

        self.el_current = QCheckBox(self)
        self.el_current.move(80, 120)
        self.el_current.setText('Сила тока')

        self.el_volt = QCheckBox(self)
        self.el_volt.move(80, 150)
        self.el_volt.setText('Электрическое напряжение')

        self.el_res = QCheckBox(self)
        self.el_res.move(80, 180)
        self.el_res.setText('Электрическое сопротивление')

        self.el_om = QCheckBox(self)
        self.el_om.move(80, 210)
        self.el_om.setText('Закон Ома')

        self.el_posled = QCheckBox(self)
        self.el_posled.move(80, 240)
        self.el_posled.setText('Последовательное соединение проводников')

        self.el_paral = QCheckBox(self)
        self.el_paral.move(80, 270)
        self.el_paral.setText('Параллельное соединение проводников')

        self.el_work = QCheckBox(self)
        self.el_work.move(80, 300)
        self.el_work.setText('Работа и мощность электрического тока')

        self.el_jl_low = QCheckBox(self)
        self.el_jl_low.move(80, 330)
        self.el_jl_low.setText('Закон Джоуля-Ленца')

        self.sp_elec = [self.el_current, self.el_volt, self.el_res, self.el_om, self.el_posled, self.el_paral,
                        self.el_work, self.el_jl_low]

        self.magn = QCheckBox(self)
        self.magn.move(430, 90)
        self.magn.setText('Электромагнитные явления')
        self.magn.stateChanged.connect(self.hide_magn)

        self.magn_ind = QCheckBox(self)
        self.magn_ind.move(430, 120)
        self.magn_ind.setText('Индукция магнитного поля')

        self.magn_flow = QCheckBox(self)
        self.magn_flow.move(430, 150)
        self.magn_flow.setText('Магнитный поток')

        self.magn_f_amp = QCheckBox(self)
        self.magn_f_amp.move(430, 180)
        self.magn_f_amp.setText('Сила Ампера')

        self.magn_capas = QCheckBox(self)
        self.magn_capas.move(430, 210)
        self.magn_capas.setText('Электроемкость конденсатора')

        self.sp_magn = [self.magn_ind, self.magn_flow, self.magn_f_amp, self.magn_capas]

        self.sp_elec_magn = [self.elec, self.magn]

        for i in range(len(self.sp_elec_magn)):
            self.sp_elec_magn[i].setStyleSheet("color: yellow")
            self.sp_elec_magn[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            self.sp_elec_magn[i].adjustSize()
            self.sp_elec_magn[i].hide()

        self.sp_elec_magn2 = self.sp_elec + self.sp_magn

        for i in range(len(self.sp_elec_magn2)):
            self.sp_elec_magn2[i].setStyleSheet("color: gray")
            self.sp_elec_magn2[i].stateChanged.connect(self.hide_elec_magn)
            self.sp_elec_magn2[i].setFont(QtGui.QFont("Times", 10))
            self.sp_elec_magn2[i].adjustSize()
            self.sp_elec_magn2[i].hide()

    def fluctuation(self):
        self.fl_per = QCheckBox(self)
        self.fl_per.move(100, 80)
        self.fl_per.setText("Период колебаний")

        self.fl_freq = QCheckBox(self)
        self.fl_freq.move(100, 120)
        self.fl_freq.setText("Период колебаний")

        self.fl_velo = QCheckBox(self)
        self.fl_velo.move(100, 160)
        self.fl_velo.setText("Скорость распространения волны")

        self.sp_fluct = [self.fl_per, self.fl_freq, self.fl_velo]
        for i in range(len(self.sp_fluct)):
            self.sp_fluct[i].setStyleSheet("color: yellow")
            self.sp_fluct[i].stateChanged.connect(self.hide_fluct)
            self.sp_fluct[i].setFont(QtGui.QFont("Times", 10))
            self.sp_fluct[i].adjustSize()
            self.sp_fluct[i].hide()

    def opt(self):
        self.op_low_refl = QCheckBox(self)
        self.op_low_refl.move(80, 90)
        self.op_low_refl.setText('Закон отражения')

        self.op_low_refract = QCheckBox(self)
        self.op_low_refract.move(80, 130)
        self.op_low_refract.setText('Закон преломления')

        self.op_lens_force = QCheckBox(self)
        self.op_lens_force.move(80, 170)
        self.op_lens_force.setText('Оптическая сила линзы')

        self.sp_opt = [self.op_low_refl, self.op_low_refract, self.op_lens_force]
        for i in range(len(self.sp_opt)):
            self.sp_opt[i].setStyleSheet("color: yellow")
            self.sp_opt[i].setFont(QtGui.QFont("Times", 10))
            self.sp_opt[i].stateChanged.connect(self.hide_optics)
            self.sp_opt[i].adjustSize()
            self.sp_opt[i].hide()

        self.op_form_lens = QCheckBox(self)
        self.op_form_lens.move(80, 215)
        self.op_form_lens.stateChanged.connect(self.hide_lens)
        self.op_form_lens.setText('Формула тонкой лизны')
        self.op_form_lens.setStyleSheet("color: yellow")
        self.op_form_lens.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.op_form_lens.adjustSize()
        self.op_form_lens.hide()
        self.sp_opt.append(self.op_form_lens)

        self.op_form_d = QCheckBox(self)
        self.op_form_d.move(80, 240)
        self.op_form_d.setText('Для d > F (собирающая линза)')

        self.op_form_f = QCheckBox(self)
        self.op_form_f.move(80, 270)
        self.op_form_f.setText('Для d < F (собирающая линза)')

        self.op_form_diff = QCheckBox(self)
        self.op_form_diff.move(80, 300)
        self.op_form_diff.setText('Рассеивающая линза')

        self.sp_lens = [self.op_form_diff, self.op_form_f, self.op_form_d]

        for i in range(len(self.sp_lens)):
            self.sp_lens[i].setStyleSheet("color: gray")
            self.sp_lens[i].stateChanged.connect(self.hide_lens)
            self.sp_lens[i].setFont(QtGui.QFont("Times", 10))
            self.sp_lens[i].adjustSize()
            self.sp_lens[i].hide()

    def atom(self):
        self.at_massdef = QCheckBox(self)
        self.at_massdef.move(80, 90)
        self.at_massdef.setText('Дефект массы')

        self.at_ener_con = QCheckBox(self)
        self.at_ener_con.move(80, 130)
        self.at_ener_con.setText("Энергия связи")

        self.at_trans = QCheckBox(self)
        self.at_trans.move(80, 170)
        self.at_trans.setText("Радиоактивные превращения")
        self.at_trans.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.at_trans.setStyleSheet("color: yellow")
        self.at_trans.stateChanged.connect(self.hide_trans)
        self.at_trans.adjustSize()
        self.at_trans.hide()

        self.at_trans_a = QCheckBox(self)
        self.at_trans_a.move(80, 210)
        self.at_trans_a.setText("Альфа-распад")

        self.at_trans_b = QCheckBox(self)
        self.at_trans_b.move(80, 250)
        self.at_trans_b.setText("Бета-распад")

        self.at_trans_g = QCheckBox(self)
        self.at_trans_g.move(80, 290)
        self.at_trans_g.setText("Гамма-распад")

        self.sp_atom = [self.at_massdef, self.at_ener_con, self.at_trans_a, self.at_trans_b, self.at_trans_g]

        for i in range(len(self.sp_atom[:2])):
            self.sp_atom[:2][i].setStyleSheet("color: yellow")
            self.sp_atom[:2][i].stateChanged.connect(self.hide_atomic)
            self.sp_atom[:2][i].setFont(QtGui.QFont("Times", 10))
            self.sp_atom[:2][i].adjustSize()
            self.sp_atom[:2][i].hide()

        for i in range(len(self.sp_atom[2:])):
            self.sp_atom[2:][i].setStyleSheet("color: gray")
            self.sp_atom[2:][i].stateChanged.connect(self.hide_trans)
            self.sp_atom[2:][i].setFont(QtGui.QFont("Times", 10))
            self.sp_atom[2:][i].adjustSize()
            self.sp_atom[2:][i].hide()

    def hide_mech(self):
        if self.themes.currentText() == "Механика;":
            for el in self.sp_mech:
                el.show()
        else:
            for el in self.sp_mech:
                el.setChecked(False)
                el.hide()

    def hide_kin(self):
        if self.kinem.isChecked():
            for el in self.sp_mech:
                if el != self.kinem:
                    el.setChecked(False)
            self.kinem.setStyleSheet("color: gray")
            self.kin_uni_circ_lab.show()
            for i in range(len(self.sp_kin)):
                self.sp_kin[i].show()
        else:
            self.kinem.setStyleSheet("color: yellow")
            self.kin_uni_circ_lab.hide()
            for i in range(len(self.sp_kin)):
                self.sp_kin[i].hide()

    def hide_dinam(self):
        if self.dinam.isChecked():
            for el in self.sp_mech:
                if el != self.dinam:
                    el.setChecked(False)
            self.dinam.setStyleSheet("color: gray")
            self.din_label_gravit.show()
            self.din_label_save.show()
            for i in range(len(self.sp_dinam)):
                self.sp_dinam[i].show()
        else:
            self.dinam.setStyleSheet("color: yellow")
            self.din_label_gravit.hide()
            self.din_label_save.hide()
            for i in range(len(self.sp_dinam)):
                self.sp_dinam[i].hide()

    def hide_stat(self):
        if self.stat.isChecked():
            for el in self.sp_mech:
                if el != self.stat:
                    el.setChecked(False)
            self.stat.setStyleSheet("color: gray")
            for i in range(len(self.sp_stat)):
                self.sp_stat[i].show()
        else:
            self.stat.setStyleSheet("color: yellow")
            for i in range(len(self.sp_stat)):
                self.sp_stat[i].hide()

    def hide_base_con(self):
        if self.base_concept.isChecked():
            for el in self.sp_mech:
                if el != self.base_concept:
                    el.setChecked(False)
            self.base_concept.setStyleSheet("color: gray")
            for i in range(len(self.sp_bc)):
                self.sp_bc[i].show()
        else:
            self.base_concept.setStyleSheet("color: yellow")
            for i in range(len(self.sp_bc)):
                self.sp_bc[i].hide()

    def hide_thermal(self):
        if self.themes.currentText() == "Тепловые явления;":
            for el in self.sp_thermal:
                el.show()
                if el.isChecked():
                    el.setStyleSheet("color: gray")
                else:
                    el.setStyleSheet("color: yellow")
        else:
            for el in self.sp_thermal:
                el.hide()

    def hide_elec_magn(self):
        if self.themes.currentText() == "Электричество и\nмагнетизм;":
            for el in self.sp_elec_magn:
                el.show()
        else:
            for el in self.sp_elec_magn:
                el.setChecked(False)
                el.hide()

    def hide_elec(self):
        if self.elec.isChecked():
            for el in self.sp_elec_magn:
                if el != self.elec:
                    el.setChecked(False)
            self.elec.setStyleSheet("color: gray")
            for i in range(len(self.sp_elec)):
                self.sp_elec[i].show()
        else:
            self.elec.setStyleSheet("color: yellow")
            for i in range(len(self.sp_elec)):
                self.sp_elec[i].hide()

    def hide_magn(self):
        if self.magn.isChecked():
            for el in self.sp_elec_magn:
                if el != self.magn:
                    el.setChecked(False)
            self.magn.setStyleSheet("color: gray")
            for i in range(len(self.sp_magn)):
                self.sp_magn[i].show()
        else:
            self.magn.setStyleSheet("color: yellow")
            for i in range(len(self.sp_magn)):
                self.sp_magn[i].hide()

    def hide_fluct(self):
        if self.themes.currentText() == "Колебания и волны;":
            for el in self.sp_fluct:
                el.show()
                if el.isChecked():
                    el.setStyleSheet("color: gray")
                else:
                    el.setStyleSheet("color: yellow")
        else:
            for el in self.sp_fluct:
                el.hide()

    def hide_optics(self):
        if self.themes.currentText() == "Оптика;":
            for el in self.sp_opt:
                el.show()
                if el.isChecked():
                    el.setStyleSheet("color: gray")
                else:
                    el.setStyleSheet("color: yellow")
        else:
            self.op_form_lens.setChecked(False)
            for el in self.sp_opt:
                el.hide()

    def hide_lens(self):
        if self.op_form_lens.isChecked():
            self.op_form_lens.setStyleSheet("color: gray")
            for i in range(len(self.sp_lens)):
                self.sp_lens[i].show()
        else:
            self.op_form_lens.setStyleSheet("color: yellow")
            for i in range(len(self.sp_lens)):
                self.sp_lens[i].hide()

    def hide_atomic(self):
        if self.themes.currentText() == "Атомная и\nядерная физика;":
            self.at_trans.show()
            for el in self.sp_atom[:2]:
                el.show()
                if el.isChecked():
                    el.setStyleSheet("color: gray")
                else:
                    el.setStyleSheet("color: yellow")
        else:
            self.at_trans.hide()
            self.at_trans.setChecked(False)
            for el in self.sp_atom[:2]:
                el.hide()

    def hide_trans(self):
        if self.at_trans.isChecked():
            self.at_trans.setStyleSheet("color: gray")
            for i in range(len(self.sp_atom[2:])):
                self.sp_atom[2:][i].show()
        else:
            self.at_trans.setStyleSheet("color: yellow")
            for i in range(len(self.sp_atom[2:])):
                self.sp_atom[2:][i].hide()

    def form_s(self):
        self.f_show = Learn_formulas()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.f_show.move(x, y)
        self.f_show.resize(w, h)
        self.f_show.show()
        self.close()

    def back(self):
        self.back_btn = QPushButton(self)
        self.back_btn.move(10, 10)
        self.back_btn.setText("<--")
        self.back_btn.clicked.connect(self.back_activ)

    def back_activ(self):
        self.close()
        self.first = First_Wind()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.first.move(x, y)
        self.first.resize(w, h)
        self.first.show()


class Learn_formulas(First_Wind):
    def __init__(self):
        super().__init__()
        self.back()

    def screen(self):
        super().screen()

    def center(self):
        super().center()

    def start(self):
        pass

    def back(self):
        self.back_btn = QPushButton(self)
        self.back_btn.move(10, 10)
        self.back_btn.setText("<--")
        self.back_btn.clicked.connect(self.back_activ)

    def back_activ(self):
        self.close()
        self.choose = Choose()
        x = self.x()
        y = self.y()
        w = self.width()
        h = self.height()
        self.choose.move(x, y)
        self.choose.resize(w, h)
        self.choose.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = First_Wind()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
