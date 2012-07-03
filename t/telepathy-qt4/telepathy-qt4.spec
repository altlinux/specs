%define qt4_ver %{get_version libqt4-devel}

Name: telepathy-qt4
Version: 0.9.1
Release: alt1

Summary: Telepathy framework - Qt4 connection manager library 
License: GPLv2
Group: System/Libraries 

URL: http://telepathy.freedesktop.org/wiki/Telepathy%%20Qt
Packager: Nazarov Denis <nenderus@altlinux.ru>

Source0: http://telepathy.freedesktop.org/releases/telepathy-qt4/%name-%version.tar.gz
Patch1: alt-fix-install.patch
Patch2: alt-pkgconfig.patch

# Automatically added by buildreq on Tue Apr 03 2012 (-bi)
# optimized out: cmake-modules elfutils farstream farstream-devel fontconfig glib2-devel gstreamer-devel libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libqt4-clucene libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel libtelepathy-farstream libtelepathy-glib libtelepathy-glib-devel libxml2-devel pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-xml xml-utils
#BuildRequires: cmake doxygen gcc-c++ git-core graphviz gst-plugins-devel libicu libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libtelepathy-farstream-devel phonon-devel python-module-dbus python-module-distribute qt4-doc-html
BuildRequires(pre): libqt4-devel
BuildRequires: cmake doxygen gcc-c++ git-core graphviz gst-plugins-devel qt4-doc-html phonon-devel
BuildRequires: farstream-devel libtelepathy-farstream-devel
BuildRequires: python-module-dbus python-module-distribute
BuildRequires: kde-common-devel

%description
Telepathy-Qt4 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 4.

%package -n lib%name
Summary: Telepathy framework - Qt4 connection manager library 
Group: System/Libraries
Requires: farstream
%description -n lib%name
Telepathy-Qt4 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 4.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development libraries and header files for %name.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export PATH=%_qt4dir/bin:$PATH
export QT_DOC_DIR=%_docdir/qt-%qt4_ver
%Kbuild
pushd BUILD*/
make doxygen-doc
popd

%install
%Kinstall

%files -n lib%name
%doc AUTHORS COPYING HACKING NEWS README BUILD*/doc/html
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/cmake/TelepathyQt4/
%_libdir/cmake/TelepathyQt4Farstream/
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/telepathy-qt4

%changelog
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
