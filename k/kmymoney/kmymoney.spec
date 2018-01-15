Name:    kmymoney
Version: 4.8.1.1
Release: alt1

Summary: A Personal Finance Manager for KDE4
Summary(ru_RU.UTF-8): Учёт финансов под KDE4
License: GPLv2 or GPLv3
Group:   Office
URL:     http://kmymoney2.sourceforge.net

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source2: %name.watch
Patch0:  %name-fix-undeclared-geteuid.patch
Patch2:  %name-%version-%release.patch

AutoReq: yes, noperl

BuildRequires(pre): kde4libs-devel
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++ 
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: kde4pimlibs-devel
BuildRequires: ktoblzcheck-devel
BuildRequires: libOpenSP-devel
BuildRequires: libalkimia-devel >= 4.3.1
BuildRequires: libaqbanking-devel >= 5.0.0
BuildRequires: libaqbanking-ofx-devel 
BuildRequires: libgamin-devel
BuildRequires: libglibmm-devel
BuildRequires: libgmp_cxx-devel
BuildRequires: libgpgme-devel
BuildRequires: libgwenhywfar-devel >= 4.0.0
BuildRequires: libical-devel
BuildRequires: libical-glib
BuildRequires: libicu-devel
BuildRequires: libofx-devel >= 0.9.4
BuildRequires: libspeex-devel
BuildRequires: libxml++2-devel 
BuildRequires: libxml2-devel
BuildRequires: kde4-kactivities-devel

Requires: kde4libs >= %{get_version kde4libs}
Requires: %name-i18n

Obsoletes: kde4-kmymoney

%description
KMyMoney strives to be the best personal finance manager.
The ultimate objectives of KMyMoney are...
* Accuracy.  Using time tested double entry accounting principles
  helps ensure that your finances are kept in correct order.
* Ease of use.  Strives to be the easiest open source personal
  finance manager to use, especially for the non-technical user.
* Familiar Features.  Intends to provide all important features
  found in the commercially-available, personal finance managers.


%package devel
Summary: Include files and libraries mandatory for KMyMoney development
Group: Development/KDE and QT
Requires: %name = %version
Obsoletes: kde4-kmymoney-devel

%description devel
Include files and libraries mandatory for development with package
kmymoney (KDE4).

%package kbanking
Summary: Online Banking plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Requires: aqbanking libgwenhywfar
Obsoletes: kde4-kmymoney-kbanking

%description kbanking
KBanking is the glue code needed to get the online banking features
provided by AqBanking into KMyMoney.

%package ofximport
Summary: OFX importing plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Requires: libofx
Obsoletes: kde4-kmymoney-ofximport

%description ofximport
OFX importing plugin for KMyMoney.

%package icalexport
Summary: ICalendar plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-icalexport

%description icalexport
KMyMoney iCalendar allows you to export information about scheduled
transactions to an iCalendar formatted file which can be read by most
calendar applications. This way, you can see your due payments in your
calendar application.

%package printcheck
Summary: Print cheques plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-printcheck

%description printcheck
This plugin gives you the ability to print transaction data onto a
preformatted paper check.

%package reconciliationreport
Summary: Reconciliation report plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-reconciliationreport

%description reconciliationreport
The reconciliation report plugin gives you a detailed report about the
status of a reconciliation. Once present, it will be automatically
invoked by KMyMoney after each reconciliation.

%package csvimport
Summary: CSV importing plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description csvimport
CSV importing plugin for KMyMoney.

%package csvexport
Summary: CSV exporting plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description csvexport
CSV exporting plugin for KMyMoney.

%package payeeidentifier
Summary: Payee identifier plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description payeeidentifier
Payee identifier plugin for KMyMoney.

%package onlinetasks
Summary: National orders plugin for online banking in KMyMoney
Group:   Office
Requires: %name = %version-%release

%description onlinetasks
Plugin with national orders for online banking in KMyMoney.

%package weboob
Summary: Weboob plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description weboob
Plugin for import transactions from Weboob to KMyMoney.

%package plugins
Summary: All KMyMoney plugins
Group:   Office
Requires: %name = %version-%release
Requires: %name-csvexport
Requires: %name-csvimport
Requires: %name-icalexport 
Requires: %name-kbanking 
Requires: %name-ofximport 
Requires: %name-onlinetasks
Requires: %name-payeeidentifier
Requires: %name-printcheck
Requires: %name-reconciliationreport
Requires: %name-weboob
Obsoletes: kde4-kmymoney-plugins

%description plugins
All KmyMoney plugins: kbanking, ofximport, icalexport, printcheck,
reconciliationreport, csvimport, csvexport, onlinetasks, payeeidentifier
and weboob.

%package i18n
Summary: Internationalization and documentation for KMyMoney
Group: System/Internationalization 
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-i18n
BuildArch: noarch

%description i18n
Internationalization and documentation for KMyMoney

%prep
%setup -q -n %name-%version
%patch0 -p2
%ifarch %ix86
%endif
%patch2 -p1

%build
# Need to build in one thread, see https://bugs.kde.org/show_bug.cgi?id=364387 for details
export NPROCS=1
%K4build -DCMAKE_SKIP_RPATH=1 -DUSE_HTML_HANDBOOK=1

%install
%K4install
mkdir -p %buildroot%_datadir/appdata
mv %buildroot%_K4apps/appdata/org.kde.kmymoney.appdata.xml %buildroot%_datadir/appdata
%K4find_lang --with-kde %name

%files
%doc AUTHORS COPYING README* TODO
%_K4bindir/%name
%_K4libdir/libkmm_widgets.so.*
%_K4libdir/libkmm_kdchart.so.*
%_K4libdir/libkmm_mymoney.so.*
%_K4libdir/libkmm_plugin.so.*
%_desktopdir/kde4/*%name.desktop
%doc %_K4doc/en/*
%_K4cfg/*.kcfg
%_K4srvtyp/*.desktop
%_K4apps/%name/*
%exclude %_K4apps/%name/templates/*
%_datadir/mime/packages/*
%_K4iconsdir/hicolor/*/apps/%name.png
%_K4iconsdir/locolor/*/apps/%name.png
%_K4iconsdir/hicolor/*/mimetypes/application-x-kmymoney.png
%_datadir/appdata/*.appdata.xml
%_K4conf_update/%name.upd
%_man1dir/%name.1*

%files devel
%dir %_K4includedir/%name
%_K4includedir/%name/*
%_K4lib/devel/libkmm_*.so

%files kbanking
%_K4lib/kmm_kbanking.so
%dir %_K4apps/kmm_kbanking
%_K4apps/kmm_kbanking/kmm_kbanking.rc
%_K4apps/kmm_kbanking/qml
%_K4srv/kmm_kbanking.desktop

%files ofximport
%_K4lib/kmm_ofximport.so
%dir %_K4apps/kmm_ofximport
%_K4apps/kmm_ofximport/kmm_ofximport.rc
%_K4srv/kmm_ofximport.desktop

%files icalexport
%_K4lib/kcm_kmm_icalendarexport.so
%_K4lib/kmm_icalendarexport.so
%dir %_K4apps/kmm_icalendarexport
%_K4apps/kmm_icalendarexport/kmm_icalendarexport.rc
%_K4srv/kcm_kmm_icalendarexport.desktop
%_K4srv/kmm_icalendarexport.desktop

%files printcheck
%_K4lib/kcm_kmm_printcheck.so
%_K4lib/kmm_printcheck.so
%dir %_K4apps/kmm_printcheck
%_K4apps/kmm_printcheck/check_template*.html
%_K4apps/kmm_printcheck/kmm_printcheck.rc
%_K4srv/kcm_kmm_printcheck.desktop
%_K4srv/kmm_printcheck.desktop

%files reconciliationreport
%_K4lib/kmm_reconciliationreport.so
%_K4srv/kmm_reconciliationreport.desktop

%files csvimport
%_K4lib/kmm_csvimport.so
%_K4srv/kmm_csvimport.desktop
%_K4apps/kmm_csvimport/kmm_csvimport.rc
%_K4conf/csvimporterrc

%files csvexport
%_K4lib/kmm_csvexport.so
%_K4srv/kmm_csvexport.desktop
%_K4apps/kmm_csvexport/kmm_csvexport.rc

%files payeeidentifier
%_libdir/libkmm_payeeidentifier.so.*
%_K4lib/payeeidentifier_*
%_K4lib/devel/libpayeeidentifier_*.so
%_libdir/libpayeeidentifier_*
%_K4srv/kmymoney-ibanbic-*.desktop
%_K4srv/kmymoney-nationalaccount-*.desktop

%files onlinetasks
%_K4lib/libkonlinetasks_*.so
%_K4srv/kmymoney-sepa*.desktop

%files weboob
%_K4lib/kmm_weboob.so
%_K4srv/kmm_weboob.desktop
%_K4apps/kmm_weboob

%files plugins

%files i18n -f %name.lang
%_K4apps/%name/templates/*
%exclude %_K4doc/en

%changelog
* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.1.1-alt1
- New version.

* Sun Oct 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt2
- Use documentation and localization from released tarball

* Wed Jun 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- new version 4.8.0
- New plugins: payeeidentifier, onlinetasks, weboob
- i18n package is required for main package

* Mon May 02 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt4
- Rebuild with new aqbanking
- Build without Nepomuk support

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt3
- Rebuild with new libalkimia

* Mon Jan 25 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt2
- Fix build

* Tue Apr 28 2015 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt1
- New version

* Sat Apr 04 2015 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- New version

* Fri Apr 03 2015 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt4
- Rebuild with new version of libgwenhywfar

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt3
- Fix source tarball name in watch file

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt2
- Rebuild with libofx-0.9.9

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt1
- New version

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt3
- Fix build with GMP 5.1.0
- Support Nepomuk
- Generate HTML documentation

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt2
- Fix build in Sisyphus

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt1
- New version 4.6.3

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.2-alt5.2
- Rebuilt

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.2-alt5.1
- Rebuilt with gmp 5.0.5

* Tue Jun 05 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt5
- Fix obsoletes to prevent "trigger effect"

* Tue Jun 05 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt4
- Replace kde4-kmymoney package

* Wed May 30 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt3
- Add missing translations to kmymoney-i18n
- Pack CVS import plugin

* Fri Feb 10 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt2
- Remove pt_BR documentation

* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version 4.6.2

* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version 4.6.1
- Remove standard library path from RPATH
- Add watch file

* Tue Sep 13 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt3
- Remove unnecessary dependencies

* Fri Sep 09 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt2
- Fix obsoletes to prevent downgrade

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt1
- New version 4.6.0
- Rename to kmymoney
- Set standard placement

* Wed Mar 02 2011 Andrey Cherepanov <cas@altlinux.org> 4.5.3-alt1
- New version 4.5.3

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 4.5.2-alt1
- New version 4.5.2

* Mon Nov 22 2010 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- new version 4.5.1

* Thu Oct 07 2010 Andrey Cherepanov <cas@altlinux.org> 4.5.0-alt1
- stable version 4.5.0
- rename package to kde4-kmymoney

* Mon May 17 2010 Andrey Cherepanov <cas@altlinux.org> 3.97.2-alt1
- Version 3.97.2 (beta)

* Thu Apr 15 2010 Andrey Cherepanov <cas@altlinux.org> 3.97.0-alt1
- Version 3.97.0 (beta)
