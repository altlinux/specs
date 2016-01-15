%define qt4_ver %{get_version libqt4-devel}
%define farstream farstream0.2
%define farstream_dev  pkgconfig(farstream-0.2) libtelepathy-farstream-devel

Name: telepathy-qt4
Version: 0.9.6.1
Release: alt3

Summary: Telepathy framework - Qt4 connection manager library 
License: GPLv2
Group: System/Libraries 

URL: http://telepathy.freedesktop.org/wiki/Telepathy%%20Qt
Packager: Nazarov Denis <nenderus@altlinux.ru>

Source: telepathy-qt-%version.tar
# FC
Patch20: telepathy-qt-0.9.5-static_fPIC.patch
Patch21: 0002-CMakeLists-Minimum-version-bumped-to-2.8.12.patch
Patch22: 0021-Farstream-gst-gstconfig.h-can-be-in-LIBDIR-search-fo.patch

# Automatically added by buildreq on Tue Apr 03 2012 (-bi)
# optimized out: cmake-modules elfutils farstream farstream-devel fontconfig glib2-devel gstreamer-devel libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libqt4-clucene libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel libtelepathy-farstream libtelepathy-glib libtelepathy-glib-devel libxml2-devel pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-xml xml-utils
#BuildRequires: cmake doxygen gcc-c++ git-core graphviz gst-plugins-devel libicu libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libtelepathy-farstream-devel phonon-devel python-module-dbus python-module-distribute qt4-doc-html
BuildRequires(pre): libqt4-devel
BuildRequires: cmake doxygen gcc-c++ git-core graphviz phonon-devel
BuildRequires: libxml2-devel glib2-devel libdbus-devel libdbus-glib-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: %farstream_dev
BuildRequires: python-module-dbus python-module-distribute
BuildRequires: kde-common-devel

%description
Telepathy-Qt4 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 4.

%package -n lib%name
Summary: Telepathy framework - Qt4 connection manager library 
Group: System/Libraries
Requires: %farstream
%description -n lib%name
Telepathy-Qt4 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 4.

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
%patch20 -p1
%patch21 -p1
%patch22 -p1

%build
export PATH=%_qt4dir/bin:$PATH
export QT_DOC_DIR=%_docdir/qt-%qt4_ver
%cmake \
    -DDESIRED_QT_VERSION=4 \
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
%_libdir/cmake/TelepathyQt4/
%_libdir/cmake/TelepathyQt4Farstream/
%_libdir/cmake/TelepathyQt4Service/
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/telepathy-qt4

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

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt2
- add upstream fixes

* Mon Sep 29 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt1
- new version
- build with gstreamer1

* Mon Jun 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.4-alt0.M70P.1
- built for M70P

* Mon Jun 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.4-alt1
- new version

* Thu Nov 14 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt6.M70P.1
- built for M70P

* Wed Nov 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt7
- fix to build with new cmake
- fix storing avatars

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt5.M70P.1
- built for M70P

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt6
- enable accounts by default

* Tue Jun 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt5
- connect automatically by default

* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt4
- fix requires

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt3
- clean build requires

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt2
- fix build requires

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- new version

* Mon Mar 26 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Nov 17 2011 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Mon Oct 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.3-alt1
- Version 0.7.3

* Mon Aug 08 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt0.M60T.1
- Build for branch t6

* Mon Aug 08 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Sat Jun 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt0.M60T.1
- Build for branch t6

* Sat Jun 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Sun Jun 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt0.M60T.1
- Build for branch t6

* Sun Jun 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Thu Jun 02 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt0.M60T.1
- Build for branch t6

* Thu Jun 02 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Fri May 27 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt0.M60T.1
- Build for branch t6

* Tue May 17 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Tue May 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.16-alt1
- Version 0.5.16

* Wed Apr 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.15-alt1
- Initial build for ALT Linux
