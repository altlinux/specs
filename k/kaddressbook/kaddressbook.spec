%define rname kaddressbook

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

%define sover 6
%define libkaddressbookprivate libkaddressbookprivate%sover
%define libkpimaddressbookimportexport libkpimaddressbookimportexport%sover

Group: Graphical desktop/KDE
Summary: Addressbook
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-kaddressbook = %EVR
Obsoletes: kde5-kaddressbook < %EVR
Requires: akonadi akonadi-search
%ifarch %qt6_qtwebengine_arches
Requires: kdepim-runtime
%endif

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-kcmutils-devel kf6-kdoctools-devel kf6-kio-devel kf6-prison-devel kf6-kiconthemes-devel
BuildRequires: kf6-kitemmodels-devel kf6-kparts-devel kf6-ki18n-devel kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel kidentitymanagement-devel kimap-devel kmime-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel akonadi-search-devel grantleetheme-devel
BuildRequires: kidentitymanagement-devel kimap-devel kmime-devel kldap-devel
BuildRequires: kontactinterface-devel kpimtextedit-devel kde6-libkdepim-devel messagelib-devel
BuildRequires: pimcommon-devel

%description
Contact manager.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kaddressbook-common = %EVR
Obsoletes: kde5-kaddressbook-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkaddressbookprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkaddressbookprivate5 < %EVR
%description -n %libkaddressbookprivate
%name library

%package -n %libkpimaddressbookimportexport
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkpimaddressbookimportexport5 < %EVR
%description -n %libkpimaddressbookimportexport
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    #

%install
%K6install
%K6install_move data kaddressbook kconf_update kontact
for f in %buildroot/%_libdir/cmake/*/*.cmake ; do
    sed -i 's|%_K6inc/KF6|%_K6inc|g' $f
done
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kaddressbook
%_K6plug/pim6/kcms/kaddressbook/
%_K6plug/*kaddressbook*.so
%_K6plug/pim6/kontact/*kaddressbook*.so
%_K6xdgapp/*kaddressbook*.desktop
%_K6data/kaddressbook/
%_K6icon/*/*/apps/kaddressbook.*
%_datadir/metainfo/*.xml

%files devel
%_includedir/KPim6/??ddress?ook?mport?xport/
%_K6link/lib*.so
%_K6lib/cmake/K*AddressbookImportExport/

%files -n %libkaddressbookprivate
%_K6lib/libkaddressbookprivate.so.%sover
%_K6lib/libkaddressbookprivate.so.*

%files -n %libkpimaddressbookimportexport
%_K6lib/libKPim6AddressbookImportExport.so.%sover
%_K6lib/libKPim6AddressbookImportExport.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

