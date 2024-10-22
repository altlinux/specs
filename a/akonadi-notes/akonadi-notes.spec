%define rname akonadi-notes

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Management of notes in Akonadi
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel extra-cmake-modules qt6-declarative-devel
BuildRequires: akonadi-devel kmime-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel

%description
Libraries and daemons to implement management of notes in Akonadi.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadinotes
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadinotes
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

%files devel
%_includedir/KPim6/AkonadiNotes/
%_K6link/lib*.so
%_K6lib/cmake/K*AkonadiNotes/

%files -n libkpim6akonadinotes
%_K6lib/libKPim6AkonadiNotes.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

