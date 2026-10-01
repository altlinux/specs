%def_disable qt5

%define sover 15
%define libqgpgme libqgpgme-dqt5_%sover
%define libqgpgme6 libqgpgme-dqt6_%sover

Name: gpgmedqt
Version: 2.1.0
Release: alt1.dde.1

Summary: Qt bindings for GPGME
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://www.gnupg.org/software/gpgme/index.html
Vcs: git://git.gnupg.org/qgpgme.git

Source: gpgmedqt-%version.tar

BuildRequires: cmake gcc-c++ gpgme2-devel gpgmepp-devel dqt6-base-devel
BuildRequires: libdqt6-test
%if_enabled qt5
BuildRequires: dqt5-base-devel
%endif

# find libraries
%add_findprov_lib_path %_dqt6_libdir

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

%package -n libgpgme-dqt6-devel
Summary: Include files for development with QGpgME
Group: Development/C++
Requires: gpgme2-devel
Requires: gpgmepp-devel
#
# Provides: qgpgme-devel = %version
# Provides: libgpgme-devel = %version-%release
# Obsoletes: libgpgme-devel < %version-%release
# Provides: libgpgme1-devel = %version-%release
# Obsoletes: libgpgme1-devel < %version-%release

%description -n libgpgme-dqt6-devel
This package contains headers and CMake/pkg-config files for QGpgME.

%description
QGpgME provides Qt bindings for GPGME.

%prep
%setup -n gpgmedqt-%version

%build
%DQ6build .. \
    -DBUILD_WITH_QT5=%{?_enable_qt5:ON}%{!?_enable_qt5:OFF} \
    -DBUILD_WITH_QT6=ON \
    -DCMAKE_INSTALL_INCLUDEDIR=%_dqt6_headerdir \
    -DCMAKE_INSTALL_LIBDIR=%_dqt6_libdir \
    #

%install
%DQ6install

%if_enabled qt5
%files -n %libqgpgme
%_dqt5_libdir/libqgpgme.so.%sover
%_dqt5_libdir/libqgpgme.so.*
%endif

%files -n %libqgpgme6
%_dqt6_libdir/libqgpgmeqt6.so.%sover
%_dqt6_libdir/libqgpgmeqt6.so.*

%files -n libgpgme-dqt6-devel
%_dqt6_headerdir/qgpgme-qt*/
%_dqt6_libdir/lib*.so
%_dqt6_libdir/cmake/QGpgme*/
#%_dqt6_libdir/pkgconfig/qgpgme*.pc

%changelog
* Thu Oct 01 2026 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1.dde.1
- fork for independent deepin build

* Thu Aug 20 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- return gpgmeqt-devel subpackage after upgrade

* Thu Jul 09 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- initial build
