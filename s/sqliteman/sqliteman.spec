Name: sqliteman
Version: 1.2.2
Release: alt1.qa3

Url: http://sqliteman.com/
License: GPL
Group: Databases

Summary: Lightweigth but powerfull Sqlite3 manager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar

# manually removed: libqt3-devel
# Automatically added by buildreq on Wed Dec 10 2008
BuildRequires: ccmake gcc-c++ libqscintilla2-qt4-devel libqt4-devel xorg-sdk

Requires: libqt4-sql-sqlite sqlite3
BuildRequires: desktop-file-utils

%description
The best developer's and/or admin's GUI tool for Sqlite3
in the world. No joking here (or just a bit only) - it
contains the most complette feature set of all tools available.

%prep
%setup

%build
%cmake
cd BUILD
%make_build

%install
cd BUILD
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Development \
	--add-category=Database \
	%buildroot%_desktopdir/sqliteman.desktop

%files
%_bindir/sqliteman
%_desktopdir/sqliteman.desktop
%_datadir/sqliteman/

%changelog
* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa3
- Rebuilt with qscintilla2 2.6

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa2
- Rebuilt with qscintilla2 2.5.1

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for sqliteman

* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- rebuild with new cmake macro, moved to git

* Sat Nov 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- rebuild (fix bug #21434)

* Tue Jul 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- cleanup spec

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Fri May 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- initial build for ALT Linux Sisyphus

* Wed Feb 20 2007 - Petr Vanek <petr@scribus.info>
- initial package
