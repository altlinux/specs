%define rname akonadi-mime

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Basic email handling implementation
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel
BuildRequires: libxslt-devel xsltproc
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel kf6-kitemmodels-devel
BuildRequires: akonadi-devel kmime-devel

%description
Libraries and daemons to implement basic email handling.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: pimlibs-common = %EVR
Obsoletes: pimlibs-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadimime
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadimime
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%_K6xdgmime/x-vnd.kde.contactgroup.xml
%_K6cfg/*.kcfg

%files devel
%_includedir/KPim6/AkonadiMime/
%_K6link/lib*.so
%_K6lib/cmake/K*AkonadiMime/

%files -n libkpim6akonadimime
%_K6lib/libKPim6AkonadiMime.so.*
%_K6plug/akonadi_serializer_mail.so
%_datadir/akonadi/plugins/serializer/akonadi_serializer_mail.desktop


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

