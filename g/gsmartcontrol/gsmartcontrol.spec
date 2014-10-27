Name: gsmartcontrol
Version: 0.8.7
Release: alt1

Summary: GSmartControl is a graphical user interface for smartctl
Group: Graphical desktop/Other
License: GPL
Url: http://gsmartcontrol.sourceforge.net/home/

Source: %name-%version.tar.bz2
Patch: gsmartcontrol-0.8.6-alt-glibc-2.16.patch
Patch1: gsmartcontrol-0.8.7-alt-lfs.patch

Requires: smartmontools

BuildRequires: libgtkmm2-devel gcc-c++ libpcre-devel gksu

%description
GSmartControl is a graphical user interface for smartctl (from
Smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART data
to determine its health, as well as run various tests on it.

%prep
%setup
%patch -p2
%patch1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_defaultdocdir/%name
%_bindir/*
%_datadir/%name/*
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/*.1*
%_desktopdir/%name.desktop

%exclude %_datadir/pixmaps/gsmartcontrol.*

%changelog
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

