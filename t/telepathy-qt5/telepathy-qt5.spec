%define farstream farstream0.2
%define farstream_dev  pkgconfig(farstream-0.2) libtelepathy-farstream-devel

Name: telepathy-qt5
Version: 0.9.6.1
Release: alt3

Summary: Telepathy framework - Qt5 connection manager library 
License: GPLv2
Group: System/Libraries

URL: http://telepathy.freedesktop.org/wiki/Telepathy%%20Qt

Source: telepathy-qt-%version.tar
# FC
Patch1: telepathy-qt-0.9.5-static_fPIC.patch
Patch2: 0002-CMakeLists-Minimum-version-bumped-to-2.8.12.patch
Patch3: 0021-Farstream-gst-gstconfig.h-can-be-in-LIBDIR-search-fo.patch

BuildRequires(pre): qt5-base-devel qt5-tools
BuildRequires: cmake doxygen gcc-c++ git-core graphviz phonon-devel
BuildRequires: libxml2-devel glib2-devel libdbus-devel libdbus-glib-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: %farstream_dev
BuildRequires: python-module-dbus python-module-distribute
BuildRequires: kde-common-devel

%description
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n lib%name
Summary: Telepathy framework - Qt5 connection manager library 
Group: System/Libraries
Requires: %farstream
%description -n lib%name
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Requires: libtelepathy-glib-devel
%description -n lib%name-devel
Development libraries and header files for %name.

%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/KDE and QT
Requires: lib%name-devel
%description -n lib%name-devel-static
Static libraries for %name.

%prep
%setup -qn telepathy-qt-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export PATH=%_qt5_bindir:$PATH
export QT_DOC_DIR=%_qt5_docdir
%cmake \
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

%files -n lib%name
%doc AUTHORS COPYING HACKING NEWS README
%_libdir/lib*.so.*

%files -n lib%name-devel
%doc BUILD*/doc/html
%_libdir/cmake/TelepathyQt5*/
%_libdir/lib*.so
%_pkgconfigdir/TelepathyQt5*.pc
%_includedir/telepathy-qt5

%files -n lib%name-devel-static
%_libdir/lib*.a

%changelog
* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt3
- build fixed
- move docs to devel subpackage

* Tue Nov 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt2
- fix data dir path

* Wed Jun 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6.1-alt1
- new version

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt1
- initial build
