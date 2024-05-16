%define _name etr

Name: extreme-tuxracer
Epoch: 1
Version: 0.8.4
Release: alt1

Summary: High speed arctic racing game based on Tux Racer

Group: Games/Arcade
License: GPL-2.0
Url: https://sourceforge.net/projects/extremetuxracer/

Source: %_name-%version.tar.xz

Requires: %name-data = %EVR

BuildRequires: libappstream-glib-devel
BuildRequires: gcc-c++ libGLU-devel libSFML-devel

%description
Extreme Tux Racer is an open source racing game featuring
Tux the Linux Penguin. ETRacer continues in the tracks of Tux Racer
and its forks.

%package data
Summary: Arch independent files for Extreme Tux Racer
Group: Games/Arcade
BuildArch: noarch

%description data
This package provides noarch data needed for Extreme Tux Racer to work.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/net.sourceforge.extremetuxracer.desktop

%files data
%_pixmapsdir/*
%_datadir/%_name
%_datadir/doc/%_name
%_datadir/metainfo/net.sourceforge.extremetuxracer.metainfo.xml

%changelog
* Thu May 16 2024 Grigory Ustinov <grenka@altlinux.org> 1:0.8.4-alt1
- Build new version.

* Tue Jul 18 2023 Grigory Ustinov <grenka@altlinux.org> 1:0.8.3-alt1
- Build new version.

* Sat Jun 25 2022 Grigory Ustinov <grenka@altlinux.org> 1:0.8.2-alt1
- Build new version.

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 1:0.8.1-alt1
- Build new version.

* Thu Sep 10 2020 Grigory Ustinov <grenka@altlinux.org> 1:0.8.0-alt1
- Build new version.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 1:0.7.5-alt4
- Fix license.

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 1:0.7.5-alt3
- Rebuilt with new SFML

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 1:0.7.5-alt2
- Add desktop file (Closes: #26342).

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.7.5-alt1
- 0.7.5

* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.7.4-alt2
- rebuilt with gcc7

* Fri Feb 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.7.4-alt1
- 0.7.4 (new url)
- updated buildreqs
- new -data subpackage

* Thu Sep 20 2012 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.svn254.1
- last snapshot
    + rebuild with libpng15

* Fri May 14 2010 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.svn197.1
- 8 month old bleeding edge svn snapshot, don't be afraid - it's playable

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.beta.1
- new beta

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4-alt0.2.1
- NMU:
  * updated build dependencies
  
* Mon Sep 15 2008 Alex Karpov <karpov@altlinux.ru> 1:0.4-alt0.2
- updated biuld requirements

* Tue Mar 18 2008 Alex Karpov <karpov@altlinux.ru> 1:0.4-alt0.1
- 0.4

* Thu Oct 04 2007 Alex Karpov <karpov@altlinux.ru> 0.35-alt0.1
- try to fix x86_64 build

* Mon Oct 01 2007 Alex Karpov <karpov@altlinux.ru> 0.35-alt0
- initial build for Sisyphus

