%define rname kldap

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: LDap support library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kmbox-devel kmime-devel
BuildRequires: kf6-kcompletion-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel kf6-kio-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kwallet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kldap-common = %EVR
Obsoletes: kde5-kldap-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6ldapcore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6ldapcore
%name library.

%package -n libkpim6ldapwidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6ldapwidgets
%name library.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
#%_K6srv/ldap*.protocol

%files devel
%_includedir/KPim6/KLDAP*/
%_K6link/lib*.so
%_K6lib/cmake/K*Ldap*/

%files -n libkpim6ldapcore
%_K6lib/libKPim6LdapCore.so.*
%_K6plug/kf6/kio/ldap.so
%files -n libkpim6ldapwidgets
%_K6lib/libKPim6LdapWidgets.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

