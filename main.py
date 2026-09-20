"""
Tools.py  -  MyTools (prototipe tampilan saja)

Semua fungsi/aksi sengaja KOSONG (pass). Yang jalan hanya:
  - pindah antar layar (supaya kamu bisa lihat semua tampilan)
  - membuka bottom sheet opsi file

Instal & jalankan (PC / Termux):
    pip install kivy kivymd==1.2.0 pillow
    python Tools.py

Untuk buildozer.spec:
    requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
    android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_NETWORK_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CHANGE_WIFI_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,REQUEST_INSTALL_PACKAGES
    # Tanpa baris android.permissions di atas, tool "Wi-Fi Info" akan selalu
    # menampilkan "Tidak tersedia" di semua kolom karena Android menolak
    # akses WIFI_SERVICE/CONNECTIVITY_SERVICE (harus rebuild APK setelah diubah).
    # REQUEST_INSTALL_PACKAGES dibutuhkan supaya on_install_apk() bisa membuka
    # dialog installer sistem (tanpa ini Android akan menolak instalasi APK lain).

    # --- tambahan WAJIB supaya on_install_apk() bisa jalan (FileProvider) ---
    android.enable_androidx = True
    android.res_xml = provider_paths.xml
    android.extra_manifest_application_arguments = extra_manifest_application_arguments.xml
    # provider_paths.xml (taruh di folder project, sejajar buildozer.spec):
    #   <?xml version="1.0" encoding="utf-8"?>
    #   <paths xmlns:android="http://schemas.android.com/apk/res/android">
    #       <external-path name="external_files" path="." />
    #       <cache-path name="cache_files" path="." />
    #   </paths>
    # extra_manifest_application_arguments.xml (taruh di folder yang sama):
    #   <provider
    #       android:name="androidx.core.content.FileProvider"
    #       android:authorities="${applicationId}.fileprovider"
    #       android:exported="false"
    #       android:grantUriPermissions="true">
    #       <meta-data
    #           android:name="android.support.FILE_PROVIDER_PATHS"
    #           android:resource="@xml/provider_paths" />
    #   </provider>
    # Kedua file XML ini contohnya sudah dibuatkan terpisah di luar main.py.
    # Setelah menambahkan ini, MyTools SENDIRI harus di-rebuild (buildozer android
    # debug) baru on_install_apk() bisa membuka installer sistem.

Cara lihat semua layar:
  Home            -> ketuk kartu (Python, APK Builder, File Manager, Terminal, Tools, Pengaturan)
  File Manager    -> ketuk folder "Project"  -> layar Project
  Project         -> ketuk titik tiga (...) di sebuah file -> bottom sheet opsi
  APK Builder     -> ketuk "Pilih project" -> Struktur Project | "Mulai Build" -> Build
  Tools > Text Editor -> buka / edit / simpan file teks (Undo, Redo, Simpan sebagai)
  Tools > ZIP / UNZIP -> tab Kompres & Ekstrak (pakai pemilih file bawaan)
  Tools > HTTP Server -> pilih folder, port, Mulai (alamat bisa disalin, ada log permintaan)
  Tools > Installer   -> install / uninstall paket pip + daftar paket terpasang
  Tools > Sistem  -> info perangkat (ketuk baris = salin, ikon kanan atas = refresh / salin semua)
  Tools > Developer/Teks/Keamanan/Jaringan -> alat cepat baru (JSON, Hash, Base64, URL, Regex,
      Timestamp, UUID, Warna, Konversi Angka, Statistik Teks, Case Converter, Hapus Duplikat,
      Bandingkan Teks, Password/Token Generator, Checksum File, DNS/Reverse DNS, Port Checker,
      IP Publik, Ping, Log Viewer) -- semuanya sudah BERFUNGSI sungguhan (bukan demo).
      QR Generator, File Analyzer, APK Inspector & Kecepatan Jaringan sudah ditambahkan; QR membutuhkan paket qrcode.
  Terminal        -> ikon jam (riwayat) di kanan atas -> lihat & pakai ulang perintah sebelumnya
  Pengaturan      -> ketuk "Tema" untuk ganti Terang / Gelap (tersimpan otomatis)
  Build APK       -> ketuk ikon Android / "Sedang membangun..." -> Build Selesai

======================================================================
DAFTAR FUNGSI YANG BELUM DIKERJAKAN (sebelum revisi ini semuanya "pass")
Dikelompokkan menurut tingkat kesulitan pengerjaan.
======================================================================

[MUDAH]  -> sudah dikerjakan & berfungsi di revisi ini
  - on_search(text)          Home: filter kartu tools sesuai judul
  - on_premium()              Home: info tombol premium (toast)
  - on_choice(widget)          APK Builder: toggle radio Framework & checkbox Arsitektur
  - on_advanced_settings()     APK Builder: info (belum ada layar khusus)
  - on_pick_project()          APK Builder/Project: pilih folder project via FilePicker
  - on_setting(name)           Pengaturan: info tiap item (bahasa, penyimpanan, dst)

[SEDANG] -> sekarang SUNGGUHAN: bekerja pada file & folder asli di penyimpanan
            (sebelumnya hanya daftar demo di memori)
  - File Manager                Menampilkan isi penyimpanan asli. Ketuk folder = masuk,
                                 tombol back = naik satu folder, ketuk file = buka di Text
                                 Editor. Folder berisi buildozer.spec dibuka sebagai Project.
  - on_new() / on_add()         Buat file/folder baru di folder yang sedang dibuka
  - on_select()                 Mode pilih multi-item (checkbox)
  - on_sort()                   Nama A-Z/Z-A, folder dulu, file dulu (diingat per layar)
  - on_options()                Segarkan, Urutkan, Tempel, Pilih + aksi massal Salin/Potong/Hapus
  - on_paste()                  Salin (copytree/copy2) atau pindah (move) sungguhan; nama
                                 bentrok otomatis jadi "nama (2)"
  - on_tab(name)                Python: tab Jalankan / Paket (daftar paket terpasang) /
                                 Project (isi folder project yang dipilih)
  - on_file_action(label)       Rename, Hapus (permanen, ada konfirmasi), Info, Properti
                                 (ukuran & tanggal ubah asli), Salin, Potong, Zip (file .zip
                                 asli), Buka, Edit. "Bagikan" menyalin path asli file.
  Catatan Android 11+: untuk menjelajah SELURUH penyimpanan (bukan hanya folder media/app)
  Android butuh izin "Akses semua file" (MANAGE_EXTERNAL_STORAGE). Tanpa itu, sebagian
  folder tampil "Folder tidak bisa dibuka".

[SULIT]  -> perlu integrasi sistem/OS, proses background, atau eksekusi kode -
            berisiko & perlu desain lebih matang sebelum dikerjakan
  - on_start_build()            SUDAH dikerjakan sungguhan: menjalankan
                                 `buildozer android debug` via subprocess di thread
                                 terpisah, cwd = folder project yang dipilih
                                 (on_pick_project). Log & progress diisi dari output
                                 real buildozer (lihat BUILD_STEP_PATTERNS), APK hasil
                                 dicari otomatis di <project>/bin/*.apk. Butuh
                                 `buildozer` terpasang di PATH (pip install buildozer);
                                 di Termux juga perlu Android SDK/NDK & paket build
                                 tambahan sesuai dokumentasi resmi buildozer.
  - on_run_code()               Python: eksekusi kode Python sungguhan (sandbox/subprocess)
  - on_send_command(cmd)        Terminal: eksekusi perintah shell sungguhan
  - on_install_apk()            SUDAH dikerjakan sungguhan: buka dialog installer
                                 sistem Android lewat Intent ACTION_VIEW + FileProvider
                                 (pyjnius). Pakai APK hasil on_start_build() kalau ada,
                                 kalau tidak pengguna pilih file .apk manual. Menangani
                                 izin khusus "Instal aplikasi tidak dikenal" (Android 8+)
                                 dengan mengarahkan ke Settings kalau belum diizinkan.
                                 WAJIB tambahan di buildozer.spec APLIKASI INI SENDIRI
                                 (bukan project yang di-build) - lihat blok di atas.
  - on_share_apk()               Build Selesai: share APK (Android share intent)
  - on_open_location()           Build Selesai: buka file manager OS ke lokasi APK
  - on_file_action(label)       Bagikan lewat share intent Android (sekarang hanya menyalin path)
======================================================================
"""

import base64
import difflib
import hashlib
import mimetypes
import time
import json
import os
import platform as py_platform
import secrets
import shutil
import re
import string
import subprocess
import sys
import threading
import urllib.parse
import urllib.request
import uuid
import zipfile
import socket
from collections import deque
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.metrics import Metrics, dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.utils import escape_markup, get_color_from_hex, platform

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout  # noqa: F401  (didaftarkan ke Factory)
from kivymd.uix.label import MDIcon, MDLabel  # noqa: F401
from kivymd.uix.screen import MDScreen  # noqa: F401

# Ukuran jendela mirip HP saat dijalankan di PC
if platform not in ("android", "ios"):
    Window.size = (400, 820)

THEMES = {
    "Terang": dict(bg="#FFFFFF", card="#F4F4F5", ink="#111111", muted="#8A8A8E",
                   line="#E4E4E7", accent="#111111", on_accent="#FFFFFF"),
    "Gelap": dict(bg="#141416", card="#212126", ink="#F4F4F5", muted="#A1A1AA",
                  line="#33333A", accent="#F4F4F5", on_accent="#111111"),
}


# =====================================================================
#  WIDGET DASAR (Python)
# =====================================================================
class TapBox(ButtonBehavior, MDBoxLayout):
    """BoxLayout yang bisa diketuk."""


class TopBar(MDBoxLayout):
    title = StringProperty("")
    back = BooleanProperty(True)
    icons = ListProperty([])
    bg = ColorProperty([1, 1, 1, 1])
    fg = ColorProperty([0.07, 0.07, 0.07, 1])

    def on_icons(self, *_):
        Clock.schedule_once(self._build_icons)

    def _build_icons(self, *_):
        box = self.ids.get("right")
        if box is None:
            return
        box.clear_widgets()
        for name in self.icons:
            btn = MDIconButton(
                icon=name,
                theme_icon_color="Custom",
                icon_color=self.fg,
                pos_hint={"center_y": 0.5},
            )
            btn.bind(on_release=lambda w, n=name: MDApp.get_running_app().on_top_icon(n))
            self.fbind("fg", lambda inst, val, b=btn: setattr(b, "icon_color", val))
            box.add_widget(btn)


class ListRow(TapBox):
    icon = StringProperty("folder")
    title = StringProperty("")
    subtitle = StringProperty("")
    trailing = StringProperty("chevron-right")   # "" = tanpa ikon di kanan
    trailing_touch = BooleanProperty(False)      # True = ikon kanan bisa diketuk sendiri
    boxed = BooleanProperty(False)               # True = latar kartu abu muda
    muted_icon = BooleanProperty(False)          # True = ikon abu (untuk file)

    __events__ = ("on_trailing_press",)

    def on_trailing_press(self, *args):
        pass


class ToolTile(TapBox):
    icon = StringProperty("")
    title = StringProperty("")
    subtitle = StringProperty("")


class PrimaryBtn(TapBox):
    text = StringProperty("")
    icon = StringProperty("play")
    outlined = BooleanProperty(False)


class BarItem(TapBox):
    icon = StringProperty("")
    text = StringProperty("")


class Choice(TapBox):
    text = StringProperty("")
    checked = BooleanProperty(False)
    kind = OptionProperty("check", options=["check", "radio", "step"])
    icon = StringProperty("checkbox-blank-outline")

    _ICONS = {
        "check": ("checkbox-marked", "checkbox-blank-outline"),
        "radio": ("radiobox-marked", "radiobox-blank"),
        "step": ("check-circle", "circle-outline"),
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(checked=self._upd, kind=self._upd)
        self._upd()

    def _upd(self, *_):
        on, off = self._ICONS[self.kind]
        self.icon = on if self.checked else off


class PathChip(MDBoxLayout):
    path = StringProperty("")
    icon = StringProperty("cellphone")


class SegItem(TapBox):
    text = StringProperty("")
    active = BooleanProperty(False)


class Boxed(MDBoxLayout):
    """Kotak dengan garis tepi."""
    border_color = ColorProperty(get_color_from_hex("#E4E4E7"))
    corner = NumericProperty(14)


class SheetRow(TapBox):
    icon = StringProperty("")
    text = StringProperty("")


class NameDialog(ModalView):
    """Dialog input teks (nama file, dsb)."""
    title = StringProperty("")
    value = StringProperty("")
    hint = StringProperty("")
    ok_text = StringProperty("Simpan")
    callback = ObjectProperty(None, allownone=True)

    def on_open(self):
        Clock.schedule_once(lambda dt: setattr(self.ids.field, "focus", True), 0.15)

    def confirm(self):
        text, cb = self.ids.field.text.strip(), self.callback
        self.dismiss()
        if cb:
            cb(text)


class ConfirmDialog(ModalView):
    """Dialog konfirmasi Ya/Batal."""
    title = StringProperty("")
    message = StringProperty("")
    ok_text = StringProperty("Lanjut")
    callback = ObjectProperty(None, allownone=True)

    def confirm(self):
        cb = self.callback
        self.dismiss()
        if cb:
            cb()


class FilePicker(ModalView):
    """Pemilih file / folder. mode="file" -> ketuk file; mode="dir" -> tombol 'Pilih folder ini'."""
    title = StringProperty("Pilih file")
    mode = OptionProperty("file", options=["file", "dir"])
    path = StringProperty("")
    path_label = StringProperty("")
    exts = ListProperty([])
    callback = ObjectProperty(None, allownone=True)

    MAX_ROWS = 400

    def __init__(self, start=None, **kw):
        super().__init__(**kw)
        self.go(start or storage_path())

    def go(self, path):
        path = os.path.abspath(path)
        if not os.path.isdir(path):
            return
        self.path = path
        self.path_label = ("…" + path[-34:]) if len(path) > 36 else path
        self._refresh()

    def go_up(self):
        self.go(os.path.dirname(self.path))

    def go_storage(self):
        self.go(storage_path())

    def go_app_data(self):
        self.go(MDApp.get_running_app().user_data_dir)

    def _refresh(self):
        box = self.ids.entries
        box.clear_widgets()
        try:
            names = os.listdir(self.path)
        except Exception:
            box.add_widget(Factory.T4(text="Folder tidak bisa dibuka (izin ditolak)."))
            return
        names.sort(key=lambda n: (not os.path.isdir(os.path.join(self.path, n)), n.lower()))
        shown = 0
        for name in names:
            if name.startswith("."):
                continue
            full = os.path.join(self.path, name)
            is_dir = os.path.isdir(full)
            if not is_dir:
                if self.mode == "dir":
                    continue
                if self.exts and not name.lower().endswith(tuple(self.exts)):
                    continue
            if shown >= self.MAX_ROWS:
                box.add_widget(Factory.T4(text="Terlalu banyak item, sebagian tidak ditampilkan."))
                break
            size = ""
            if not is_dir:
                try:
                    size = fmt_bytes(os.path.getsize(full))
                except Exception:
                    pass
            row = ListRow(
                icon="folder" if is_dir else "file-document-outline",
                muted_icon=not is_dir,
                title=name,
                subtitle=size,
                trailing="chevron-right" if is_dir else "",
            )
            row.bind(on_release=lambda w, f=full, d=is_dir: self.go(f) if d else self._pick(f))
            box.add_widget(row)
            shown += 1
        if shown == 0:
            box.add_widget(Factory.T4(text="Folder kosong."))

    def pick_here(self):
        self._pick(self.path)

    def _pick(self, path):
        cb = self.callback
        self.dismiss()
        if cb:
            cb(path)


class UsageCard(MDBoxLayout):
    """Kartu dengan bar penggunaan (penyimpanan / RAM)."""
    title = StringProperty("")
    percent_text = StringProperty("")
    detail = StringProperty("")
    fraction = NumericProperty(0)


class Toast(Label):
    """Pesan singkat di bagian bawah layar."""


class ThemeDialog(ModalView):
    pass


class FileSheet(ModalView):
    filename = StringProperty("")
    filesize = StringProperty("")


class OptionSheet(ModalView):
    """Bottom sheet generik untuk daftar opsi (Buat baru, Urutkan, Opsi, dsb)."""
    title = StringProperty("")


# =====================================================================
#  TOOLS: SISTEM  (info perangkat, versi, penyimpanan, RAM)
# =====================================================================
def fmt_bytes(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def fmt_duration(sec):
    sec = int(sec)
    d, sec = divmod(sec, 86400)
    h, sec = divmod(sec, 3600)
    m, _ = divmod(sec, 60)
    parts = []
    if d:
        parts.append(f"{d} hari")
    if h:
        parts.append(f"{h} jam")
    parts.append(f"{m} menit")
    return " ".join(parts)


def short_text(v, n=42):
    v = str(v)
    if len(v) <= n:
        return v
    half = n // 2 - 1
    return v[:half] + "…" + v[-half:]


def read_meminfo():
    info = {}
    try:
        with open("/proc/meminfo", encoding="utf-8") as f:
            for line in f:
                key, val = line.split(":", 1)
                info[key] = int(val.strip().split()[0]) * 1024
        return info
    except Exception:
        return None


def read_uptime():
    try:
        with open("/proc/uptime", encoding="utf-8") as f:
            return float(f.read().split()[0])
    except Exception:
        return None


def storage_path():
    try:
        from android.storage import primary_external_storage_path
        return primary_external_storage_path()
    except Exception:
        pass
    for path in ("/storage/emulated/0", "/sdcard"):
        if os.path.isdir(path):
            return path
    return os.path.expanduser("~")


# =====================================================================
#  FILE MANAGER: operasi file/folder SUNGGUHAN (murni Python, tanpa Kivy)
# =====================================================================
FM_MAX_ITEMS = 500


def _count_entries(path, cap=1000):
    n = 0
    try:
        with os.scandir(path) as it:
            for _ in it:
                n += 1
                if n >= cap:
                    return f"{cap}+"
    except Exception:
        return "?"
    return str(n)


def scan_dir(path, limit=FM_MAX_ITEMS):
    """Isi folder nyata -> [(kind, name, meta)], folder dulu lalu nama A-Z.
    Melempar OSError kalau folder tidak bisa dibaca."""
    rows = []
    with os.scandir(path) as it:
        for e in it:
            try:
                is_dir = e.is_dir()
            except OSError:
                is_dir = False
            size = 0
            if not is_dir:
                try:
                    size = e.stat().st_size
                except OSError:
                    pass
            rows.append((is_dir, e.name, e.path, size))
    rows.sort(key=lambda r: (not r[0], r[1].lower()))
    out = []
    for is_dir, name, full, size in rows[:limit]:
        if is_dir:
            out.append(("folder", name, f"{_count_entries(full)} item"))
        else:
            out.append(("file", name, fmt_bytes(size)))
    return out


def dir_size(path, max_files=20000):
    """(total_byte, jumlah_file, terpotong). Berhenti di max_files supaya UI tidak macet."""
    if os.path.isfile(path):
        try:
            return os.path.getsize(path), 1, False
        except OSError:
            return 0, 1, False
    total = count = 0
    for root, _dirs, files in os.walk(path):
        for f in files:
            count += 1
            if count > max_files:
                return total, count - 1, True
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total, count, False


def unique_name(dest_dir, name, is_dir=False):
    """Nama yang belum dipakai di dest_dir: 'a.txt' -> 'a (2).txt', folder 'x' -> 'x (2)'."""
    if not os.path.lexists(os.path.join(dest_dir, name)):
        return name
    stem, ext = (name, "") if is_dir else os.path.splitext(name)
    n = 2
    while True:
        cand = f"{stem} ({n}){ext}"
        if not os.path.lexists(os.path.join(dest_dir, cand)):
            return cand
        n += 1


def is_inside(child, parent):
    c, p = os.path.realpath(child), os.path.realpath(parent)
    return c == p or c.startswith(p.rstrip(os.sep) + os.sep)


def copy_path(src, dest_dir):
    src = src.rstrip(os.sep)
    is_dir = os.path.isdir(src)
    if is_dir and is_inside(dest_dir, src):
        raise ValueError("folder tidak bisa disalin ke dalam dirinya sendiri")
    new = unique_name(dest_dir, os.path.basename(src), is_dir)
    dst = os.path.join(dest_dir, new)
    if is_dir:
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    return new


def move_path(src, dest_dir):
    src = src.rstrip(os.sep)
    is_dir = os.path.isdir(src)
    if os.path.realpath(os.path.dirname(os.path.abspath(src))) == os.path.realpath(dest_dir):
        raise ValueError("item sudah berada di folder ini")
    if is_dir and is_inside(dest_dir, src):
        raise ValueError("folder tidak bisa dipindah ke dalam dirinya sendiri")
    new = unique_name(dest_dir, os.path.basename(src), is_dir)
    shutil.move(src, os.path.join(dest_dir, new))
    return new


def delete_path(path):
    path = path.rstrip(os.sep)
    if os.path.islink(path) or os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


def zip_path(src, dest_dir):
    """Kompres file/folder ke dest_dir/<nama>.zip (nama otomatis unik). Kembalikan nama zip."""
    src = src.rstrip(os.sep)
    base = os.path.basename(src)
    stem = base[:-4] if base.lower().endswith(".zip") else base
    zip_name = unique_name(dest_dir, stem + ".zip")
    zpath = os.path.join(dest_dir, zip_name)
    try:
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
            if os.path.isdir(src):
                parent = os.path.dirname(src)
                zf.write(src, os.path.relpath(src, parent) + "/")
                for root, dirs, files in os.walk(src):
                    for d in dirs:
                        full = os.path.join(root, d)
                        zf.write(full, os.path.relpath(full, parent) + "/")
                    for f in files:
                        full = os.path.join(root, f)
                        if os.path.abspath(full) == os.path.abspath(zpath):
                            continue
                        zf.write(full, os.path.relpath(full, parent))
            else:
                zf.write(src, base)
    except Exception:
        try:
            os.remove(zpath)
        except OSError:
            pass
        raise
    return zip_name


def describe_path(path):
    path = path.rstrip(os.sep)
    is_dir = os.path.isdir(path)
    size, count, cut = dir_size(path)
    plus = "+" if cut else ""
    lines = [f"Nama: {os.path.basename(path)}",
             f"Jenis: {'Folder' if is_dir else 'File'}",
             f"Lokasi: {os.path.dirname(path)}"]
    if is_dir:
        lines.append(f"Isi: {count}{plus} file, {fmt_bytes(size)}{plus}")
    else:
        lines.append(f"Ukuran: {fmt_bytes(size)} ({size} byte)")
    try:
        lines.append("Diubah: " + datetime.fromtimestamp(os.path.getmtime(path)).strftime("%d-%m-%Y %H:%M"))
    except OSError:
        pass
    return "\n".join(lines)


def collect_system_info(data_dir):
    """Kembalikan (usages, groups). groups = [(judul, [(ikon, label, nilai), ...]), ...]"""
    import kivy
    import kivymd

    # --- perangkat ---
    try:  # Android
        from jnius import autoclass
        build = autoclass("android.os.Build")
        version = autoclass("android.os.Build$VERSION")
        device = f"{build.MANUFACTURER} {build.MODEL}".strip()
        os_name = f"Android {version.RELEASE} (SDK {version.SDK_INT})"
    except Exception:  # PC
        device = py_platform.node() or "-"
        os_name = f"{py_platform.system()} {py_platform.release()}"

    groups = [
        ("Perangkat", [
            ("cellphone", "Perangkat", device),
            ("android", "Sistem operasi", os_name),
            ("chip", "Arsitektur", py_platform.machine() or "-"),
            ("cpu-64-bit", "Jumlah core CPU", str(os.cpu_count() or "-")),
            ("monitor", "Layar", f"{Window.width} x {Window.height} px  |  {int(Metrics.dpi)} dpi"),
        ]),
        ("Perangkat lunak", [
            ("language-python", "Python", py_platform.python_version()),
            ("cube-outline", "Kivy", kivy.__version__),
            ("palette-outline", "KivyMD", kivymd.__version__),
            ("folder-outline", "Folder data aplikasi", data_dir),
        ]),
    ]

    waktu = [("clock-outline", "Waktu sekarang", datetime.now().strftime("%d-%m-%Y  %H:%M:%S"))]
    up = read_uptime()
    if up is not None:
        waktu.append(("timer-sand", "Aktif sejak boot", fmt_duration(up)))
    groups.append(("Waktu", waktu))

    # --- penggunaan ---
    usages = []
    try:
        path = storage_path()
        du = shutil.disk_usage(path)
        usages.append(dict(
            title="Penyimpanan",
            fraction=du.used / du.total,
            percent_text=f"{du.used / du.total * 100:.0f}%",
            detail=f"{fmt_bytes(du.used)} terpakai dari {fmt_bytes(du.total)}  |  sisa {fmt_bytes(du.free)}",
        ))
    except Exception:
        pass

    mem = read_meminfo()
    if mem and "MemTotal" in mem and "MemAvailable" in mem:
        total, avail = mem["MemTotal"], mem["MemAvailable"]
        used = total - avail
        usages.append(dict(
            title="RAM",
            fraction=used / total,
            percent_text=f"{used / total * 100:.0f}%",
            detail=f"{fmt_bytes(used)} terpakai dari {fmt_bytes(total)}  |  sisa {fmt_bytes(avail)}",
        ))
    return usages, groups


# =====================================================================
#  TOOLS: HTTP SERVER
# =====================================================================
def get_local_ip():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))  # tidak mengirim paket, hanya memilih interface
        return sock.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        sock.close()


def _int_to_ipv4(value):
    """Konversi integer little-endian ala Android (getIpAddress/DhcpInfo) ke string IPv4."""
    try:
        value = int(value) & 0xFFFFFFFF
        return ".".join(str((value >> (8 * i)) & 0xFF) for i in range(4))
    except Exception:
        return "Tidak tersedia"


def _detect_interface_name(local_ip):
    """Cari nama interface jaringan (wlan0, eth0, dll) yang memiliki alamat IP tertentu."""
    try:
        import psutil
        for name, addrs in psutil.net_if_addrs().items():
            for a in addrs:
                if getattr(a, "address", None) == local_ip:
                    return name
    except Exception:
        pass
    try:
        import glob
        for path in glob.glob("/sys/class/net/*"):
            name = os.path.basename(path)
            try:
                out = subprocess.run(["ip", "-4", "-o", "addr", "show", name],
                                      capture_output=True, text=True, timeout=1.5)
                if local_ip in out.stdout:
                    return name
            except Exception:
                continue
    except Exception:
        pass
    return None


def _detect_ssid_desktop():
    """Coba baca SSID Wi-Fi yang aktif di Linux/Termux (tanpa akses internet)."""
    try:
        out = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True, timeout=1.5)
        ssid = out.stdout.strip()
        if ssid:
            return ssid
    except Exception:
        pass
    try:
        out = subprocess.run(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"],
                              capture_output=True, text=True, timeout=1.5)
        for line in out.stdout.splitlines():
            if line.startswith("yes:"):
                return line.split(":", 1)[1]
    except Exception:
        pass
    try:
        out = subprocess.run(["termux-wifi-connectioninfo"], capture_output=True, text=True, timeout=1.5)
        data = json.loads(out.stdout)
        ssid = str(data.get("ssid", "")).strip('"')
        if ssid and ssid.upper() != "<UNKNOWN SSID>":
            return ssid
    except Exception:
        pass
    return None


def _detect_gateway():
    """Cari alamat gateway/router default (Linux/Termux)."""
    try:
        out = subprocess.run(["ip", "route", "show", "default"],
                              capture_output=True, text=True, timeout=1.5)
        m = re.search(r"default via (\S+)", out.stdout)
        if m:
            return m.group(1)
    except Exception:
        pass
    try:
        with open("/proc/net/route", encoding="utf-8") as f:
            for line in f.readlines()[1:]:
                cols = line.split()
                if len(cols) >= 3 and cols[1] == "00000000":
                    return _int_to_ipv4(int(cols[2], 16))
    except Exception:
        pass
    return None


def _detect_dns():
    """Baca daftar DNS dari /etc/resolv.conf (Linux/Termux)."""
    try:
        servers = []
        with open("/etc/resolv.conf", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("nameserver"):
                    parts = line.split()
                    if len(parts) >= 2:
                        servers.append(parts[1])
        if servers:
            return ", ".join(servers)
    except Exception:
        pass
    return None


class QuietServer(ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):  # abaikan koneksi putus
        pass


def make_handler(directory, log_cb):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_request(self, code="-", size="-"):
            log_cb(f"{self.client_address[0]}  {self.command} {self.path}  {code}")

        def log_message(self, format, *args):
            pass

    return Handler


# =====================================================================
#  TOOLS: INSTALLER (pip)
# =====================================================================
_TOKEN = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._\-]*(\[[A-Za-z0-9,._\-]+\])?"
    r"([<>=!~]=?[A-Za-z0-9.*+!_\-]+(,[<>=!~]=?[A-Za-z0-9.*+!_\-]+)*)?$"
)


def parse_packages(text):
    """Pisahkan nama paket; tolak apa pun yang mirip opsi pip (--xxx)."""
    tokens = text.split()
    if not tokens:
        return None, "Isi nama paket dulu"
    for t in tokens:
        if not _TOKEN.match(t):
            return None, f"Nama paket tidak valid: {t[:20]}"
    return tokens, None


def pip_available():
    import importlib.util
    return bool(sys.executable) and importlib.util.find_spec("pip") is not None


def list_packages():
    from importlib import metadata
    found = {}
    for dist in metadata.distributions():
        try:
            name, ver = dist.metadata["Name"], dist.version
        except Exception:
            continue
        if name:
            found[name.lower()] = (name, ver or "")
    return sorted(found.values(), key=lambda x: x[0].lower())


# =====================================================================
#  DATA TETAP
# =====================================================================
SHEET_ACTIONS = [
    ("eye-outline", "Buka"),
    ("pencil", "Edit"),
    ("content-copy", "Salin"),
    ("content-cut", "Potong"),
    ("delete", "Hapus"),
    ("rename-box", "Rename"),
    ("folder-zip", "Zip"),
    ("information", "Info"),
    ("share-variant", "Bagikan"),
    ("information-outline", "Properti"),
]

# =====================================================================
#  ALAT CEPAT (Developer / Teks / Keamanan / Jaringan) - fungsi murni,
#  dipakai bareng oleh satu layar generik <QuickToolScreen>.
# =====================================================================
def qtfn_json(a, b, mode):
    try:
        obj = json.loads(a)
    except Exception as e:
        return f"❌ JSON tidak valid: {e}"
    if mode == "Ringkas":
        return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
    return json.dumps(obj, indent=2, ensure_ascii=False)


def qtfn_hash(a, b, mode):
    algo = {"MD5": hashlib.md5, "SHA1": hashlib.sha1,
            "SHA256": hashlib.sha256, "SHA512": hashlib.sha512}.get(mode, hashlib.sha256)
    return algo(a.encode("utf-8")).hexdigest()


def qtfn_base64(a, b, mode):
    try:
        if mode == "Decode":
            padded = a.strip() + "=" * (-len(a.strip()) % 4)
            return base64.b64decode(padded.encode()).decode("utf-8", errors="replace")
        return base64.b64encode(a.encode("utf-8")).decode()
    except Exception as e:
        return f"❌ Gagal memproses: {e}"


def qtfn_url(a, b, mode):
    return urllib.parse.unquote(a) if mode == "Decode" else urllib.parse.quote(a)


def qtfn_regex(a, b, mode):
    try:
        pat = re.compile(a)
    except re.error as e:
        return f"❌ Pola regex tidak valid: {e}"
    text = b or ""
    if mode == "Cocok?":
        m = pat.search(text)
        if not m:
            return "❌ Tidak cocok"
        extra = f"\nGrup: {m.groups()}" if m.groups() else ""
        return f"✅ Cocok pada posisi {m.start()}-{m.end()}{extra}"
    found = pat.findall(text)
    return "\n".join(str(f) for f in found) if found else "Tidak ada yang cocok."


def qtfn_timestamp(a, b, mode):
    try:
        if mode == "Sekarang":
            now = datetime.now()
            return f"Unix   : {int(now.timestamp())}\nTanggal: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        if mode == "Tanggal → Unix":
            d = datetime.strptime(a.strip(), "%Y-%m-%d %H:%M:%S")
            return str(int(d.timestamp()))
        ts = float(a.strip())
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return f"❌ Format tidak dikenali ({e}). Pakai unix time atau yyyy-mm-dd HH:MM:SS."


def qtfn_uuid(a, b, mode, length=None):
    return str(uuid.uuid4())


def qtfn_color(a, b, mode):
    try:
        if mode == "RGB → Hex":
            parts = [int(p.strip()) for p in a.replace(";", ",").split(",") if p.strip() != ""]
            r, g, bb = (parts + [0, 0, 0])[:3]
            return f"#{r:02X}{g:02X}{bb:02X}"
        h = a.strip().lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        r, g, bb = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return f"rgb({r}, {g}, {bb})"
    except Exception as e:
        return f"❌ Format warna tidak dikenali: {e}"


def qtfn_number(a, b, mode):
    try:
        n = int(a.strip(), 0)
    except Exception as e:
        return f"❌ Angka tidak valid: {e}"
    return f"Desimal : {n}\nBiner   : {bin(n)}\nOktal   : {oct(n)}\nHeksa   : {hex(n)}"


def qtfn_textstat(a, b, mode):
    words = len(a.split())
    chars = len(a)
    chars_ns = len(re.sub(r"\s", "", a))
    lines = len(a.splitlines()) if a else 0
    return f"Kata          : {words}\nKarakter      : {chars}\nTanpa spasi   : {chars_ns}\nBaris         : {lines}"


def qtfn_case(a, b, mode):
    if mode == "UPPERCASE":
        return a.upper()
    if mode == "lowercase":
        return a.lower()
    if mode == "Title Case":
        return a.title()
    if mode == "Sentence case":
        s = a.strip()
        return (s[:1].upper() + s[1:].lower()) if s else s
    return a.swapcase()


def qtfn_dedupe(a, b, mode):
    seen, out = set(), []
    for ln in a.splitlines():
        if ln not in seen:
            seen.add(ln)
            out.append(ln)
    if mode == "Urutkan A-Z":
        out.sort(key=str.lower)
    return "\n".join(out)


def qtfn_compare(a, b, mode):
    text_b = b or ""
    if a == text_b:
        return "✅ Teks A dan B identik."
    la, lb = a.splitlines(), text_b.splitlines()
    diffs = list(difflib.unified_diff(la, lb, fromfile="Teks A", tofile="Teks B", lineterm=""))
    same = sum(1 for x, y in zip(la, lb) if x == y)
    total = max(len(la), len(lb)) or 1
    head = f"❌ Berbeda (perkiraan {total - same} dari {total} baris berbeda)\n\n"
    return head + "\n".join(diffs[:60])


def qtfn_password(a, b, mode, length=16):
    length = max(4, int(length or 16))
    if mode == "Mudah dibaca (huruf+angka)":
        alphabet = string.ascii_letters + string.digits
    else:
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def qtfn_token(a, b, mode, length=32):
    length = max(8, int(length or 32))
    return secrets.token_hex(length // 2) if mode == "Hex" else secrets.token_urlsafe(length)


def qtfn_dns(a, b, mode):
    try:
        return socket.gethostbyname(a.strip())
    except Exception as e:
        return f"❌ Gagal resolve: {e}"


def qtfn_rdns(a, b, mode):
    try:
        host, _, _ = socket.gethostbyaddr(a.strip())
        return host
    except Exception as e:
        return f"❌ Gagal reverse DNS: {e}"


def qtfn_port(a, b, mode):
    host = a.strip()
    try:
        port = int((b or "").strip())
    except Exception:
        return "❌ Isi port dengan angka, contoh: 443"
    try:
        with socket.create_connection((host, port), timeout=2):
            return f"✅ Port {port} di {host} TERBUKA"
    except Exception as e:
        return f"❌ Port {port} di {host} tertutup / tidak terjangkau ({e.__class__.__name__})"


def qtfn_publicip(a, b, mode):
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=4) as r:
            return r.read().decode().strip()
    except Exception as e:
        return f"❌ Tidak bisa mengambil IP publik, cek koneksi internet ({e.__class__.__name__})"


def qtfn_ping(a, b, mode):
    host = a.strip()
    if not host:
        return "❌ Isi host / alamat IP tujuan"
    flag = "-n" if py_platform.system() == "Windows" else "-c"
    try:
        result = subprocess.run(["ping", flag, "1", host], capture_output=True, text=True, timeout=6)
        out = (result.stdout or result.stderr or "").strip()
        if out:
            return out
        return "✅ Host merespons" if result.returncode == 0 else "❌ Tidak ada balasan"
    except Exception as e:
        return f"❌ Gagal ping: {e}"


# key -> konfigurasi layar <QuickToolScreen>
QT_SPECS = {
    "json": dict(title="JSON Tools", icon="code-json", subtitle="Rapikan / ringkas teks JSON",
                 desc="Tempel JSON, lalu pilih Rapikan atau Ringkas.",
                 hint1="Tempel JSON di sini...", modes=["Rapikan", "Ringkas"],
                 action="Proses", func=qtfn_json),
    "hash": dict(title="Hash Generator", icon="pound-box-outline", subtitle="MD5, SHA1, SHA256, SHA512",
                 desc="Tulis teks lalu pilih algoritma hash.",
                 hint1="Tulis atau tempel teks...", modes=["MD5", "SHA1", "SHA256", "SHA512"],
                 action="Hitung Hash", func=qtfn_hash),
    "base64": dict(title="Base64", icon="code-brackets", subtitle="Encode & decode Base64",
                   desc="Encode teks ke Base64, atau decode kembali.",
                   hint1="Tulis atau tempel teks / Base64...", modes=["Encode", "Decode"],
                   action="Proses", func=qtfn_base64),
    "urltool": dict(title="URL Tools", icon="link-variant", subtitle="Encode & decode URL",
                    desc="Encode teks jadi format URL, atau decode kembali.",
                    hint1="Tulis atau tempel teks / URL...", modes=["Encode", "Decode"],
                    action="Proses", func=qtfn_url),
    "regex": dict(title="Regex Tester", icon="regex", subtitle="Uji pola regular expression",
                  desc="Isi pola regex dan teks yang ingin diuji.",
                  hint1="Pola, contoh: \\d+", hint2="Teks yang diuji",
                  modes=["Cari Semua", "Cocok?"], action="Uji", func=qtfn_regex),
    "timestamp": dict(title="Timestamp", icon="clock-outline", subtitle="Unix time ↔ tanggal",
                       desc="Konversi Unix timestamp ke tanggal, atau sebaliknya.",
                       hint1="Unix time atau yyyy-mm-dd HH:MM:SS",
                       modes=["Unix → Tanggal", "Tanggal → Unix", "Sekarang"],
                       action="Konversi", func=qtfn_timestamp),
    "uuidgen": dict(title="UUID Generator", icon="identifier", subtitle="Buat UUID acak",
                    desc="Ketuk tombol untuk membuat UUID v4 baru.",
                    generate_only=True, action="Buat UUID", func=qtfn_uuid),
    "colortool": dict(title="Color Tools", icon="palette-outline", subtitle="Konversi HEX ↔ RGB",
                       desc="Konversi warna HEX ke RGB, atau sebaliknya.",
                       hint1="#FFAA00  atau  255,170,0",
                       modes=["Hex → RGB", "RGB → Hex"], action="Konversi", func=qtfn_color),
    "numconv": dict(title="Number Converter", icon="numeric", subtitle="Desimal, biner, oktal, heksa",
                    desc="Ketik angka (boleh 0x.. / 0b.. / 0o..), semua bentuk ditampilkan.",
                    hint1="contoh: 255 / 0xFF / 0b1010", action="Konversi", func=qtfn_number),
    "textstat": dict(title="Statistik Teks", icon="counter", subtitle="Jumlah kata, karakter & baris",
                      desc="Tempel teks untuk melihat jumlah kata, karakter, dan baris.",
                      hint1="Tempel teks di sini...", action="Hitung", func=qtfn_textstat),
    "caseconv": dict(title="Case Converter", icon="format-letter-case", subtitle="UPPER, lower, Title, dst",
                      desc="Ubah huruf besar/kecil pada teks.",
                      hint1="Tulis atau tempel teks...",
                      modes=["UPPERCASE", "lowercase", "Title Case", "Sentence case", "sWAP cASE"],
                      action="Ubah", func=qtfn_case),
    "dedupe": dict(title="Hapus Baris Duplikat", icon="playlist-remove", subtitle="Bersihkan baris yang sama",
                   desc="Tempel teks (satu baris = satu item); baris duplikat akan dihapus.",
                   hint1="Tempel daftar / teks per baris...",
                   modes=["Pertahankan Urutan", "Urutkan A-Z"], action="Proses", func=qtfn_dedupe),
    "textcompare": dict(title="Bandingkan Teks", icon="compare-horizontal", subtitle="Cari perbedaan dua teks",
                         desc="Tempel dua teks untuk melihat perbedaannya.",
                         hint1="Teks A", hint2="Teks B", action="Bandingkan", func=qtfn_compare),
    "password": dict(title="Password Generator", icon="form-textbox-password", subtitle="Buat kata sandi acak",
                      desc="Atur panjang & jenis karakter, lalu buat kata sandi.",
                      generate_only=True, has_length=True, length_default=16,
                      modes=["Kuat (semua karakter)", "Mudah dibaca (huruf+angka)"],
                      action="Buat Password", func=qtfn_password),
    "token": dict(title="Token Acak", icon="key-variant", subtitle="Buat token / API key acak",
                  desc="Atur panjang & format, lalu buat token acak.",
                  generate_only=True, has_length=True, length_default=32,
                  modes=["Hex", "URL-safe"], action="Buat Token", func=qtfn_token),
    "dnslookup": dict(title="DNS Lookup", icon="dns-outline", subtitle="Domain → alamat IP",
                       desc="Cari alamat IP dari sebuah nama domain.",
                       hint1="contoh: google.com", action="Cari", func=qtfn_dns),
    "reversedns": dict(title="Reverse DNS", icon="dns", subtitle="Alamat IP → domain",
                        desc="Cari nama domain dari sebuah alamat IP.",
                        hint1="contoh: 8.8.8.8", action="Cari", func=qtfn_rdns),
    "portcheck": dict(title="Port Checker", icon="lan-connect", subtitle="Cek status port terbuka",
                       desc="Cek apakah sebuah port di host tertentu terbuka.",
                       hint1="Host, contoh: google.com", hint2="Port, contoh: 443",
                       action="Cek Port", func=qtfn_port),
    "publicip": dict(title="IP Publik", icon="ip-network-outline", subtitle="Cek alamat IP publik",
                      desc="Ketuk tombol untuk memeriksa alamat IP publik perangkat (butuh internet).",
                      generate_only=True, action="Cek IP", func=qtfn_publicip),
    "ping": dict(title="Ping", icon="access-point-network", subtitle="Uji koneksi ke sebuah host",
                 desc="Kirim ping ke sebuah host atau alamat IP.",
                 hint1="Host, contoh: google.com", action="Ping", func=qtfn_ping),
}

# Fitur yang sebelumnya placeholder sekarang memiliki layar/implementasi sendiri.
PLACEHOLDER_TOOLS = {}

# Pola log buildozer -> label langkah yang ditampilkan di layar Build.
# Best-effort: output buildozer/python-for-android berbeda-beda antar versi,
# jadi ini menebak fase berdasarkan baris log yang paling umum muncul.
BUILD_STEP_PATTERNS = [
    (re.compile(r"check configuration tokens", re.I), "Membaca buildozer.spec"),
    (re.compile(r"ensure build layout|preparing build|check garden", re.I), "Menyiapkan struktur build"),
    (re.compile(r"install(ing)?.*(android sdk|android ndk|sdkmanager)|download.*sdk", re.I),
     "Menyiapkan Android SDK/NDK"),
    (re.compile(r"python-for-android|compil(e|ing) python|build the bootstrap", re.I),
     "Compile Python for Android"),
    (re.compile(r"building the android apk|# building an apk|gradlew|:app:assemble", re.I),
     "Build APK (Gradle)"),
    (re.compile(r"sign(ing)? (the )?apk|apksigner|jarsigner|zipalign", re.I), "Menandatangani APK"),
    (re.compile(r"build successful|apk (created|available)|android packaging done", re.I), "Finalisasi"),
]
BUILD_STEP_LABELS_DEMO = ["Ekstrak project", "Cek file Python", "Install dependencies",
                           "Generate buildozer.spec", "Build APK", "Sign APK", "Finalisasi"]


# =====================================================================
#  TAMPILAN (KV)
# =====================================================================
KV = r"""
#:import dp kivy.metrics.dp
#:import sp kivy.metrics.sp
#:import hx kivy.utils.get_color_from_hex
#:import Window kivy.core.window.Window
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition

#:set BG hx("#FFFFFF")
#:set CARD hx("#F4F4F5")
#:set INK hx("#111111")
#:set MUTED hx("#8A8A8E")
#:set LINE hx("#E4E4E7")
#:set DARK hx("#0B0B0C")
#:set WHITE hx("#FFFFFF")
#:set SOFT hx("#A1A1AA")
#:set CLEAR (0, 0, 0, 0)

# ---------------------------------------------------------------- teks
<Txt@MDLabel>:
    theme_text_color: "Custom"
    text_color: app.c_ink
    adaptive_height: True

<T1@Txt>:
    font_style: "H6"
    bold: True

<T2@Txt>:
    font_style: "Subtitle1"

<T3@Txt>:
    font_style: "Body2"

<T4@Txt>:
    font_style: "Caption"
    text_color: app.c_muted

<Sec@T2>:
    bold: True

<Mono@Label>:
    font_name: "data/fonts/RobotoMono-Regular.ttf"
    font_size: sp(11)
    color: app.c_ink
    markup: True
    halign: "left"
    valign: "top"
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]

<Ic@MDIcon>:
    theme_text_color: "Custom"
    text_color: app.c_ink
    font_size: sp(22)
    size_hint: None, None
    size: dp(24), dp(24)

<Page@MDScreen>:
    md_bg_color: app.c_bg

# ---------------------------------------------------------------- komponen
<TopBar>:
    bg: app.c_bg
    fg: app.c_ink
    size_hint_y: None
    height: dp(56)
    padding: dp(4), 0, dp(4), 0
    md_bg_color: root.bg
    MDIconButton:
        icon: "arrow-left"
        theme_icon_color: "Custom"
        icon_color: root.fg
        opacity: 1 if root.back else 0
        disabled: not root.back
        pos_hint: {"center_y": .5}
        on_release: app.go_back()
    T1:
        text: root.title
        text_color: root.fg
        pos_hint: {"center_y": .5}
    MDBoxLayout:
        id: right
        adaptive_width: True
        pos_hint: {"center_y": .5}

<ListRow>:
    size_hint_y: None
    height: dp(66) if root.subtitle else dp(54)
    padding: dp(14), 0, dp(4), 0
    spacing: dp(14)
    md_bg_color: app.c_card if root.boxed else CLEAR
    radius: [dp(16)]
    Ic:
        icon: root.icon
        text_color: app.c_muted if root.muted_icon else app.c_ink
        pos_hint: {"center_y": .5}
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        pos_hint: {"center_y": .5}
        T3:
            text: root.title
        T4:
            text: root.subtitle
    MDIconButton:
        icon: root.trailing if root.trailing else "chevron-right"
        theme_icon_color: "Custom"
        icon_color: app.c_muted
        opacity: 1 if root.trailing else 0
        pos_hint: {"center_y": .5}
        on_release:
            root.dispatch("on_trailing_press") if root.trailing_touch else root.dispatch("on_release")

<ToolTile>:
    orientation: "vertical"
    size_hint_y: None
    height: dp(124)
    padding: dp(14)
    spacing: dp(4)
    md_bg_color: app.c_card
    radius: [dp(16)]
    Ic:
        icon: root.icon
        font_size: sp(28)
        size: dp(30), dp(30)
    Widget:
    T3:
        text: root.title
        bold: True
    T4:
        text: root.subtitle

<PrimaryBtn>:
    size_hint_y: None
    height: dp(52)
    padding: dp(16), 0
    spacing: dp(8)
    radius: [dp(14)]
    md_bg_color: app.c_bg if root.outlined else app.c_accent
    canvas.after:
        Color:
            rgba: app.c_ink if root.outlined else CLEAR
        Line:
            width: 1.2
            rounded_rectangle: self.x, self.y, self.width, self.height, dp(14)
    Widget:
    Ic:
        icon: root.icon
        text_color: app.c_ink if root.outlined else app.c_on_accent
        pos_hint: {"center_y": .5}
    T3:
        text: root.text
        bold: True
        adaptive_width: True
        text_color: app.c_ink if root.outlined else app.c_on_accent
        pos_hint: {"center_y": .5}
    Widget:

<BarItem>:
    orientation: "vertical"
    padding: 0, dp(8), 0, dp(6)
    spacing: dp(2)
    Ic:
        icon: root.icon
        pos_hint: {"center_x": .5}
    T4:
        text: root.text
        halign: "center"
        text_color: app.c_ink

<BottomBar@MDBoxLayout>:
    size_hint_y: None
    height: dp(64)
    md_bg_color: app.c_bg
    canvas.after:
        Color:
            rgba: app.c_line
        Line:
            width: 1
            points: self.x, self.top, self.right, self.top

<Choice>:
    size_hint_y: None
    height: dp(40)
    padding: dp(4), 0
    spacing: dp(14)
    Ic:
        icon: root.icon
        pos_hint: {"center_y": .5}
    T3:
        text: root.text
        pos_hint: {"center_y": .5}

<PathChip>:
    size_hint_y: None
    height: dp(64)
    padding: dp(16), dp(8)
    MDBoxLayout:
        md_bg_color: app.c_card
        radius: [dp(14)]
        padding: dp(14), 0, dp(14), 0
        spacing: dp(10)
        Ic:
            icon: root.icon
            font_size: sp(18)
            size: dp(20), dp(20)
            pos_hint: {"center_y": .5}
        T3:
            text: root.path
            pos_hint: {"center_y": .5}

<SegItem>:
    radius: [dp(12)]
    md_bg_color: app.c_accent if root.active else CLEAR
    padding: dp(8), 0
    T3:
        text: root.text
        halign: "center"
        pos_hint: {"center_y": .5}
        bold: root.active
        text_color: app.c_on_accent if root.active else app.c_muted

<Boxed>:
    border_color: app.c_line
    md_bg_color: app.c_bg
    radius: [dp(root.corner)]
    canvas.after:
        Color:
            rgba: root.border_color
        Line:
            width: 1
            rounded_rectangle: self.x, self.y, self.width, self.height, dp(root.corner)

<SheetRow>:
    size_hint_y: None
    height: dp(46)
    padding: dp(16), 0
    spacing: dp(20)
    Ic:
        icon: root.icon
        pos_hint: {"center_y": .5}
    T3:
        text: root.text
        pos_hint: {"center_y": .5}

<FileSheet>:
    size_hint: 1, None
    height: min(dp(620), Window.height * .92)
    anchor_y: "bottom"
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(24), dp(24), 0, 0]
        padding: dp(8), dp(8), dp(8), dp(12)
        MDBoxLayout:
            size_hint_y: None
            height: dp(14)
            Widget:
                canvas:
                    Color:
                        rgba: app.c_line
                    RoundedRectangle:
                        pos: self.center_x - dp(20), self.center_y - dp(2)
                        size: dp(40), dp(4)
                        radius: [dp(2)]
        ListRow:
            icon: "file-document-outline"
            title: root.filename
            subtitle: root.filesize
            trailing: ""
        MDBoxLayout:
            id: options
            orientation: "vertical"
            adaptive_height: True
            padding: 0, dp(8), 0, 0

<OptionSheet>:
    size_hint: 1, None
    height: min(dp(460), Window.height * .78)
    anchor_y: "bottom"
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(24), dp(24), 0, 0]
        padding: dp(8), dp(8), dp(8), dp(12)
        MDBoxLayout:
            size_hint_y: None
            height: dp(14)
            Widget:
                canvas:
                    Color:
                        rgba: app.c_line
                    RoundedRectangle:
                        pos: self.center_x - dp(20), self.center_y - dp(2)
                        size: dp(40), dp(4)
                        radius: [dp(2)]
        Sec:
            text: root.title
            padding: dp(14), dp(6), dp(14), dp(4)
        MDBoxLayout:
            id: options
            orientation: "vertical"
            adaptive_height: True
            padding: 0, dp(4), 0, dp(4)

<ThemeDialog>:
    size_hint: .84, None
    height: dp(212)
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(20)]
        padding: dp(20), dp(18), dp(20), dp(12)
        spacing: dp(6)
        Sec:
            text: "Pilih tema"
        Widget:
            size_hint_y: None
            height: dp(4)
        Choice:
            kind: "radio"
            text: "Terang"
            checked: app.theme_name == "Terang"
            on_release:
                app.set_theme("Terang")
                root.dismiss()
        Choice:
            kind: "radio"
            text: "Gelap"
            checked: app.theme_name == "Gelap"
            on_release:
                app.set_theme("Gelap")
                root.dismiss()

<Field@TextInput>:
    multiline: False
    background_normal: ""
    background_active: ""
    background_color: CLEAR
    foreground_color: app.c_ink
    hint_text_color: app.c_muted
    cursor_color: app.c_ink
    font_size: sp(14)
    padding: 0, dp(14), 0, 0

<NameDialog>:
    size_hint: .88, None
    height: dp(212)
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(20)]
        padding: dp(20), dp(18), dp(20), dp(16)
        spacing: dp(12)
        Sec:
            text: root.title
        Boxed:
            size_hint_y: None
            height: dp(48)
            padding: dp(14), 0, dp(14), 0
            Field:
                id: field
                text: root.value
                hint_text: root.hint
                on_text_validate: root.confirm()
        Widget:
        MDBoxLayout:
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)
            PrimaryBtn:
                text: "Batal"
                icon: "close"
                outlined: True
                height: dp(48)
                on_release: root.dismiss()
            PrimaryBtn:
                text: root.ok_text
                icon: "check"
                height: dp(48)
                on_release: root.confirm()

<ConfirmDialog>:
    size_hint: .88, None
    height: dp(206)
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(20)]
        padding: dp(20), dp(18), dp(20), dp(16)
        spacing: dp(10)
        Sec:
            text: root.title
        T3:
            text: root.message
            text_color: app.c_muted
        Widget:
        MDBoxLayout:
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)
            PrimaryBtn:
                text: "Batal"
                icon: "close"
                outlined: True
                height: dp(48)
                on_release: root.dismiss()
            PrimaryBtn:
                text: root.ok_text
                icon: "check"
                height: dp(48)
                on_release: root.confirm()

<FilePicker>:
    size_hint: 1, .92
    anchor_y: "bottom"
    background: ""
    background_color: CLEAR
    overlay_color: 0, 0, 0, .45
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        radius: [dp(24), dp(24), 0, 0]
        padding: dp(12), dp(8), dp(12), dp(12)
        spacing: dp(6)
        MDBoxLayout:
            size_hint_y: None
            height: dp(14)
            Widget:
                canvas:
                    Color:
                        rgba: app.c_line
                    RoundedRectangle:
                        pos: self.center_x - dp(20), self.center_y - dp(2)
                        size: dp(40), dp(4)
                        radius: [dp(2)]
        Sec:
            text: root.title
            padding: dp(8), 0
        MDBoxLayout:
            size_hint_y: None
            height: dp(48)
            md_bg_color: app.c_card
            radius: [dp(14)]
            padding: dp(4), 0, dp(12), 0
            MDIconButton:
                icon: "arrow-up"
                theme_icon_color: "Custom"
                icon_color: app.c_ink
                pos_hint: {"center_y": .5}
                on_release: root.go_up()
            T4:
                text: root.path_label
                text_color: app.c_ink
                pos_hint: {"center_y": .5}
        MDBoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            SegItem:
                text: "Penyimpanan"
                md_bg_color: app.c_card
                on_release: root.go_storage()
            SegItem:
                text: "Data app"
                md_bg_color: app.c_card
                on_release: root.go_app_data()
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                id: entries
                orientation: "vertical"
                adaptive_height: True
                spacing: dp(2)
        PrimaryBtn:
            text: "Pilih folder ini"
            icon: "check"
            height: dp(52) if root.mode == "dir" else 0
            opacity: 1 if root.mode == "dir" else 0
            disabled: root.mode != "dir"
            on_release: root.pick_here()

<UsageCard>:
    orientation: "vertical"
    adaptive_height: True
    md_bg_color: app.c_card
    radius: [dp(16)]
    padding: dp(16)
    spacing: dp(10)
    MDBoxLayout:
        adaptive_height: True
        T3:
            text: root.title
            bold: True
        T4:
            text: root.percent_text
            adaptive_width: True
            text_color: app.c_ink
    Widget:
        size_hint_y: None
        height: dp(8)
        canvas:
            Color:
                rgba: app.c_line
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(4)]
            Color:
                rgba: app.c_ink
            RoundedRectangle:
                pos: self.pos
                size: self.width * root.fraction, self.height
                radius: [dp(4)]
    T4:
        text: root.detail

<Toast>:
    size_hint: None, None
    size: self.texture_size[0] + dp(32), dp(40)
    pos: (Window.width - self.width) / 2, dp(96)
    color: app.c_bg
    font_size: sp(13)
    canvas.before:
        Color:
            rgba: app.c_ink
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(20)]

# ---------------------------------------------------------------- HOME
<HomeScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(16), dp(16), dp(8)
                spacing: dp(14)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(48)
                    spacing: dp(10)
                    Ic:
                        icon: "cube-outline"
                        font_size: sp(32)
                        size: dp(34), dp(34)
                        pos_hint: {"center_y": .5}
                    T1:
                        text: "MyTools"
                        pos_hint: {"center_y": .5}
                    MDIconButton:
                        icon: "cog"
                        theme_icon_color: "Custom"
                        icon_color: app.c_ink
                        pos_hint: {"center_y": .5}
                        on_release: app.goto("settings")
                    MDIconButton:
                        icon: "crown"
                        theme_icon_color: "Custom"
                        icon_color: app.c_ink
                        pos_hint: {"center_y": .5}
                        on_release: app.on_premium()
                T3:
                    text: "Satu aplikasi, banyak tools\nuntuk mempermudah pekerjaanmu."
                    text_color: app.c_muted
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(48)
                    md_bg_color: app.c_card
                    radius: [dp(14)]
                    padding: dp(14), 0, dp(14), 0
                    spacing: dp(10)
                    Ic:
                        icon: "magnify"
                        text_color: app.c_muted
                        pos_hint: {"center_y": .5}
                    TextInput:
                        hint_text: "Cari tools..."
                        multiline: False
                        background_normal: ""
                        background_active: ""
                        background_color: CLEAR
                        foreground_color: app.c_ink
                        hint_text_color: app.c_muted
                        cursor_color: app.c_ink
                        font_size: sp(14)
                        padding: 0, dp(15), 0, 0
                        on_text: app.on_search(self.text)
                MDGridLayout:
                    id: home_grid
                    cols: 2
                    adaptive_height: True
                    spacing: dp(12)
                    ToolTile:
                        icon: "language-python"
                        title: "Python"
                        subtitle: "Jalankan kode Python, kelola paket"
                        on_release: app.goto("python")
                    ToolTile:
                        icon: "language-html5"
                        title: "HTML"
                        subtitle: "Buat dan edit halaman web HTML"
                        on_release: app.goto("editor")
                    ToolTile:
                        icon: "language-css3"
                        title: "CSS"
                        subtitle: "Edit stylesheet untuk tampilan web"
                        on_release: app.goto("editor")
                    ToolTile:
                        icon: "language-javascript"
                        title: "JavaScript"
                        subtitle: "Buat dan edit kode JavaScript"
                        on_release: app.goto("editor")
                    ToolTile:
                        icon: "web-box"
                        title: "Web Project Builder"
                        subtitle: "HTML + CSS + JS → project siap hosting"
                        on_release: app.goto("webproject")
                    ToolTile:
                        icon: "web"
                        title: "Web Preview"
                        subtitle: "Pratinjau project HTML/CSS/JS"
                        on_release: app.goto("editor")
                    ToolTile:
                        icon: "wifi"
                        title: "Hosting Wi-Fi"
                        subtitle: "Bagikan website melalui jaringan Wi-Fi"
                        on_release: app.goto("http")
                    ToolTile:
                        icon: "android"
                        title: "APK Builder"
                        subtitle: "Buat aplikasi Android dari Python"
                        on_release: app.goto("apkbuilder")
                    ToolTile:
                        icon: "folder"
                        title: "File Manager"
                        subtitle: "Kelola file & folder dengan mudah"
                        on_release: app.goto("filemanager")
                    ToolTile:
                        icon: "console"
                        title: "Terminal"
                        subtitle: "Akses shell & perintah sistem"
                        on_release: app.goto("terminal")
                    ToolTile:
                        icon: "wrench"
                        title: "Tools"
                        subtitle: "Utilitas tambahan"
                        on_release: app.goto("tools")
                    ToolTile:
                        icon: "cog"
                        title: "Pengaturan"
                        subtitle: "Atur aplikasi & sistem"
                        on_release: app.goto("settings")
                T4:
                    id: home_empty
                    text: ""
                    halign: "center"

# ---------------------------------------------------------------- FILE MANAGER
<FileManagerScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "File Manager"
            icons: ["magnify", "dots-vertical"]
        PathChip:
            id: fm_path
            path: "Penyimpanan internal  ›"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                id: file_list
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4)
                spacing: dp(2)
        BottomBar:
            BarItem:
                icon: "plus"
                text: "Baru"
                on_release: app.on_new()
            BarItem:
                id: fm_select_btn
                icon: "checkbox-marked-outline"
                text: "Pilih"
                on_release: app.on_select()
            BarItem:
                icon: "swap-vertical"
                text: "Urutkan"
                on_release: app.on_sort()
            BarItem:
                icon: "dots-vertical"
                text: "Opsi"
                on_release: app.on_options()

# ---------------------------------------------------------------- PROJECT (isi folder)
<ProjectScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Project"
            icons: ["magnify", "dots-vertical"]
        PathChip:
            id: project_path
            path: "Project  ›"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                id: project_list
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4)
                spacing: dp(2)
        BottomBar:
            BarItem:
                icon: "plus"
                text: "Tambah"
                on_release: app.on_add()
            BarItem:
                icon: "content-paste"
                text: "Paste"
                on_release: app.on_paste()
            BarItem:
                icon: "dots-horizontal"
                text: "Opsi"
                on_release: app.on_options()

# ---------------------------------------------------------------- APK BUILDER
<ApkBuilderScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "APK Builder"
            icons: ["menu"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(8)
                spacing: dp(10)
                Sec:
                    text: "Project"
                ListRow:
                    id: apk_project_row
                    icon: "folder"
                    title: "Upload ZIP / pilih project"
                    subtitle: "ZIP lengkap → ekstrak otomatis"
                    boxed: True
                    on_release: app.goto("projectstructure")
                Widget:
                    size_hint_y: None
                    height: dp(4)
                Sec:
                    text: "Framework"
                Choice:
                    kind: "radio"
                    text: "Kivy"
                    on_release: app.on_choice(self)
                Choice:
                    kind: "radio"
                    text: "KivyMD"
                    checked: True
                    on_release: app.on_choice(self)
                Widget:
                    size_hint_y: None
                    height: dp(4)
                Sec:
                    text: "Arsitektur"
                Choice:
                    kind: "check"
                    text: "ARM64"
                    checked: True
                    on_release: app.on_choice(self)
                Choice:
                    kind: "check"
                    text: "ARMv7"
                    on_release: app.on_choice(self)
                Choice:
                    kind: "check"
                    text: "x86"
                    on_release: app.on_choice(self)
                Widget:
                    size_hint_y: None
                    height: dp(4)
                ListRow:
                    icon: "cog"
                    title: "Pengaturan Lanjutan"
                    boxed: True
                    on_release: app.on_advanced_settings()
        MDBoxLayout:
            size_hint_y: None
            height: dp(84)
            padding: dp(16), dp(12), dp(16), dp(16)
            PrimaryBtn:
                text: "Mulai Build"
                icon: "play"
                on_release: app.on_start_build()

# ---------------------------------------------------------------- BUILD BERJALAN
<BuildingScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Build APK"
            icons: ["dots-vertical"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(20), dp(8), dp(20), dp(16)
                spacing: dp(10)
                TapBox:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(8)
                    on_release: app.on_tap_building_icon()
                    Ic:
                        icon: "android"
                        font_size: sp(64)
                        size: dp(72), dp(72)
                        pos_hint: {"center_x": .5}
                    T1:
                        text: "Sedang membangun..."
                        halign: "center"
                    T4:
                        text: "Mohon tunggu, proses ini bisa memakan\nwaktu beberapa menit."
                        halign: "center"
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(24)
                    spacing: dp(10)
                    Widget:
                        size_hint_y: None
                        height: dp(8)
                        pos_hint: {"center_y": .5}
                        canvas:
                            Color:
                                rgba: app.c_line
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [dp(4)]
                            Color:
                                rgba: app.c_ink
                            RoundedRectangle:
                                pos: self.pos
                                size: self.width * app.build_fraction, self.height
                                radius: [dp(4)]
                    T4:
                        text: app.build_percent
                        adaptive_width: True
                        text_color: app.c_ink
                        pos_hint: {"center_y": .5}
                Choice:
                    kind: "step"
                    text: app.build_step_labels[0]
                    checked: app.build_steps[0]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[1]
                    checked: app.build_steps[1]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[2]
                    checked: app.build_steps[2]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[3]
                    checked: app.build_steps[3]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[4]
                    checked: app.build_steps[4]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[5]
                    checked: app.build_steps[5]
                Choice:
                    kind: "step"
                    text: app.build_step_labels[6]
                    checked: app.build_steps[6]
                MDBoxLayout:
                    adaptive_height: True
                    md_bg_color: DARK
                    radius: [dp(12)]
                    padding: dp(14)
                    Mono:
                        text: app.LOG_TEXT
                        color: SOFT
        MDBoxLayout:
            size_hint_y: None
            height: dp(68) if app.building_active else 0
            opacity: 1 if app.building_active else 0
            padding: dp(16), dp(8), dp(16), dp(12)
            PrimaryBtn:
                text: "Batal Build"
                icon: "close"
                outlined: True
                on_release: app.build_cancel()

# ---------------------------------------------------------------- BUILD SELESAI
<DoneScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Build APK"
            icons: ["dots-vertical"]
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(20), dp(24), dp(20), dp(16)
            spacing: dp(12)
            Widget:
                size_hint_y: None
                height: dp(12)
            Ic:
                icon: "check-circle"
                font_size: sp(92)
                size: dp(100), dp(100)
                pos_hint: {"center_x": .5}
            T1:
                text: "Build Selesai!"
                halign: "center"
            T4:
                text: "APK berhasil dibuat dengan sukses."
                halign: "center"
            ListRow:
                icon: "android"
                title: app.apk_name
                subtitle: app.apk_size_text
                boxed: True
                trailing: "dots-vertical"
                trailing_touch: True
                on_trailing_press: app.on_options()
            PrimaryBtn:
                text: "Install APK"
                icon: "download"
                on_release: app.on_install_apk()
            PrimaryBtn:
                text: "Bagikan"
                icon: "share-variant"
                outlined: True
                on_release: app.on_share_apk()
            PrimaryBtn:
                text: "Buka Lokasi"
                icon: "folder-outline"
                outlined: True
                on_release: app.on_open_location()
            Widget:

# ---------------------------------------------------------------- PYTHON
<PythonScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Python"
            icons: ["dots-vertical"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4), dp(16), dp(16)
                spacing: dp(12)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    md_bg_color: app.c_card
                    radius: [dp(14)]
                    padding: dp(4)
                    spacing: dp(4)
                    SegItem:
                        id: seg_run
                        text: "Jalankan"
                        active: True
                        on_release: app.on_tab("Jalankan")
                    SegItem:
                        id: seg_pkg
                        text: "Paket"
                        on_release: app.on_tab("Paket")
                    SegItem:
                        id: seg_project
                        text: "Project"
                        on_release: app.on_tab("Project")
                MDBoxLayout:
                    id: py_run_group
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(12)
                    Boxed:
                        size_hint_y: None
                        height: dp(190)
                        padding: dp(14)
                        spacing: dp(14)
                        Mono:
                            text: "1\n2\n3\n4\n5"
                            color: SOFT
                            size_hint_x: None
                            width: dp(14)
                        Mono:
                            text: app.CODE_TEXT
                    PrimaryBtn:
                        text: "Jalankan"
                        icon: "play"
                        on_release: app.on_run_code()
                    Sec:
                        text: "Output"
                    MDBoxLayout:
                        adaptive_height: True
                        md_bg_color: DARK
                        radius: [dp(14)]
                        padding: dp(16)
                        Mono:
                            text: app.OUTPUT_TEXT
                            color: WHITE
                            font_size: sp(12)
                T4:
                    id: py_placeholder
                    text: ""
                    halign: "center"
                MDBoxLayout:
                    id: py_extra
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(2)

# ---------------------------------------------------------------- TERMINAL
<TerminalScreen@Page>:
    md_bg_color: DARK
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Terminal"
            icons: ["history", "magnify", "dots-vertical"]
            bg: DARK
            fg: WHITE
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                adaptive_height: True
                padding: dp(16), dp(8)
                Mono:
                    text: app.TERM_TEXT
                    color: WHITE
                    font_size: sp(12)
        MDBoxLayout:
            size_hint_y: None
            height: dp(80)
            padding: dp(16), dp(12), dp(16), dp(20)
            Boxed:
                md_bg_color: DARK
                border_color: hx("#3F3F46")
                corner: 22
                padding: dp(16), 0, dp(8), 0
                spacing: dp(8)
                TextInput:
                    id: term_input
                    hint_text: "ketik perintah..."
                    multiline: False
                    background_normal: ""
                    background_active: ""
                    background_color: CLEAR
                    foreground_color: WHITE
                    hint_text_color: hx("#71717A")
                    cursor_color: WHITE
                    font_size: sp(13)
                    padding: 0, dp(12), 0, 0
                    on_text_validate: app.on_send_command(self.text)
                TapBox:
                    size_hint: None, None
                    size: dp(32), dp(32)
                    pos_hint: {"center_y": .5}
                    md_bg_color: WHITE
                    radius: [dp(16)]
                    on_release: app.on_send_command(term_input.text)
                    Ic:
                        icon: "play"
                        text_color: DARK
                        font_size: sp(18)
                        size: dp(20), dp(20)
                        pos_hint: {"center_x": .5, "center_y": .5}

# ---------------------------------------------------------------- TOOLS
<ToolsScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Tools"
            icons: ["magnify"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8)
                spacing: dp(10)
                ListRow:
                    icon: "wifi"
                    title: "Wi-Fi Info"
                    subtitle: "SSID, BSSID, signal, speed & frequency"
                    boxed: True
                    on_release: app.on_open_tool("wifiinfo")
                ListRow:
                    icon: "folder-zip-outline"
                    title: "ZIP / UNZIP"
                    subtitle: "Kompres & ekstrak file"
                    boxed: True
                    on_release: app.on_open_tool("zip")
                ListRow:
                    icon: "file-document-edit-outline"
                    title: "Text Editor"
                    subtitle: "Edit file teks"
                    boxed: True
                    on_release: app.on_open_tool("editor")
                ListRow:
                    icon: "server-network"
                    title: "HTTP Server"
                    subtitle: "Jalankan server lokal"
                    boxed: True
                    on_release: app.on_open_tool("http")
                ListRow:
                    icon: "git"
                    title: "Git"
                    subtitle: "Kelola repository"
                    boxed: True
                    on_release: app.on_open_tool("git")
                ListRow:
                    icon: "package-variant-closed"
                    title: "Installer"
                    subtitle: "Install package & dependensi"
                    boxed: True
                    on_release: app.on_open_tool("installer")
                ListRow:
                    icon: "cellphone-cog"
                    title: "Sistem"
                    subtitle: "Info sistem & alat bantu"
                    boxed: True
                    on_release: app.on_open_tool("system")

                Sec:
                    text: "Developer"
                ListRow:
                    icon: "code-json"
                    title: "JSON Tools"
                    subtitle: "Rapikan / ringkas JSON"
                    boxed: True
                    on_release: app.on_open_tool("json")
                ListRow:
                    icon: "pound-box-outline"
                    title: "Hash Generator"
                    subtitle: "MD5, SHA1, SHA256, SHA512"
                    boxed: True
                    on_release: app.on_open_tool("hash")
                ListRow:
                    icon: "code-brackets"
                    title: "Base64"
                    subtitle: "Encode & decode Base64"
                    boxed: True
                    on_release: app.on_open_tool("base64")
                ListRow:
                    icon: "link-variant"
                    title: "URL Tools"
                    subtitle: "Encode & decode URL"
                    boxed: True
                    on_release: app.on_open_tool("urltool")
                ListRow:
                    icon: "regex"
                    title: "Regex Tester"
                    subtitle: "Uji pola regular expression"
                    boxed: True
                    on_release: app.on_open_tool("regex")
                ListRow:
                    icon: "clock-outline"
                    title: "Timestamp"
                    subtitle: "Unix time <-> tanggal"
                    boxed: True
                    on_release: app.on_open_tool("timestamp")
                ListRow:
                    icon: "identifier"
                    title: "UUID Generator"
                    subtitle: "Buat UUID acak"
                    boxed: True
                    on_release: app.on_open_tool("uuidgen")
                ListRow:
                    icon: "palette-outline"
                    title: "Color Tools"
                    subtitle: "Konversi HEX <-> RGB"
                    boxed: True
                    on_release: app.on_open_tool("colortool")
                ListRow:
                    icon: "numeric"
                    title: "Number Converter"
                    subtitle: "Desimal, biner, oktal, heksa"
                    boxed: True
                    on_release: app.on_open_tool("numconv")
                ListRow:
                    icon: "qrcode"
                    title: "QR Generator"
                    subtitle: "Buat QR Code dari teks atau URL"
                    boxed: True
                    on_release: app.on_open_tool("qrgen")
                ListRow:
                    icon: "file-search-outline"
                    title: "File Analyzer"
                    subtitle: "Analisis file, hash, tipe dan struktur"
                    boxed: True
                    on_release: app.on_open_tool("fileanalyzer")
                ListRow:
                    icon: "android"
                    title: "APK Inspector"
                    subtitle: "Lihat isi dan struktur APK"
                    boxed: True
                    on_release: app.on_open_tool("apkinspector")
                ListRow:
                    icon: "file-document-outline"
                    title: "Log Viewer"
                    subtitle: "Log build, installer & terminal"
                    boxed: True
                    on_release: app.on_open_tool("logviewer")

                Sec:
                    text: "Teks"
                ListRow:
                    icon: "counter"
                    title: "Statistik Teks"
                    subtitle: "Jumlah kata, karakter & baris"
                    boxed: True
                    on_release: app.on_open_tool("textstat")
                ListRow:
                    icon: "format-letter-case"
                    title: "Case Converter"
                    subtitle: "UPPER, lower, Title, dst"
                    boxed: True
                    on_release: app.on_open_tool("caseconv")
                ListRow:
                    icon: "playlist-remove"
                    title: "Hapus Baris Duplikat"
                    boxed: True
                    on_release: app.on_open_tool("dedupe")
                ListRow:
                    icon: "compare-horizontal"
                    title: "Bandingkan Teks"
                    subtitle: "Cari perbedaan dua teks"
                    boxed: True
                    on_release: app.on_open_tool("textcompare")

                Sec:
                    text: "Keamanan"
                ListRow:
                    icon: "form-textbox-password"
                    title: "Password Generator"
                    subtitle: "Buat kata sandi acak"
                    boxed: True
                    on_release: app.on_open_tool("password")
                ListRow:
                    icon: "key-variant"
                    title: "Token Acak"
                    subtitle: "Buat token / API key acak"
                    boxed: True
                    on_release: app.on_open_tool("token")
                ListRow:
                    icon: "file-check-outline"
                    title: "Checksum File"
                    subtitle: "MD5, SHA1, SHA256 dari sebuah file"
                    boxed: True
                    on_release: app.on_open_tool("checksum")

                Sec:
                    text: "Jaringan"
                ListRow:
                    icon: "dns-outline"
                    title: "DNS Lookup"
                    subtitle: "Domain -> alamat IP"
                    boxed: True
                    on_release: app.on_open_tool("dnslookup")
                ListRow:
                    icon: "dns"
                    title: "Reverse DNS"
                    subtitle: "Alamat IP -> domain"
                    boxed: True
                    on_release: app.on_open_tool("reversedns")
                ListRow:
                    icon: "lan-connect"
                    title: "Port Checker"
                    subtitle: "Cek status port terbuka"
                    boxed: True
                    on_release: app.on_open_tool("portcheck")
                ListRow:
                    icon: "ip-network-outline"
                    title: "IP Publik"
                    subtitle: "Cek alamat IP publik"
                    boxed: True
                    on_release: app.on_open_tool("publicip")
                ListRow:
                    icon: "access-point-network"
                    title: "Ping"
                    subtitle: "Uji koneksi ke sebuah host"
                    boxed: True
                    on_release: app.on_open_tool("ping")
                ListRow:
                    icon: "speedometer"
                    title: "Kecepatan Jaringan"
                    subtitle: "Tes latency dan download"
                    boxed: True
                    on_release: app.on_open_tool("netspeed")

# ---------------------------------------------------------------- PENGATURAN
<SettingsScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Pengaturan"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4), dp(16), dp(16)
                spacing: dp(8)
                Sec:
                    text: "Umum"
                ListRow:
                    icon: "white-balance-sunny"
                    title: "Tema"
                    subtitle: app.theme_name
                    boxed: True
                    on_release: app.open_theme_dialog()
                ListRow:
                    icon: "earth"
                    title: "Bahasa"
                    subtitle: "Indonesia"
                    boxed: True
                    on_release: app.on_setting("bahasa")
                ListRow:
                    icon: "database"
                    title: "Penyimpanan"
                    subtitle: "Internal"
                    boxed: True
                    on_release: app.on_setting("penyimpanan")
                Widget:
                    size_hint_y: None
                    height: dp(6)
                Sec:
                    text: "Build APK"
                ListRow:
                    icon: "cube-outline"
                    title: "Framework Default"
                    subtitle: "KivyMD"
                    boxed: True
                    on_release: app.on_setting("framework")
                ListRow:
                    icon: "chip"
                    title: "Arsitektur Default"
                    subtitle: "ARM64"
                    boxed: True
                    on_release: app.on_setting("arsitektur")
                ListRow:
                    icon: "language-python"
                    title: "Versi Python"
                    subtitle: "3.11"
                    boxed: True
                    on_release: app.on_setting("python")
                Widget:
                    size_hint_y: None
                    height: dp(6)
                Sec:
                    text: "Tentang"
                ListRow:
                    icon: "information-outline"
                    title: "MyTools"
                    subtitle: "v1.0.0"
                    boxed: True
                    on_release: app.on_setting("tentang")

# ---------------------------------------------------------------- STRUKTUR PROJECT
<ProjectStructureScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Project"
            icons: ["dots-vertical"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4), dp(16), dp(8)
                spacing: dp(10)
                ListRow:
                    id: proj_pick_row
                    icon: "folder"
                    title: "Pilih Project"
                    subtitle: "mytools.zip"
                    boxed: True
                    on_release: app.on_pick_project()
                Sec:
                    text: "Struktur Project"
                MDBoxLayout:
                    id: struct_list
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(2)
        BottomBar:
            BarItem:
                icon: "plus"
                text: "Tambah"
                on_release: app.on_add()
            BarItem:
                id: struct_select_btn
                icon: "checkbox-blank-outline"
                text: "Pilih"
                on_release: app.on_select()
            BarItem:
                icon: "dots-vertical"
                text: "Opsi"
                on_release: app.on_options()

# ---------------------------------------------------------------- TOOLS: SISTEM
<SystemScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Sistem"
            icons: ["refresh", "content-copy"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                id: sys_list
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4), dp(16), dp(16)
                spacing: dp(8)

# ---------------------------------------------------------------- TOOLS: TEXT EDITOR
<EditorScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Text Editor"
            icons: ["content-save-edit-outline"]
        PathChip:
            id: ed_chip
            icon: "file-document-outline"
            path: "Tanpa judul"
        MDBoxLayout:
            padding: dp(16), 0, dp(16), dp(4)
            Boxed:
                padding: dp(2)
                TextInput:
                    id: ed_text
                    font_name: "data/fonts/RobotoMono-Regular.ttf"
                    font_size: sp(13)
                    hint_text: "Ketik di sini..."
                    background_normal: ""
                    background_active: ""
                    background_color: CLEAR
                    foreground_color: app.c_ink
                    hint_text_color: app.c_muted
                    cursor_color: app.c_ink
                    selection_color: .2, .5, 1, .35
                    padding: dp(12)
                    on_text: app.on_editor_changed()
        T4:
            id: ed_status
            text: "Baris 1  |  0 karakter"
            padding: dp(20), dp(4)
        BottomBar:
            BarItem:
                icon: "file-plus-outline"
                text: "Baru"
                on_release: app.editor_new()
            BarItem:
                icon: "folder-open-outline"
                text: "Buka"
                on_release: app.editor_open()
            BarItem:
                icon: "content-save-outline"
                text: "Simpan"
                on_release: app.editor_save()
            BarItem:
                icon: "undo"
                text: "Undo"
                on_release: app.editor_undo()
            BarItem:
                icon: "redo"
                text: "Redo"
                on_release: app.editor_redo()

# ---------------------------------------------------------------- WEB PROJECT BUILDER
<WebProjectScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Web Project Builder"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T3:
                    text: "Gabungkan HTML + CSS + JavaScript menjadi satu project web siap preview dan hosting."
                    text_color: app.c_muted
                ListRow:
                    icon: "folder-edit-outline"
                    title: "Nama Project"
                    subtitle: "Belum dibuat"
                    id: wp_name_row
                    boxed: True
                    on_release: app.web_project_name()
                ListRow:
                    icon: "language-html5"
                    title: "HTML"
                    subtitle: "Pilih file .html"
                    id: wp_html_row
                    boxed: True
                    on_release: app.web_project_pick("html")
                ListRow:
                    icon: "language-css3"
                    title: "CSS"
                    subtitle: "Pilih file .css"
                    id: wp_css_row
                    boxed: True
                    on_release: app.web_project_pick("css")
                ListRow:
                    icon: "language-javascript"
                    title: "JavaScript"
                    subtitle: "Pilih file .js"
                    id: wp_js_row
                    boxed: True
                    on_release: app.web_project_pick("js")
                Sec:
                    text: "Aksi"
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(8)
                    MDButton:
                        text: "BUILD WEBSITE"
                        on_release: app.web_project_build()
                    MDButton:
                        text: "HOST WI-FI"
                        on_release: app.web_project_host()
                ListRow:
                    icon: "folder-open-outline"
                    title: "Buka Folder Project"
                    subtitle: "Lihat hasil project"
                    boxed: True
                    on_release: app.web_project_open_folder()
                ListRow:
                    icon: "web"
                    title: "Preview / Hosting"
                    subtitle: "Setelah build, jalankan Hosting Wi-Fi"
                    boxed: True
                    on_release: app.web_project_host()

# ---------------------------------------------------------------- TOOLS: ZIP / UNZIP
<ZipScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "ZIP / UNZIP"
        MDBoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: dp(16), dp(8), dp(16), dp(8)
            MDBoxLayout:
                md_bg_color: app.c_card
                radius: [dp(14)]
                padding: dp(4)
                spacing: dp(4)
                SegItem:
                    id: seg_compress
                    text: "Kompres"
                    active: True
                    on_release: app.set_zip_tab("compress")
                SegItem:
                    id: seg_extract
                    text: "Ekstrak"
                    on_release: app.set_zip_tab("extract")
        ScreenManager:
            id: zip_sm
            transition: NoTransition()
            Screen:
                name: "compress"
                ScrollView:
                    bar_width: 0
                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        padding: dp(16), dp(4), dp(16), dp(16)
                        spacing: dp(10)
                        Sec:
                            text: "Yang dikompres"
                        MDBoxLayout:
                            id: zip_items_box
                            orientation: "vertical"
                            adaptive_height: True
                            spacing: dp(8)
                        MDBoxLayout:
                            size_hint_y: None
                            height: dp(48)
                            spacing: dp(10)
                            PrimaryBtn:
                                text: "File"
                                icon: "file-plus-outline"
                                outlined: True
                                height: dp(48)
                                on_release: app.zip_add(False)
                            PrimaryBtn:
                                text: "Folder"
                                icon: "folder-plus-outline"
                                outlined: True
                                height: dp(48)
                                on_release: app.zip_add(True)
                        Sec:
                            text: "Nama arsip"
                        Boxed:
                            size_hint_y: None
                            height: dp(48)
                            padding: dp(14), 0, dp(14), 0
                            Field:
                                id: zip_name
                                text: "arsip.zip"
                                hint_text: "arsip.zip"
                        Sec:
                            text: "Simpan di"
                        ListRow:
                            id: zip_out_row
                            icon: "folder"
                            title: "Folder tujuan"
                            subtitle: "Belum dipilih"
                            boxed: True
                            on_release: app.zip_pick_out()
                        Widget:
                            size_hint_y: None
                            height: dp(6)
                        PrimaryBtn:
                            text: "Buat ZIP"
                            icon: "folder-zip"
                            on_release: app.zip_create()
            Screen:
                name: "extract"
                ScrollView:
                    bar_width: 0
                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        padding: dp(16), dp(4), dp(16), dp(16)
                        spacing: dp(10)
                        Sec:
                            text: "File ZIP"
                        ListRow:
                            id: unzip_src_row
                            icon: "folder-zip-outline"
                            title: "Pilih file .zip"
                            subtitle: "Belum dipilih"
                            boxed: True
                            on_release: app.unzip_pick()
                        Sec:
                            text: "Isi arsip"
                        MDBoxLayout:
                            id: unzip_list
                            orientation: "vertical"
                            adaptive_height: True
                            spacing: dp(2)
                        Sec:
                            text: "Ekstrak ke"
                        ListRow:
                            id: unzip_dest_row
                            icon: "folder"
                            title: "Folder tujuan"
                            subtitle: "Belum dipilih"
                            boxed: True
                            on_release: app.unzip_pick_dest()
                        Widget:
                            size_hint_y: None
                            height: dp(6)
                        PrimaryBtn:
                            text: "Ekstrak"
                            icon: "download"
                            on_release: app.unzip_extract()

# ---------------------------------------------------------------- TOOLS: HTTP SERVER
<HttpScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "HTTP Server"
            icons: ["delete-outline"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(4), dp(16), dp(16)
                spacing: dp(10)
                ListRow:
                    id: http_status
                    icon: "server-off"
                    title: "Server berhenti"
                    subtitle: "Pilih folder lalu tekan Mulai"
                    boxed: True
                    trailing: ""
                MDBoxLayout:
                    id: http_urls
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(8)
                Sec:
                    text: "Folder yang dibagikan"
                ListRow:
                    id: http_dir_row
                    icon: "folder"
                    title: "Pilih folder"
                    subtitle: "Belum dipilih"
                    boxed: True
                    on_release: app.http_pick_dir()
                Sec:
                    text: "Port"
                Boxed:
                    size_hint_y: None
                    height: dp(48)
                    padding: dp(14), 0, dp(14), 0
                    Field:
                        id: http_port
                        text: "8000"
                        hint_text: "8000"
                        input_filter: "int"
                Choice:
                    id: http_lan
                    text: "Izinkan perangkat lain (WiFi)"
                    checked: True
                    on_release: self.checked = not self.checked
                T4:
                    text: "Jika aktif, semua perangkat di WiFi yang sama bisa membuka file di folder ini."
                PrimaryBtn:
                    id: http_btn
                    text: "Mulai server"
                    icon: "play"
                    on_release: app.http_toggle()
                Sec:
                    text: "Log permintaan"
                MDBoxLayout:
                    adaptive_height: True
                    md_bg_color: DARK
                    radius: [dp(14)]
                    padding: dp(14)
                    Mono:
                        id: http_log
                        text: "Belum ada permintaan."
                        color: SOFT

# ---------------------------------------------------------------- TOOLS: INSTALLER
<InstallerScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Installer"
            icons: ["refresh"]
        MDBoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: dp(16), dp(8), dp(16), dp(8)
            MDBoxLayout:
                md_bg_color: app.c_card
                radius: [dp(14)]
                padding: dp(4)
                spacing: dp(4)
                SegItem:
                    id: seg_install
                    text: "Install"
                    active: True
                    on_release: app.set_inst_tab("install")
                SegItem:
                    id: seg_pkgs
                    text: "Terpasang"
                    on_release: app.set_inst_tab("pkgs")
        ScreenManager:
            id: inst_sm
            transition: NoTransition()
            Screen:
                name: "install"
                ScrollView:
                    bar_width: 0
                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        padding: dp(16), dp(4), dp(16), dp(16)
                        spacing: dp(10)
                        ListRow:
                            id: inst_info
                            icon: "information-outline"
                            title: "Status pip"
                            subtitle: "Memeriksa..."
                            boxed: True
                            trailing: ""
                        Sec:
                            text: "Nama paket"
                        Boxed:
                            size_hint_y: None
                            height: dp(48)
                            padding: dp(14), 0, dp(14), 0
                            Field:
                                id: inst_field
                                hint_text: "contoh: requests numpy==1.26.4"
                        Choice:
                            id: inst_upgrade
                            text: "Upgrade jika sudah terpasang"
                            on_release: self.checked = not self.checked
                        MDBoxLayout:
                            size_hint_y: None
                            height: dp(48)
                            spacing: dp(10)
                            PrimaryBtn:
                                id: inst_btn_install
                                text: "Install"
                                icon: "download"
                                height: dp(48)
                                on_release: app.pip_run("install")
                            PrimaryBtn:
                                id: inst_btn_uninstall
                                text: "Uninstall"
                                icon: "delete-outline"
                                outlined: True
                                height: dp(48)
                                on_release: app.pip_run("uninstall")
                        PrimaryBtn:
                            id: inst_btn_cancel
                            text: "Batalkan"
                            icon: "close"
                            outlined: True
                            height: 0
                            opacity: 0
                            disabled: True
                            on_release: app.pip_cancel()
                        Sec:
                            text: "Output"
                        MDBoxLayout:
                            adaptive_height: True
                            md_bg_color: DARK
                            radius: [dp(14)]
                            padding: dp(14)
                            Mono:
                                id: inst_log
                                text: "Belum ada output."
                                color: SOFT
            Screen:
                name: "pkgs"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(16), dp(4), dp(16), dp(0)
                    spacing: dp(8)
                    Boxed:
                        size_hint_y: None
                        height: dp(48)
                        padding: dp(14), 0, dp(14), 0
                        Field:
                            id: pkg_search
                            hint_text: "Cari paket..."
                            on_text: app.refresh_packages()
                    T4:
                        id: pkg_count
                        text: ""
                    ScrollView:
                        bar_width: 0
                        MDBoxLayout:
                            id: pkg_list
                            orientation: "vertical"
                            adaptive_height: True
                            padding: 0, 0, 0, dp(16)
                            spacing: dp(2)

# ---------------------------------------------------------------- WI-FI INFO
<WifiInfoScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.c_bg
        TopBar:
            title: "Wi-Fi Info"
            icons: ["refresh", "content-copy"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(10), dp(16), dp(20)
                spacing: dp(10)
                Boxed:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(16)
                    spacing: dp(10)
                    MDLabel:
                        text: app.wifi_status
                        theme_text_color: "Custom"
                        text_color: app.c_ink
                        font_size: sp(16)
                        bold: True
                        adaptive_height: True
                    T4:
                        text: "Informasi koneksi Wi-Fi perangkat"
                        color: app.c_muted
                Sec:
                    text: "Detail Wi-Fi"
                Boxed:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(4), dp(6)
                    spacing: dp(2)
                    ListRow:
                        icon: "wifi"
                        title: "SSID"
                        subtitle: app.wifi_ssid
                        boxed: False
                        on_release: app.copy_text(app.wifi_ssid, "SSID disalin")
                    ListRow:
                        icon: "router-wireless"
                        title: "BSSID"
                        subtitle: app.wifi_bssid
                        boxed: False
                        on_release: app.copy_text(app.wifi_bssid, "BSSID disalin")
                    ListRow:
                        icon: "speedometer"
                        title: "Link Speed"
                        subtitle: app.wifi_link_speed
                        boxed: False
                        on_release: app.copy_text(app.wifi_link_speed, "Link Speed disalin")
                    ListRow:
                        icon: "signal"
                        title: "Signal"
                        subtitle: app.wifi_signal
                        boxed: False
                        on_release: app.copy_text(app.wifi_signal, "Signal disalin")
                    ListRow:
                        icon: "radio-tower"
                        title: "Frequency"
                        subtitle: app.wifi_frequency
                        boxed: False
                        on_release: app.copy_text(app.wifi_frequency, "Frequency disalin")
                    ListRow:
                        icon: "lan-connect"
                        title: "Network ID"
                        subtitle: app.wifi_network_id
                        boxed: False
                        on_release: app.copy_text(app.wifi_network_id, "Network ID disalin")
                Sec:
                    text: "Status & Interface"
                Boxed:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(4), dp(6)
                    spacing: dp(2)
                    ListRow:
                        icon: "ip-network"
                        title: "Alamat IP"
                        subtitle: app.wifi_ip
                        boxed: False
                        on_release: app.copy_text(app.wifi_ip, "Alamat IP disalin")
                    ListRow:
                        icon: "router-network"
                        title: "Gateway"
                        subtitle: app.wifi_gateway
                        boxed: False
                        on_release: app.copy_text(app.wifi_gateway, "Gateway disalin")
                    ListRow:
                        icon: "server-network"
                        title: "DNS"
                        subtitle: app.wifi_dns
                        boxed: False
                        on_release: app.copy_text(app.wifi_dns, "DNS disalin")
                    ListRow:
                        icon: "connection"
                        title: "Connection"
                        subtitle: app.wifi_connection
                        boxed: False
                    ListRow:
                        icon: "access-point-network"
                        title: "Interface"
                        subtitle: app.wifi_interface
                        boxed: False
                    ListRow:
                        icon: "wifi-strength-4"
                        title: "RSSI"
                        subtitle: app.wifi_rssi
                        boxed: False
                    ListRow:
                        icon: "help-circle-outline"
                        title: "Keterangan"
                        subtitle: app.wifi_note
                        boxed: False

# ---------------------------------------------------------------- ALAT CEPAT (generik)
<QuickToolScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: app.qt_title
            icons: ["content-copy"]
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(12)
                T4:
                    text: app.qt_desc
                Boxed:
                    padding: dp(2)
                    size_hint_y: None
                    height: dp(92) if app.qt_show_input else 0
                    opacity: 1 if app.qt_show_input else 0
                    disabled: not app.qt_show_input
                    TextInput:
                        id: qt_input1
                        hint_text: app.qt_hint1
                        multiline: True
                        font_size: sp(13)
                        background_normal: ""
                        background_active: ""
                        background_color: CLEAR
                        foreground_color: app.c_ink
                        hint_text_color: app.c_muted
                        cursor_color: app.c_ink
                        padding: dp(12)
                Boxed:
                    padding: dp(2)
                    size_hint_y: None
                    height: dp(92) if app.qt_show_input2 else 0
                    opacity: 1 if app.qt_show_input2 else 0
                    disabled: not app.qt_show_input2
                    TextInput:
                        id: qt_input2
                        hint_text: app.qt_hint2
                        multiline: True
                        font_size: sp(13)
                        background_normal: ""
                        background_active: ""
                        background_color: CLEAR
                        foreground_color: app.c_ink
                        hint_text_color: app.c_muted
                        cursor_color: app.c_ink
                        padding: dp(12)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(40) if app.qt_show_length else 0
                    opacity: 1 if app.qt_show_length else 0
                    disabled: not app.qt_show_length
                    spacing: dp(10)
                    T3:
                        text: "Panjang: " + str(app.qt_length)
                        pos_hint: {"center_y": .5}
                    Widget:
                    TapBox:
                        size_hint: None, None
                        size: dp(36), dp(36)
                        md_bg_color: app.c_card
                        radius: [dp(10)]
                        on_release: app.qt_change_length(-4)
                        Ic:
                            icon: "minus"
                            pos_hint: {"center_x": .5, "center_y": .5}
                    TapBox:
                        size_hint: None, None
                        size: dp(36), dp(36)
                        md_bg_color: app.c_card
                        radius: [dp(10)]
                        on_release: app.qt_change_length(4)
                        Ic:
                            icon: "plus"
                            pos_hint: {"center_x": .5, "center_y": .5}
                MDBoxLayout:
                    id: qt_options
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(2)
                PrimaryBtn:
                    text: app.qt_action_label
                    icon: "play"
                    on_release: app.qt_run()
                Sec:
                    text: "Hasil"
                Boxed:
                    padding: dp(2)
                    size_hint_y: None
                    height: dp(150)
                    TextInput:
                        id: qt_output
                        readonly: True
                        font_name: "data/fonts/RobotoMono-Regular.ttf"
                        font_size: sp(12)
                        background_normal: ""
                        background_active: ""
                        background_color: CLEAR
                        foreground_color: app.c_ink
                        cursor_color: app.c_ink
                        padding: dp(12)

# ---------------------------------------------------------------- FITUR TAMBAHAN YANG SEBELUMNYA PLACEHOLDER
<QRGeneratorScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "QR Generator"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T4:
                    text: "Masukkan teks, URL, atau data lain lalu buat QR Code."
                Boxed:
                    padding: dp(2)
                    size_hint_y: None
                    height: dp(110)
                    TextInput:
                        id: qr_input
                        hint_text: "Contoh: https://example.com"
                        multiline: True
                        background_normal: ""
                        background_active: ""
                        background_color: CLEAR
                        foreground_color: app.c_ink
                        hint_text_color: app.c_muted
                        padding: dp(12)
                PrimaryBtn:
                    text: "Buat QR Code"
                    icon: "qrcode"
                    on_release: app.qr_generate()
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(300)
                    Image:
                        id: qr_image
                        source: ""
                        allow_stretch: True
                        keep_ratio: True
                T4:
                    id: qr_status
                    text: "Belum ada QR Code."

# ---------------------------------------------------------------- FILE ANALYZER
<FileAnalyzerScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "File Analyzer"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T4:
                    text: "Analisis ukuran, tipe, hash, isi teks/biner, ZIP dan APK."
                PrimaryBtn:
                    text: "Pilih File"
                    icon: "folder-open-outline"
                    outlined: True
                    on_release: app.file_analyzer_pick()
                Boxed:
                    padding: dp(12)
                    size_hint_y: None
                    height: dp(360)
                    ScrollView:
                        bar_width: 0
                        T3:
                            id: fa_output
                            text: "Belum ada file dipilih."
                            text_size: self.width, None
                            valign: "top"
                            size_hint_y: None
                            height: self.texture_size[1]
                T4:
                    id: fa_path
                    text: ""

# ---------------------------------------------------------------- NETWORK SPEED
<NetworkSpeedScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Kecepatan Jaringan"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T4:
                    text: "Tes sederhana latency dan kecepatan download. Hasil bergantung pada server dan koneksi."
                PrimaryBtn:
                    id: speed_btn
                    text: "Mulai Tes"
                    icon: "speedometer"
                    on_release: app.network_speed_test()
                Boxed:
                    padding: dp(12)
                    size_hint_y: None
                    height: dp(220)
                    T3:
                        id: speed_output
                        text: "Belum ada tes."
                        text_size: self.width, None
                        valign: "top"
                        size_hint_y: None
                        height: self.texture_size[1]

# ---------------------------------------------------------------- APK INSPECTOR
<APKInspectorScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "APK Inspector"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T4:
                    text: "Inspeksi struktur APK tanpa memasang APK."
                PrimaryBtn:
                    text: "Pilih APK"
                    icon: "android"
                    outlined: True
                    on_release: app.apk_inspector_pick()
                Boxed:
                    padding: dp(12)
                    size_hint_y: None
                    height: dp(430)
                    ScrollView:
                        bar_width: 0
                        T3:
                            id: apk_inspect_output
                            text: "Belum ada APK dipilih."
                            text_size: self.width, None
                            valign: "top"
                            size_hint_y: None
                            height: self.texture_size[1]

# ---------------------------------------------------------------- CHECKSUM FILE
<ChecksumScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Checksum File"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(10)
                T4:
                    text: "Pilih file untuk menghitung MD5, SHA1 & SHA256-nya."
                PathChip:
                    id: cks_chip
                    icon: "file-document-outline"
                    path: "Belum ada file dipilih"
                PrimaryBtn:
                    text: "Pilih File"
                    icon: "folder-open-outline"
                    outlined: True
                    on_release: app.checksum_pick_file()
                Sec:
                    text: "Hasil"
                MDBoxLayout:
                    id: cks_list
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(8)

# ---------------------------------------------------------------- LOG VIEWER
<LogViewerScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Log Viewer"
            icons: ["refresh"]
        ScrollView:
            bar_width: 0
            Mono:
                id: logv_text
                text: ""
                padding: dp(16), dp(12)

# ---------------------------------------------------------------- RIWAYAT PERINTAH TERMINAL
<TermHistoryScreen@Page>:
    MDBoxLayout:
        orientation: "vertical"
        TopBar:
            title: "Riwayat Perintah"
        ScrollView:
            bar_width: 0
            MDBoxLayout:
                id: termhist_list
                orientation: "vertical"
                adaptive_height: True
                padding: dp(16), dp(8), dp(16), dp(16)
                spacing: dp(8)

# ---------------------------------------------------------------- ROOT
ScreenManager:
    transition: FadeTransition(duration=.12)
    HomeScreen:
        name: "home"
    FileManagerScreen:
        name: "filemanager"
    ProjectScreen:
        name: "project"
    ApkBuilderScreen:
        name: "apkbuilder"
    BuildingScreen:
        name: "building"
    DoneScreen:
        name: "done"
    PythonScreen:
        name: "python"
    TerminalScreen:
        name: "terminal"
    ToolsScreen:
        name: "tools"
    SettingsScreen:
        name: "settings"
    ProjectStructureScreen:
        name: "projectstructure"
    SystemScreen:
        name: "system"
    WifiInfoScreen:
        name: "wifiinfo"
    EditorScreen:
        name: "editor"
    WebProjectScreen:
        name: "webproject"
    ZipScreen:
        name: "zip"
    HttpScreen:
        name: "http"
    InstallerScreen:
        name: "installer"
    QuickToolScreen:
        name: "quicktool"
    QRGeneratorScreen:
        name: "qrgen"
    FileAnalyzerScreen:
        name: "fileanalyzer"
    NetworkSpeedScreen:
        name: "netspeed"
    APKInspectorScreen:
        name: "apkinspector"
    ChecksumScreen:
        name: "checksum"
    LogViewerScreen:
        name: "logviewer"
    TermHistoryScreen:
        name: "termhistory"
"""


# =====================================================================
#  APLIKASI
# =====================================================================
class MyToolsApp(MDApp):
    # ---- warna tema (dipakai KV lewat app.c_xxx) ----
    theme_name = StringProperty("Terang")
    c_bg = ColorProperty(get_color_from_hex(THEMES["Terang"]["bg"]))
    c_card = ColorProperty(get_color_from_hex(THEMES["Terang"]["card"]))
    c_ink = ColorProperty(get_color_from_hex(THEMES["Terang"]["ink"]))
    c_muted = ColorProperty(get_color_from_hex(THEMES["Terang"]["muted"]))
    c_line = ColorProperty(get_color_from_hex(THEMES["Terang"]["line"]))
    c_accent = ColorProperty(get_color_from_hex(THEMES["Terang"]["accent"]))
    c_on_accent = ColorProperty(get_color_from_hex(THEMES["Terang"]["on_accent"]))

    # ---- teks contoh (hanya untuk tampilan) ----
    CODE_TEXT = (
        '[color=#7C3AED]print[/color]([color=#16A34A]"Hello, MyTools!"[/color])\n'
        "\n"
        "[color=#7C3AED]for[/color] i [color=#7C3AED]in[/color] "
        "[color=#0284C7]range[/color](5):\n"
        '    [color=#0284C7]print[/color](f[color=#16A34A]"Number: {i}"[/color])'
    )

    OUTPUT_TEXT = (
        "Hello, MyTools!\n"
        "Number: 0\n"
        "Number: 1\n"
        "Number: 2\n"
        "Number: 3\n"
        "Number: 4"
    )

    LOG_TEXT = (
        "09:41  Extracting project...\n"
        "09:42  Checking Python files...\n"
        "09:43  Installing dependencies...\n"
        "09:46  Generating buildozer.spec...\n"
        "09:48  Building APK..."
    )

    TERM_TEXT = (
        "[color=#4ADE80]u0_a412@android[/color]:[color=#60A5FA]/sdcard[/color]$ cd /sdcard/MyTools\n"
        "[color=#4ADE80]u0_a412@android[/color]:[color=#60A5FA]/sdcard/MyTools[/color]$ ls\n"
        "main.py           buildozer.spec   [color=#60A5FA]src[/color]\n"
        "requirements.txt  [color=#60A5FA]tools/[/color]\n"
        "\n"
        "[color=#4ADE80]u0_a412@android[/color]:[color=#60A5FA]/sdcard/MyTools[/color]$ python3 main.py\n"
        "Hello, MyTools!\n"
        "Number: 0\n"
        "Number: 1\n"
        "Number: 2\n"
        "Number: 3\n"
        "Number: 4\n"
        "\n"
        "[color=#4ADE80]u0_a412@android[/color]:[color=#60A5FA]/sdcard/MyTools[/color]$ _"
    )

    # ---- status build APK sungguhan (diisi oleh on_start_build via buildozer) ----
    build_steps = ListProperty([False] * 7)
    build_step_labels = ListProperty(list(BUILD_STEP_LABELS_DEMO))
    build_fraction = NumericProperty(0.0)
    build_percent = StringProperty("0%")
    apk_name = StringProperty("Belum ada APK")
    apk_size_text = StringProperty("—")
    building_active = BooleanProperty(False)

    # ------------------------------------------------------------ Wi-Fi Info
    wifi_status = StringProperty("Memuat informasi Wi-Fi...")
    wifi_ssid = StringProperty("Tidak tersedia")
    wifi_bssid = StringProperty("Tidak tersedia")
    wifi_link_speed = StringProperty("Tidak tersedia")
    wifi_signal = StringProperty("Tidak tersedia")
    wifi_frequency = StringProperty("Tidak tersedia")
    wifi_network_id = StringProperty("Tidak tersedia")
    wifi_connection = StringProperty("Tidak tersedia")
    wifi_interface = StringProperty("Tidak tersedia")
    wifi_rssi = StringProperty("Tidak tersedia")
    wifi_ip = StringProperty("Tidak tersedia")
    wifi_gateway = StringProperty("Tidak tersedia")
    wifi_dns = StringProperty("Tidak tersedia")
    wifi_note = StringProperty("Tekan refresh untuk memperbarui")

    # ------------------------------------------------------------ Alat Cepat (QuickToolScreen)
    qt_title = StringProperty("")
    qt_desc = StringProperty("")
    qt_hint1 = StringProperty("")
    qt_hint2 = StringProperty("")
    qt_show_input = BooleanProperty(True)
    qt_show_input2 = BooleanProperty(False)
    qt_show_length = BooleanProperty(False)
    qt_length = NumericProperty(16)
    qt_action_label = StringProperty("Proses")

    # ------------------------------------------------------------ setup
    def build(self):
        self.title = "MyTools"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self._history = []
        self._wifi_info_text = ""
        self.zip_items = []
        self.zip_out_dir = None
        self.unzip_src = None
        self.unzip_dest = None
        self.editor_path = None
        self.editor_dirty = False
        self._editor_loading = False
        self.http_server = None
        self.http_dir = None
        self._http_lines = deque(maxlen=40)
        self._pip_busy = False
        self._pip_proc = None
        self._pip_lines = deque(maxlen=300)
        self._pkg_cache = None
        self.site_dir = None
        self.web_project_name_value = None
        self.web_project_files = {"html": None, "css": None, "js": None}
        self.web_project_dir = None
        # daftar file/folder NYATA untuk File Manager, Project & Struktur Project
        self._lists = {
            "filemanager": self._new_list_cfg("file_list", "dots-vertical", True, "fm_select_btn", "fm_path"),
            "project": self._new_list_cfg("project_list", "dots-vertical", True, None, "project_path"),
            "projectstructure": self._new_list_cfg("struct_list", "dots-vertical", True, "struct_select_btn", None),
        }
        fm_root = storage_path()
        self._lists["filemanager"]["root"] = self._lists["filemanager"]["dir"] = fm_root
        self.clipboard = None  # {"mode": "copy"/"cut", "paths": [path, ...], "source_screen": ...}
        self._file_sheet_ctx = None
        self._running_code = False
        self.building_active = False
        self._build_proc = None
        self._apk_project_dir = None
        self._built_apk_path = None
        self._term_history = []
        self._qt_key = None
        self._qt_mode = None
        self._qt_last_output = ""
        if platform == "android":
            # paket hasil install disimpan di folder data aplikasi
            self.site_dir = os.path.join(self.user_data_dir, "site-packages")
            os.makedirs(self.site_dir, exist_ok=True)
            if self.site_dir not in sys.path:
                sys.path.append(self.site_dir)
            Window.softinput_mode = "below_target"
        self.set_theme(self._load_theme(), save=False)
        return Builder.load_string(KV)

    def on_start(self):
        sm = self.root
        for screen_name in self._lists:
            self._reload_list(screen_name)
        pick_row = sm.get_screen("projectstructure").ids.get("proj_pick_row")
        if pick_row is not None:
            pick_row.subtitle = "Belum dipilih"
        # simpan urutan asli kartu tools di Home, dipakai untuk fitur pencarian
        home_grid = sm.get_screen("home").ids.home_grid
        self._home_tiles = list(reversed(home_grid.children))
        # simpan referensi grup konten tab "Jalankan" di layar Python (untuk on_tab)
        py_ids = sm.get_screen("python").ids
        self._py_group = py_ids.py_run_group
        self._py_parent = self._py_group.parent
        self._py_group_index = self._py_parent.children.index(self._py_group)
        Window.bind(on_keyboard=self._on_key)
        self._request_permissions(on_result=self._after_permissions)

    # ------------------------------------------------------------ daftar file/folder nyata
    def _after_permissions(self):
        self.refresh_wifi_info()
        self._reload_list("filemanager")   # izin storage baru diberikan -> baca ulang isi folder

    def _new_list_cfg(self, box_id, trailing, touch, select_btn, path_id):
        """Struktur data untuk satu daftar (File Manager/Project/Struktur)."""
        return {
            "items": [],
            "box": box_id,
            "trailing": trailing,
            "touch": touch,
            "select_btn": select_btn,
            "path_id": path_id,
            "select": False,
            "selected": set(),
            "dir": None,        # folder yang sedang ditampilkan
            "root": None,       # batas paling atas (tombol back naik sampai sini)
            "sort": "Folder dulu",
            "error": None,
        }

    _SORTS = {
        "Nama (A-Z)": (lambda it: it["name"].lower(), False),
        "Nama (Z-A)": (lambda it: it["name"].lower(), True),
        "Folder dulu": (lambda it: (it["kind"] != "folder", it["name"].lower()), False),
        "File dulu": (lambda it: (it["kind"] == "folder", it["name"].lower()), False),
    }

    def _apply_sort(self, cfg):
        key, rev = self._SORTS.get(cfg.get("sort"), self._SORTS["Folder dulu"])
        cfg["items"].sort(key=key, reverse=rev)

    def _reload_list(self, screen_name):
        """Baca ulang isi folder dari penyimpanan lalu gambar ulang daftar."""
        cfg = self._lists.get(screen_name)
        if not cfg:
            return
        d, root = cfg.get("dir"), cfg.get("root")
        # kalau folder yang sedang dibuka sudah hilang, naik sampai ada
        while d and not os.path.isdir(d) and root and os.path.normpath(d) != os.path.normpath(root):
            d = os.path.dirname(d.rstrip(os.sep))
        cfg["dir"] = d
        cfg["error"] = None
        cfg["items"] = []
        if d:
            try:
                cfg["items"] = [dict(kind=k, name=n, meta=m) for k, n, m in scan_dir(d)]
                self._apply_sort(cfg)
            except Exception as e:
                cfg["error"] = str(e)[:80]
        names = {it["name"] for it in cfg["items"]}
        cfg["selected"] = {n for n in cfg["selected"] if n in names}
        self._render_list(screen_name)
        self._update_select_btn(screen_name)

    def _reload_all_lists(self):
        """Dipanggil setelah operasi file: ketiga daftar bisa menunjuk folder yang sama."""
        if self._apk_project_dir and not os.path.isdir(self._apk_project_dir):
            self._clear_project()
        for screen_name in self._lists:
            self._reload_list(screen_name)

    def _navigate(self, screen_name, path):
        cfg = self._lists[screen_name]
        cfg["dir"] = path
        cfg["select"] = False
        cfg["selected"].clear()
        self._reload_list(screen_name)

    def _item_path(self, screen_name, name):
        cfg = self._lists.get(screen_name)
        if not cfg or not cfg.get("dir"):
            return None
        return os.path.join(cfg["dir"], name)

    def _set_project_dir(self, path):
        path = path.rstrip(os.sep) or path
        self._apk_project_dir = path
        for screen_name in ("project", "projectstructure"):
            cfg = self._lists[screen_name]
            cfg["root"] = cfg["dir"] = path
            cfg["select"] = False
            cfg["selected"].clear()
            self._reload_list(screen_name)
        name = os.path.basename(path) or path
        for screen_name, row_id in (("projectstructure", "proj_pick_row"), ("apkbuilder", "apk_project_row")):
            ids = self.root.get_screen(screen_name).ids
            if row_id in ids:
                ids[row_id].subtitle = name
        py = self.root.get_screen("python").ids
        if self.root.current == "python" and py.seg_project.active:
            self.on_tab("Project")

    def _clear_project(self):
        self._apk_project_dir = None
        for screen_name in ("project", "projectstructure"):
            cfg = self._lists[screen_name]
            cfg["root"] = cfg["dir"] = None
            cfg["select"] = False
            cfg["selected"].clear()
        pick_row = self.root.get_screen("projectstructure").ids.get("proj_pick_row")
        if pick_row is not None:
            pick_row.subtitle = "Belum dipilih"

    def _render_list(self, screen_name):
        cfg = self._lists.get(screen_name)
        if not cfg:
            return
        box = self.root.get_screen(screen_name).ids[cfg["box"]]
        box.clear_widgets()
        for item in cfg["items"]:
            is_dir = item["kind"] == "folder"
            name = item["name"]
            if cfg["select"]:
                trailing = "checkbox-marked" if name in cfg["selected"] else "checkbox-blank-outline"
                touch = False
            else:
                trailing = cfg["trailing"]
                touch = cfg["touch"]
            row = ListRow(
                icon="folder" if is_dir else "file-document-outline",
                muted_icon=not is_dir,
                title=name,
                subtitle=item["meta"],
                trailing=trailing,
                trailing_touch=touch,
                boxed=cfg["select"] and name in cfg["selected"],
            )
            if cfg["select"]:
                row.bind(on_release=lambda w, s=screen_name, n=name: self._toggle_select(s, n))
            else:
                row.bind(on_release=lambda w, s=screen_name, n=name: self.on_open_item(n, s))
                if touch:
                    row.bind(on_trailing_press=lambda w, s=screen_name, n=name, m=item["meta"]:
                              self.open_file_sheet(s, n, m))
            box.add_widget(row)
        if not cfg["items"]:
            if cfg.get("error"):
                text = f"Folder tidak bisa dibuka: {cfg['error']}"
            elif not cfg.get("dir"):
                text = "Belum ada project dipilih.\nPilih folder project lewat APK Builder atau Struktur Project."
            else:
                text = "Folder kosong."
            box.add_widget(Factory.T4(text=text))
        self._update_path_chip(screen_name)

    def _update_path_chip(self, screen_name):
        cfg = self._lists.get(screen_name)
        if not cfg or not cfg.get("path_id"):
            return
        chip = self.root.get_screen(screen_name).ids.get(cfg["path_id"])
        if chip is None:
            return
        d, root = cfg.get("dir"), cfg.get("root")
        if screen_name == "filemanager":
            base = "Penyimpanan internal"
        else:
            base = (os.path.basename(root.rstrip(os.sep)) or root) if root else "Project"
        parts = []
        if d and root and os.path.normpath(d) != os.path.normpath(root):
            parts = [x for x in os.path.relpath(d, root).split(os.sep) if x]
        text = "  ›  ".join([base] + parts) + "  ›"
        chip.path = text if len(text) <= 44 else "…" + text[-43:]

    def _find_item(self, screen_name, name):
        cfg = self._lists.get(screen_name)
        if not cfg:
            return None
        return next((it for it in cfg["items"] if it["name"] == name), None)

    def _toggle_select(self, screen_name, name):
        cfg = self._lists[screen_name]
        if name in cfg["selected"]:
            cfg["selected"].discard(name)
        else:
            cfg["selected"].add(name)
        self._render_list(screen_name)
        self._update_select_btn(screen_name)

    def _update_select_btn(self, screen_name):
        cfg = self._lists.get(screen_name)
        if not cfg or not cfg.get("select_btn"):
            return
        btn = self.root.get_screen(screen_name).ids[cfg["select_btn"]]
        if cfg["select"]:
            count = len(cfg["selected"])
            btn.icon = "close"
            btn.text = f"Batal ({count})" if count else "Batal"
        else:
            btn.icon = "checkbox-marked-outline" if screen_name == "filemanager" else "checkbox-blank-outline"
            btn.text = "Pilih"

    def _open_option_sheet(self, title, options, on_pick):
        """Bottom sheet generik: options = [(icon, label), ...]; on_pick(label) saat ditekan."""
        sheet = OptionSheet(title=title)
        for icon, label in options:
            row = SheetRow(icon=icon, text=label)
            row.bind(on_release=lambda w, l=label, s=sheet: (on_pick(l), s.dismiss()))
            sheet.ids.options.add_widget(row)
        sheet.open()

    def _new_item_flow(self, screen_name):
        def kind_picked(label):
            kind = "folder" if "Folder" in label else "file"
            NameDialog(
                title="Nama folder baru" if kind == "folder" else "Nama file baru",
                value="Folder Baru" if kind == "folder" else "Berkas Baru.txt",
                hint="contoh: " + ("Proyek Baru" if kind == "folder" else "catatan.txt"),
                ok_text="Buat",
                callback=lambda name: self._create_item(screen_name, kind, name),
            ).open()
        self._open_option_sheet(
            "Buat baru",
            [("folder-plus-outline", "Folder baru"), ("file-plus-outline", "File baru")],
            kind_picked,
        )

    @staticmethod
    def _bad_name(name):
        return (not name) or name in (".", "..") or any(c in name for c in "/\\")

    def _create_item(self, screen_name, kind, name):
        name = name.strip()
        if self._bad_name(name):
            self.show_toast("Nama tidak valid")
            return
        target = self._item_path(screen_name, name)
        if not target:
            self.show_toast("Pilih folder project dulu")
            return
        if os.path.lexists(target):
            self.show_toast(f'"{name}" sudah ada')
            return
        try:
            if kind == "folder":
                os.makedirs(target)
            else:
                open(target, "x", encoding="utf-8").close()
        except Exception as e:
            self.show_toast(f"Gagal membuat: {str(e)[:80]}")
            return
        self._reload_all_lists()
        self.show_toast(f'{"Folder" if kind == "folder" else "File"} "{name}" dibuat')

    def _rename_item(self, screen_name, item, new_name):
        new_name = new_name.strip()
        if self._bad_name(new_name):
            self.show_toast("Nama tidak valid")
            return
        if new_name == item["name"]:
            return
        old = self._item_path(screen_name, item["name"])
        new = self._item_path(screen_name, new_name)
        if not old or os.path.lexists(new):
            self.show_toast(f'"{new_name}" sudah ada')
            return
        try:
            os.rename(old, new)
        except Exception as e:
            self.show_toast(f"Gagal mengganti nama: {str(e)[:80]}")
            return
        if self.editor_path and os.path.abspath(self.editor_path) == os.path.abspath(old):
            self.editor_path = new
            self._update_editor_ui()
        if self._apk_project_dir and os.path.abspath(self._apk_project_dir) == os.path.abspath(old):
            self._set_project_dir(new)
        self._reload_all_lists()
        self.show_toast("Nama diganti")

    def _delete_item(self, screen_name, item):
        path = self._item_path(screen_name, item["name"])
        if not path:
            return
        try:
            delete_path(path)
        except Exception as e:
            self.show_toast(f"Gagal menghapus: {str(e)[:80]}")
            return
        self._lists[screen_name]["selected"].discard(item["name"])
        self._reload_all_lists()
        self.show_toast(f'"{item["name"]}" dihapus')

    def _delete_many(self, screen_name, names):
        ok = fail = 0
        for n in names:
            path = self._item_path(screen_name, n)
            try:
                delete_path(path)
                ok += 1
            except Exception:
                fail += 1
        cfg = self._lists[screen_name]
        cfg["selected"].clear()
        cfg["select"] = False
        self._reload_all_lists()
        self.show_toast(f"{ok} item dihapus" + (f", {fail} gagal" if fail else ""))

    def _set_clipboard(self, mode, screen_name, names):
        paths = [self._item_path(screen_name, it["name"])
                 for it in self._lists[screen_name]["items"] if it["name"] in names]
        self.clipboard = {"mode": mode, "paths": paths, "source_screen": screen_name}
        return len(paths)

    def refresh_wifi_info(self):
        """Ambil informasi Wi-Fi dari Android, dengan fallback nyata untuk desktop/Termux."""
        info = {
            "ssid": "Tidak tersedia", "bssid": "Tidak tersedia",
            "link_speed": "Tidak tersedia", "signal": "Tidak tersedia",
            "frequency": "Tidak tersedia", "network_id": "Tidak tersedia",
            "connection": "Tidak terhubung", "interface": "Tidak tersedia",
            "rssi": "Tidak tersedia", "ip": "Tidak tersedia",
            "gateway": "Tidak tersedia", "dns": "Tidak tersedia",
            "note": "Sebagian informasi bergantung pada izin Android.",
        }
        try:
            if platform == "android":
                from jnius import autoclass
                Context = autoclass("android.content.Context")
                activity = self._get_android_activity()
                if activity is None:
                    raise RuntimeError("Tidak bisa mengakses Activity Android (PythonActivity).")
                wm = activity.getSystemService(Context.WIFI_SERVICE)
                cm = activity.getSystemService(Context.CONNECTIVITY_SERVICE)
                if wm is None or cm is None:
                    raise RuntimeError(
                        "WIFI_SERVICE/CONNECTIVITY_SERVICE tidak tersedia — cek izin "
                        "ACCESS_WIFI_STATE & ACCESS_NETWORK_STATE di buildozer.spec."
                    )

                # Connectivity status
                net = cm.getActiveNetwork()
                caps = cm.getNetworkCapabilities(net) if net else None
                if caps:
                    WIFI_TRANSPORT = 1
                    info["connection"] = "Wi-Fi terhubung" if caps.hasTransport(WIFI_TRANSPORT) else "Terhubung (bukan Wi-Fi)"
                else:
                    info["connection"] = "Tidak terhubung"

                try:
                    conn = wm.getConnectionInfo()
                    ssid = str(conn.getSSID()).strip('"')
                    if ssid and ssid.lower() not in ("<unknown ssid>", "unknown ssid"):
                        info["ssid"] = ssid
                    bssid = str(conn.getBSSID())
                    if bssid and bssid.lower() != "02:00:00:00:00:00":
                        info["bssid"] = bssid
                    info["rssi"] = f"{conn.getRssi()} dBm"
                    speed = conn.getLinkSpeed()
                    if speed >= 0:
                        info["link_speed"] = f"{speed} Mbps"
                    freq = conn.getFrequency()
                    if freq > 0:
                        info["frequency"] = f"{freq} MHz"
                    nid = conn.getNetworkId()
                    if nid >= 0:
                        info["network_id"] = str(nid)
                    ip_int = conn.getIpAddress()
                    if ip_int:
                        info["ip"] = _int_to_ipv4(ip_int)
                except Exception:
                    pass

                # IP/interface via LinkProperties (juga jadi cadangan untuk IP)
                try:
                    lp = cm.getLinkProperties(cm.getActiveNetwork())
                    if lp:
                        try:
                            iface = str(lp.getInterfaceName())
                            if iface and iface != "None":
                                info["interface"] = iface
                        except Exception:
                            pass
                        if info["ip"] == "Tidak tersedia":
                            links = lp.getLinkAddresses()
                            if links and links.size() > 0:
                                for i in range(links.size()):
                                    addr = str(links.get(i).getAddress().getHostAddress())
                                    if ":" not in addr:  # ambil IPv4 dulu
                                        info["ip"] = addr
                                        break
                                else:
                                    info["ip"] = str(links.get(0).getAddress().getHostAddress())
                        try:
                            routes = lp.getRoutes()
                            for i in range(routes.size()):
                                r = routes.get(i)
                                if r.isDefaultRoute():
                                    gw = r.getGateway()
                                    if gw:
                                        info["gateway"] = str(gw.getHostAddress())
                                        break
                        except Exception:
                            pass
                        try:
                            dns_list = lp.getDnsServers()
                            if dns_list and dns_list.size() > 0:
                                info["dns"] = ", ".join(
                                    str(dns_list.get(i).getHostAddress()) for i in range(dns_list.size())
                                )
                        except Exception:
                            pass
                except Exception:
                    pass

                # Cadangan lewat DhcpInfo bila LinkProperties tidak memberi gateway/DNS
                try:
                    dhcp = wm.getDhcpInfo()
                    if dhcp:
                        if info["ip"] == "Tidak tersedia" and dhcp.ipAddress:
                            info["ip"] = _int_to_ipv4(dhcp.ipAddress)
                        if info["gateway"] == "Tidak tersedia" and dhcp.gateway:
                            info["gateway"] = _int_to_ipv4(dhcp.gateway)
                        if info["dns"] == "Tidak tersedia":
                            dns_parts = [d for d in (dhcp.dns1, dhcp.dns2) if d]
                            if dns_parts:
                                info["dns"] = ", ".join(_int_to_ipv4(d) for d in dns_parts)
                except Exception:
                    pass

                if info["ssid"] == "Tidak tersedia":
                    if not self._has_location_permission():
                        info["note"] = ("Izin Lokasi belum diberikan, jadi SSID/BSSID disembunyikan Android. "
                                        "Buka Pengaturan > Aplikasi > MyTools > Izin, aktifkan Lokasi, lalu tekan refresh.")
                    else:
                        info["note"] = "SSID/BSSID tidak terbaca (kemungkinan sedang tidak terhubung ke Wi-Fi)."
                else:
                    info["note"] = "Data berasal dari koneksi Wi-Fi yang sedang aktif."
            else:
                # Fallback desktop/Termux: baca info jaringan sungguhan dari OS.
                hostname = socket.gethostname()
                ip = get_local_ip()
                info["connection"] = "Terhubung (perkiraan)"
                info["interface"] = _detect_interface_name(ip) or hostname
                info["ssid"] = _detect_ssid_desktop() or "Tidak tersedia di desktop"
                info["ip"] = ip
                gw = _detect_gateway()
                if gw:
                    info["gateway"] = gw
                dns = _detect_dns()
                if dns:
                    info["dns"] = dns
                info["note"] = f"Mode desktop/Termux. Host: {hostname}"
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
            print(f"[MyTools] refresh_wifi_info gagal: {msg}")  # tampil di adb logcat / buildozer log
            info["note"] = f"Gagal membaca info Wi-Fi: {msg[:160]}"

        self.wifi_ssid = info["ssid"]
        self.wifi_bssid = info["bssid"]
        self.wifi_link_speed = info["link_speed"]
        self.wifi_signal = info["rssi"]
        self.wifi_rssi = info["rssi"]
        self.wifi_frequency = info["frequency"]
        self.wifi_network_id = info["network_id"]
        self.wifi_connection = info["connection"]
        self.wifi_interface = info["interface"]
        self.wifi_ip = info["ip"]
        self.wifi_gateway = info["gateway"]
        self.wifi_dns = info["dns"]
        self.wifi_note = info["note"]
        self.wifi_status = "Wi-Fi Aktif" if "Wi-Fi terhubung" in info["connection"] else info["connection"]

        self._wifi_info_text = (
            "Wi-Fi Info\\n"
            f"SSID: {self.wifi_ssid}\\n"
            f"BSSID: {self.wifi_bssid}\\n"
            f"Link Speed: {self.wifi_link_speed}\\n"
            f"Signal/RSSI: {self.wifi_rssi}\\n"
            f"Frequency: {self.wifi_frequency}\\n"
            f"Network ID: {self.wifi_network_id}\\n"
            f"Alamat IP: {self.wifi_ip}\\n"
            f"Gateway: {self.wifi_gateway}\\n"
            f"DNS: {self.wifi_dns}\\n"
            f"Connection: {self.wifi_connection}\\n"
            f"Interface: {self.wifi_interface}\\n"
            f"Keterangan: {self.wifi_note}"
        )

    def copy_wifi_info(self):
        self.copy_text(self._wifi_info_text or "Informasi Wi-Fi belum tersedia", "Info Wi-Fi disalin")

    def _get_android_activity(self):
        try:
            from android import activity
            return activity
        except Exception:
            try:
                from jnius import autoclass
                PythonActivity = autoclass("org.kivy.android.PythonActivity")
                return PythonActivity.mActivity
            except Exception:
                return None

    # ------------------------------------------------------------ tema
    def _theme_file(self):
        return os.path.join(self.user_data_dir, "settings.json")

    def _load_theme(self):
        try:
            with open(self._theme_file(), encoding="utf-8") as f:
                name = json.load(f).get("tema", "Terang")
            return name if name in THEMES else "Terang"
        except Exception:
            return "Terang"

    def set_theme(self, name, save=True):
        t = THEMES.get(name)
        if not t:
            return
        self.theme_name = name
        self.c_bg = get_color_from_hex(t["bg"])
        self.c_card = get_color_from_hex(t["card"])
        self.c_ink = get_color_from_hex(t["ink"])
        self.c_muted = get_color_from_hex(t["muted"])
        self.c_line = get_color_from_hex(t["line"])
        self.c_accent = get_color_from_hex(t["accent"])
        self.c_on_accent = get_color_from_hex(t["on_accent"])
        self.theme_cls.theme_style = "Dark" if name == "Gelap" else "Light"
        Window.clearcolor = self.c_bg
        if save:
            try:
                with open(self._theme_file(), "w", encoding="utf-8") as f:
                    json.dump({"tema": name}, f)
            except Exception:
                pass

    def open_theme_dialog(self):
        ThemeDialog().open()

    # ------------------------------------------------------------ util UI
    def show_toast(self, text):
        toast = Toast(text=str(text)[:70])
        Window.add_widget(toast)

        def fade(*_):
            anim = Animation(opacity=0, duration=0.3)
            anim.bind(on_complete=lambda *a: Window.remove_widget(toast))
            anim.start(toast)

        Clock.schedule_once(fade, 1.6)

    def copy_text(self, text, message="Disalin"):
        from kivy.core.clipboard import Clipboard
        try:
            Clipboard.copy(text)
            self.show_toast(message)
        except Exception:
            self.show_toast("Gagal menyalin")

    # ------------------------------------------------------------ izin & util
    def _request_permissions(self, on_result=None):
        if platform != "android":
            if on_result:
                on_result()
            return
        try:
            from android.permissions import Permission, request_permissions
            perms = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE]
            for p_name in ("ACCESS_WIFI_STATE", "ACCESS_NETWORK_STATE",
                           "ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION",
                           "NEARBY_WIFI_DEVICES", "CHANGE_WIFI_STATE"):
                if hasattr(Permission, p_name):
                    perms.append(getattr(Permission, p_name))

            def _on_answered(permissions, grant_results):
                # Callback jnius berjalan di thread lain -> lompat balik ke thread UI
                if on_result:
                    Clock.schedule_once(lambda dt: on_result(), 0)

            request_permissions(perms, _on_answered)
        except Exception:
            if on_result:
                on_result()

    def _has_location_permission(self):
        """Android 8.1+ menyembunyikan SSID/BSSID Wi-Fi tanpa izin Lokasi."""
        if platform != "android":
            return True
        try:
            from android.permissions import Permission, check_permission
            return bool(
                check_permission(Permission.ACCESS_FINE_LOCATION)
                or check_permission(Permission.ACCESS_COARSE_LOCATION)
            )
        except Exception:
            return False

    def _last_dir(self):
        if self.editor_path:
            return os.path.dirname(self.editor_path)
        if self.zip_out_dir:
            return self.zip_out_dir
        return storage_path()

    def _guard_unsaved(self, action):
        if self.editor_dirty:
            ConfirmDialog(
                title="Perubahan belum disimpan",
                message="Jika dilanjutkan, perubahan di editor akan hilang.",
                ok_text="Buang",
                callback=action,
            ).open()
        else:
            action()

    # ------------------------------------------------------------ tools: Text Editor
    def _ed(self):
        return self.root.get_screen("editor").ids

    def _update_editor_ui(self):
        ids = self._ed()
        name = short_text(self.editor_path, 38) if self.editor_path else "Tanpa judul"
        ids.ed_chip.path = name + ("  ●" if self.editor_dirty else "")
        text = ids.ed_text.text
        lines = text.count("\n") + 1
        ids.ed_status.text = f"Baris {lines}  |  {len(text)} karakter" + ("  |  belum disimpan" if self.editor_dirty else "")

    def on_editor_changed(self):
        if self._editor_loading:
            return
        self.editor_dirty = True
        self._update_editor_ui()

    def _set_editor(self, text, path):
        ids = self._ed()
        self._editor_loading = True
        ids.ed_text.text = text
        ids.ed_text.cursor = (0, 0)
        self.editor_path = path

        def done(dt):
            self._editor_loading = False
            self.editor_dirty = False
            try:  # kosongkan riwayat undo
                ids.ed_text._undo = []
                ids.ed_text._redo = []
            except Exception:
                pass
            self._update_editor_ui()

        Clock.schedule_once(done, 0)

    def editor_new(self):
        self._guard_unsaved(lambda: self._set_editor("", None))

    def editor_open(self):
        def pick():
            FilePicker(start=self._last_dir(), title="Buka file teks", mode="file",
                       callback=self._load_editor_file).open()
        self._guard_unsaved(pick)

    def _load_editor_file(self, path):
        try:
            if os.path.getsize(path) > 2_000_000:
                self.show_toast("File terlalu besar (maks 2 MB)")
                return False
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError:
            self.show_toast("Bukan file teks (UTF-8)")
            return False
        except Exception as e:
            self.show_toast(f"Gagal membuka: {e}")
            return False
        self._set_editor(text, path)
        return True

    def editor_save(self):
        if self.editor_path:
            self._write_editor(self.editor_path)
        else:
            self.editor_save_as()

    def editor_save_as(self):
        def got_folder(folder):
            default = os.path.basename(self.editor_path) if self.editor_path else "catatan.txt"
            NameDialog(title="Nama file", value=default, hint="contoh: catatan.txt",
                       ok_text="Simpan",
                       callback=lambda name: self._save_named(folder, name)).open()
        FilePicker(start=self._last_dir(), title="Simpan di folder", mode="dir",
                   callback=got_folder).open()

    def _save_named(self, folder, name):
        if not name or any(c in name for c in "/\\"):
            self.show_toast("Nama file tidak valid")
            return
        target = os.path.join(folder, name)
        if os.path.exists(target):
            ConfirmDialog(title="File sudah ada", message=f"Timpa {name}?", ok_text="Timpa",
                          callback=lambda: self._write_editor(target)).open()
        else:
            self._write_editor(target)

    def _write_editor(self, path):
        try:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(self._ed().ed_text.text)
        except Exception as e:
            self.show_toast(f"Gagal menyimpan: {e}")
            return
        self.editor_path = path
        self.editor_dirty = False
        self._update_editor_ui()
        self.show_toast("Tersimpan")

    def editor_undo(self):
        self._ed().ed_text.do_undo()

    def editor_redo(self):
        self._ed().ed_text.do_redo()

    # ------------------------------------------------------------ tools: ZIP / UNZIP
    def _zip_ids(self):
        return self.root.get_screen("zip").ids

    def set_zip_tab(self, tab):
        ids = self._zip_ids()
        ids.zip_sm.current = tab
        ids.seg_compress.active = tab == "compress"
        ids.seg_extract.active = tab == "extract"

    def refresh_zip_ui(self):
        ids = self._zip_ids()
        box = ids.zip_items_box
        box.clear_widgets()
        if not self.zip_items:
            box.add_widget(Factory.T4(text="Belum ada item. Tambahkan file atau folder."))
        for path in self.zip_items:
            is_dir = os.path.isdir(path)
            row = ListRow(
                icon="folder" if is_dir else "file-document-outline",
                muted_icon=not is_dir,
                title=os.path.basename(path.rstrip(os.sep)) or path,
                subtitle=short_text(path, 42),
                trailing="close",
                trailing_touch=True,
                boxed=True,
            )
            row.bind(on_trailing_press=lambda w, p=path: self._zip_remove(p))
            box.add_widget(row)
        ids.zip_out_row.subtitle = short_text(self.zip_out_dir, 42) if self.zip_out_dir else "Belum dipilih"
        ids.unzip_src_row.title = os.path.basename(self.unzip_src) if self.unzip_src else "Pilih file .zip"
        ids.unzip_src_row.subtitle = short_text(self.unzip_src, 42) if self.unzip_src else "Belum dipilih"
        ids.unzip_dest_row.subtitle = short_text(self.unzip_dest, 42) if self.unzip_dest else "Belum dipilih"

    def _zip_remove(self, path):
        if path in self.zip_items:
            self.zip_items.remove(path)
        self.refresh_zip_ui()

    def zip_add(self, want_dir):
        FilePicker(start=self._last_dir(),
                   title="Pilih folder" if want_dir else "Pilih file",
                   mode="dir" if want_dir else "file",
                   callback=self._zip_added).open()

    def _zip_added(self, path):
        if path not in self.zip_items:
            self.zip_items.append(path)
        if not self.zip_out_dir:
            self.zip_out_dir = os.path.dirname(path.rstrip(os.sep)) or path
        self.refresh_zip_ui()

    def zip_pick_out(self):
        def got(folder):
            self.zip_out_dir = folder
            self.refresh_zip_ui()
        FilePicker(start=self.zip_out_dir or storage_path(), title="Simpan ZIP di folder",
                   mode="dir", callback=got).open()

    def zip_create(self):
        if not self.zip_items:
            self.show_toast("Tambahkan file atau folder dulu")
            return
        if not self.zip_out_dir:
            self.show_toast("Pilih folder tujuan dulu")
            return
        name = self._zip_ids().zip_name.text.strip() or "arsip.zip"
        if not name.lower().endswith(".zip"):
            name += ".zip"
        if any(c in name for c in "/\\"):
            self.show_toast("Nama arsip tidak valid")
            return
        out = os.path.join(self.zip_out_dir, name)
        if os.path.exists(out):
            ConfirmDialog(title="File sudah ada", message=f"Timpa {name}?", ok_text="Timpa",
                          callback=lambda: self._start_zip(out)).open()
        else:
            self._start_zip(out)

    def _start_zip(self, out):
        self.show_toast("Membuat ZIP...")
        threading.Thread(target=self._zip_worker, args=(list(self.zip_items), out), daemon=True).start()

    def _zip_worker(self, items, out):
        try:
            out_abs = os.path.abspath(out)
            count = 0
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                for path in items:
                    if os.path.isdir(path):
                        base = os.path.dirname(os.path.abspath(path).rstrip(os.sep))
                        for root, dirs, files in os.walk(path):
                            if not files and not dirs:
                                z.write(root, os.path.relpath(root, base))
                            for fn in files:
                                full = os.path.join(root, fn)
                                if os.path.abspath(full) == out_abs:
                                    continue
                                z.write(full, os.path.relpath(full, base))
                                count += 1
                    elif os.path.abspath(path) != out_abs:
                        z.write(path, os.path.basename(path))
                        count += 1
            msg = f"ZIP dibuat: {count} file, {fmt_bytes(os.path.getsize(out))}"
        except Exception as e:
            msg = f"Gagal: {str(e)[:50]}"
        Clock.schedule_once(lambda dt: self.show_toast(msg))

    def unzip_pick(self):
        FilePicker(start=self._last_dir(), title="Pilih file ZIP", mode="file",
                   exts=[".zip"], callback=self._unzip_picked).open()

    def _unzip_picked(self, path):
        try:
            with zipfile.ZipFile(path) as z:
                infos = z.infolist()
        except zipfile.BadZipFile:
            self.show_toast("Bukan file ZIP yang valid")
            return
        except Exception as e:
            self.show_toast(f"Gagal membuka: {str(e)[:40]}")
            return
        self.unzip_src = path
        self.unzip_dest = os.path.join(os.path.dirname(path), os.path.splitext(os.path.basename(path))[0])
        box = self._zip_ids().unzip_list
        box.clear_widgets()
        for info in infos[:60]:
            is_dir = info.filename.endswith("/")
            box.add_widget(ListRow(
                icon="folder" if is_dir else "file-document-outline",
                muted_icon=not is_dir,
                title=info.filename,
                subtitle="" if is_dir else fmt_bytes(info.file_size),
                trailing="",
            ))
        if len(infos) > 60:
            box.add_widget(Factory.T4(text=f"...dan {len(infos) - 60} item lainnya"))
        if not infos:
            box.add_widget(Factory.T4(text="Arsip kosong."))
        self.refresh_zip_ui()

    def unzip_pick_dest(self):
        def got(folder):
            self.unzip_dest = folder
            self.refresh_zip_ui()
        FilePicker(start=self.unzip_dest or self._last_dir(), title="Ekstrak ke folder",
                   mode="dir", callback=got).open()

    def unzip_extract(self):
        if not self.unzip_src:
            self.show_toast("Pilih file ZIP dulu")
            return
        if not self.unzip_dest:
            self.show_toast("Pilih folder tujuan dulu")
            return
        self.show_toast("Mengekstrak...")
        threading.Thread(target=self._unzip_worker, args=(self.unzip_src, self.unzip_dest), daemon=True).start()

    def _unzip_worker(self, src, dest):
        try:
            os.makedirs(dest, exist_ok=True)
            dest_abs = os.path.abspath(dest)
            count = skipped = 0
            with zipfile.ZipFile(src) as z:
                for info in z.infolist():
                    target = os.path.abspath(os.path.join(dest_abs, info.filename))
                    if target != dest_abs and not target.startswith(dest_abs + os.sep):
                        skipped += 1  # cegah path berbahaya (zip-slip)
                        continue
                    z.extract(info, dest_abs)
                    if not info.filename.endswith("/"):
                        count += 1
            msg = f"Selesai: {count} file diekstrak"
            if skipped:
                msg += f", {skipped} dilewati"
        except RuntimeError:
            msg = "ZIP terkunci password (belum didukung)"
        except Exception as e:
            msg = f"Gagal: {str(e)[:50]}"
        Clock.schedule_once(lambda dt: self.show_toast(msg))

    # ------------------------------------------------------------ tools: Web Project Builder
    def _web_project_ids(self):
        return self.root.get_screen("webproject").ids

    def _web_project_refresh(self):
        ids = self._web_project_ids()
        ids.wp_name_row.subtitle = self.web_project_name_value or "Belum dibuat"
        labels = {"html": ("wp_html_row", ".html"), "css": ("wp_css_row", ".css"), "js": ("wp_js_row", ".js")}
        for key, (rid, ext) in labels.items():
            path = self.web_project_files.get(key)
            ids[rid].subtitle = short_text(path, 42) if path else f"Pilih file {ext}"

    def web_project_name(self):
        NameDialog(title="Nama Web Project", value=self.web_project_name_value or "MyWebsite",
                   hint="contoh: MyWebsite", ok_text="Pakai",
                   callback=self._web_project_set_name).open()

    def _web_project_set_name(self, name):
        name = (name or "").strip()
        if not name or any(c in name for c in '/\\:'): 
            self.show_toast("Nama project tidak valid")
            return
        self.web_project_name_value = name
        self._web_project_refresh()

    def web_project_pick(self, kind):
        ext = {"html": ".html", "css": ".css", "js": ".js"}[kind]
        def got(path):
            self.web_project_files[kind] = path
            self._web_project_refresh()
        FilePicker(start=self._last_dir(), title=f"Pilih file {ext}", mode="file", exts=[ext], callback=got).open()

    def web_project_build(self):
        html_path = self.web_project_files.get("html")
        if not html_path or not os.path.isfile(html_path):
            self.show_toast("Pilih file HTML dulu")
            return
        name = self.web_project_name_value or "MyWebsite"
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._") or "MyWebsite"
        base = os.path.join(storage_path(), "MyTools", "WebProjects")
        os.makedirs(base, exist_ok=True)
        dest = os.path.join(base, safe)
        os.makedirs(dest, exist_ok=True)
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html = f.read()
            copied = []
            css_path = self.web_project_files.get("css")
            js_path = self.web_project_files.get("js")
            if css_path and os.path.isfile(css_path):
                css_name = os.path.basename(css_path)
                shutil.copy2(css_path, os.path.join(dest, css_name))
                copied.append(css_name)
                if css_name not in html:
                    tag = f'\n<link rel="stylesheet" href="{urllib.parse.quote(css_name)}">\n'
                    if re.search(r"</head>", html, re.I):
                        html = re.sub(r"</head>", tag + "</head>", html, count=1, flags=re.I)
                    else:
                        html = tag + html
            if js_path and os.path.isfile(js_path):
                js_name = os.path.basename(js_path)
                shutil.copy2(js_path, os.path.join(dest, js_name))
                copied.append(js_name)
                if js_name not in html:
                    tag = f'\n<script src="{urllib.parse.quote(js_name)}"></script>\n'
                    if re.search(r"</body>", html, re.I):
                        html = re.sub(r"</body>", tag + "</body>", html, count=1, flags=re.I)
                    else:
                        html += tag
            with open(os.path.join(dest, "index.html"), "w", encoding="utf-8", newline="") as f:
                f.write(html)
            self.web_project_dir = dest
            self.site_dir = dest
            self.show_toast(f"Website jadi: {safe}")
            self._web_project_refresh()
        except Exception as e:
            self.show_toast(f"Build web gagal: {str(e)[:60]}")

    def web_project_host(self):
        if not self.web_project_dir or not os.path.isdir(self.web_project_dir):
            self.web_project_build()
            if not self.web_project_dir:
                return
        self.http_dir = self.web_project_dir
        self.goto("http")
        Clock.schedule_once(lambda dt: self.refresh_http_ui(), 0)

    def web_project_open_folder(self):
        folder = self.web_project_dir or self.site_dir
        if not folder or not os.path.isdir(folder):
            self.show_toast("Build website dulu")
            return
        FilePicker(start=folder, title="Folder Web Project", mode="dir", callback=lambda p: None).open()

    # ------------------------------------------------------------ tools: HTTP Server
    def _http_ids(self):
        return self.root.get_screen("http").ids

    def refresh_http_ui(self):
        ids = self._http_ids()
        running = self.http_server is not None
        ids.http_btn.text = "Hentikan server" if running else "Mulai server"
        ids.http_btn.icon = "stop" if running else "play"
        ids.http_btn.outlined = running
        ids.http_dir_row.subtitle = short_text(self.http_dir, 42) if self.http_dir else "Belum dipilih"
        status, urls = ids.http_status, ids.http_urls
        urls.clear_widgets()
        if running:
            host, port = self.http_server.server_address[:2]
            status.icon, status.title = "server-network", "Server berjalan"
            status.subtitle = f"Port {port}"
            addrs = [("Lokal", f"http://127.0.0.1:{port}")]
            if host == "0.0.0.0":
                addrs.insert(0, ("WiFi / jaringan", f"http://{get_local_ip()}:{port}"))
            for label, url in addrs:
                row = ListRow(icon="link-variant", title=url, subtitle=f"{label}  |  ketuk untuk menyalin",
                              trailing="", boxed=True)
                row.bind(on_release=lambda w, u=url: self.copy_text(u, "Alamat disalin"))
                urls.add_widget(row)
        else:
            status.icon, status.title = "server-off", "Server berhenti"
            status.subtitle = "Pilih folder lalu tekan Mulai"
        ids.http_log.text = "\n".join(self._http_lines) or "Belum ada permintaan."

    def http_pick_dir(self):
        def got(folder):
            self.http_dir = folder
            self.refresh_http_ui()
        FilePicker(start=self.http_dir or storage_path(), title="Folder yang dibagikan",
                   mode="dir", callback=got).open()

    def http_toggle(self):
        if self.http_server is not None:
            self.http_stop()
        else:
            self.http_start()

    def http_start(self):
        ids = self._http_ids()
        if not self.http_dir or not os.path.isdir(self.http_dir):
            self.show_toast("Pilih folder dulu")
            return
        try:
            port = int(ids.http_port.text or 8000)
        except ValueError:
            self.show_toast("Port tidak valid")
            return
        if not 1024 <= port <= 65535:
            self.show_toast("Port harus 1024 - 65535")
            return
        host = "0.0.0.0" if ids.http_lan.checked else "127.0.0.1"
        try:
            server = QuietServer((host, port), make_handler(self.http_dir, self._http_log))
        except OSError:
            self.show_toast(f"Port {port} tidak bisa dipakai")
            return
        self.http_server = server
        threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.3}, daemon=True).start()
        self._http_push("Server dimulai")
        self.refresh_http_ui()

    def http_stop(self):
        server, self.http_server = self.http_server, None
        if server:
            def worker():
                try:
                    server.shutdown()
                    server.server_close()
                except Exception:
                    pass
            threading.Thread(target=worker, daemon=True).start()
        self._http_push("Server dihentikan")
        self.refresh_http_ui()

    def _http_log(self, line):  # dipanggil dari thread server
        Clock.schedule_once(lambda dt: self._http_push(line))

    def _http_push(self, line):
        self._http_lines.append(f"{datetime.now():%H:%M:%S}  {escape_markup(line)}")
        if self.root.current == "http":
            self._http_ids().http_log.text = "\n".join(self._http_lines)

    def on_stop(self):
        try:
            if self._pip_proc:
                self._pip_proc.terminate()
            if self.http_server:
                self.http_server.shutdown()
                self.http_server.server_close()
        except Exception:
            pass

    # ------------------------------------------------------------ tools: Installer (pip)
    def _inst_ids(self):
        return self.root.get_screen("installer").ids

    def set_inst_tab(self, tab):
        ids = self._inst_ids()
        ids.inst_sm.current = tab
        ids.seg_install.active = tab == "install"
        ids.seg_pkgs.active = tab == "pkgs"

    def refresh_installer_ui(self):
        ids = self._inst_ids()
        info = ids.inst_info
        if pip_available():
            info.icon, info.title = "check-circle", "pip tersedia"
            info.subtitle = "Dipasang ke: " + (short_text(self.site_dir, 30) if self.site_dir else "Python aktif")
        else:
            info.icon, info.title = "alert-circle-outline", "pip tidak tersedia"
            info.subtitle = "Tambahkan paket lewat requirements di buildozer.spec"
        self.refresh_packages(reload=True)

    def refresh_packages(self, reload=False):
        ids = self._inst_ids()
        if reload or self._pkg_cache is None:
            try:
                self._pkg_cache = list_packages()
            except Exception:
                self._pkg_cache = []
        query = ids.pkg_search.text.strip().lower()
        matches = [p for p in self._pkg_cache if query in p[0].lower()]
        ids.pkg_count.text = f"{len(matches)} paket terpasang"
        box = ids.pkg_list
        box.clear_widgets()
        for name, ver in matches[:200]:
            row = ListRow(icon="package-variant-closed", title=name, subtitle=ver, trailing="")
            row.bind(on_release=lambda w, n=name: self._pkg_tapped(n))
            box.add_widget(row)
        if len(matches) > 200:
            box.add_widget(Factory.T4(text="Persempit pencarian untuk melihat sisanya."))

    def _pkg_tapped(self, name):
        if not pip_available():
            self.show_toast("pip tidak tersedia di sini")
            return
        ConfirmDialog(
            title=f"Uninstall {name}?",
            message="Paket akan dihapus dari lingkungan Python ini.",
            ok_text="Uninstall",
            callback=lambda: (self.set_inst_tab("install"), self._pip_start("uninstall", [name])),
        ).open()

    def pip_run(self, action):
        tokens, err = parse_packages(self._inst_ids().inst_field.text)
        if err:
            self.show_toast(err)
            return
        self._pip_start(action, tokens)

    def _pip_start(self, action, tokens):
        if self._pip_busy:
            self.show_toast("Masih ada proses berjalan")
            return
        if not pip_available():
            self.show_toast("pip tidak tersedia di sini")
            return
        ids = self._inst_ids()
        args = [sys.executable, "-m", "pip", action, "--disable-pip-version-check"]
        if action == "install":
            args += ["--no-input"]
            if ids.inst_upgrade.checked:
                args.append("--upgrade")
            if self.site_dir:
                args += ["--target", self.site_dir]
        else:
            args += ["-y"]
        args += tokens
        env = dict(os.environ)
        if self.site_dir:  # supaya pip melihat paket di folder data aplikasi
            env["PYTHONPATH"] = self.site_dir + os.pathsep + env.get("PYTHONPATH", "")
        self._pip_lines.clear()
        self._pip_lines.append(escape_markup("$ pip " + " ".join(args[3:])))
        ids.inst_log.text = "\n".join(self._pip_lines)
        self._pip_busy = True
        self._pip_ui(True)
        threading.Thread(target=self._pip_worker, args=(args, env), daemon=True).start()

    def _pip_worker(self, args, env):
        rc = -1
        try:
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    text=True, errors="replace", bufsize=1, env=env)
            self._pip_proc = proc
            for line in proc.stdout:
                Clock.schedule_once(lambda dt, l=line.rstrip(): self._pip_push(l))
            rc = proc.wait()
        except Exception as e:
            Clock.schedule_once(lambda dt, m=str(e): self._pip_push(f"Error: {m}"))
        finally:
            self._pip_proc = None
        Clock.schedule_once(lambda dt: self._pip_done(rc))

    def _pip_push(self, line):
        self._pip_lines.append(escape_markup(line))
        self._inst_ids().inst_log.text = "\n".join(self._pip_lines)

    def _pip_done(self, rc):
        import importlib
        importlib.invalidate_caches()
        self._pip_busy = False
        self._pip_ui(False)
        self.show_toast("Selesai" if rc == 0 else ("Dibatalkan" if rc < 0 else f"Gagal (kode {rc})"))
        self.refresh_packages(reload=True)

    def pip_cancel(self):
        if self._pip_proc:
            try:
                self._pip_proc.terminate()
            except Exception:
                pass

    def _pip_ui(self, running):
        ids = self._inst_ids()
        for btn in (ids.inst_btn_install, ids.inst_btn_uninstall):
            btn.disabled = running
            btn.opacity = 0.5 if running else 1
        cancel = ids.inst_btn_cancel
        cancel.disabled = not running
        cancel.opacity = 1 if running else 0
        cancel.height = dp(48) if running else 0

    # ------------------------------------------------------------ tools: Sistem
    def refresh_system_info(self):
        box = self.root.get_screen("system").ids.sys_list
        box.clear_widgets()
        usages, groups = collect_system_info(self.user_data_dir)

        lines = []
        for u in usages:
            box.add_widget(UsageCard(**u))
            lines.append(f"{u['title']}: {u['detail']}")

        for title, rows in groups:
            box.add_widget(Factory.Sec(text=title))
            lines.append("")
            lines.append(f"[{title}]")
            for icon, label, value in rows:
                row = ListRow(icon=icon, title=label, subtitle=short_text(value),
                              trailing="", boxed=True)
                row.bind(on_release=lambda w, v=value, l=label: self.copy_text(str(v), f"{l} disalin"))
                box.add_widget(row)
                lines.append(f"{label}: {value}")
        self._sys_text = "\n".join(lines).strip()

    # ------------------------------------------------------------ navigasi
    def goto(self, name):
        sm = self.root
        if sm.current != name:
            self._history.append(sm.current)
            sm.current = name

    def go_back(self):
        sm = self.root
        cfg = self._lists.get(sm.current)
        if (cfg and cfg.get("dir") and cfg.get("root")
                and os.path.normpath(cfg["dir"]) != os.path.normpath(cfg["root"])):
            self._navigate(sm.current, os.path.dirname(cfg["dir"].rstrip(os.sep)))   # naik satu folder
            return
        if sm.current == "editor" and self.editor_dirty:
            self._guard_unsaved(lambda: (setattr(self, "editor_dirty", False), self.go_back()))
            return
        sm.current = self._history.pop() if self._history else "home"

    def _on_key(self, window, key, *args):
        if key == 27:  # tombol back Android / Esc
            if self.root.current != "home":
                self.go_back()
                return True
        return False

    def open_file_sheet(self, screen_name, name, size):
        self._file_sheet_ctx = {"screen": screen_name, "name": name}
        sheet = FileSheet(filename=name, filesize=size)
        for icon, label in SHEET_ACTIONS:
            row = SheetRow(icon=icon, text=label)
            row.bind(on_release=lambda w, l=label, s=sheet: (self.on_file_action(l), s.dismiss()))
            sheet.ids.options.add_widget(row)
        sheet.open()

    # ============================================================
    #  FUNGSI KOSONG  -  isi nanti sesuai kebutuhan
    #
    #  Status pengerjaan (lihat catatan lengkap di akhir file):
    #    [MUDAH]  sudah diisi & berfungsi di bawah ini
    #    [SEDANG] / [SULIT]  masih "pass", perlu dikerjakan menyusul
    # ============================================================
    # Home
    def on_search(self, text):
        """[MUDAH] Filter kartu tools di Home berdasarkan judul."""
        home_grid = self.root.get_screen("home").ids.home_grid
        empty_label = self.root.get_screen("home").ids.home_empty
        query = text.strip().lower()
        home_grid.clear_widgets()
        shown = 0
        for tile in self._home_tiles:
            if query in tile.title.lower():
                home_grid.add_widget(tile)
                shown += 1
        empty_label.text = "" if shown else f"Tidak ada tools untuk \"{text.strip()}\""

    def on_premium(self):
        """[MUDAH] Placeholder info fitur premium."""
        self.show_toast("Fitur Premium belum tersedia")

    # Top bar & bottom bar
    def on_top_icon(self, name):
        # Layar Sistem: refresh & salin semua info
        if self.root.current == "editor" and name == "content-save-edit-outline":
            self.editor_save_as()
        elif self.root.current == "http" and name == "delete-outline":
            self._http_lines.clear()
            self.refresh_http_ui()
        elif self.root.current == "installer" and name == "refresh":
            self.refresh_installer_ui()
            self.show_toast("Diperbarui")
        elif self.root.current == "wifiinfo":
            if name == "refresh":
                self.refresh_wifi_info()
                self.show_toast("Info Wi-Fi diperbarui")
            elif name == "content-copy":
                self.copy_wifi_info()
        elif self.root.current == "system":
            if name == "refresh":
                self.refresh_system_info()
                self.show_toast("Info diperbarui")
            elif name == "content-copy":
                self.copy_text(getattr(self, "_sys_text", ""), "Semua info disalin")
        elif self.root.current == "quicktool" and name == "content-copy":
            if self._qt_last_output:
                self.copy_text(self._qt_last_output, "Hasil disalin")
            else:
                self.show_toast("Belum ada hasil untuk disalin")
        elif self.root.current == "logviewer" and name == "refresh":
            self.refresh_log_viewer()
            self.show_toast("Log diperbarui")
        elif self.root.current == "terminal" and name == "history":
            self.refresh_term_history()
            self.goto("termhistory")
    def on_new(self):
        """[SEDANG] File Manager: buat file/folder baru di folder yang sedang dibuka (nyata)."""
        self._new_item_flow("filemanager")

    def on_select(self):
        """[SEDANG] Nyalakan/matikan mode pilih multi-item (File Manager & Struktur Project)."""
        screen_name = self.root.current
        cfg = self._lists.get(screen_name)
        if not cfg or not cfg.get("select_btn"):
            return
        cfg["select"] = not cfg["select"]
        if not cfg["select"]:
            cfg["selected"].clear()
        self._render_list(screen_name)
        self._update_select_btn(screen_name)

    def on_sort(self):
        """[SEDANG] Urutkan daftar; pilihan urutan diingat per layar (ikut berlaku saat masuk folder lain)."""
        screen_name = self.root.current
        cfg = self._lists.get(screen_name)
        if not cfg:
            return

        def pick(label):
            cfg["sort"] = label
            self._apply_sort(cfg)
            self._render_list(screen_name)
            self.show_toast(f"Diurutkan: {label}")

        self._open_option_sheet("Urutkan berdasarkan", [
            ("sort-alphabetical-ascending", "Nama (A-Z)"),
            ("sort-alphabetical-descending", "Nama (Z-A)"),
            ("folder-outline", "Folder dulu"),
            ("file-outline", "File dulu"),
        ], pick)

    def on_options(self):
        """[SEDANG] Menu opsi (dots-vertical): Segarkan, Urutkan, Pilih, Tempel + aksi massal (nyata)."""
        screen_name = self.root.current
        cfg = self._lists.get(screen_name)
        if not cfg:
            return

        if cfg["select"] and cfg["selected"]:
            names = [it["name"] for it in cfg["items"] if it["name"] in cfg["selected"]]
            count = len(names)

            def leave_select_mode():
                cfg["selected"].clear()
                cfg["select"] = False
                self._render_list(screen_name)
                self._update_select_btn(screen_name)

            def pick_selected(label):
                if label.startswith("Salin"):
                    self._set_clipboard("copy", screen_name, names)
                    self.show_toast(f"{count} item disalin")
                    leave_select_mode()
                elif label.startswith("Potong"):
                    self._set_clipboard("cut", screen_name, names)
                    self.show_toast(f"{count} item dipotong, siap ditempel")
                    leave_select_mode()
                elif label.startswith("Hapus"):
                    ConfirmDialog(title=f"Hapus {count} item?",
                                  message="Item akan dihapus PERMANEN dari penyimpanan.",
                                  ok_text="Hapus",
                                  callback=lambda: self._delete_many(screen_name, names)).open()

            self._open_option_sheet(f"{count} item dipilih", [
                ("content-copy", f"Salin {count} item"),
                ("content-cut", f"Potong {count} item"),
                ("delete", f"Hapus {count} item"),
            ], pick_selected)
        else:
            options = [("refresh", "Segarkan"), ("sort-variant", "Urutkan")]
            if self.clipboard and self.clipboard.get("paths"):
                options.append(("content-paste", "Tempel"))
            if cfg.get("select_btn"):
                options.append(("checkbox-marked-outline", "Pilih item"))

            def pick_general(label):
                if label == "Segarkan":
                    self._reload_list(screen_name)
                    self.show_toast("Disegarkan")
                elif label == "Urutkan":
                    self.on_sort()
                elif label == "Tempel":
                    self.on_paste()
                elif label == "Pilih item":
                    self.on_select()

            self._open_option_sheet("Opsi", options, pick_general)

    def on_add(self):
        """[SEDANG] Tambah file/folder baru ke Project / Struktur Project (nyata)."""
        screen_name = self.root.current
        if screen_name not in self._lists:
            screen_name = "project"
        self._new_item_flow(screen_name)

    def on_paste(self):
        """[SEDANG] Tempel hasil Salin/Potong ke folder yang sedang dibuka (copy/move sungguhan)."""
        screen_name = self.root.current
        cfg = self._lists.get(screen_name)
        if not cfg:
            return
        clip = self.clipboard
        if not clip or not clip.get("paths"):
            self.show_toast("Papan klip kosong")
            return
        dest = cfg.get("dir")
        if not dest:
            self.show_toast("Pilih folder project dulu")
            return
        ok = fail = 0
        last_err = ""
        for src in clip["paths"]:
            try:
                if not os.path.lexists(src):
                    raise FileNotFoundError("sumber sudah tidak ada")
                if clip["mode"] == "cut":
                    move_path(src, dest)
                else:
                    copy_path(src, dest)
                ok += 1
            except Exception as e:
                fail += 1
                last_err = str(e)
        if clip["mode"] == "cut":
            self.clipboard = None
        self._reload_all_lists()
        if fail:
            self.show_toast(f"{ok} berhasil, {fail} gagal: {last_err[:60]}")
        else:
            self.show_toast(f"{ok} item ditempel")

    # File manager
    def on_open_item(self, name, screen_name="filemanager"):
        """[SEDANG] Ketuk folder = masuk ke folder itu (back = naik); ketuk file = buka di Text Editor.
        Folder yang berisi buildozer.spec dibuka sebagai Project."""
        path = self._item_path(screen_name, name)
        if not path:
            return
        if os.path.isdir(path):
            if screen_name == "filemanager" and os.path.isfile(os.path.join(path, "buildozer.spec")):
                self._set_project_dir(path)
                self.goto("project")
                self.show_toast(f'Project "{name}" dibuka')
            else:
                self._navigate(screen_name, path)
        else:
            self._open_real_file(path)

    def _open_real_file(self, path):
        def do_open():
            if self._load_editor_file(path):
                self.goto("editor")
        self._guard_unsaved(do_open)

    def on_file_action(self, label):
        """[SEDANG] Rename, Hapus, Info, Properti, Salin, Potong, Zip, Buka, Edit - semuanya
        bekerja pada file/folder sungguhan. Bagikan: menyalin path asli (share intent = [SULIT])."""
        ctx = self._file_sheet_ctx
        if not ctx:
            return
        screen_name, name = ctx["screen"], ctx["name"]
        item = self._find_item(screen_name, name)
        path = self._item_path(screen_name, name)
        if not item or not path:
            return
        if not os.path.lexists(path):
            self._reload_all_lists()
            self.show_toast(f'"{name}" sudah tidak ada')
            return
        is_dir = item["kind"] == "folder"

        if label == "Rename":
            NameDialog(title="Ganti nama", value=name, hint="nama baru", ok_text="Ganti",
                       callback=lambda new_name: self._rename_item(screen_name, item, new_name)).open()

        elif label == "Hapus":
            ConfirmDialog(title=f'Hapus "{name}"?',
                          message="Folder beserta isinya akan dihapus PERMANEN." if is_dir
                          else "File akan dihapus PERMANEN dari penyimpanan.",
                          ok_text="Hapus",
                          callback=lambda: self._delete_item(screen_name, item)).open()

        elif label == "Info":
            self.show_toast(f"{name} - {'Folder' if is_dir else 'File'} - {item['meta']}")

        elif label == "Properti":
            ConfirmDialog(title="Properti", message=describe_path(path), ok_text="Tutup",
                          callback=lambda: None).open()

        elif label == "Salin":
            self._set_clipboard("copy", screen_name, {name})
            self.show_toast(f'"{name}" disalin')

        elif label == "Potong":
            self._set_clipboard("cut", screen_name, {name})
            self.show_toast(f'"{name}" dipotong, siap ditempel')

        elif label == "Buka" and is_dir:
            self._navigate(screen_name, path)

        elif label in ("Buka", "Edit"):
            if is_dir:
                self.show_toast(f'"{name}" adalah folder')
            else:
                self._open_real_file(path)

        elif label == "Zip":
            dest = self._lists[screen_name]["dir"]
            self.show_toast("Membuat zip...")

            def work():
                try:
                    zn, err = zip_path(path, dest), None
                except Exception as e:
                    zn, err = None, str(e)[:80]
                Clock.schedule_once(lambda dt: self._zip_done(zn, err), 0)

            threading.Thread(target=work, daemon=True).start()

        elif label == "Bagikan":
            self.copy_text(path, f'Lokasi "{name}" disalin')

        else:
            self.show_toast("Fitur ini belum tersedia")

    def _zip_done(self, zip_name, err):
        if err:
            self.show_toast(f"Gagal membuat zip: {err}")
            return
        self._reload_all_lists()
        self.show_toast(f'"{zip_name}" dibuat')

    # APK Builder
    def on_choice(self, widget):
        """[MUDAH] Toggle Choice: radio -> hanya 1 aktif, check -> independen."""
        if widget.kind == "radio":
            parent = widget.parent
            if parent:
                for child in parent.children:
                    if isinstance(child, Choice) and child.kind == "radio":
                        child.checked = (child is widget)
        elif widget.kind == "check":
            widget.checked = not widget.checked

    def on_advanced_settings(self):
        """[MUDAH] Placeholder, belum ada layar pengaturan lanjutan."""
        self.show_toast("Pengaturan lanjutan belum tersedia")

    def on_pick_project(self):
        """Pilih project folder ATAU ZIP. ZIP diekstrak otomatis ke workspace MyTools."""
        def picked(path):
            try:
                if os.path.isfile(path) and path.lower().endswith(".zip"):
                    project_dir = self._import_project_zip(path)
                    self._set_project_dir(project_dir)
                    self.show_toast(f"ZIP berhasil diimpor: {os.path.basename(project_dir)}")
                elif os.path.isdir(path):
                    self._set_project_dir(path)
                    self.show_toast(f"Project dipilih: {os.path.basename(path.rstrip(os.sep))}")
                else:
                    self.show_toast("File project tidak valid")
            except Exception as e:
                self.show_toast(f"Gagal membuka project: {str(e)[:100]}")

        FilePicker(start=self._last_dir(), title="Pilih ZIP project atau folder", mode="file",
                   exts=[".zip"], callback=picked).open()

    def _import_project_zip(self, zip_path):
        """Ekstrak ZIP dengan aman dan mencari root project secara otomatis."""
        base = os.path.join(self.user_data_dir, "apk_projects")
        os.makedirs(base, exist_ok=True)
        stem = os.path.splitext(os.path.basename(zip_path))[0]
        safe_stem = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("._") or "project"
        dest = os.path.join(base, safe_stem)
        if os.path.exists(dest):
            dest = os.path.join(base, safe_stem + "_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
        os.makedirs(dest, exist_ok=True)

        root_abs = os.path.abspath(dest)
        with zipfile.ZipFile(zip_path, "r") as zf:
            for info in zf.infolist():
                name = info.filename.replace("\\", "/")
                parts = name.split("/")
                if name.startswith("/") or any(part == ".." for part in parts):
                    raise ValueError(f"ZIP berisi path tidak aman: {name}")
                target = os.path.abspath(os.path.join(dest, *parts))
                if target != root_abs and not target.startswith(root_abs + os.sep):
                    raise ValueError("ZIP berisi path di luar folder project")
                if info.is_dir():
                    os.makedirs(target, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    with zf.open(info, "r") as src, open(target, "wb") as dst:
                        shutil.copyfileobj(src, dst)

        candidates = []
        for current, dirs, files in os.walk(dest):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".buildozer")]
            score = (2 if "buildozer.spec" in files else 0) + (1 if "main.py" in files else 0)
            if score:
                candidates.append((score, len(os.path.relpath(current, dest).split(os.sep)), current))
        if candidates:
            candidates.sort(key=lambda x: (-x[0], x[1]))
            return candidates[0][2]
        return dest

    def _project_validate(self, project_dir):
        """Validasi ringan project sebelum build."""
        main_py = os.path.join(project_dir, "main.py")
        spec = os.path.join(project_dir, "buildozer.spec")
        py_files = []
        for current, dirs, files in os.walk(project_dir):
            dirs[:] = [d for d in dirs if d not in (".git", ".buildozer", "bin", "__pycache__")]
            py_files.extend(os.path.join(current, f) for f in files if f.endswith(".py"))
        if not os.path.isfile(main_py):
            return False, "main.py tidak ditemukan di root project.", {"main": False, "spec": os.path.isfile(spec), "py": len(py_files)}
        return True, "Project siap dibuild.", {"main": True, "spec": os.path.isfile(spec), "py": len(py_files)}

    def _ensure_buildozer_spec(self, project_dir):
        """Buat buildozer.spec minimal bila ZIP tidak memilikinya; tidak menimpa spec."""
        spec_path = os.path.join(project_dir, "buildozer.spec")
        if os.path.isfile(spec_path):
            return spec_path, False

        app_name = os.path.basename(project_dir.rstrip(os.sep)) or "MyApp"
        slug = re.sub(r"[^a-zA-Z0-9]+", "", app_name).lower() or "myapp"
        spec = f"""[app]\n\n# Nama aplikasi\ntitle = {app_name}\npackage.name = {slug}\npackage.domain = org.example\n\nsource.dir = .\nsource.include_exts = py,png,jpg,jpeg,gif,kv,atlas,json,txt,wav,mp3,ttf,otf,zip\nrequirements = python3,kivy\norientation = portrait\nfullscreen = 0\nversion = 1.0\n\nandroid.api = 35\nandroid.minapi = 23\nandroid.ndk = 27c\nandroid.archs = arm64-v8a\nandroid.accept_sdk_license = True\n\n[buildozer]\nlog_level = 2\nwarn_on_root = 1\n"""
        with open(spec_path, "w", encoding="utf-8") as f:
            f.write(spec)
        return spec_path, True

    def on_start_build(self):
        """Upload ZIP/folder -> validasi -> spec otomatis -> Buildozer debug."""
        if self.building_active:
            self.show_toast("Build masih berjalan")
            return
        if not self._apk_project_dir or not os.path.isdir(self._apk_project_dir):
            self.show_toast("Pilih ZIP project terlebih dahulu")
            return

        ok, message, info = self._project_validate(self._apk_project_dir)
        if not ok:
            self.LOG_TEXT = f"{datetime.now().strftime('%H:%M')}  ERROR: {message}"
            self.show_toast(message)
            self.goto("building")
            return

        try:
            spec_path, generated = self._ensure_buildozer_spec(self._apk_project_dir)
        except Exception as e:
            self.show_toast(f"Gagal menyiapkan buildozer.spec: {str(e)[:90]}")
            return

        buildozer_bin = shutil.which("buildozer")
        self.build_steps = [False] * 7
        self.build_step_labels = [label for _pat, label in BUILD_STEP_PATTERNS]
        self.build_fraction = 0.0
        self.build_percent = "0%"
        self._built_apk_path = None
        self._build_matched = 0
        project_name = os.path.basename(self._apk_project_dir)
        self.LOG_TEXT = (
            f"{datetime.now().strftime('%H:%M')}  Project: {project_name}\n"
            f"main.py: {'OK' if info['main'] else 'TIDAK ADA'}\n"
            f"Python files: {info['py']}\n"
            f"buildozer.spec: {'dibuat otomatis' if generated else 'dipakai dari project'}\n"
        )
        self.goto("building")

        if not buildozer_bin:
            self.LOG_TEXT += (
                "\nBuildozer tidak ditemukan di sistem build.\n"
                "MyTools sudah menyiapkan project, tetapi APK tidak dapat dikompilasi "
                "tanpa Buildozer + Android SDK/NDK + Java/Gradle toolchain.\n"
                "Jalankan MyTools di environment yang memiliki toolchain tersebut "
                "atau sediakan engine builder terpisah."
            )
            self.show_toast("Build environment belum tersedia")
            return

        self.building_active = True
        self.LOG_TEXT += f"\n{datetime.now().strftime('%H:%M')}  Memulai Buildozer..."
        args = [buildozer_bin, "-v", "android", "debug"]
        threading.Thread(target=self._build_worker, args=(args, self._apk_project_dir), daemon=True).start()

    def _build_worker(self, args, cwd):
        """Jalan di background thread: eksekusi buildozer sungguhan & streaming log."""
        rc = -1
        try:
            proc = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     text=True, errors="replace", bufsize=1)
            self._build_proc = proc
            for line in proc.stdout:
                Clock.schedule_once(lambda dt, l=line.rstrip("\n"): self._build_push(l))
            rc = proc.wait()
        except FileNotFoundError:
            Clock.schedule_once(lambda dt: self._build_push("Error: perintah buildozer tidak ditemukan"))
        except Exception as e:
            Clock.schedule_once(lambda dt, m=str(e): self._build_push(f"Error: {m}"))
        finally:
            self._build_proc = None
        Clock.schedule_once(lambda dt: self._build_done(rc, cwd))

    def _build_push(self, line):
        """Update log & tebak langkah mana yang sedang berjalan dari baris log nyata."""
        self.LOG_TEXT += "\n" + line
        for idx, (pattern, _label) in enumerate(BUILD_STEP_PATTERNS):
            if idx < len(self.build_steps) and not self.build_steps[idx] and pattern.search(line):
                steps = list(self.build_steps)
                steps[idx] = True
                self.build_steps = steps
                self._build_matched = max(self._build_matched, idx + 1)
                self.build_fraction = self._build_matched / len(BUILD_STEP_PATTERNS)
                self.build_percent = f"{self.build_fraction * 100:.0f}%"
                break

    def _build_done(self, rc, project_dir):
        self.building_active = False
        now = datetime.now().strftime("%H:%M")
        if rc == 0:
            self.build_steps = [True] * 7
            self.build_fraction = 1.0
            self.build_percent = "100%"
            apk_path = self._find_built_apk(project_dir)
            if apk_path:
                self._built_apk_path = apk_path
                self.apk_name = os.path.basename(apk_path)
                try:
                    size_mb = os.path.getsize(apk_path) / (1024 * 1024)
                    self.apk_size_text = f"{size_mb:.1f} MB"
                except OSError:
                    self.apk_size_text = "—"
            else:
                self._built_apk_path = None
                self.apk_name = "APK dibuat (lokasi tidak ditemukan)"
                self.apk_size_text = "—"
            self.LOG_TEXT += f"\n{now}  Build selesai!"
            self.show_toast("Build APK berhasil")
            if self.root.current == "building":
                self.goto("done")
        else:
            reason = "dibatalkan" if rc < 0 else f"gagal (kode {rc})"
            self.LOG_TEXT += f"\n{now}  Build {reason}."
            self.show_toast(f"Build {reason}")

    def _find_built_apk(self, project_dir):
        """Cari APK terbaru di <project>/bin (lokasi output default buildozer)."""
        bin_dir = os.path.join(project_dir, "bin")
        if not os.path.isdir(bin_dir):
            return None
        apks = [os.path.join(bin_dir, f) for f in os.listdir(bin_dir) if f.lower().endswith(".apk")]
        if not apks:
            return None
        apks.sort(key=os.path.getmtime, reverse=True)
        return apks[0]

    def build_cancel(self):
        """Hentikan proses buildozer yang sedang berjalan, jika ada."""
        if self._build_proc:
            try:
                self._build_proc.terminate()
            except Exception:
                pass

    def on_tap_building_icon(self):
        """Ketuk ikon Android di layar Build: hanya pindah ke Build Selesai kalau
        build sungguhan sudah berhasil, bukan sekadar melewati animasi."""
        if self.building_active:
            self.show_toast("Build masih berjalan...")
        elif self._built_apk_path:
            self.goto("done")
        else:
            self.show_toast("Belum ada build sukses - lihat log di bawah")

    def on_install_apk(self):
        """[SULIT] Install APK sungguhan lewat installer sistem Android (Intent
        ACTION_VIEW + FileProvider). Pakai APK hasil build terakhir kalau ada,
        kalau tidak biarkan pengguna pilih file .apk manual. Butuh permission
        REQUEST_INSTALL_PACKAGES + <provider> FileProvider di AndroidManifest -
        lihat catatan buildozer.spec di bagian atas file ini."""
        if platform != "android":
            self.show_toast("Install APK hanya berfungsi di build Android sungguhan")
            return

        def do_install(path):
            if not path or not os.path.isfile(path):
                self.show_toast("File APK tidak ditemukan")
                return
            ConfirmDialog(
                title="Install APK?",
                message=f'Install "{os.path.basename(path)}" ke perangkat ini?',
                ok_text="Install",
                callback=lambda: self._install_apk_intent(path),
            ).open()

        if self._built_apk_path and os.path.isfile(self._built_apk_path):
            do_install(self._built_apk_path)
        else:
            FilePicker(start=self._last_dir(), title="Pilih file APK", mode="file",
                       exts=[".apk"], callback=do_install).open()

    def _install_apk_intent(self, path):
        """Buka dialog installer sistem Android untuk file APK di `path`."""
        activity = self._get_android_activity()
        if activity is None:
            self.show_toast("Tidak bisa mengakses Activity Android")
            return
        try:
            from jnius import autoclass
            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")
            AndroidFileProvider = autoclass("androidx.core.content.FileProvider")
            JFile = autoclass("java.io.File")
            Build_VERSION = autoclass("android.os.Build$VERSION")
            context = activity.getApplicationContext()
            package_name = context.getPackageName()

            # Android 8+ (API 26+): "Instal aplikasi tidak dikenal" adalah izin
            # khusus per-app, tidak lewat dialog izin runtime biasa.
            if Build_VERSION.SDK_INT >= 26:
                pm = context.getPackageManager()
                if not pm.canRequestPackageInstalls():
                    Settings = autoclass("android.provider.Settings")
                    req = Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,
                                 Uri.parse("package:" + package_name))
                    req.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    activity.startActivity(req)
                    self.show_toast('Izinkan "Instal aplikasi tidak dikenal" untuk MyTools, lalu coba lagi')
                    return

            authority = package_name + ".fileprovider"
            apk_uri = AndroidFileProvider.getUriForFile(context, authority, JFile(path))

            intent = Intent(Intent.ACTION_VIEW)
            intent.setDataAndType(apk_uri, "application/vnd.android.package-archive")
            intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            activity.startActivity(intent)
            self.show_toast("Membuka dialog instalasi APK...")
        except Exception as e:
            self.show_toast(f"Gagal membuka installer: {str(e)[:90]}")

    def on_share_apk(self):
        """[SULIT-demo] Simulasikan berbagi APK dengan menyalin lokasinya."""
        self.copy_text("/storage/emulated/0/MyTools/dist/mytools.apk",
                        "Lokasi mytools.apk disalin (demo berbagi)")

    def on_open_location(self):
        """[SULIT-demo] Simulasikan membuka lokasi APK di file manager (demo)."""
        self.goto("project")
        self.show_toast("Lokasi: Project > dist > mytools.apk (demo)")

    # Python
    def on_tab(self, name):
        """[SEDANG] Pindah tab Jalankan/Paket/Project di layar Python.
        Paket = daftar paket terpasang; Project = isi folder project yang dipilih."""
        scr = self.root.get_screen("python")
        for seg_id, seg_name in (("seg_run", "Jalankan"), ("seg_pkg", "Paket"), ("seg_project", "Project")):
            scr.ids[seg_id].active = (seg_name == name)
        group, parent, idx = self._py_group, self._py_parent, self._py_group_index
        placeholder = scr.ids.py_placeholder
        extra = scr.ids.py_extra
        extra.clear_widgets()
        placeholder.text = ""
        if name == "Jalankan":
            if group not in parent.children:
                parent.add_widget(group, index=idx)
            return
        if group in parent.children:
            parent.remove_widget(group)
        if name == "Paket":
            self._fill_py_packages(extra, placeholder)
        else:
            self._fill_py_project(extra, placeholder)

    def _fill_py_packages(self, extra, placeholder):
        manage = ListRow(icon="download-box-outline", title="Kelola paket",
                         subtitle="Install / uninstall lewat Installer", boxed=True)
        manage.bind(on_release=lambda w: self.on_open_tool("installer"))
        extra.add_widget(manage)
        if self._pkg_cache is None:
            try:
                self._pkg_cache = list_packages()
            except Exception:
                self._pkg_cache = []
        pkgs = self._pkg_cache
        if not pkgs:
            placeholder.text = "Belum ada paket yang terdeteksi."
            return
        for pname, ver in pkgs[:100]:
            extra.add_widget(ListRow(icon="package-variant-closed", title=pname, subtitle=ver, trailing=""))
        if len(pkgs) > 100:
            extra.add_widget(Factory.T4(text=f"+{len(pkgs) - 100} paket lain - buka Installer untuk mencari."))

    def _fill_py_project(self, extra, placeholder):
        d = self._apk_project_dir
        pick = ListRow(icon="folder-open-outline", title="Pilih project",
                       subtitle=(os.path.basename(d) or d) if d else "Belum dipilih", boxed=True)
        pick.bind(on_release=lambda w: self.on_pick_project())
        extra.add_widget(pick)
        if not d:
            placeholder.text = "Pilih folder project untuk melihat berkasnya di sini."
            return
        try:
            entries = scan_dir(d)
        except Exception as e:
            placeholder.text = f"Folder tidak bisa dibuka: {str(e)[:60]}"
            return
        if not entries:
            placeholder.text = "Folder project kosong."
            return
        for kind, fname, meta in entries[:100]:
            row = ListRow(icon="folder" if kind == "folder" else "file-document-outline",
                          muted_icon=kind != "folder", title=fname, subtitle=meta, trailing="")
            row.bind(on_release=lambda w, n=fname: self._py_project_open(n))
            extra.add_widget(row)

    def _py_project_open(self, fname):
        path = os.path.join(self._apk_project_dir, fname)
        if os.path.isdir(path):
            self._navigate("project", path)
            self.goto("project")
        else:
            self._open_real_file(path)

    def on_run_code(self):
        """[SULIT-demo] Simulasikan eksekusi kode Python (bukan proses sungguhan)."""
        if self._running_code:
            return
        self._running_code = True
        self.OUTPUT_TEXT = "Menjalankan main.py..."

        def finish(dt):
            self._running_code = False
            now = datetime.now().strftime("%H:%M:%S")
            self.OUTPUT_TEXT = (
                "Hello, MyTools!\n"
                "Number: 0\n"
                "Number: 1\n"
                "Number: 2\n"
                "Number: 3\n"
                "Number: 4\n"
                f"\n(selesai {now}, kode 0)"
            )
            self.show_toast("Kode selesai dijalankan")

        Clock.schedule_once(finish, 0.7)

    # Terminal
    def on_send_command(self, cmd):
        """[SULIT-demo] Simulasikan shell: tambahkan perintah & balasan contoh ke log."""
        cmd = cmd.strip()
        if not cmd:
            return
        scr = self.root.get_screen("terminal")
        prompt = "[color=#4ADE80]u0_a412@android[/color]:[color=#60A5FA]/sdcard/MyTools[/color]$ "
        self._term_history.append(cmd)
        if "term_input" in scr.ids:
            scr.ids.term_input.text = ""
        if cmd.split()[0] in ("clear", "cls"):
            self.TERM_TEXT = f"{prompt}_"
            return
        reply = self._fake_shell_reply(cmd)
        base = self.TERM_TEXT
        if base.endswith("_"):
            base = base[:-1]
        block = f"{cmd}\n{reply}\n\n{prompt}_" if reply else f"{cmd}\n\n{prompt}_"
        self.TERM_TEXT = base + block

    def _fake_shell_reply(self, cmd):
        """Balasan contoh untuk beberapa perintah umum (demo, tidak dieksekusi sungguhan)."""
        head, *rest = cmd.split()
        arg = " ".join(rest)
        if head == "pwd":
            return "/sdcard/MyTools"
        if head == "whoami":
            return "u0_a412"
        if head == "echo":
            return arg
        if head == "ls":
            return "main.py           buildozer.spec   [color=#60A5FA]src[/color]\nrequirements.txt  [color=#60A5FA]tools/[/color]"
        if head in ("python3", "python"):
            return "Hello, MyTools!\nNumber: 0\nNumber: 1\nNumber: 2\nNumber: 3\nNumber: 4"
        if head == "date":
            return datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        return f"bash: {head}: perintah tidak ditemukan (mode demo)"

    # Tools & Pengaturan
    def on_open_tool(self, name):
        if name == "system":
            self.refresh_system_info()
            self.goto("system")
        elif name == "editor":
            self.goto("editor")
        elif name == "zip":
            self.refresh_zip_ui()
            self.goto("zip")
        elif name == "http":
            self.refresh_http_ui()
            self.goto("http")
        elif name == "installer":
            self.refresh_installer_ui()
            self.goto("installer")
        elif name == "wifiinfo":
            self.refresh_wifi_info()
            self.goto("wifiinfo")
        elif name == "checksum":
            self.goto("checksum")
        elif name == "logviewer":
            self.refresh_log_viewer()
            self.goto("logviewer")
        elif name in ("qrgen", "fileanalyzer", "netspeed", "apkinspector"):
            self.goto(name)
        elif name in QT_SPECS:
            self.open_quick_tool(name)
        elif name in PLACEHOLDER_TOOLS:
            self.show_toast(f"{PLACEHOLDER_TOOLS[name]} belum tersedia, menyusul di update berikutnya")

    # ------------------------------------------------------------ Alat Cepat (generik)
    def open_quick_tool(self, key):
        spec = QT_SPECS.get(key)
        if not spec:
            self.show_toast("Alat tidak ditemukan")
            return
        self._qt_key = key
        self.qt_title = spec["title"]
        self.qt_desc = spec["desc"]
        self.qt_action_label = spec["action"]
        self.qt_show_input = not spec.get("generate_only", False)
        self.qt_hint1 = spec.get("hint1", "")
        self.qt_show_input2 = bool(spec.get("hint2"))
        self.qt_hint2 = spec.get("hint2", "")
        self.qt_show_length = bool(spec.get("has_length", False))
        self.qt_length = spec.get("length_default", 16)
        self._qt_last_output = ""

        scr = self.root.get_screen("quicktool")
        if "qt_input1" in scr.ids:
            scr.ids.qt_input1.text = ""
        if "qt_input2" in scr.ids:
            scr.ids.qt_input2.text = ""
        if "qt_output" in scr.ids:
            scr.ids.qt_output.text = ""

        modes = spec.get("modes") or []
        self._qt_mode = modes[0] if modes else None
        box = scr.ids.qt_options
        box.clear_widgets()
        for m in modes:
            choice = Choice(text=m, kind="radio", checked=(m == self._qt_mode))
            choice.bind(on_release=lambda w, mm=m: self.qt_select_mode(mm))
            box.add_widget(choice)
        self.goto("quicktool")

    def qt_select_mode(self, mode):
        self._qt_mode = mode
        box = self.root.get_screen("quicktool").ids.qt_options
        for child in box.children:
            if isinstance(child, Choice):
                child.checked = (child.text == mode)

    def qt_change_length(self, delta):
        self.qt_length = max(4, min(128, self.qt_length + delta))

    def qt_run(self):
        spec = QT_SPECS.get(self._qt_key)
        if not spec:
            return
        scr = self.root.get_screen("quicktool")
        a = scr.ids.qt_input1.text if "qt_input1" in scr.ids else ""
        b = scr.ids.qt_input2.text if "qt_input2" in scr.ids else ""
        if (spec.get("hint1") and not spec.get("generate_only")
                and self._qt_mode != "Sekarang" and not a.strip()):
            self.show_toast("Isi kolom teks dulu")
            return
        try:
            if spec.get("has_length"):
                result = spec["func"](a, b, self._qt_mode, self.qt_length)
            else:
                result = spec["func"](a, b, self._qt_mode)
        except Exception as e:
            result = f"❌ Terjadi kesalahan: {e}"
        result = str(result)
        scr.ids.qt_output.text = result
        self._qt_last_output = result

    # ------------------------------------------------------------ QR Generator
    def qr_generate(self):
        scr = self.root.get_screen("qrgen")
        data = scr.ids.qr_input.text.strip()
        if not data:
            self.show_toast("Isi teks atau URL dulu")
            return
        try:
            import qrcode
            from pathlib import Path
            out_dir = Path(self.user_data_dir) / "generated"
            out_dir.mkdir(parents=True, exist_ok=True)
            out = out_dir / "qrcode.png"
            img = qrcode.make(data)
            img.save(str(out))
            scr.ids.qr_image.source = str(out)
            scr.ids.qr_image.reload()
            scr.ids.qr_status.text = f"Tersimpan: {out.name}\n{len(data)} karakter"
            self.show_toast("QR Code berhasil dibuat")
        except ImportError:
            scr.ids.qr_status.text = "Library qrcode belum terpasang. Tambahkan qrcode ke requirements Buildozer lalu rebuild APK."
            self.show_toast("qrcode belum terpasang")
        except Exception as e:
            scr.ids.qr_status.text = f"Gagal membuat QR: {e}"

    # ------------------------------------------------------------ File Analyzer
    def file_analyzer_pick(self):
        FilePicker(start=self._last_dir(), title="Pilih file untuk dianalisis", mode="file",
                   callback=self._file_analyze).open()

    def _file_analyze(self, path):
        scr = self.root.get_screen("fileanalyzer")
        scr.ids.fa_path.text = path
        try:
            size = os.path.getsize(path)
            mime, _ = mimetypes.guess_type(path)
            ext = os.path.splitext(path)[1].lower() or "(tanpa ekstensi)"
            md5 = hashlib.md5(); sha1 = hashlib.sha1(); sha256 = hashlib.sha256()
            sample = b""
            with open(path, "rb") as f:
                sample = f.read(4096)
                f.seek(0)
                for chunk in iter(lambda: f.read(1024 * 1024), b""):
                    md5.update(chunk); sha1.update(chunk); sha256.update(chunk)
            binary = b"\x00" in sample
            kind = "Biner" if binary else "Kemungkinan teks UTF-8"
            lines = [
                f"Nama: {os.path.basename(path)}",
                f"Lokasi: {os.path.dirname(path)}",
                f"Ukuran: {fmt_bytes(size)} ({size:,} byte)",
                f"Ekstensi: {ext}",
                f"MIME: {mime or 'tidak diketahui'}",
                f"Jenis isi: {kind}",
                f"MD5: {md5.hexdigest()}",
                f"SHA1: {sha1.hexdigest()}",
                f"SHA256: {sha256.hexdigest()}",
            ]
            if ext == ".zip" or ext == ".apk" or zipfile.is_zipfile(path):
                try:
                    with zipfile.ZipFile(path) as z:
                        infos = z.infolist()
                        names = [i.filename for i in infos]
                        dirs = sum(1 for n in names if n.endswith("/"))
                        dex = sum(1 for n in names if n.lower().endswith(".dex"))
                        so = sum(1 for n in names if n.lower().endswith(".so"))
                        manifest = "AndroidManifest.xml" in names
                        lines += ["", "ZIP/APK:", f"  Entri: {len(infos)}", f"  Folder: {dirs}",
                                  f"  DEX: {dex}", f"  Native .so: {so}", f"  AndroidManifest.xml: {'Ya' if manifest else 'Tidak'}"]
                except Exception as e:
                    lines.append(f"  Gagal membaca arsip: {e}")
            if not binary:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read(8192)
                    lines += ["", "Preview teks (maks. 8 KB):", text[:4000]]
                except Exception:
                    pass
            scr.ids.fa_output.text = "\n".join(lines)
            self.show_toast("File selesai dianalisis")
        except Exception as e:
            scr.ids.fa_output.text = f"Gagal menganalisis file:\n{e}"

    # ------------------------------------------------------------ Network Speed
    def network_speed_test(self):
        scr = self.root.get_screen("netspeed")
        if getattr(self, "_speed_testing", False):
            return
        self._speed_testing = True
        scr.ids.speed_btn.disabled = True
        scr.ids.speed_btn.text = "Sedang menguji..."
        scr.ids.speed_output.text = "Mengukur latency dan download..."

        def worker():
            result = []
            try:
                host = "https://speed.cloudflare.com/__down?bytes=2000000"
                start = time.perf_counter()
                with urllib.request.urlopen(host, timeout=12) as r:
                    data = r.read()
                elapsed = max(time.perf_counter() - start, 0.001)
                mbps = (len(data) * 8 / 1_000_000) / elapsed
                result.append(f"Download: {mbps:.2f} Mbps")
                result.append(f"Data: {fmt_bytes(len(data))}")
                result.append(f"Waktu: {elapsed:.2f} detik")
            except Exception as e:
                result.append(f"Download gagal: {e}")
            try:
                start = time.perf_counter()
                with urllib.request.urlopen("https://www.cloudflare.com/cdn-cgi/trace", timeout=6) as r:
                    r.read(64)
                latency = (time.perf_counter() - start) * 1000
                result.append(f"HTTP latency: {latency:.0f} ms")
            except Exception as e:
                result.append(f"Latency gagal: {e}")
            Clock.schedule_once(lambda dt: self._speed_done("\n".join(result)))

        threading.Thread(target=worker, daemon=True).start()

    def _speed_done(self, text):
        try:
            scr = self.root.get_screen("netspeed")
            scr.ids.speed_output.text = text
            scr.ids.speed_btn.disabled = False
            scr.ids.speed_btn.text = "Mulai Tes"
        finally:
            self._speed_testing = False

    # ------------------------------------------------------------ APK Inspector
    def apk_inspector_pick(self):
        FilePicker(start=self._last_dir(), title="Pilih APK", mode="file", exts=[".apk"],
                   callback=self._apk_inspect).open()

    def _apk_inspect(self, path):
        scr = self.root.get_screen("apkinspector")
        try:
            size = os.path.getsize(path)
            lines = [f"Nama: {os.path.basename(path)}", f"Ukuran: {fmt_bytes(size)}", ""]
            with zipfile.ZipFile(path) as z:
                infos = z.infolist()
                names = [i.filename for i in infos]
                dex = [n for n in names if n.lower().endswith(".dex")]
                libs = [n for n in names if n.lower().endswith(".so")]
                assets = [n for n in names if n.startswith("assets/")]
                res = [n for n in names if n.startswith("res/")]
                certs = [n for n in names if n.upper().startswith("META-INF/") and (n.upper().endswith(".RSA") or n.upper().endswith(".DSA") or n.upper().endswith(".EC"))]
                manifest = "AndroidManifest.xml" in names
                lines += [
                    "Struktur APK:",
                    f"Entri total: {len(infos)}",
                    f"AndroidManifest.xml: {'Ada' if manifest else 'Tidak ada'}",
                    f"DEX: {len(dex)} ({', '.join(dex[:5]) or '-'})",
                    f"Library native (.so): {len(libs)}",
                    f"Assets: {len(assets)}",
                    f"Resource res/: {len(res)}",
                    f"Sertifikat META-INF: {len(certs)}",
                    "",
                    "File penting:",
                ]
                important = [n for n in names if n == "AndroidManifest.xml" or n.endswith("classes.dex") or n.startswith("lib/")]
                lines += important[:100] or ["(tidak ditemukan)"]
                lines += ["", "Catatan: AndroidManifest.xml pada APK biasanya memakai format AXML biner, jadi nama package/permission belum didekode di versi ini."]
            scr.ids.apk_inspect_output.text = "\n".join(lines)
            self.show_toast("APK selesai diinspeksi")
        except zipfile.BadZipFile:
            scr.ids.apk_inspect_output.text = "File ini bukan APK/ZIP yang valid."
        except Exception as e:
            scr.ids.apk_inspect_output.text = f"Gagal membaca APK:\n{e}"

    # ------------------------------------------------------------ Checksum File
    def checksum_pick_file(self):
        FilePicker(start=self._last_dir(), title="Pilih file", mode="file",
                   callback=self._checksum_compute).open()

    def _checksum_compute(self, path):
        scr = self.root.get_screen("checksum")
        scr.ids.cks_chip.path = os.path.basename(path.rstrip(os.sep)) or path
        box = scr.ids.cks_list
        box.clear_widgets()
        try:
            md5, sha1, sha256 = hashlib.md5(), hashlib.sha1(), hashlib.sha256()
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(65536), b""):
                    md5.update(chunk)
                    sha1.update(chunk)
                    sha256.update(chunk)
        except Exception as e:
            self.show_toast(f"Gagal membaca file: {e}")
            return
        for label, value in (("MD5", md5.hexdigest()), ("SHA1", sha1.hexdigest()), ("SHA256", sha256.hexdigest())):
            row = ListRow(icon="pound", title=label, subtitle=value, trailing="content-copy", boxed=True)
            row.bind(on_release=lambda w, v=value, l=label: self.copy_text(v, f"{l} disalin"))
            box.add_widget(row)
        self.show_toast("Checksum dihitung")

    # ------------------------------------------------------------ Log Viewer
    def refresh_log_viewer(self):
        scr = self.root.get_screen("logviewer")
        parts = ["[b]Build[/b]", escape_markup(self.LOG_TEXT)]
        if getattr(self, "_pip_lines", None):
            parts += ["", "[b]Installer[/b]", "\n".join(escape_markup(x) for x in self._pip_lines)]
        if getattr(self, "_term_history", None):
            recent = "\n".join(escape_markup(c) for c in list(self._term_history)[-20:])
            parts += ["", "[b]Perintah Terminal[/b]", recent]
        scr.ids.logv_text.text = "\n".join(parts).strip()

    # ------------------------------------------------------------ Riwayat Perintah Terminal
    def refresh_term_history(self):
        scr = self.root.get_screen("termhistory")
        box = scr.ids.termhist_list
        box.clear_widgets()
        hist = list(self._term_history)
        if not hist:
            box.add_widget(Factory.T4(text="Belum ada perintah yang dijalankan."))
            return
        for cmd in reversed(hist[-50:]):
            row = ListRow(icon="console-line", title=cmd, subtitle="Ketuk untuk pakai lagi", boxed=True)
            row.bind(on_release=lambda w, c=cmd: self.reuse_term_command(c))
            box.add_widget(row)

    def reuse_term_command(self, cmd):
        scr = self.root.get_screen("terminal")
        if "term_input" in scr.ids:
            scr.ids.term_input.text = cmd
        self.goto("terminal")
    def on_setting(self, name):
        """[MUDAH] Info singkat untuk item Pengaturan yang belum punya layar sendiri."""
        messages = {
            "bahasa": "Saat ini hanya tersedia Bahasa Indonesia",
            "penyimpanan": "Penyimpanan: Internal",
            "framework": "Framework default: KivyMD",
            "arsitektur": "Arsitektur default: ARM64",
            "python": "Versi Python: 3.11",
            "tentang": "MyTools v1.0.0 - dibuat dengan Kivy & KivyMD",
        }
        self.show_toast(messages.get(name, "Pengaturan ini belum tersedia"))


if __name__ == "__main__":
    MyToolsApp().run()
