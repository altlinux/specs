Name: qsynth
Version: 0.3.6
Release: alt1

Summary: QSynth is a GUI front-end for FluidSynth
Summary(ru_RU.KOI8-R): QSynth - это графическая надстройка над FluidSynth
Group: Sound
License: GPL
Url: http://%name.sourceforge.net

Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz

Requires: fluidsynth

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ ladspa_sdk libfluidsynth-devel libqt4-devel libXext-devel

%description
QSynth is a fluidsynth GUI front-end application. Eventually it may
evolve into a softsynth management application allowing the user to
control and manage a variety of command line softsynth but for the
moment it wraps the excellent Fluidsynth. Fluidsynth is a command line
software synthesiser based on the Soundfont specification.

%description -l ru_RU.KOI8-R
QSynth -- это графическая надстройка над FluidSynth. В будущем 
программа может превратиться в универсальный фронт-энд для многих 
других синтезаторов, работающих из командной строки, но пока 
используется только FluidSynth. FluidSynth же, в свою очередь, 
является программным синтезатором на основе спецификаций SoundFont 2.

%define qtdir %_libdir/qt4

%prep
%setup -q

# move translations to proper locations
subst 's@share/locale@share/qsynth/locale@g' Makefile* src/CMakeLists.txt src/%name.cpp

%build
export QTDIR=%qtdir
export PATH=%qtdir/bin:$PATH
%configure

# SMP-incompatible build
%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%name
%_datadir/applications/*
%_iconsdir/hicolor/*/*/*.png
%_datadir/%name/*
%doc AUTHORS ChangeLog README TODO

%changelog
* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- new version

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3
- updated buildreqs

* Mon May 15 2006 Mikhail Yakshin <greycat@altlinux.org> 0.2.5-alt1
- 0.2.5

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.1-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- 0.2.1

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt0.5
- 0.1.2

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt0.5
- 0.1.0

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.3-alt0.5
- 0.0.3

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.2-alt0.5
- new version.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.1-alt0.5
- First build for Sisyphus.
- summary, description by avp.
