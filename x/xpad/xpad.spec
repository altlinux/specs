Name: xpad
Version: 4.6.0
Release: alt1

Summary: F virtual sticky pad system using GTK+-3
Group: Office
License: GPLv3+

URL: https://launchpad.net/xpad
Source0: http://launchpad.net/xpad/trunk/%version/+download/xpad-%version.tar.bz2

BuildRequires: intltool libgtksourceview3-devel >= 3.10 at-spi2-atk-devel
BuildRequires: libSM-devel
BuildRequires: desktop-file-utils

%description
Xpad is a sticky note application that strives to be simple, fault-tolerant,
and customizable. It consists of independent pad windows; each is basically
a text box in which notes can be written.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/xpad.desktop

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_sysconfdir/xdg/autostart/%name.desktop
%doc README NEWS ChangeLog TODO

%changelog
* Sun Feb 28 2016 Yuri N. Sedunov <aris@altlinux.org> 4.6.0-alt1
- 4.6.0

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 4.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xpad

* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 4.1-alt2
- Fix glib include compile problem.

* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 4.1-alt1
- 4.1

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 4.0-alt2_8
- update to new release by fcimport

* Sun Aug 14 2011 Igor Vlasenko <viy@altlinux.ru> 4.0-alt2_7
- initial release by fcimport

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 4.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xpad

* Fri Nov 20 2009 Victor Forsyuk <force@altlinux.org> 4.0-alt1
- 4.0

* Tue Oct 10 2006 Serge Polkovnikov <robin@altlinux.ru> 2.12-alt1
- bug fix release
- remove obsolete russian translation
- add ukrainian translation

* Mon Feb 27 2006 Serge Polkovnikov <robin@altlinux.ru> 2.11-alt1
- initial build for Sisyphus
