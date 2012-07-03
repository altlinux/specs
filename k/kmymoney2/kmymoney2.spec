%set_verify_elf_method unresolved=relaxed

Name: kmymoney2
Version: 1.0.5
Release: alt3

Summary: A personal finance manager for KDE
Summary(ru_RU.UTF-8): Учёт финансов под KDE
License: GPL
Group: Office
URL: http://kmymoney2.sourceforge.net/index-home.html

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: kmymoney2-%version.tar.bz2
Patch0: fix-missing-headers.patch

AutoReq: yes, noperl

%set_automake_version 1.10

BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++
BuildRequires: libqt3-devel libjpeg-devel 
BuildRequires: libofx-devel >= 0.9.0 libOpenSP-devel
BuildRequires: libxml2-devel libxml++2-devel libcurl-devel libsqlite3-devel
BuildRequires: chrpath
Requires: lib%name = %version-%release
Requires: %name-i18n
Provides: %name = %version-%release

%description
KMyMoney2 provides a simple but functional personal finance
manager for KDE.
For the most up-to-date information and sources please
use the CVS repository available at http://kmymoney2.sourceforge.net/.

%package -n lib%name
Summary: Shared libraries for KMyMoney2
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
This package provides shared libraries for KMyMoney2 application.

%package devel
Summary: Header files for %name plugin development
Group: Development/KDE and QT
Requires: kmymoney2

%description devel
Header files for %name plugin development

%package i18n
Summary: Internationalization and documentation for %name
Group: System/Internationalization 
Requires: %name = %version-%release
BuildArch: noarch

%description i18n
Internationalization and documentation for %name

%prep
%setup -q -n %name-%version
subst "s/\.la/.so/g" ./configure
subst "s/kmymoneytitlelabel.png//" ./kmymoney2/widgets/Makefile.*
%patch0 -p2
rm -f po/*.gmo

%build
%add_optflags -I%_includedir/tqtinterface
export PATH=%_K3bindir:$PATH
%configure \
	--with-qt-libraries=%_libdir/qt3/lib \
	--enable-qtdesigner \
	--enable-ofxplugin \
	--enable-ofxbanking \
	--enable-new-ldflags \
	--without-arts \
	--disable-debug \
	--prefix=%_K3prefix \
	--bindir=%_K3bindir \
	--exec-prefix=%_K3prefix \
	--datadir=%_K3datadir \
	--includedir=%_K3includedir
%make_build

%install
%K3install
%K3find_lang --with-kde --with-man %name
rm -f %buildroot%_K3lib/*.la
chrpath -d %buildroot%_K3lib/kmm_ofximport.so

%files
%doc README README.Fileformats AUTHORS TODO INSTALL COPYING
%doc %_K3doc/en/%name/
%_K3bindir/*
%_K3apps/%name/templates/C
%_K3apps/%name/html/home.html
%_K3apps/%name/html/images/
%_K3apps/%name/html/kmymoney2.css
%_K3apps/%name/html/welcome.css
%_K3apps/%name/html/whats_new.html
%_K3apps/%name/icons
%_K3apps/%name/pics
%_K3apps/%name/misc
%_K3apps/%name/kmymoney2ui.rc
%_K3apps/%name/tips
%_K3mimelnk/application/*
%_K3srv/*.desktop
%_K3srvtyp/*
%_K3xdg_apps/*
%_K3apps/kmm_ofximport/kmm_ofximport.rc
%_K3cfg/%name.kcfg
%_kde3_iconsdir/hicolor/*/*/*.png
%_iconsdir/*/*/*/*.png
%_iconsdir/*/scalable/*.svgz
%_kde3_iconsdir/locolor/*/apps/*
%_kde3_iconsdir/locolor/32x32/apps/*

%files -n lib%name
%_K3libdir/*.so*
%_K3lib/*.so
%_K3libdir/qt3/plugins/designer/*.so

%files devel
%dir %_K3includedir/kmymoney
%_K3includedir/kmymoney/*.h

%files i18n -f %name.lang
%_K3apps/%name/templates/*
%exclude %_K3apps/%name/templates/C
%_K3apps/%name/html/home_*.html
%_K3apps/%name/html/whats_new_*.html
%exclude %_K3doc/en/%name/

%changelog
* Tue Feb 21 2012 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt3
- Remove standard library path from library RPATH

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt2
- Move to alterante place

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version 1.0.5

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt3
- Fix build

* Thu Jan 20 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Fix missing headers

* Wed Mar 31 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version 1.0.4 

* Mon Nov 23 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- version 1.0.2 
- remove Vendor tag
- extract architecture-independent i18n subpackage

* Fri Sep 18 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Version 1.0.1 

* Wed Sep 02 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- Remove unnecessary aqbanking devel requirement 

* Wed Sep 02 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- Fix Russian translations (see http://forum.kde.org/viewtopic.php?f=69&t=76926) 

* Fri Aug 21 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- new version 1.0.0 

* Fri Aug 07 2009 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt3
- Completely translate application interface on Russian
- Really fix content of russian account template

* Mon Feb 16 2009 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt2
- Fix russian account template (bug #18833) 
- Remove deprecated update-desktop-database, update-menus and ldconfig macros 

* Thu Sep 25 2008 Andrey Cherepanov <cas@altlinux.ru> 0.9.2-alt1
- new version 0.9.2

* Sun May 04 2008 Andrey Cherepanov <cas@altlinux.ru> 0.8.9-alt2
- Disable internal KBanking plugin (see http://sourceforge.net/project/shownotes.php?group_id=4708&release_id=586664)

* Wed Apr 02 2008 Andrey Cherepanov <cas@altlinux.ru> 0.8.9-alt1
- Version 0.8.9
- Fix Exec= value according Freedesktop.org standard in desktop file

* Fri Feb 08 2008 Andrey Cherepanov <cas@altlinux.ru> 0.8.8-alt1
- Fix build number for branch

* Tue Dec 25 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8.8-alt0
- Version 0.8.8

* Fri Oct 12 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8.7-alt0
- Version 0.8.7

* Fri May 25 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8.6-alt4
- Fix Russian translation.
- Separated package:
  + lib%name: libraries

* Thu May 10 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8.6-alt3
- Fix build (update menus). Fix requires for kmymoney2-devel.

* Mon May 07 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8.6-alt2
- New version
- Fix Russian translation and template

* Mon Jan 29 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt1
- New version (cvs20070129)

* Wed Oct 25 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5-alt1
- New version
- Spec cleanups
- Developement files are in the devel package now

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 0.8-alt0
- first build for ALT

* Sat Jul 30 2005 <ch.nolte@fh-wolfenbuettel.de>
- Version 0.7.5

* Mon Jul 25 2005 <ch.nolte@fh-wolfenbuettel.de>
- Update for version 0.7.4
- CVS-Version 0.7.5

* Sat Jul 9 2005 <ch.nolte@fh-wolfenbuettel.de>
- migrated to Fedora Core 4
- added gpg-patch

* Thu Jan 9 2003 - ipwizard (at) user.sourcforge.net
- Added missing files home.html and kmymoney2.css

* Mon Dec 16 2002 - ipwizard (at) user.sourcforge.net
- Removed make command only required for CVS download
- Update version to match filename

* Sun Dec 15 2002 - ipwizard (at) user.sourcforge.net
- Updated for version 0.51

* Tue Jan 15 2002 - ipwizard (at) user.sourcforge.net
- Initial implementation
