%def_disable snapshot
%def_enable qt6
# enable/disable JACK version support
%def_enable jack_version
%def_enable portaudio

%define rdn_name org.rncbc.qjackctl

Name: qjackctl
Version: 0.9.9
Release: alt1

Summary: Qjackctl is a programm to control the JACK sound server daemon
Summary(ru_RU.UTF-8): Qjackctl -- это программа для контроля над демоном JACK-сервера
Group: Sound
License: GPL-2.0-or-later
Url: https://%name.sourceforge.net

%if_enabled snapshot
Vcs: https://github.com/rncbc/qjackctl.git
Source: %name-%cvsdate.tar
%else
Source: https://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
%endif

%define jack_ver 0.118
Requires: jackd >= %jack_ver

BuildRequires(pre): rpm-macros-cmake
BuildRequires: jackit-devel >= %jack_ver
BuildRequires: cmake gcc-c++ libalsa-devel
%{?_enable_portaudio:BuildRequires: pkgconfig(portaudio-2.0)}
BuildRequires: libX11-devel libXext-devel
%if_enabled qt6
BuildRequires: qt6-base-devel qt6-tools-devel qt6-svg-devel
%else
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools-devel
%endif

%description
Qjackctl -- is an easy to use GUI to low-latency JACK audio server. You
can change options of starting JACK, assign scripts to be executed on
start/stop of the server, connect/disconnect loaded JACK clients and
route MIDI inputs'outputs.

%description -l ru_RU.UTF-8
Qjackctl -- это удобная программа с графическим интерфейсом для
управления звуковым сервером JACK. С её помощью можно изменять параметры
запуска сервера, указывать сценарии, запускаемые после старта сервера, а
также коммутировать звуковые и MIDI входы и выходы подключенных
JACK-клиентов.

%prep
%setup -n %name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    %{?_enable_jack_version:-DCONFIG_JACK_VERSION=ON} \
    %{?_disable_portaudio:-DCONFIG_PORTAUDIO=OFF}
%nil
%cmake_build

%install
%cmake_install

%find_lang --with-qt --with-man --all-name --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_iconsdir/hicolor/*/*/*.*
%_man1dir/*
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc ChangeLog README

%changelog
* Wed Dec 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Sun Apr 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- 0.9.7

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6
- build against qt6 libraries

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

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

* Sat Jul 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- 0.5.9

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Mon Nov 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Dec 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Thu Sep 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Mon Feb 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Jul 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Oct 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- 0.3.12

* Fri Jan 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11

* Mon Apr 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Mon May 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Fri Oct 02 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5 (closes #21809)

* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4 release
- removed obsolete %%{update,clean}_menus
- updated {build,}reqs

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.2.20.17-alt0.cvs20060910
- CVS snapshot 2006-09-10.

* Tue Apr 04 2006 LAKostis <lakostis at altlinux.ru> 0.2.20-alt1
- 0.2.20.
- cleanup buildreq.

* Wed Aug 10 2005 LAKostis <lakostis at altlinux.ru> 0.2.18-alt1
- NMU.
- 0.2.18.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.15-alt1
- 0.2.15.

* Mon Jan 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.14-alt1
- 0.2.14.

* Tue Nov 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.13-alt1
- 0.2.13

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.11-alt1
- 0.2.11

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.9-alt0.5
- 0.2.9

* Wed May 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.8-alt0.5
- 0.2.8

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.5-alt0.5
- 0.2.5

* Tue Jan 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt0.5a
- 0.2.3a

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- 0.2.1

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt0.5
- 0.2.0

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt0.5
- 0.1.2

* Thu Oct 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt0.5
- 0.1.0

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.9-alt0.5
- 0.0.9

* Sat Sep 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.6-alt0.5
- 0.0.6

* Sat Sep 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.5-alt0.5
- 0.0.5

* Sat Aug 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.4-alt0.5
- 0.0.4

* Fri Aug 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.3-alt0.5
- First build for Sisyphus.
- russian summary, description by avp.
