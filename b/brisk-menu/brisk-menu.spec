%define _libexecdir %_prefix/libexec
Name: brisk-menu
Version: 0.5.0
Release: alt1

Summary: An efficient menu for the MATE Desktop
Summary(ru_RU.UTF-8): Эффективное меню для MATE Desktop

License: GPLv2+
Group: Graphical desktop/MATE
Url: https://github.com/solus-project/brisk-menu

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: libgio-devel pkgconfig(gdk-x11-3.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-3.0) pkgconfig(x11) pkgconfig(libmate-menu) pkgconfig(libmatepanelapplet-4.0) pkgconfig(libnotify) meson

%description
Modern, efficient menu for the MATE Desktop Environment.
Features:
- Keyboard centric (mice welcome too, of course)
- Basic hotkey support (CTRL+F10) Needs fixing to support Super shortcut
- Stupid-fast
- Efficient, useful searching.
- Automatically reload
- Filter via categories
- Session/screensaver controls
- Drag & drop support for launchers
- GTK3
- Fully correct X11 WM integration (grab policy and window types)
- Not Python.


%description -l ru_RU.UTF-8
Современное, эффективное меню для окружения рабочего стола MATE.
Достоинства:
- Клавиатуро-ориентированный (мышь конечно же тоже приветствуется)
- Базовая поддержка горячих клавиш (CTRL+F10)
- Эффективный поиск
- Автоматическая перезагрузка
- Фильтры по категориям
- Управление сессией/скринсейвером
- Поддержка Drag & drop для лаунчера
- GTK3
- Полностью корректная интеграция с X11 WM (grab policy and window types)
- Не требует для своей работы Python.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc LICENSE* README.md
%_datadir/dbus-1/services/*.service
%_datadir/mate-panel/applets/*
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/scalable/actions/*
%_libexecdir/%name

%changelog
* Sun Dec 24 2017 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- new version 0.5.0
- switch to meson build

* Tue May 23 2017 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Fri Mar 31 2017 Anton Midyukov <antohami@altlinux.org> 0.3.5-alt1
- new version 0.3.5

* Sun Jan 29 2017 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Sat Jan 07 2017 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Sun Jan 01 2017 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt1
- Initial build for ALT Linux Sisyphus.
