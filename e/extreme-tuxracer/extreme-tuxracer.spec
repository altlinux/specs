%define _name etr

Name: extreme-tuxracer
Version: 0.7.4
Release: alt1
Epoch: 1

Summary: High speed arctic racing game based on Tux Racer
Group: Games/Arcade
License: GPL
Url: https://sourceforge.net/projects/extremetuxracer/

Source: https://downloads.sourceforge.net/extremetuxracer/etr-0.7.4.tar.xz

Obsoletes: %name <= 0.35
Requires: %name-data = %EVR

# Automatically added by buildreq on Fri Feb 03 2017
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

%files data
%_desktopdir/%_name.desktop
%_pixmapsdir/*
%_datadir/%_name/
%_datadir/doc/%_name/

%changelog
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

