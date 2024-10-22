%define rname kdepim-addons

%define sover 6
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

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

%add_findreq_skiplist %_K6bin/kmail_*.sh

Group: Graphical desktop/KDE
Summary: PIM addons
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-pim-addons = %EVR
Obsoletes: kde5-pim-addons < %EVR

Requires: %name-kaddressbook
Requires: %name-kmail
Requires: %name-korganizer
Requires: %name-plugins

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel qt6-webengine-devel
BuildRequires: libpoppler-qt6-devel libdiscount-devel
BuildRequires: libsasl2-devel libgpgme-devel libassuan-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kdeclarative-devel  kf6-kdoctools-devel kf6-kio-devel kf6-kpackage-devel kf6-kparts-devel
BuildRequires: kf6-kwallet-devel kf6-syntax-highlighting-devel kf6-prison-devel kf6-kholidays-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemmodels-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: kde6-libkgapi-devel kaddressbook-devel kidentitymanagement-devel kcalutils-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel akonadi-mime-devel akonadi-notes-devel
BuildRequires: calendarsupport-devel eventviews-devel grantleetheme-devel incidenceeditor-devel kde6-libksieve-devel
BuildRequires: kimap-devel kmailtransport-devel kmime-devel kpimtextedit-devel ktnef-devel kde6-libgravatar-devel
BuildRequires: kde6-libkdepim-devel mailcommon-devel messagelib-devel  pimcommon-devel
BuildRequires: mailimporter-devel akonadi-import-wizard-devel kontactinterface-devel
BuildRequires: kpkpass-devel kitinerary-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-pim-addons-common = %EVR
Obsoletes: kde5-pim-addons-common < %EVR
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
Requires: %name-common >= %EVR
Provides: kde5-pim-addons-kaddressbook = %EVR
Obsoletes: kde5-pim-addons-kaddressbook < %EVR
%description kaddressbook
%summary.

%package kmail
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common >= %EVR
Provides: kde5-pim-addons-kmail = %EVR
Obsoletes: kde5-pim-addons-kmail < %EVR
%description kmail
%summary.

%package korganizer
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common >= %EVR
Provides: kde5-pim-addons-korganizer = %EVR
Obsoletes: kde5-pim-addons-korganizer < %EVR
%description korganizer
%summary.

%package plugins
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common >= %EVR
Requires: kf6-ktextaddons
Provides: kde5-pim-addons-plugins = %EVR
Obsoletes: kde5-pim-addons-plugins < %EVR
%description plugins
%summary.

%package -n %libkmailconfirmbeforedeleting
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkmailconfirmbeforedeleting5 < %EVR
%description -n %libkmailconfirmbeforedeleting
%name library

%package -n %libkaddressbookmergelibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkaddressbookmergelibprivate5 < %EVR
%description -n %libkaddressbookmergelibprivate
%name library

%package -n %libkaddressbookimportexportlibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkaddressbookimportexportlibprivate
%name library

%package -n %libshorturlpluginprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libshorturlpluginprivate5 < %EVR
%description -n %libshorturlpluginprivate
%name library

%package -n %libadblocklibprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libadblocklibprivate5 < %EVR
%description -n %libadblocklibprivate
%name library

%package -n %libgrammarcommon
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libgrammarcommon
%name library

%package -n %libkmailgrammalecte
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkmailgrammalecte
%name library

%package -n %libkmaillanguagetool
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkmaillanguagetool
%name library

%package -n %libkmailmarkdown
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkmailmarkdown5 < %EVR
%description -n %libkmailmarkdown
%name library

%package -n %libdkimverifyconfigure
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdkimverifyconfigure5 < %EVR
%description -n %libdkimverifyconfigure
%name library

%package -n %libkmailquicktextpluginprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkmailquicktextpluginprivate5 < %EVR
%description -n %libkmailquicktextpluginprivate
%name library

%package -n %libexpireaccounttrashfolderconfig
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libexpireaccounttrashfolderconfig5 < %EVR
%description -n %libexpireaccounttrashfolderconfig
%name library

%package -n %libfolderconfiguresettings
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libfolderconfiguresettings5 < %EVR
%description -n %libfolderconfiguresettings
%name library

%package -n %libscamconfiguresettings
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libscamconfiguresettings5 < %EVR
%description -n %libscamconfiguresettings
%name library

%package -n %libopenurlwithconfigure
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libopenurlwithconfigure5 < %EVR
%description -n %libopenurlwithconfigure
%name library

%package -n %libakonadidatasetools
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libakonadidatasetools5 < %EVR
%description -n %libakonadidatasetools
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDEPIMADDONS_BUILD_EXAMPLES=OFF \
    #

%install
%K6install
%K6install_move data kmail2 messageviewer kconf_update contacteditor
%find_lang %name --with-kde --all-name


%files

%files common -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K6xdgconf/*kmail*
%_datadir/qlogging-categories6/*.*categories

%files kaddressbook
%_K6plug/pim6/kaddressbook/
%_K6plug/pim6/contacteditor/editorpageplugins/cryptopageplugin.so

%files kmail
%_K6bin/kmail_*.sh
%_K6plug/pim6/kmail/
%_K6plug/pim6/mailtransport/

%files korganizer
%_K6plug/pim6/akonadi/emailaddressselectionldapdialogplugin.so
%_K6plug/plasmacalendarplugins/
%_K6qml/org/kde/plasma/PimCalendars/

%files plugins
%_K6plug/pim6/libksieve/
%_K6plug/pim6/pimcommon/
%_K6plug/pim6/messageviewer/
%_K6plug/pim6/importwizard/
%_K6plug/pim6/templateparser/
%_K6plug/pim6/webengineviewer/

%files devel
#%_datadir/qtcreator/templates/*
#%_K6inc/kdepim-addons_version.h
#%_K6inc/kdepim-addons/
#%_K6link/lib*.so
#%_K6lib/cmake/kdepim-addons
#%_K6archdata/mkspecs/modules/qt_kdepim-addons.pri
#%_datadir/qtcreator/templates/*/

%files -n %libkmailmarkdown
%_K6lib/libkmailmarkdown.so.%sover
%_K6lib/libkmailmarkdown.so.*
%files -n %libshorturlpluginprivate
%_K6lib/libshorturlpluginprivate.so.%sover
%_K6lib/libshorturlpluginprivate.so.*
%files -n %libkaddressbookmergelibprivate
%_K6lib/libkaddressbookmergelibprivate.so.%sover
%_K6lib/libkaddressbookmergelibprivate.so.*
%files -n %libkmailconfirmbeforedeleting
%_K6lib/libkmailconfirmbeforedeleting.so.%sover
%_K6lib/libkmailconfirmbeforedeleting.so.*
%files -n %libkmailquicktextpluginprivate
%_K6lib/libkmailquicktextpluginprivate.so.%sover
%_K6lib/libkmailquicktextpluginprivate.so.*
%files -n %libfolderconfiguresettings
%_K6lib/libfolderconfiguresettings.so.%sover
%_K6lib/libfolderconfiguresettings.so.*
%files -n %libexpireaccounttrashfolderconfig
%_K6lib/libexpireaccounttrashfolderconfig.so.%sover
%_K6lib/libexpireaccounttrashfolderconfig.so.*
%files -n %libdkimverifyconfigure
%_K6lib/libdkimverifyconfigure.so.%sover
%_K6lib/libdkimverifyconfigure.so.*
%files -n %libopenurlwithconfigure
%_K6lib/libopenurlwithconfigure.so.%sover
%_K6lib/libopenurlwithconfigure.so.*
%files -n %libakonadidatasetools
%_K6lib/libakonadidatasetools.so.%sover
%_K6lib/libakonadidatasetools.so.*



%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

