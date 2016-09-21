%define farstream farstream0.2
%define farstream_dev  pkgconfig(farstream-0.2) libtelepathy-farstream-devel

%define sover 0
%define lib_main libtelepathy-qt5%sover
%define lib_farstream libtelepathy-qt5-farstream%sover
%define lib_service libtelepathy-qt5-service%sover
%define dev_main libtelepathy-qt5%name-devel

Name: telepathy-qt5
Version: 0.9.7
Release: alt1

Summary: Telepathy framework - Qt5 connection manager library 
License: GPLv2
Group: System/Libraries

URL: http://telepathy.freedesktop.org/wiki/Telepathy%%20Qt

Source: telepathy-qt-%version.tar
# FC
Patch1: 0001-FindQt5.cmake-look-in-the-correct-pkg-config-file-fo.patch
Patch2: 0002-FindQt5.cmake-remove-hardcoded-fPIC-flag.patch
Patch3: 0003-CMakeLists.txt-require-python-2.7.patch
Patch4: 0004-Adapt-the-client-registrar-to-the-new-thread-based-i.patch
# ALT
Patch100: alt-fix-linking.patch

BuildRequires(pre): qt5-base-devel qt5-tools
BuildRequires: python < 3 python >= 2.7
BuildRequires: cmake doxygen gcc-c++ git-core graphviz phonon-devel
BuildRequires: libxml2-devel glib2-devel libdbus-devel libdbus-glib-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: %farstream_dev
BuildRequires: python-module-dbus python-module-distribute
BuildRequires: kde-common-devel

%description
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n %lib_main
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
Requires: %farstream
%description -n %lib_main
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n %lib_farstream
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %lib_farstream
%name library.

%package -n %lib_service
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %lib_service
%name library.

%package -n lib%name
Summary: Telepathy framework - Qt5 connection manager library 
Group: System/Libraries
Requires: %lib_main %lib_farstream %lib_service
%description -n lib%name
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package devel
Summary: Development libraries and header files for %name
Group: Development/KDE and QT
Provides: lib%name-devel = %EVR
Obsoletes: lib%name-devel < %EVR
Requires: libtelepathy-glib-devel
%description devel
Development libraries and header files for %name.

%package devel-static
Summary: Static libraries for %name
Group: Development/KDE and QT
Provides: lib%name-devel-static = %EVR
Obsoletes: lib%name-devel-static < %EVR
Requires: %name-devel
%description devel-static
Static libraries for %name.

%prep
%setup -qn telepathy-qt-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p1

%build
export PATH=%_qt5_bindir:$PATH
export QT_DOC_DIR=%_qt5_docdir
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=release \
    -DDESIRED_QT_VERSION=5 \
    -DENABLE_FARSTREAM:BOOL=ON \
    -DENABLE_FARSIGHT:BOOL=OFF \
    -DQT_DOC_DIR=%_qt5_docdir \
    -DENABLE_TESTS=OFF \
    -DENABLE_EXAMPLES=OFF \
    -DDISABLE_WERROR=ON \
    #

%cmake_build
%cmake_build doxygen-doc

%install
%make install DESTDIR=%buildroot -C BUILD

%files common
%doc AUTHORS COPYING HACKING NEWS README

%files -n lib%name

%files -n %lib_main
%_libdir/libtelepathy-qt5.so.%sover
%_libdir/libtelepathy-qt5.so.*
%files -n %lib_farstream
%_libdir/libtelepathy-qt5-farstream.so.%sover
%_libdir/libtelepathy-qt5-farstream.so.*
%files -n %lib_service
%_libdir/libtelepathy-qt5-service.so.%sover
%_libdir/libtelepathy-qt5-service.so.*

%files devel
%doc BUILD*/doc/html
%_libdir/cmake/TelepathyQt5*/
%_libdir/lib*.so
%_pkgconfigdir/TelepathyQt5*.pc
%_includedir/telepathy-qt5

%files devel-static
#%_libdir/lib*.a

%changelog
* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1
- new version

* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt3
- build fixed
- move docs to devel subpackage

* Tue Nov 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt2
- fix data dir path

* Wed Jun 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt1
- new version

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt1
- initial build
