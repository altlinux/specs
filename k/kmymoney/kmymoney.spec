%define _unpackaged_files_terminate_build 1
%ifarch %qt6_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif
# There is no qt6 subdirectory in https://github.com/aqbanking/gwenhywfar/tree/master/gui
%def_without kbanking

Name:    kmymoney
Version: 5.2.1
Release: alt1

Summary: A Personal Finance Manager for KDE
Summary(ru_RU.UTF-8): Учёт финансов под KDE
License: GPL-2.0 or GPL-3.0
Group:   Office
URL:     http://kmymoney2.org
# Download from https://download.kde.org/stable/kmymoney/

Source0: %name-%version.tar
Source1: ru.po

AutoReq: yes, noperl

ExclusiveArch: %qt6_qtwebengine_arches

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: python3-dev
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: kf6-kauth-devel
BuildRequires: kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kwallet-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kholidays-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: akonadi-devel
BuildRequires: kidentitymanagement-devel
BuildRequires: plasma6-activities-devel
BuildRequires: qt6-5compat-devel
BuildRequires: kpimtextedit-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kde6-kdiagram-devel
BuildRequires: libqtkeychain-qt6-devel

BuildRequires: boost-devel
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: ktoblzcheck-devel
BuildRequires: libOpenSP-devel
BuildRequires: libalkimia-devel >= 7.0.0
BuildRequires: libaqbanking-devel >= 5.0.0
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
BuildRequires: libsqlcipher-devel
BuildRequires: python-devel
BuildRequires: python3-module-weboob

Requires: %name-i18n

Obsoletes: kde4-kmymoney

# For weboob python helper requirements
#add_python_compile_include %_datadir/kmymoney/weboob

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
kmymoney (KDE).

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

%package csv
Summary: CSV importing and exporting plugin for KMyMoney
Group:   Office
Provides: %name-csvexport = %EVR
Obsoletes: %name-csvexport < %EVR
Provides: %name-csvimport = %EVR
Obsoletes: %name-csvimport < %EVR
Requires: %name = %version-%release

%description csv
CSV importing and exporting plugin for KMyMoney.

%package qif
Summary: QIF importing and exporting plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description qif 
QIF importing and exporting plugin for KMyMoney.

%package gncimport
Summary: GNC importing plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description gncimport
GNC importing plugin for KMyMoney.

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
Requires: python3(weboob)

%description weboob
Plugin for import transactions from Weboob to KMyMoney.

%package plugins
Summary: All KMyMoney plugins
Group:   Office
Requires: %name = %version-%release
Requires: %name-csv
Requires: %name-qif
Requires: %name-csvimport
Requires: %name-gncimport
Requires: %name-icalexport 
%if_with kbanking
Requires: %name-kbanking 
%endif
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

%description i18n
Internationalization and documentation for KMyMoney

%prep
%setup -q -n %name-%version
#cp %SOURCE1 po/ru/kmymoney.po

%build
%K6init no_altplace
# Need to build in one thread, see https://bugs.kde.org/show_bug.cgi?id=364387 for details
#export NPROCS=1
%K6build -DCMAKE_SKIP_RPATH=1 \
         -DBUILD_WITH_QT6=ON \
         -DENABLE_ADDRESSBOOK=ON \
         -DENABLE_IBANBICDATA=OFF \
         -DENABLE_KBANKING=ON \
         -DAQBANKING_INCLUDE_DIRS=%_includedir/aqbanking6 \
         -DKDE_INSTALL_METAINFODIR=%_datadir/appdata \
%if_enabled qtwebengine
         -DENABLE_WEBENGINE=ON \
%else
         -DENABLE_WEBENGINE=OFF \
%endif
         -DENABLE_WOOB=ON \
         -DENABLE_SQLCIPHER=OFF

%install
%K6install
%find_lang %name --all

%files
%_K6bin/%name
%_K6lib/libkmm_base_dialogs.so.*
%_K6lib/libkmm_base_widgets.so.*
%_K6lib/libkmm_codec.so.*
%_K6lib/libkmm_extended_dialogs.so.*
%_K6lib/libkmm_gpgfile.so.*
%_K6lib/libkmm_icons.so.*
%_K6lib/libkmm_keychain.so.*
%_K6lib/libkmm_menuactionexchanger.so.*
%_K6lib/libkmm_menus.so.*
%_K6lib/libkmm_models.so.*
%_K6lib/libkmm_mymoney.so.*
%_K6lib/libkmm_plugin.so.*
%_K6lib/libkmm_printer.so.*
%_K6lib/libkmm_selections.so.*
%_K6lib/libkmm_settings.so.*
%_K6lib/libkmm_templates.so.*
%_K6lib/libkmm_webconnect.so.*
%_K6lib/libkmm_widgets.so.*
%_K6lib/libkmm_wizard.so.*
%_K6lib/libkmm_yesno.so.*
%_K6lib/libonlinetask_interfaces.so.*
%_K6xdgapp/*%name.desktop
%doc %_K6doc/en/*
%_K6cfg/*.kcfg
%_datadir/%name/*
%_datadir/mime/packages/*
%_K6icon/hicolor/*/apps/%name.png
%_K6icon/hicolor/*/mimetypes/application-x-kmymoney.png
%_datadir/kconf_update/%name.upd
%_datadir/appdata/org.*.appdata.xml
%_qt6_plugindir/kmymoney_plugins/budgetview.so
%_qt6_plugindir/kmymoney_plugins/forecastview.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_forecastview.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_reportsview.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_xmlstorage.so
%_qt6_plugindir/kmymoney_plugins/onlinejoboutboxview.so
%_qt6_plugindir/kmymoney_plugins/reportsview.so
%_qt6_plugindir/kmymoney_plugins/sqlstorage.so
%_qt6_plugindir/kmymoney_plugins/xmlstorage.so

%files devel
%dir %_includedir/%name
%_includedir/%name/*
%_K6link/lib*.so

%if_with kbanking
%files kbanking
%_qt6_plugindir/kmymoney/kbanking.so
%_K6xmlgui/kbanking
%_datadir/kbanking
%endif

%files ofximport
%_qt6_plugindir/kmymoney_plugins/ofximporter.so

%files icalexport
%_qt6_plugindir/kmymoney_plugins/icalendarexporter.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_icalendarexporter.so

%files printcheck
%_qt6_plugindir/kmymoney_plugins/checkprinting.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_checkprinting.so
%_datadir/checkprinting

%files reconciliationreport
%_qt6_plugindir/kmymoney_plugins/reconciliationreport.so

%files csv
%_libdir/libkmm_csvimportercore.so*
%_qt6_plugindir/kmymoney_plugins/csvimporter.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_csvimporter.so
%_qt6_plugindir/kmymoney_plugins/csvexporter.so

%files qif
%_qt6_plugindir/kmymoney_plugins/qifimporter.so
%_qt6_plugindir/kmymoney_plugins/qifexporter.so
%_qt6_plugindir/kmymoney_plugins/kcms/kcm_qif.so

%files gncimport
%_qt6_plugindir/kmymoney_plugins/gncimporter.so

%files payeeidentifier
%_libdir/libkmm_payeeidentifier.so.*

%files onlinetasks
%_qt6_plugindir/kmymoney_plugins/konlinetasks_sepa.so

%files weboob
#_datadir/%name/weboob
%_qt6_plugindir/kmymoney_plugins/woob.so

%files plugins

%files i18n -f %name.lang
%_K6doc/*/kmymoney/
%exclude %_K6doc/en

%changelog
* Thu Aug 07 2025 Andrey Cherepanov <cas@altlinux.org> 5.2.1-alt1
- New version.

* Fri Jun 27 2025 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.
- Rebuilt with KF6 (ALT #54993).
- Removed kmymoney-kbanking because gwenhywfar has no version for Qt6.

* Tue Nov 28 2023 Ivan A. Melnikov <iv@altlinux.org> 5.1.3-alt3.1
- NMU: Used rpm-macros-qt5-webengine (fixes build on loongarch64).

* Thu Nov 23 2023 Andrey Cherepanov <cas@altlinux.org> 5.1.3-alt3
- Used correct macros for desktop file location (ALT #48222).

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 5.1.3-alt2
- FTBFS: fixed desktop file location.

* Sun Jul 31 2022 Andrey Cherepanov <cas@altlinux.org> 5.1.3-alt1
- New version.

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.2-alt7
- Build with qtwebkit instead of qtwebengine on e2k and ppc64le.

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.2-alt6
- Build with parity of qtwebengine arches.

* Mon Jan 24 2022 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt5
- FTBFS: Rebuild with new Akonadi.

* Mon Sep 27 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt4
- FTBFS: fix build with GCC11.

* Fri Jul 02 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt3
- Build with qt5-webengine (thanks zerg@).

* Thu Jul 01 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt2
- Complete Russian localization (thanks Olesya Gerasimenko).

* Fri Jun 25 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt1
- New version.

* Sat May 08 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt3
- Move weboob plugin script to kmymoney-weboob.
- Set python2.7(weboob) as kmymoney-weboob requirements.

* Fri Feb 26 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt2
- Complete Russian localization (thanks Olesya Gerasimenko).

* Tue Dec 22 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Fri Jun 19 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.
- Fix License and Summary.

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 5.0.8-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.6-alt1
- New version.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.5-alt1
- New version.

* Tue Apr 23 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- New version.

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1
- New version.

* Tue Nov 06 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt2.qa1
- NMU: applied repocop patch

* Sat Sep 29 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt2
- Fix build with Qt 5.11.
- Package appdata file.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.
- Do not build API documentation.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt2
- Rebuild with libgwenhywfar-4.20.0.

* Thu Feb 15 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version for KDE 5.

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
