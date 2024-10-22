%define rname akonadi-contacts

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Contact Management in Akonadi
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-no-qwebengine.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-prison-devel kf6-kcmutils-devel kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-ktextwidgets-devel kf6-kitemmodels-devel kf6-ktexttemplate-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: akonadi-devel akonadi-mime-devel kmime-devel
BuildRequires: grantleetheme-devel kde6-libkleo-devel

%description
Libraries and daemons to implement Contact Management in Akonadi.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: grantleetheme-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadicontactcore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadicontactcore
%name library

%package -n libkpim6akonadicontactwidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadicontactwidgets
%name library


%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data akonadicontact contacteditor
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/*ontact*/
%_K6link/lib*.so
%_K6lib/cmake/K**Contact*/

%files -n libkpim6akonadicontactcore
%_K6lib/libKPim6AkonadiContactCore.so.*
#
%_K6plug/akonadi_serializer_addressee.so
%_datadir/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
#
%_K6plug/akonadi_serializer_contactgroup.so
%_datadir/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
#
%_kf6_data/akonadi/contact/

%files -n libkpim6akonadicontactwidgets
%_K6lib/libKPim6AkonadiContactWidgets.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

