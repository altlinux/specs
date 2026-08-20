%def_enable qt5

%define sover 15
%define libqgpgme libqgpgme%sover
%define libqgpgme6 libqgpgmeqt6_%sover

Name: gpgmeqt
Version: 2.1.0
Release: alt2

Summary: Qt bindings for GPGME
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://www.gnupg.org/software/gpgme/index.html
Vcs: git://git.gnupg.org/qgpgme.git

Source: gpgmeqt-%version.tar

BuildRequires: cmake gcc-c++ gpgme2-devel gpgmepp-devel qt6-base-devel
%if_enabled qt5
BuildRequires: qt5-base-devel
%endif

%package -n %libqgpgme
Group: System/Libraries
Summary: Qt5 QGpgME library

%description -n %libqgpgme
Qt5 binding library for GPGME.

%package -n %libqgpgme6
Group: System/Libraries
Summary: Qt6 QGpgME library

%description -n %libqgpgme6
Qt6 binding library for GPGME.

%package -n gpgmeqt-devel
Summary: Include files for development with QGpgME
Group: Development/C++
Requires: gpgme2-devel
Requires: gpgmepp-devel
#
Provides: qgpgme-devel = %version
Provides: libgpgme-devel = %version-%release
Obsoletes: libgpgme-devel < %version-%release
Provides: libgpgme1-devel = %version-%release
Obsoletes: libgpgme1-devel < %version-%release

%description -n gpgmeqt-devel
This package contains headers and CMake/pkg-config files for QGpgME.

%description
QGpgME provides Qt bindings for GPGME.

%prep
%setup -n gpgmeqt-%version

%build
mkdir -p BUILD
pushd BUILD
%cmake .. \
    -DBUILD_WITH_QT5=%{?_enable_qt5:ON}%{!?_enable_qt5:OFF} \
    -DBUILD_WITH_QT6=ON \
    #
%cmake_build
popd

%install
pushd BUILD
%cmake_install
popd

%if_enabled qt5
%files -n %libqgpgme
%_libdir/libqgpgme.so.%sover
%_libdir/libqgpgme.so.*
%endif

%files -n %libqgpgme6
%_libdir/libqgpgmeqt6.so.%sover
%_libdir/libqgpgmeqt6.so.*

%files -n gpgmeqt-devel
%_includedir/qgpgme-qt*/
%_libdir/lib*.so
%_libdir/cmake/QGpgme*/
#%_pkgconfigdir/qgpgme*.pc

%changelog
* Thu Aug 20 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- return gpgmeqt-devel subpackage after upgrade

* Thu Jul 09 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- initial build
