Name: gsmartcontrol
Version: 1.1.4
Release: alt1

Summary: GSmartControl - Hard disk drive and SSD health inspection tool
Group: Monitoring
License: GPL-2.0 or GPL-3.0
Url: https://gsmartcontrol.sourceforge.io/home/

Source: http://download.sourceforge.net/%name/%name-%version.tar.bz2
Patch1: gsmartcontrol-0.8.7-alt-lfs.patch

Requires: smartmontools >= 5.43 polkit

BuildRequires: gcc-c++ libgtkmm3-devel >= 3.4.0 libpcrecpp-devel libappstream-glib-devel

%description
GSmartControl is a graphical user interface for smartctl (from
Smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART data
to determine its health, as well as run various tests on it.

%prep
%setup
%patch1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_sbindir/%name
%_bindir/%name-root
%_datadir/%name/
%_datadir/polkit-1/actions/org.%name.policy
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/*.1*
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/pixmaps/gsmartcontrol.*
%_defaultdocdir/%name/
%exclude %_defaultdocdir/%name/LICENSE*

%changelog
* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Thu Apr 16 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt2
- removed obsolete gksu from dependencies
- changed Group tag to Monitoring
- fixed License tag

* Sat Nov 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Fri Oct 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Jun 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0 (ported to GTK+3)

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt2
- applied gsmartcontrol_parser_crash_fix.diff from upstream
- built with newer *mm libraries

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.7-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Oct 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7
- spec cleanup

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.1
- Fixed build with glibc 2.16 & gcc 4.7

* Thu May 03 2012 Mikhail Pokidko <pma@altlinux.org> 0.8.6-alt2
- fixed build with glib 2.31

* Tue Aug 23 2011 Mikhail Pokidko <pma@altlinux.org> 0.8.6-alt1
- version up

* Thu Nov 19 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.5-alt1
- Version up

* Wed Jun 10 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.4-alt1
- Version up. Fixed build errors.

* Fri Mar 13 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- Initial build

