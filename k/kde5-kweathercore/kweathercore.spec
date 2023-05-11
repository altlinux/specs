%define rname kweathercore

%define sover 5
%define libkweathercore libkf5weathercore

Name: kde5-%rname
Version: 0.7
Release: alt2
%K5init altplace

Group: System/Libraries
Summary: QToolButton with color popup menu with lets you select a color
Url: https://invent.kde.org/libraries/kweathercore
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-clear-country-name.patch

# Automatically added by buildreq on Tue Apr 25 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libgpg-error libp11-kit libqt5-core libqt5-network libqt5-positioning libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules git-core kf5-kholidays-devel kf5-ki18n-devel python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-location-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-location-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kholidays-devel kf5-ki18n-devel

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

%package -n %libkweathercore
Group: System/Libraries
Summary: KF5 library
#Requires: %name-common = %version-%release
%description -n %libkweathercore
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K5install
#find_lang %name --with-kde --all-name

%files devel
%_K5inc/KWeatherCore/
%_K5inc/kweathercore_version.h
%_libdir/cmake/KF5KWeatherCore/
%_K5link/lib*.so
%_K5archdata/mkspecs/modules/qt_KWeatherCore.pri

%files -n %libkweathercore
%doc LICENSES/* README.md
%_K5lib/libKF5KWeatherCore.so.%sover
%_K5lib/libKF5KWeatherCore.so.*

%changelog
* Thu May 11 2023 Sergey V Turchin <zerg@altlinux.org> 0.7-alt2
- clear country names

* Tue Apr 25 2023 Sergey V Turchin <zerg@altlinux.org> 0.7-alt1
- initial build
