%define rname ksmtp

%define sover 6
%define libkpimsmtp libkpim6smtp%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: A job-based API for interacting with SMTP servers
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libsasl2-devel libssl-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel
BuildRequires: kmime-devel

%description
This library provides a job-based API for interacting with an SMTP server.

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

%package -n %libkpimsmtp
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpimsmtp
%name library


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

%files devel
%_includedir/KPim6/KSMTP/
%_K6link/lib*.so
%_K6lib/cmake/K*SMTP/
#%_K6archdata/mkspecs/modules/qt_KSMTP.pri

%files -n %libkpimsmtp
%_K6lib/libKPim6SMTP.so.*
%_K6lib/libKPim6SMTP.so.%sover


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

