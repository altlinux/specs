Name: gnusim8085
Version: 1.3.7
Release: alt1

Summary: Simulator and assembler for the Intel 8085 Microprocessor

License: GPL
Group: Emulators
Url: http://gnusim8085.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source:  http://launchpad.net/%name/trunk/%version/+download/%name-%version.tar.gz
Patch: gnusim8085-1.3.7-desktop.patch

BuildRequires: libSM-devel libgtk+2-devel libgio-devel libgtksourceview-devel

Obsoletes: GNUSim8085
Provides: GNUSim8085

%description
GNUSim8085 is a graphical simulator plus assembler with debugger for the
Intel 8085 microprocessor. It is written using GNOME libs. It can also
run on several window managers.

%prep
%setup -q
%patch

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%_datadir/doc/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man1dir/%name.1.*

%changelog
* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 1.3.7-alt1
- 1.3.7
- updated buildreqs
- spec cleanup

* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1.qa3
- NMU: second cleanup of .desktop files

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1.qa2
- NMU: .desktop file cleanup

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gnusim8085
  * postclean-05-filetriggers for spec file

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (with rpmrb script)
- enable update/clean menus scripts
- rename package to low case name
- update buildrequires

* Mon Jul 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.90-alt0.1
- initial build for ALT Linux Sisyphus
