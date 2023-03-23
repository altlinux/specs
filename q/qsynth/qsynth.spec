%def_enable qt6

%define rdn_name org.rncbc.qsynth

Name: qsynth
Version: 0.9.10
Release: alt1

Summary: QSynth is a GUI front-end for FluidSynth
Summary(ru_RU.UTF-8): QSynth - это графическая надстройка над FluidSynth
Group: Sound
License: GPL-2.0-or-later
Url: https://%name.sourceforge.net

Vcs: https://github.com/rncbc/qsynth.git
Source: https://prdownloads.sourceforge.net/%name/%name-%version.tar.gz

Requires: fluidsynth

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ladspa_sdk libfluidsynth-devel libXext-devel
%if_enabled qt6
BuildRequires: qt6-tools-devel qt6-tools-devel qt6-svg-devel
%else
BuildRequires: qt5-tools-devel qt5-x11extras-devel
%endif

%description
QSynth is a fluidsynth GUI front-end application. Eventually it may
evolve into a softsynth management application allowing the user to
control and manage a variety of command line softsynth but for the
moment it wraps the excellent Fluidsynth. Fluidsynth is a command line
software synthesiser based on the Soundfont specification.

%description -l ru_RU.UTF-8
QSynth -- это графическая надстройка над FluidSynth. В будущем
программа может превратиться в универсальный фронт-энд для многих
других синтезаторов, работающих из командной строки, но пока
используется только FluidSynth. FluidSynth же, в свою очередь,
является программным синтезатором на основе спецификаций SoundFont 2.

%define qtdir %_libdir/qt4

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake
%cmake_build

%install
%cmake_install
%find_lang --with-qt --with-man --all-name --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/*/*.*
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/metainfo/%rdn_name.metainfo.xml
%_man1dir/%name.1.*
%doc ChangeLog README

%changelog
* Thu Mar 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1
- 0.9.10

* Wed Dec 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Sun Apr 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- 0.9.7

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5
- build against qt6 libraries

* Mon Jul 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4 (ported to CMake build system)

* Wed May 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Sun Feb 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Dec 18 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Sat Aug 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Dec 23 2019 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Oct 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sat Jul 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt2
- rebuilt against libfluidsynth.so.2

* Fri Dec 28 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Dec 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Sep 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Apr 05 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1 with qt5

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Tue Dec 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

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
