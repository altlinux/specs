%define rname libksane

Name: kde5-%rname
Version: 15.12.2
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: SANE Library interface
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Feb 01 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-kconfig-devel kf5-ki18n-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-sonnet-devel libsane-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libsane-devel
BuildRequires: kf5-kconfig-devel kf5-ki18n-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-sonnet-devel

%description
Libksane is a KDE interface for SANE library to control flat scanners.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5sane
Group: System/Libraries
Summary: KF5 library
#Requires: %name-common = %EVR
%description -n libkf5sane
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files devel
%_K5inc/ksane_version.h
%_K5inc/KSane/
%_K5link/lib*.so
%_K5lib/cmake/KF5Sane/
#%_K5archdata/mkspecs/modules/qt_ksane.pri

%files -n libkf5sane
%doc COPYING*
%_K5lib/libKF5Sane.so.*

%changelog
* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- initial build
