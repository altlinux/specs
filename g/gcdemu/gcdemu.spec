Summary: GTK+ based GUI for controlling CDEmu daemon
Summary(ru_RU.UTF-8): Основанная на GTK+ GUI для управления CDEmu
Name: gcdemu
Version: 3.0.0
Release: alt1
Group: Emulators
License: GPLv2+
Url: http://cdemu.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake intltool
Requires: cdemu-daemon python-module-notify python-module-appindicator
BuildArch: noarch

%description
gCDEmu is a Gtk+ based GUI for controlling CDEmu daemon. It is part of the
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux.

It provides a graphic interface that allows performing the key tasks related to
controlling the CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting devices' debug masks.

In addition, it listens to signals emitted by CDEmu daemon and provides
notifications via libnotify.

%description -l ru_RU.UTF-8
gCDEmu -  базирующаяся на Gtk+ программа с графическим интерфейсом для
управления службой CDEmu. Является частью проекта CDEmu, свободного (GPL)
эмулятора устройства CD/DVD-ROM для Линукс. 

Обеспечивает графический интерфейс, который позволяет выполнять основные задачи,
связанные с управления службой CDEmu, например монтирование и отмонтирование
образов, отображение статуса виртуальных устройств CD/DVD-ROM.

Кроме того, он слушает сигналы, посылаемые службой CDEmu и обеспечивает вывод
уведомлений, используя библиотеку libnotify.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name
install -d -m755 %buildroot/%_sysconfdir/xdg/autostart/
install -m644 %buildroot/%_desktopdir/%name.desktop %buildroot/%_sysconfdir/xdg/autostart/

%files -f %name.lang
%doc README AUTHORS
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/gcdemu*.svg
%_datadir/glib-2.0/schemas/net.sf.cdemu.gcdemu.gschema.xml
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Mon Sep 21 2015 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus.
