%define rname kdnssd

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 network service discovery using Zeroconf
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 11 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt6-core libqt6-dbus libqt6-network libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ libavahi-devel python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ libavahi-devel qt6-tools-devel

%description
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of (Zeroconf](http://www.zeroconf.org) that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

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

%package -n libkf6dnssd
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6dnssd
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md

%files devel
#%_K6inc/kdnssd_version.h
%_K6inc/KDNSSD/
%_K6link/lib*.so
%_K6lib/cmake/KF6DNSSD

%files -n libkf6dnssd
%_K6lib/libKF6DNSSD.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

