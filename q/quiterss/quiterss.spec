Name: quiterss
Version: 0.17.1
Release: alt1

Summary: RSS/Atom aggregator
License: GPLv3
Group: Networking/WWW

Url: http://code.google.com/p/quite-rss/
Source: http://quite-rss.googlecode.com/files/QuiteRSS-%version-src.tar.bz2
Source44: import.info
Source45: quiterss.watch
BuildRequires: pkgconfig(QtGui) pkgconfig(QtNetwork) pkgconfig(QtWebKit) pkgconfig(QtXml) pkgconfig(QtSql)
BuildRequires: desktop-file-utils
BuildRequires: libqtsingleapplication-devel pkgconfig(sqlite3) pkgconfig(phonon)
Requires: libqt4-sql-sqlite

Summary(ru): QuiteRSS - быстрая и удобная программа для чтения новостных лент RSS/Atom

# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel
# END SourceDeps(oneline)

%description
Qt-based RSS/Atom aggregator.

%description -l ru
Быстрая и удобная программа для чтения новостных лент RSS/Atom,
написанная на Qt.

%prep
%setup -n QuiteRSS-%version-src
sed -i 's,qtsingleapplication.h,QtSolutions/&,' src/application/mainapplication.h
sed -i 's,phonon/audiooutput.h,kde4/&,' src/application/mainwindow.h
sed -i 's,phonon/mediaobject.h,kde4/&,' src/application/mainwindow.h

%build
qmake-qt4 PREFIX=%prefix SYSTEMQTSA=True
%make_build release

%install
make install INSTALL_ROOT=%buildroot
desktop-file-validate %buildroot%_desktopdir/%name.desktop
%find_lang %name --with-qt --without-mo

%files -f %name.lang
%doc AUTHORS CHANGELOG COPYING README
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/sound/
%_datadir/%name/style/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png
%dir %_datadir/%name/lang

%changelog
* Tue Nov 18 2014 Michael Shigorin <mike@altlinux.org> 0.17.1-alt1
- new version (watch file uupdate)

* Thu Oct 30 2014 Michael Shigorin <mike@altlinux.org> 0.17.0-alt2
- no need to fcimport it anymore

* Tue Sep 09 2014 Michael Shigorin <mike@altlinux.org> 0.17.0-alt1
- new version (watch file uupdate)

* Thu Aug 21 2014 Michael Shigorin <mike@altlinux.org> 0.16.2-alt1
- new version (watch file uupdate)

* Fri Jul 11 2014 Michael Shigorin <mike@altlinux.org> 0.16.1-alt1
- new version (watch file uupdate)

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 0.16.0-alt1
- new version (watch file uupdate)

* Tue May 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.15.4-alt1_1
- by mike@ request

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.5-alt1_1
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.4-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt1_1
- update to new release by fcimport

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_1
- new release

