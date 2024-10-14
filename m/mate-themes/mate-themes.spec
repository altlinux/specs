Name: mate-themes
Version: 3.22.26
Release: alt2
Epoch: 1
Summary: MATE Desktop themes
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-icon-theme libgtk-engines-default libgtk-engine-murrine

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common glib2-devel pkgconfig(gtk+-2.0) pkgconfig(gdk-pixbuf-2.0)

%description
MATE Desktop themes

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README ChangeLog
%_datadir/themes/*
%_iconsdir/*

%changelog
* Thu Oct 10 2024 Leonid Krivoshein <klark@altlinux.ru> 1:3.22.26-alt2
- Fix for displaying LibreOffice autofilter window

* Tue Apr 09 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.26-alt1
- 3.22.26

* Mon May 15 2023 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.24-alt1
- 3.22.24

* Mon Sep 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.23-alt1
- 3.22.23

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.21-alt1
- 3.22.21

* Tue Dec 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.20-alt1
- 3.22.20

* Mon Mar 11 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.19-alt1
- 3.22.19

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.18-alt1
- 3.22.18

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.17-alt1
- 3.22.17

* Fri Mar 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.16-alt1
- 3.22.16

* Fri Mar 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.15-alt1
- initial build from git.mate-desktop.org

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.22.14-alt1_2
- new fc release

