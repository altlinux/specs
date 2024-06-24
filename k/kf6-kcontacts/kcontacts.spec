%define rname kcontacts

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: Address book API for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 11 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt6-core libqt6-dbus libqt6-gui libqt6-xml libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf6-kcodecs-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel libdb4-devel python-module-google qt6-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kcodecs-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6contacts
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6contacts
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name
mkdir -p %buildroot/%_K6data/kcontacts/

%files common -f %name.lang
%doc LICENSES/* README.md
#%config(noreplace) %_K6xdgconf/*.*categories
%_datadir/qlogging-categories6/*.*categories
%dir %_K6data/kcontacts/

%files devel
#%_K6inc/kcontacts_version.h
%_K6inc/KContacts/
%_K6link/lib*.so
%_K6lib/cmake/KF6Contacts/

%files -n libkf6contacts
%_K6lib/libKF6Contacts.so.*
%_K6qml/org/kde/contacts/

%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

