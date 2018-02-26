Name: pyro
Version: 1.5
Release: alt6

Summary: Pyrotechnics, an OpenGL-based firework simulator.
License: GPL
Group: Toys

Url: http://nostatic.org/pyro
Source: %url/%name-%version.tgz
Patch0: pyro-nomesa.patch.bz2
Patch1: pyro-1.5-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): OpenGL-пиротехника
Summary(uk_UA.KOI8-U): OpenGL-п╕ротехн╕ка

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: libGL-devel libXext-devel libXi-devel libXmu-devel libfreeglut-devel libjpeg-devel

%description
PyroTechnics is an OpenGL-based firework simulator. Features include
multiple kinds of fireworks, the ability to choreograph firework displays, a
texture-mapped water surface, reflections, a moving camera, and the ability
to save screenshots.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
%makeinstall "PREFIX=%buildroot%_usr"

%files
%doc README CHANGES
%_bindir/pyro
%_datadir/pyro/pyro.dsp
%_datadir/pyro/water.jpg

%changelog
* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 1.5-alt6
- buildreq

* Mon Sep 08 2008 Michael Shigorin <mike@altlinux.org> 1.5-alt5
- buildreq

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 1.5-alt4
- buildreq

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 1.5-alt3
- fixed x86_64 build (noarch data moved from lib/ to share/)

* Fri Aug 22 2003 Michael Shigorin <mike@altlinux.ru> 1.5-alt2
- %%url updated

* Mon Oct 14 2002 Michael Shigorin <mike@altlinux.ru> 1.5-alt1.1
- built with gcc3.2
- BuildRequires updated

* Sat Mar 30 2002 Michael Shigorin <mike@altlinux.ru> 1.5-alt1
- built for ALT Linux

