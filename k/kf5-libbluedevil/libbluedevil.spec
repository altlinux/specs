%define rname libbluedevil
%define sover 5
%define libbluedevil libbluedevil%sover

Name: kf5-%rname
Version: 5.2.2
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 Bluetooth functionality handling
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 26 2015 (-bi)
# optimized out: cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-dbus libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake extra-cmake-modules gcc-c++ qt5-base-devel

%description
Bluetooth functionality handling library

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

%package -n %libbluedevil
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libbluedevil
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIB_INSTALL_DIR=%_K5lib \
    #

%install
%K5install
mkdir -p %buildroot/%_K5inc
mv %buildroot/%_includedir/bluedevil %buildroot/%_K5inc/
%find_lang %name --all-name

%files common -f %name.lang
#%doc COPYING.LIB README.md

%files devel
#%_K5inc/bluedevil_version.h
%_K5inc/bluedevil/
%_K5link/lib*.so
#%_K5lib/cmake/BlueDevil
#%_K5archdata/mkspecs/modules/qt_BlueDevil.pri
#%_pkgconfigdir/bludevil.pc

%files -n %libbluedevil
%_K5lib/libbluedevil.so.%sover
%_K5lib/libbluedevil.so.%sover.*

%changelog
* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
