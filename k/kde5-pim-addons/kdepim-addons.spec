%define rname kdepim-addons

%define sover 5
%define libkaddressbookmergelibprivate libkaddressbookmergelibprivate%sover
%define libkaddressbookimportexportlibprivate libkaddressbookimportexportlibprivate%sover
%define libshorturlpluginprivate libshorturlpluginprivate%sover
%define libadblocklibprivate libadblocklibprivate%sover
%define libgrammarcommon libgrammarcommon%sover
%define libkmailgrammalecte libkmailgrammalecte%sover
%define libkmaillanguagetool libkmaillanguagetool%sover
%define libkmailmarkdown libkmailmarkdown%sover
%define libkmailquicktextpluginprivate libkmailquicktextpluginprivate%sover
%define libdkimverifyconfigure libdkimverifyconfigure%sover
%define libexpireaccounttrashfolderconfig libexpireaccounttrashfolderconfig%sover
%define libfolderconfiguresettings libfolderconfiguresettings%sover
%define libkmailconfirmbeforedeleting libkmailconfirmbeforedeleting%sover
%define libscamconfiguresettings libscamconfiguresettings%sover
%define libopenurlwithconfigure libopenurlwithconfigure%sover
%define libakonadidatasetools libakonadidatasetools%sover

Name: kde5-pim-addons
Version: 22.08.3
Release: alt1
%K5init

%add_findreq_skiplist %_K5bin/kmail_*.sh

Group: Graphical desktop/KDE
Summary: PIM addons
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

ExcludeArch: %not_qt5_qtwebengine_arches

Requires: %name-kaddressbook
Requires: %name-kmail
Requires: %name-korganizer
Requires: %name-plugins

Source: %rname-%version.tar
Patch1: alt-akonadi-plugins-dir.patch

# Automatically added by buildreq on Thu Sep 01 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils fontconfig gcc-c++ grantlee5-devel kde5-libkleo-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libical-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kdgantt2-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel  kde5-pimcommon-devel kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kdoctools-devel kf5-kio-devel kf5-kpackage-devel kf5-kwallet-devel kf5-libkgapi-devel libsasl2-devel python-module-google python3-dev qt5-webengine-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: libpoppler-qt5-devel libdiscount-devel
BuildRequires: libsasl2-devel libgpgme-devel libassuan-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: kde5-libkleo-devel
BuildRequires: kde5-libkgapi-devel kde5-kaddressbook-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel
BuildRequires: kde5-calendarsupport-devel kde5-eventviews-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-libksieve-devel
BuildRequires: kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel
BuildRequires: kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel
BuildRequires: kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel  kde5-pimcommon-devel
BuildRequires: kde5-mailimporter-devel kde5-akonadi-import-wizard-devel kde5-kontactinterface-devel
BuildRequires: kde5-kpkpass-devel kde5-kitinerary-devel
BuildRequires: kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kdoctools-devel kf5-kio-devel kf5-kpackage-devel
BuildRequires: kf5-kwallet-devel kf5-syntax-highlighting-devel kf5-prison-devel kf5-kholidays-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package kaddressbook
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description kaddressbook
%summary.

%package kmail
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description kmail
%summary.

%package korganizer
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description korganizer
%summary.

%package plugins
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description plugins
%summary.

%package -n %libkmailconfirmbeforedeleting
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkmailconfirmbeforedeleting
%name library

%package -n %libkaddressbookmergelibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkaddressbookmergelibprivate
%name library

%package -n %libkaddressbookimportexportlibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkaddressbookimportexportlibprivate
%name library

%package -n %libshorturlpluginprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libshorturlpluginprivate
%name library

%package -n %libadblocklibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libadblocklibprivate
%name library

%package -n %libgrammarcommon
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libgrammarcommon
%name library

%package -n %libkmailgrammalecte
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkmailgrammalecte
%name library

%package -n %libkmaillanguagetool
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkmaillanguagetool
%name library

%package -n %libkmailmarkdown
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkmailmarkdown
%name library

%package -n %libdkimverifyconfigure
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libdkimverifyconfigure
%name library

%package -n %libkmailquicktextpluginprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkmailquicktextpluginprivate
%name library

%package -n %libexpireaccounttrashfolderconfig
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libexpireaccounttrashfolderconfig
%name library

%package -n %libfolderconfiguresettings
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libfolderconfiguresettings
%name library

%package -n %libscamconfiguresettings
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libscamconfiguresettings
%name library

%package -n %libopenurlwithconfigure
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libopenurlwithconfigure
%name library

%package -n %libakonadidatasetools
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libakonadidatasetools
%name library

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K5build \
    -DKDEPIMADDONS_BUILD_EXAMPLES=OFF \
    #

%install
%K5install
%K5install_move data kmail2 messageviewer kconf_update contacteditor
%find_lang %name --with-kde --all-name


%files

%files common -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K5xdgconf/kmail.*
%_datadir/qlogging-categories5/*.*categories
%_K5conf_up/*.upd
%_K5icon/hicolor/*/status/*moon*.*

%files kaddressbook
%_K5plug/pim5/kaddressbook/
%_K5plug/pim5/contacteditor/editorpageplugins/cryptopageplugin.so

%files kmail
%_K5bin/kmail_*.sh
%_K5plug/pim5/kmail/
%_K5plug/kf5/mailtransport/

%files korganizer
%_K5plug/pim5/korganizer/
%_K5plug/pim5/akonadi/emailaddressselectionldapdialogplugin.so
%_K5plug/plasmacalendarplugins/
%_K5qml/org/kde/plasma/PimCalendars/

%files plugins
%_K5plug/pim5/libksieve/
%_K5plug/pim5/pimcommon/
%_K5plug/pim5/messageviewer/
%_K5plug/pim5/importwizard/
%_K5plug/pim5/templateparser/
%_K5plug/pim5/webengineviewer/

%files devel
%_datadir/qtcreator/templates/*
#%_K5inc/kdepim-addons_version.h
#%_K5inc/kdepim-addons/
#%_K5link/lib*.so
#%_K5lib/cmake/kdepim-addons
#%_K5archdata/mkspecs/modules/qt_kdepim-addons.pri
#%_datadir/qtcreator/templates/*/

%files -n %libadblocklibprivate
%_K5lib/libadblocklibprivate.so.%sover
%_K5lib/libadblocklibprivate.so.*
%files -n %libkmailmarkdown
%_K5lib/libkmailmarkdown.so.%sover
%_K5lib/libkmailmarkdown.so.*
%files -n %libshorturlpluginprivate
%_K5lib/libshorturlpluginprivate.so.%sover
%_K5lib/libshorturlpluginprivate.so.*
%files -n %libkaddressbookmergelibprivate
%_K5lib/libkaddressbookmergelibprivate.so.%sover
%_K5lib/libkaddressbookmergelibprivate.so.*
%files -n %libkmailconfirmbeforedeleting
%_K5lib/libkmailconfirmbeforedeleting.so.%sover
%_K5lib/libkmailconfirmbeforedeleting.so.*
%files -n %libscamconfiguresettings
%_K5lib/libscamconfiguresettings.so.%sover
%_K5lib/libscamconfiguresettings.so.*
%files -n %libkmailquicktextpluginprivate
%_K5lib/libkmailquicktextpluginprivate.so.%sover
%_K5lib/libkmailquicktextpluginprivate.so.*
%files -n %libkmaillanguagetool
%_K5lib/libkmaillanguagetool.so.%sover
%_K5lib/libkmaillanguagetool.so.*
%files -n %libkmailgrammalecte
%_K5lib/libkmailgrammalecte.so.%sover
%_K5lib/libkmailgrammalecte.so.*
%files -n %libgrammarcommon
%_K5lib/libgrammarcommon.so.%sover
%_K5lib/libgrammarcommon.so.*
%files -n %libfolderconfiguresettings
%_K5lib/libfolderconfiguresettings.so.%sover
%_K5lib/libfolderconfiguresettings.so.*
%files -n %libexpireaccounttrashfolderconfig
%_K5lib/libexpireaccounttrashfolderconfig.so.%sover
%_K5lib/libexpireaccounttrashfolderconfig.so.*
%files -n %libdkimverifyconfigure
%_K5lib/libdkimverifyconfigure.so.%sover
%_K5lib/libdkimverifyconfigure.so.*
%files -n %libopenurlwithconfigure
%_K5lib/libopenurlwithconfigure.so.%sover
%_K5lib/libopenurlwithconfigure.so.*
%files -n %libakonadidatasetools
%_K5lib/libakonadidatasetools.so.%sover
%_K5lib/libakonadidatasetools.so.*


%changelog
* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 08 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Feb 21 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.2-alt1
- new version

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt4
- using not_qt5_qtwebengine_arches macro

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt3
- build with parity of qtwebengine arches

* Wed Jan 26 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtwebengine on ppc64le

* Thu Jan 13 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Mon May 17 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Wed Mar 10 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Jan 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Wed Dec 16 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Mon Nov 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Tue Jul 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 16 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue Apr 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.03.90-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Wed Apr 12 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2
- fix build requires

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
