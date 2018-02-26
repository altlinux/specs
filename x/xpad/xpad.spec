Name: xpad
Version: 4.1
Release: alt2

Summary: Sticky notepad for GTK+2
License: GPLv3+
Group: Office

URL: https://launchpad.net/xpad
Source0: http://launchpad.net/xpad/trunk/%version/+download/xpad-%version.tar.bz2

# Automatically added by buildreq on Mon Jan 09 2012
BuildRequires: imake intltool libSM-devel libgtk+2-devel xorg-cf-files

%description
Xpad is a sticky note application that strives to be simple, fault-tolerant, 
and customizable. It consists of independent pad windows; each is basically a 
text box in which notes can be written. Despite being called xpad, all that is
needed to run or compile it is the GTK+ 2.0 libraries.

%prep
%setup

subst "/include <glib\/glist.h>/d" src/xpad-undo.c

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%changelog
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
