Group: Networking/WWW
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel
# END SourceDeps(oneline)
Summary(ru): QuiteRSS - быстрая и удобная программа для чтения новостных лент RSS/Atom
Name:		quiterss
Version:	0.16.0
Release:	alt1_1
License:	GPLv3
Summary:	RSS/Atom aggregator
Source0:	http://quite-rss.googlecode.com/files/QuiteRSS-%{version}-src.tar.bz2
Source1:	sqlitex.pri
Patch0:		QuiteRSS-0.16.0.diff
URL:		http://code.google.com/p/quite-rss/
BuildRequires:	pkgconfig(QtGui) pkgconfig(QtNetwork) pkgconfig(QtWebKit) pkgconfig(QtXml) pkgconfig(QtSql)
BuildRequires:	desktop-file-utils
BuildRequires:  libqtsingleapplication-devel pkgconfig(sqlite3) pkgconfig(phonon)
Source44: import.info
Requires: libqt4-sql-sqlite

%description
Qt-based RSS/Atom aggregator.


%description -l ru
Быстрая и удобная программа для чтения новостных лент RSS/Atom,
написанная на Qt.

%prep
%setup -q -n QuiteRSS-%{version}-src
%patch0 -p 0
cp %{SOURCE1} 3rdparty/sqlitex/
# be asure
rm -rf 3rdparty/{qtsingleapplication,sqlite_qt4?x}
rm -f 3rdparty/sqlite.pri
sed -i -e s,qtsingleapplication.h,QtSolutions/qtsingleapplication.h, src/application/mainapplication.h
sed -i -e s,phonon/audiooutput.h,kde4/phonon/audiooutput.h, src/application/mainwindow.h
sed -i -e s,phonon/mediaobject.h,kde4/phonon/mediaobject.h, src/application/mainwindow.h

%build
qmake-qt4 PREFIX=%{_prefix} SYSTEMQTSA=True
make release %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/sound/
%{_datadir}/%{name}/style/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %_datadir/%name/lang

%changelog
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

