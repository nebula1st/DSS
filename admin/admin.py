

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.core.window import Window
Window.maximize()
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.modalview import ModalView

import pandas as pd
import numpy as np
from datetime import datetime as dt
from utils.connectdb import ConnectDB
from utils.datatable import DataTable
from collections import OrderedDict

class Notify(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.7,.7)

class DSSWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #notif
        self.notify = Notify()

        #crud nilai
        self.ids.list_krit_n.values = []
        conn = ConnectDB().Connect()
        cursor = conn.cursor()
        find_k = ("SELECT * FROM Kriteria")
        cursor.execute(find_k)
        results = cursor.fetchall()
        for i in results:
            self.ids.list_krit_n.values.append(str(i[0]))

        #dates & set spinner nilai & saw values
        self.today = dt.today().date()
        
        year = int(dt.today().date().strftime("%Y"))
        self.ids.list_tahun_n.values = []
        self.ids.list_bulan_n.values = []
        self.ids.list_tahun_s.values = []
        self.ids.list_bulan_s.values = []
        for i in range(year-4, year+1):
            self.ids.list_tahun_n.values.append(str(i))
            self.ids.list_tahun_s.values.append(str(i))
        for i in range(1, 13):
            self.ids.list_bulan_n.values.append(str(i))
            self.ids.list_bulan_s.values.append(str(i))
        
        #karyawan
        karyawan_scrn = self.ids.karyawan_contents
        karyawans = self.get_karyawans()
        karyawans_table = DataTable(table=karyawans)
        karyawan_scrn.add_widget(karyawans_table)

        #kriteria
        kriteria_scrn = self.ids.kriteria_contents
        krtierias = self.get_kriterias()
        kriterias_table = DataTable(table=krtierias)
        kriteria_scrn.add_widget(kriterias_table)

        #subkriteria
        subkriteria_scrn = self.ids.subkriteria_contents
        subkrtierias = self.get_subkriterias()
        subkriterias_table = DataTable(table=subkrtierias)
        subkriteria_scrn.add_widget(subkriterias_table)
        
    def logout(self):
        self.parent.parent.current = 'scrn_log'
        self.ids.file_dropdown.dismiss()

    def add_karyawan_fields(self):
            target = self.ids.ops_fields_k
            target.clear_widgets()
            crud_id = TextInput(hint_text='ID Karyawan',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_divisi = Spinner(text='Divisi',values=['it','mk', 'pr'])
            crud_jk = Spinner(text='JK',values=['P', 'L'])
            crud_ultah = TextInput(hint_text='Tgl Lahir',multiline=False)
            crud_alamat = TextInput(hint_text='Alamat',multiline=False)
            crud_telp = TextInput(hint_text='No Telpon',multiline=False)
            crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_user(crud_id.text, crud_nama.text, crud_divisi.text, crud_jk.text, crud_ultah.text, crud_alamat.text, crud_telp.text))

            target.add_widget(crud_id)
            target.add_widget(crud_nama)
            target.add_widget(crud_divisi)
            target.add_widget(crud_jk)
            target.add_widget(crud_ultah)
            target.add_widget(crud_alamat)
            target.add_widget(crud_telp)
            target.add_widget(crud_submit)

    def update_karyawan_fields(self):
            target = self.ids.ops_fields_k
            target.clear_widgets()
            crud_id = TextInput(hint_text='ID Karyawan',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_divisi = Spinner(text='Divisi',values=['it','mk', 'pr'])
            crud_jk = Spinner(text='JK',values=['P', 'L'])
            crud_ultah = TextInput(hint_text='Tgl Lahir',multiline=False)
            crud_alamat = TextInput(hint_text='Alamat',multiline=False)
            crud_telp = TextInput(hint_text='No Telpon',multiline=False)
            crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_user(crud_id.text, crud_nama.text, crud_divisi.text, crud_jk.text, crud_ultah.text, crud_alamat.text, crud_telp.text))

            target.add_widget(crud_id)
            target.add_widget(crud_nama)
            target.add_widget(crud_divisi)
            target.add_widget(crud_jk)
            target.add_widget(crud_ultah)
            target.add_widget(crud_alamat)
            target.add_widget(crud_telp)
            target.add_widget(crud_submit)

    def remove_karyawan_fields(self):
            target = self.ids.ops_fields_k
            target.clear_widgets()
            crud_id = TextInput(hint_text='ID Karyawan',multiline=False)
            crud_submit = Button(text='Delete',size_hint_x=None,width=100,on_release=lambda x: self.delete_user(crud_id.text))
            target.add_widget(crud_id)
            target.add_widget(crud_submit)

    def add_kriteria_fields(self):
            target = self.ids.ops_fields_krit
            target.clear_widgets()
            crud_kode = TextInput(hint_text='Kode Kriteria',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_bobot = TextInput(hint_text='Bobot',multiline=False)
            crud_keterangan = TextInput(hint_text='Keterangan',multiline=False)
            crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_kriteria(crud_kode.text, crud_nama.text, crud_bobot.text, crud_keterangan.text))

            target.add_widget(crud_kode)
            target.add_widget(crud_nama)
            target.add_widget(crud_bobot)
            target.add_widget(crud_keterangan)
            target.add_widget(crud_submit)

    def update_kriteria_fields(self):
            target = self.ids.ops_fields_krit
            target.clear_widgets()
            crud_kode = TextInput(hint_text='Kode Kriteria',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_bobot = TextInput(hint_text='Bobot',multiline=False)
            crud_keterangan = TextInput(hint_text='Keterangan',multiline=False)
            crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_kriteria(crud_kode.text, crud_nama.text, crud_bobot.text, crud_keterangan.text))

            target.add_widget(crud_kode)
            target.add_widget(crud_nama)
            target.add_widget(crud_bobot)
            target.add_widget(crud_keterangan)
            target.add_widget(crud_submit)

    def remove_kriteria_fields(self):
            target = self.ids.ops_fields_krit
            target.clear_widgets()
            crud_kode = TextInput(hint_text='Kode Kriteria',multiline=False)
            crud_submit = Button(text='Delete',size_hint_x=None,width=100,on_release=lambda x: self.delete_kriteria(crud_kode.text))
            target.add_widget(crud_kode)
            target.add_widget(crud_submit)

    def add_sk_fields(self):
            target = self.ids.ops_fields_sk
            target.clear_widgets()
            crud_kode_kriteria = Spinner(text='Kode K')
            crud_kode_kriteria.values = []
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_k = ("SELECT * FROM Kriteria")
            cursor.execute(find_k)
            results = cursor.fetchall()
            for i in results:
                crud_kode_kriteria.values.append(str(i[0]))
            crud_kode = TextInput(hint_text='Kode SubKriteria',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_bobot = TextInput(hint_text='Bobot',multiline=False)
            crud_keterangan = TextInput(hint_text='Keterangan',multiline=False)
            crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_sk(crud_kode.text, crud_kode_kriteria.text, crud_nama.text, crud_bobot.text, crud_keterangan.text))

            target.add_widget(crud_kode)
            target.add_widget(crud_kode_kriteria)
            target.add_widget(crud_nama)
            target.add_widget(crud_bobot)
            target.add_widget(crud_keterangan)
            target.add_widget(crud_submit)

    def update_sk_fields(self):
            target = self.ids.ops_fields_sk
            target.clear_widgets()
            crud_kode_kriteria = Spinner(text='Kode K')
            crud_kode_kriteria.values = []
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_k = ("SELECT * FROM Kriteria")
            cursor.execute(find_k)
            results = cursor.fetchall()
            for i in results:
                crud_kode_kriteria.values.append(str(i[0]))
            crud_kode = TextInput(hint_text='Kode SubKriteria',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_bobot = TextInput(hint_text='Bobot',multiline=False)
            crud_keterangan = TextInput(hint_text='Keterangan',multiline=False)
            crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_sk(crud_kode.text, crud_kode_kriteria.text, crud_nama.text, crud_bobot.text, crud_keterangan.text))

            target.add_widget(crud_kode)
            target.add_widget(crud_kode_kriteria)
            target.add_widget(crud_nama)
            target.add_widget(crud_bobot)
            target.add_widget(crud_keterangan)
            target.add_widget(crud_submit)

    def remove_sk_fields(self):
            target = self.ids.ops_fields_sk
            target.clear_widgets()
            crud_kode = TextInput(hint_text='Kode SubKriteria',multiline=False)
            crud_submit = Button(text='Delete',size_hint_x=None,width=100,on_release=lambda x: self.delete_sk(crud_kode.text))
            target.add_widget(crud_kode)
            target.add_widget(crud_submit)


    def on_kode_krit_select(self, kode_krit):
            self.ids.list_subkrit_n.values = []
            target = self.ids.ops_fields_n
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_sk = ("SELECT * FROM subKriteria WHERE kode_krit_fk = %s")
            cursor.execute(find_sk, [(kode_krit)])
            results = cursor.fetchall()
            for i in results:
                self.ids.list_subkrit_n.values.append(str(i[0]))   

    def add_nilai_fields(self):
            target = self.ids.ops_fields_n
            target.clear_widgets()
            crud_id = TextInput(hint_text='ID Karyawan',multiline=False)
            crud_tgl = self.today
            crud_nilai = TextInput(hint_text='Nilai',multiline=False)
            crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_nilai(crud_id.text, crud_tgl, self.ids.list_krit_n.text, self.ids.list_subkrit_n.text, crud_nilai.text))

            target.add_widget(crud_id)
            target.add_widget(self.ids.list_krit_n)
            target.add_widget(self.ids.list_subkrit_n)
            target.add_widget(crud_nilai)
            target.add_widget(crud_submit)

    def update_nilai_fields(self):
            target = self.ids.ops_fields_n
            target.clear_widgets()
            crud_kode_kriteria = Spinner(text='Kode K')
            crud_kode_kriteria.values = []
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_k = ("SELECT * FROM Kriteria")
            cursor.execute(find_k)
            results = cursor.fetchall()
            for i in results:
                crud_kode_kriteria.values.append(str(i[0]))
            crud_kode = TextInput(hint_text='Kode SubKriteria',multiline=False)
            crud_nama = TextInput(hint_text='Nama',multiline=False)
            crud_bobot = TextInput(hint_text='Bobot',multiline=False)
            crud_keterangan = TextInput(hint_text='Keterangan',multiline=False)
            crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_sk(crud_kode.text, crud_kode_kriteria.text, crud_nama.text, crud_bobot.text, crud_keterangan.text))

            target.add_widget(crud_kode)
            target.add_widget(crud_kode_kriteria)
            target.add_widget(crud_nama)
            target.add_widget(crud_bobot)
            target.add_widget(crud_keterangan)
            target.add_widget(crud_submit)

    def remove_nilai_fields(self):
            target = self.ids.ops_fields_n
            target.clear_widgets()
            crud_id = TextInput(hint_text='ID Karyawan',multiline=False)
            crud_submit = Button(text='Delete',size_hint_x=None,width=100,on_release=lambda x: self.delete_nilai(crud_id.text, self.ids.list_krit_n.text, self.ids.list_subkrit_n.text))
            target.add_widget(crud_id)
            target.add_widget(self.ids.list_krit_n)
            target.add_widget(self.ids.list_subkrit_n)
            target.add_widget(crud_submit)
        
    def add_user(self, id, nama, divisi, jk, ultah, alamat, telp):
            if id == '' or nama == '' or divisi == 'Divisi' or jk == 'JK' or telp == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM Karyawan WHERE IDKaryawan = %s")
                cursor.execute(find_k, [(id)])
                results = cursor.fetchall()
                if results:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]ID Karyawan Sudah Ada![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)     
                else:
                    insert_karyawan = ("INSERT INTO Karyawan VALUES ( %s, %s, %s, %s, %s, %s, %s)")
                    cursor.execute(insert_karyawan,[(id), (nama), (divisi), (jk),
                                                    (ultah), (alamat), (telp)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Dimasukkan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.karyawan_contents
                content.clear_widgets()

                users = self.get_karyawans()
                userstable = DataTable(table=users)
                content.add_widget(userstable)
    
    def update_user(self, id, nama, divisi, jk, ultah, alamat, telp):
            if id == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]ID Karyawan Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM Karyawan WHERE IDKaryawan = %s")
                cursor.execute(find_k, [(id)])
                results = cursor.fetchall()
                if results:
                    for i in results:
                        if nama == '':
                            nama = i[1]
                        if divisi == 'Divisi':
                            divisi = i[2]
                        if jk == 'JK':
                            jk = i[3]
                        if telp == '':
                            telp = i[6]
                        update_karyawan = ("UPDATE karyawan SET Nama = %s, Divisi = %s, Jns_Kelamin = %s, Tgl_Lahir = %s, Alamat = %s, No_Telpon = %s WHERE IDKaryawan = %s")
                        cursor.execute(update_karyawan,[(nama), (divisi), (jk),
                                                        (ultah), (alamat), (telp), (id)])
                        conn.commit()
                        self.notify.add_widget(Label(text='[color=#FF0000][b]Data Karyawan Sukses Diupdate![/b][/color]',markup=True))
                        self.notify.open()
                        Clock.schedule_once(self.killswitch,2)     
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Karyawan Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.karyawan_contents
                content.clear_widgets()

                users = self.get_karyawans()
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def delete_user(self, id):
            if id == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM Karyawan WHERE IDKaryawan = %s")
                cursor.execute(find_k, [(id)])
                results = cursor.fetchall()
                if results:
                    delete_k = ("DELETE FROM Karyawan WHERE IDKaryawan = %s")
                    cursor.execute(delete_k, [(id)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Karyawan Sukses Dihapus![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch, 2) 
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Karyawan Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.karyawan_contents
                content.clear_widgets()

                users = self.get_karyawans()
                userstable = DataTable(table=users)
                content.add_widget(userstable)
    
    def add_kriteria(self, kode, nama, bobot, keterangan):
            if kode == '' or nama == '' or bobot == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM Kriteria WHERE kode_krit = %s")
                cursor.execute(find_k, [(kode)])
                results = cursor.fetchall()
                if results:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Kriteria Sudah Ada![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)     
                else:
                    show_k = ("SELECT * FROM kriteria")
                    cursor.execute(show_k)
                    results = cursor.fetchall()
                    bobott=0
                    for i in results:
                        bobott = bobott + i[2]
                    if (bobott + float(bobot)) > 1:
                        self.notify.add_widget(Label(text='[color=#FF0000][b]Bobot Kriteria Melebihi 100%![/b][/color]',markup=True))
                        self.notify.open()
                        Clock.schedule_once(self.killswitch,2)  
                    else:
                        insert_kriteria = ("INSERT INTO kriteria VALUES ( %s, %s, %s, %s)")
                        cursor.execute(insert_kriteria,[(kode),(nama),(bobot),(keterangan)])
                        conn.commit()
                        self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Dimasukkan![/b][/color]',markup=True))
                        self.notify.open()
                        Clock.schedule_once(self.killswitch,2)
                content = self.ids.kriteria_contents
                content.clear_widgets()

                users = self.get_kriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)
    
    def update_kriteria(self, kode, nama, bobot, keterangan):
            if kode == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]Kode Kriteria Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM kriteria WHERE kode_krit = %s")
                cursor.execute(find_k, [(kode)])
                results = cursor.fetchall()
                if results:
                    for i in results:
                        if nama == '':
                            nama = i[1]
                        if bobot == '':
                            bobot = i[2]
                        if keterangan == '':
                            keterangan = i[3]
                        show_k = ("SELECT * FROM kriteria")
                        cursor.execute(show_k)
                        results = cursor.fetchall()
                        bobott=0
                        for j in results:
                            bobott = bobott + j[2]
                        if (bobott - i[2] + float(bobot)) > 1:
                            self.notify.add_widget(Label(text='[color=#FF0000][b]Bobot Kriteria Melebihi 100%![/b][/color]',markup=True))
                            self.notify.open()
                            Clock.schedule_once(self.killswitch,2)  
                        else:
                            update_kriteria = ("UPDATE kriteria SET nama_krit = %s, bobot_krit = %s, keterangan_krit = %s WHERE kode_krit = %s")
                            cursor.execute(update_kriteria,[(nama), (bobot), (keterangan), (kode)])
                            conn.commit()
                            self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Diupdate![/b][/color]',markup=True))
                            self.notify.open()
                            Clock.schedule_once(self.killswitch,2)     
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Kriteria Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.kriteria_contents
                content.clear_widgets()

                users = self.get_kriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def delete_kriteria(self, kode):
            if kode == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]Kode Kriteria Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM kriteria WHERE kode_krit = %s")
                cursor.execute(find_k, [(kode)])
                results = cursor.fetchall()
                if results:
                    delete_k = ("DELETE FROM kriteria WHERE kode_krit = %s")
                    cursor.execute(delete_k, [(kode)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Kriteria Sukses Dihapus![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch, 2) 
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Kriteria Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.kriteria_contents
                content.clear_widgets()

                users = self.get_kriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def add_sk(self, kode, kode_kriteria, nama, bobot, keterangan):
            if kode == '' or kode_kriteria == 'Kode K' or nama == '' or bobot == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM SubKriteria WHERE kode_sub = %s")
                cursor.execute(find_k, [(kode)])
                results = cursor.fetchall()
                if results:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]SubKriteria Sudah Ada![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)     
                else:
                    show_sk = ("SELECT * FROM SubKriteria WHERE kode_krit_fk = %s")
                    cursor.execute(show_sk, [(kode_kriteria)])
                    results = cursor.fetchall()
                    bobott=0
                    for i in results:
                        bobott = bobott + i[3]
                    if (bobott + float(bobot)) > 1:
                        self.notify.add_widget(Label(text='[color=#FF0000][b]Bobot SubKriteria Melebihi 100%![/b][/color]',markup=True))
                        self.notify.open()
                        Clock.schedule_once(self.killswitch,2)  
                    else:
                        insert_subkriteria = ("INSERT INTO subkriteria VALUES ( %s, %s, %s, %s, %s)")
                        cursor.execute(insert_subkriteria,[(kode), (kode_kriteria), (nama), (bobot), (keterangan)])
                        conn.commit()
                        self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Dimasukkan![/b][/color]',markup=True))
                        self.notify.open()
                        Clock.schedule_once(self.killswitch,2)
                content = self.ids.subkriteria_contents
                content.clear_widgets()

                users = self.get_subkriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)
    
    def update_sk(self, kode, kode_kriteria, nama, bobot, keterangan):
            if kode == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]Kode SubKriteria Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_k = ("SELECT * FROM subkriteria WHERE kode_sub = %s")
                cursor.execute(find_k, [(kode)])
                results = cursor.fetchall()
                if results:
                    for i in results:
                        if kode_kriteria == 'Kode K':
                            kode_kriteria = i[1]
                        if nama == '':
                            nama = i[2]
                        if bobot == '':
                            bobot = i[3]
                        if keterangan == '':
                            keterangan = i[4]
                        show_sk = ("SELECT * FROM SubKriteria WHERE kode_krit_fk = %s")
                        cursor.execute(show_sk, [(kode_kriteria)])
                        results = cursor.fetchall()
                        bobott=0
                        for j in results:
                            bobott = bobott + j[3]
                        if (bobott - i[3] + float(bobot)) > 1:
                            self.notify.add_widget(Label(text='[color=#FF0000][b]Bobot SubKriteria Melebihi 100%![/b][/color]',markup=True))
                            self.notify.open()
                            Clock.schedule_once(self.killswitch,2)  
                        else:
                            update_kriteria = ("UPDATE subkriteria SET kode_krit_fk = %s, nama_sub = %s, bobot_sub = %s, keterangan_sub = %s WHERE kode_sub = %s")
                            cursor.execute(update_kriteria,[(kode_kriteria), (nama), (bobot), (keterangan), (kode)])
                            conn.commit()
                            self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Diupdate![/b][/color]',markup=True))
                            self.notify.open()
                            Clock.schedule_once(self.killswitch,2)     
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data SubKriteria Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.subkriteria_contents
                content.clear_widgets()

                users = self.get_subkriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def delete_sk(self, kode):
            if kode == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]Kode SubKriteria Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_sk = ("SELECT * FROM subkriteria WHERE kode_sub = %s")
                cursor.execute(find_sk, [(kode)])
                results = cursor.fetchall()
                if results:
                    delete_sk = ("DELETE FROM subkriteria WHERE kode_sub = %s")
                    cursor.execute(delete_sk, [(kode)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data SubKriteria Sukses Dihapus![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch, 2) 
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data SubKriteria Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.subkriteria_contents
                content.clear_widgets()

                users = self.get_subkriterias()
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def add_nilai(self, id, tgl, krit, subkrit, nilai):
            bln = dt.today().date().strftime("%m")
            thn = dt.today().date().strftime("%Y")
            if id == '' or krit == 'Kode K' or subkrit == 'Kode SK' or nilai == '':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_n = ("select * from penilaiankaryawan where IDKaryawan_nilai = %s AND month(Tanggal) = %s && YEAR(Tanggal) = %s AND kode_sub_nilai = %s AND kode_krit_nilai = %s")
                cursor.execute(find_n, [(id), (bln), (thn), (subkrit), (krit)])
                results = cursor.fetchall()
                if results:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Nilai Sudah Ada![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)     
                else:
                    insert_n = ("INSERT INTO penilaiankaryawan VALUES ( %s, %s, %s, %s, %s)")
                    cursor.execute(insert_n,[(id), (tgl), (subkrit), (krit), (nilai)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Sukses Dimasukkan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.nilai_contents
                content.clear_widgets()

                users = self.get_nilais(bln, thn)
                userstable = DataTable(table=users)
                content.add_widget(userstable)
        
    def delete_nilai(self, id, krit, subkrit):
            bln = dt.today().date().strftime("%m")
            thn = dt.today().date().strftime("%Y")
            if id == '' or krit == 'Kode K' or subkrit == 'Kode SK':
                self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]',markup=True))
                self.notify.open()
                Clock.schedule_once(self.killswitch,2)
            else:
                conn = ConnectDB().Connect()
                cursor = conn.cursor()
                find_n = ("select * from penilaiankaryawan where IDKaryawan_nilai = %s AND month(Tanggal) = %s && YEAR(Tanggal) = %s AND kode_sub_nilai = %s AND kode_krit_nilai = %s")
                cursor.execute(find_n, [(id), (bln), (thn), (subkrit), (krit)])
                results = cursor.fetchall()
                if results:
                    delete_n = ("delete from penilaiankaryawan where IDKaryawan_nilai = %s AND month(Tanggal) = %s && YEAR(Tanggal) = %s AND kode_sub_nilai = %s AND kode_krit_nilai = %s")
                    cursor.execute(delete_n, [(id), (bln), (thn), (subkrit), (krit)])
                    conn.commit()
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Nilai Sukses Dihapus![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch, 2) 
                else:
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Data Nilai Tidak Ditemukan![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                content = self.ids.nilai_contents
                content.clear_widgets()

                users = self.get_nilais(bln, thn)
                userstable = DataTable(table=users)
                content.add_widget(userstable)

    def killswitch(self,dtx):
            self.notify.dismiss()
            self.notify.clear_widgets()

    def on_release_nilai(self, bulan, tahun):       
            #nilai
            nilai_scrn = self.ids.nilai_contents
            nilais = self.get_nilais(bulan, tahun)
            nilais_table = DataTable(table=nilais)
            nilai_scrn.clear_widgets()
            nilai_scrn.add_widget(nilais_table)
    
    def on_release_saw(self, bulan, tahun):       
            #saw
            saw_scrn = self.ids.saw_contents
            saws = self.get_saws(bulan, tahun)
            saws_table = DataTable(table=saws)
            saw_scrn.clear_widgets()
            saw_scrn.add_widget(saws_table)

    def on_release_hitung_saw(self, bulan, tahun):       
            #hitung saw
            norm_scrn = self.ids.saw_contents
            norms = self.get_hitungsaws(bulan, tahun)
            norms_table = DataTable(table=norms)
            norm_scrn.clear_widgets()
            norm_scrn.add_widget(norms_table)        

    def get_karyawans(self):
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_user = ("SELECT * FROM karyawan")
            cursor.execute(find_user)
            results = cursor.fetchall()
            _karyawan = OrderedDict()
            _karyawan['No'] = {}
            _karyawan['ID Karyawan'] = {}
            _karyawan['Nama'] = {}
            _karyawan['Divisi'] = {}
            _karyawan['Jns_Kelamin'] = {}
            _karyawan['Tgl_Lahir'] = {}
            _karyawan['Alamat'] = {}
            _karyawan['NoTelpon'] = {}

            No = []
            IDKaryawan = []
            Nama = []
            Divisi = []
            Jns_Kelamin = []
            Tgl_Lahir = []
            Alamat = []
            NoTelpon = []

            noawal = 1
            for i in results:
                No.append(noawal)
                IDKaryawan.append(i[0])
                Nama.append(i[1])
                Divisi.append(i[2])
                Jns_Kelamin.append(i[3])
                Tgl_Lahir.append(i[4])
                Alamat.append(i[5])
                NoTelpon.append(i[6])
                
                noawal+=1
            # print(designations)
            results_length = len(IDKaryawan)
            idx = 0
            while idx < results_length:
                _karyawan['No'][idx] = No[idx]
                _karyawan['ID Karyawan'][idx] = IDKaryawan[idx]
                _karyawan['Nama'][idx] = Nama[idx]
                _karyawan['Divisi'][idx] = Divisi[idx]
                _karyawan['Jns_Kelamin'][idx] = Jns_Kelamin[idx]
                _karyawan['Tgl_Lahir'][idx] = Tgl_Lahir[idx]
                _karyawan['Alamat'][idx] = Alamat[idx]
                _karyawan['NoTelpon'][idx] = NoTelpon[idx]
                
                idx += 1
            
            return _karyawan
    
    def get_kriterias(self):
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_kriteria = ("SELECT * FROM kriteria")
            cursor.execute(find_kriteria)
            results = cursor.fetchall()
            _kriteria = OrderedDict()
            _kriteria['No'] = {}
            _kriteria['Kode Kriteria'] = {}
            _kriteria['Nama Kriteria'] = {}
            _kriteria['Bobot Kriteria'] = {}
            _kriteria['Keterangan'] = {}

            No = []
            Kode = []
            Nama = []
            Bobot = []
            Keterangan = []

            noawal = 1
            for i in results:
                No.append(noawal)
                Kode.append(i[0])
                Nama.append(i[1])
                Bobot.append(i[2])
                Keterangan.append(i[3])
                
                noawal+=1
            # print(designations)
            results_length = len(Kode)
            idx = 0
            while idx < results_length:
                _kriteria['No'][idx] = No[idx]
                _kriteria['Kode Kriteria'][idx] = Kode[idx]
                _kriteria['Nama Kriteria'][idx] = Nama[idx]
                _kriteria['Bobot Kriteria'][idx] = Bobot[idx]
                _kriteria['Keterangan'][idx] = Keterangan[idx]
                
                idx += 1
            
            return _kriteria

    def get_subkriterias(self):
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_subkriteria = ("SELECT * FROM subkriteriaview")
            cursor.execute(find_subkriteria)
            results = cursor.fetchall()
            _subkriteria = OrderedDict()
            _subkriteria['No'] = {}
            _subkriteria['Kode SubKriteria'] = {}
            _subkriteria['Nama SubKriteria'] = {}
            _subkriteria['Nama Kriteria'] = {}
            _subkriteria['Bobot SubKriteria'] = {}
            _subkriteria['Keterangan'] = {}

            No = []
            Kode = []
            Nama = []
            Nama_Krit = []
            Bobot = []
            Keterangan = []

            noawal = 1
            for i in results:
                No.append(noawal)
                Kode.append(i[0])
                Nama.append(i[1])
                Nama_Krit.append(i[2])
                Bobot.append(i[3])
                Keterangan.append(i[4])
                
                noawal+=1
            # print(designations)
            results_length = len(Kode)
            idx = 0
            while idx < results_length:
                _subkriteria['No'][idx] = No[idx]
                _subkriteria['Kode SubKriteria'][idx] = Kode[idx]
                _subkriteria['Nama SubKriteria'][idx] = Nama[idx]
                _subkriteria['Nama Kriteria'][idx] = Nama_Krit[idx]
                _subkriteria['Bobot SubKriteria'][idx] = Bobot[idx]
                _subkriteria['Keterangan'][idx] = Keterangan[idx]
                
                idx += 1
            
            return _subkriteria
    
    def get_nilais(self, bulan, tahun):
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_nilai = ("SELECT * FROM shownilai where MONTH(Tanggal) = %s && YEAR(Tanggal) = %s")
            cursor.execute(find_nilai, [(bulan), (tahun)])
            results = cursor.fetchall()
            _nilai = OrderedDict()
            _nilai['No'] = {}
            _nilai['ID Karyawan'] = {}
            _nilai['Nama'] = {}
            _nilai['Tanggal'] = {}
            _nilai['Nama Kriteria'] = {}
            _nilai['Nama SubKriteria'] = {}
            _nilai['Nilai'] = {}

            No = []
            IDK = []
            Nama = []
            Tanggal = []
            Nama_Krit = []
            Nama_Sub = []
            Nilai = []

            noawal = 1
            for i in results:
                No.append(noawal)
                IDK.append(i[0])
                Nama.append(i[1])
                Tanggal.append(i[2])
                Nama_Krit.append(i[3])
                Nama_Sub.append(i[4])
                Nilai.append(i[5])
                
                noawal+=1
            # print(designations)
            results_length = len(IDK)
            idx = 0
            while idx < results_length:
                _nilai['No'][idx] = No[idx]
                _nilai['ID Karyawan'][idx] = IDK[idx]
                _nilai['Nama'][idx] = Nama[idx]
                _nilai['Tanggal'][idx] = Tanggal[idx]
                _nilai['Nama Kriteria'][idx] = Nama_Krit[idx]
                _nilai['Nama SubKriteria'][idx] = Nama_Sub[idx]
                _nilai['Nilai'][idx] = Nilai[idx]
                
                idx += 1
            
            return _nilai

    def get_saws(self, bulan, tahun):
            alter = {}
            crit = {}
            subcrit = {}
            

            #main_proc_saw
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_saw = ("SELECT IDKaryawan, Nama FROM karyawan")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                alter['{0}'.format(i[0])] = i[1]

            find_saw = ("SELECT kode_krit, bobot_krit FROM kriteria")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                crit['{0}'.format(i[0])] = i[1]

            find_saw = ("SELECT kode_sub, bobot_sub FROM subkriteria")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                subcrit['{0}'.format(i[0])] = i[1]

            _saw = OrderedDict()
            _saw['Alternatif'] = {}
            for i in crit.keys():
                _saw['{0}'.format(i)] = {}

            find_saw = ("select * from showsaw where MONTh(tanggal) = %s && year(tanggal) = %s")
            cursor.execute(find_saw, [(bulan), (tahun)])
            resultss = cursor.fetchall()
            test = {}
            if resultss:
                for i in resultss:
                    for k in crit:
                        if i[1] not in test: 
                            test['{0}'.format(i[1])] = {}
                            if i[1] == k:
                                for j in alter: 
                                    if i[0] not in test['{0}'.format(i[1])]:
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = {}
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = []
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                 
                                    else:
                                        if i[0] == j:
                                            for l in subcrit: 
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                                 
                        else:
                            if i[1] == k:
                                for j in alter:
                                    if i[0] not in test['{0}'.format(i[1])]:
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = {}
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = []
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                   
                                    else:
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                   
                                                    
                for i in test.keys():
                    for j in crit.keys():
                        if i == j:
                            for k, l in test[i].items():
                                for m in alter.keys():
                                    if k == m:
                                        v = l[0]
                                        test[i][k] = v

                df = pd.DataFrame(test)
                
                #outputordereddict
                if df.isnull().values.any():
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Nilai Masih Ada Yang Kosong![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                else:
                    for i, j in alter.items():
                        idx = 0
                        while idx < len(df.index):
                            if i == df.index[idx]:
                                _saw['Alternatif'][idx]=j
                                l=0
                                for k in crit.keys():
                                    _saw['{0}'.format(k)][idx] = df.iloc[idx, l]
                                    l+=1
                            idx+=1

            return _saw

    def get_hitungsaws(self, bulan, tahun):
            _saw = OrderedDict()
            _saw['Alternatif'] = {}
            _saw['Vs'] = {}
            #_saw['C1.2'] = {}
            #_saw['C1.3'] = {}
            #_saw['C1'] = {}

            alter = {}
            crit = {}
            subcrit = {}
            

            #main_proc_saw
            conn = ConnectDB().Connect()
            cursor = conn.cursor()
            find_saw = ("SELECT IDKaryawan, Nama FROM karyawan")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                alter['{0}'.format(i[0])] = i[1]

            find_saw = ("SELECT kode_krit, bobot_krit FROM kriteria")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                crit['{0}'.format(i[0])] = i[1]

            find_saw = ("SELECT kode_sub, bobot_sub FROM subkriteria")
            cursor.execute(find_saw)
            results = cursor.fetchall()
            for i in results:
                subcrit['{0}'.format(i[0])] = i[1]

            find_saw = ("select * from showsaw where MONTh(tanggal) = %s && year(tanggal) = %s")
            cursor.execute(find_saw, [(bulan), (tahun)])
            resultss = cursor.fetchall()
            test = {}
            if resultss:
                for i in resultss:
                    for k in crit:
                        if i[1] not in test: 
                            test['{0}'.format(i[1])] = {}
                            if i[1] == k:
                                for j in alter: 
                                    if i[0] not in test['{0}'.format(i[1])]:
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = {}
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = []
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                 
                                    else:
                                        if i[0] == j:
                                            for l in subcrit: 
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                                 
                        else:
                            if i[1] == k:
                                for j in alter:
                                    if i[0] not in test['{0}'.format(i[1])]:
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = {}
                                        test['{0}'.format(i[1])]['{0}'.format(i[0])] = []
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                                   
                                    else:
                                        if i[0] == j:
                                            for l in subcrit:
                                                if i[2] == l:
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])].append(round(i[3]*i[4], 2))
                                                    
                                                    test['{0}'.format(i[1])]['{0}'.format(i[0])] = [sum(test['{0}'.format(i[1])]['{0}'.format(i[0])])]                   
                for i in test.keys():
                    for j in crit.keys():
                        if i == j:
                            for k, l in test[i].items():
                                for m in alter.keys():
                                    if k == m:
                                        v = l[0]
                                        test[i][k] = v

                df = pd.DataFrame(test)
                
                x, y = df.shape
                
                for i in range(y):
                    V = []
                    for j in range(x):
                            v = round((df.iloc[j, i]/max(df.iloc[:, i])), 2)
                            V.append(v)
                    df.iloc[:, i]=V 
                   
                V = []
                for i in range(x):
                    v = 0
                    j = 0
                    for k in df.columns:
                        for l, m in crit.items():
                            if l == k: 
                                v = v + (df.iloc[i, j]*m)
                                j+=1
                    V.append(round(v, 2))    
                 
                #outputordereddict
                if df.isnull().values.any():
                    self.notify.add_widget(Label(text='[color=#FF0000][b]Nilai Masih Ada Yang Kosong![/b][/color]',markup=True))
                    self.notify.open()
                    Clock.schedule_once(self.killswitch,2)
                else:
                    for i, j in alter.items():
                        idx = 0
                        while idx < len(df.index):
                            if i == df.index[idx]:
                                _saw['Alternatif'][idx] = j
                                _saw['Vs'][idx] = V[idx]
                                break
                            idx+=1

            return _saw

    def change_screen(self, instance):
        if instance.state == 'down':
            if instance.text == 'Manage Karyawan':  
                self.ids.scrn_mngr.current = 'karyawan_content'
            elif instance.text == 'Manage Kriteria':
                self.ids.scrn_mngr.current = 'kriteria_content'
            elif instance.text == 'Manage SubKriteria':
                self.ids.scrn_mngr.current = 'subkriteria_content'
            elif instance.text == 'Manage Nilai':
                self.ids.scrn_mngr.current = 'nilai_content'
            elif instance.text == 'Hitung SAW':
                self.ids.scrn_mngr.current = 'saw_content'
            else:
                self.ids.scrn_mngr.current = 'topsis_content'
        else:
            self.ids.scrn_mngr.current = 'welcome_content'

    

kv = Builder.load_file("admin/admin.kv")

class DSSApp(App):
    def build(self):

        return DSSWindow()

if __name__=='__main__':
    DSSApp().run()