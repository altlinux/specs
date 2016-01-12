%define rname libkdcraw

Name: kde5-%rname
Version: 15.12.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: LibRaw C++ interface for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 12 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libstdc++-devel pkg-config python-base python-modules python3 python3-base ruby ruby-stdlibs
BuildRequires: extra-cmake-modules libraw-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libraw-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5kdcraw
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kdcraw
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K5inc/libkdcraw_version.h
%_K5inc/KDCRAW/
%_K5link/lib*.so
%_K5lib/cmake/KF5KDcraw/
#%_K5archdata/mkspecs/modules/qt_libkdcraw.pri

%files -n libkf5kdcraw
%_K5lib/libKF5KDcraw.so.*

%changelog
* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
