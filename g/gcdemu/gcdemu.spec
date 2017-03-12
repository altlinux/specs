Summary: GTK+ based GUI for controlling CDEmu daemon
Summary(ru_RU.UTF-8): Основанная на GTK+ GUI для управления CDEmu
Name: gcdemu
Version: 3.0.2
Release: alt2
Group: Emulators
License: GPLv2+
Url: http://cdemu.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
Patch1: autostart.patch
Patch2: enabled_ru_translation.patch
Patch3: fix_desktop.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake intltool rpm-build-gir
Requires: cdemu-daemon cdemu-client
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
gCDEmu - базирующийся на Gtk+ и Appindicator апплет в области уведомлений для
управления службой CDEmu. Является частью проекта CDEmu, свободного (GPL)
эмулятора устройств CD/DVD-ROM для Линукс.

Обеспечивает графический интерфейс, который позволяет выполнять основные задачи,
связанные с управлением службой CDEmu, например монтирование и размонтирование
образов, отображение статуса виртуальных устройств CD/DVD-ROM.

Кроме того, он слушает сигналы, посылаемые службой CDEmu и обеспечивает вывод
уведомлений, используя библиотеку libnotify.

%prep
%setup
%patch1 -p1
%patch2
%patch3 -p2

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot/%_sysconfdir/xdg/autostart/
mv %buildroot/%_desktopdir/%name.desktop %buildroot/%_sysconfdir/xdg/autostart/

%files -f %name.lang
%doc README AUTHORS
%_bindir/%name
%_pixmapsdir/gcdemu*.svg
%_datadir/glib-2.0/schemas/net.sf.cdemu.gcdemu.gschema.xml
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt2
- Added buildrequires rpm-build-gir.

* Fri Oct 14 2016 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt1
- New version.

* Fri Sep 23 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt3
- Fix requires (Closes: 32518).

* Sun Apr 03 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt2
- Added russian translation of git
- fix desktop file

* Thu Jan 14 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- New version;
- Added russian translation.

* Sun Oct 18 2015 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt2
- Added autostart.patch;
- Added requires: cdemu-client.

* Mon Sep 21 2015 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus.
