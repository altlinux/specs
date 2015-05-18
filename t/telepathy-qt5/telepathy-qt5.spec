%define farstream farstream0.2
%define farstream_dev  pkgconfig(farstream-0.2) libtelepathy-farstream-devel

Name: telepathy-qt5
Version: 0.9.5
Release: alt1

Summary: Telepathy framework - Qt5 connection manager library 
License: GPLv2
Group: System/Libraries

URL: http://telepathy.freedesktop.org/wiki/Telepathy%%20Qt

Source: telepathy-qt-%version.tar
# SuSE
Patch10: Add-missing-QObject-include.patch
Patch11: add-the-telepathy-qt-include.patch
# ALT
Patch100: alt-fix-install.patch

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
%patch10 -p1
%patch11 -p1
%patch100 -p1

find -type f -name \*.pc.in | \
while read f ; do
    sed -i 's|${CMAKE_INSTALL_PREFIX}||g' $f
done

%build
export PATH=%_qt5_bindir:$PATH
export QT_DOC_DIR=%_qt5_docdir
%Kbuild \
    -DDESIRED_QT_VERSION=5 \
    -DENABLE_FARSTREAM:BOOL=ON \
    -DENABLE_FARSIGHT:BOOL=OFF \
    -DQT_DOC_DIR=%_qt5_docdir \
    -DENABLE_TESTS=OFF \
    -DENABLE_EXAMPLES=OFF \
    -DDISABLE_WERROR=ON \
    #
pushd BUILD*/
make doxygen-doc
popd

%install
%Kinstall

%files -n lib%name
%doc AUTHORS COPYING HACKING NEWS README BUILD*/doc/html
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/cmake/TelepathyQt5*/
%_libdir/lib*.so
%_pkgconfigdir/TelepathyQt5*.pc
%_includedir/telepathy-qt5

%files -n lib%name-devel-static
%_libdir/lib*.a

%changelog
* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt1
- initial build
