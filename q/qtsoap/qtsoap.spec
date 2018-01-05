Name: qtsoap
Version: 2.7
Release: alt2%ubt

Group: System/Libraries
Summary: The Simple Object Access Protocol Qt-based client side library
Url: http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtsoap/
License: LGPLv2 with exceptions or GPLv3

#http://get.qt.nokia.com/qt/solutions/lgpl/
Source: qtsoap-%version.tar.gz
# FC
Patch1: qtsoap-2.7_1-opensource-install-pub-headers.patch
Patch2: qtsoap-2.7_1-qt5-cleanups.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glibc-devel-static phonon-devel libqt4-devel qt5-base-devel

%description
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

%package -n lib%name
Group: System/Libraries
Summary: The Simple Object Access Protocol Qt-based client side library

%description -n lib%name
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT

%description devel
Development files for %name.

%package -n libqtsoap5
Summary: The Simple Object Access Protocol Qt5-based client side library
Group: System/Libraries

%description -n libqtsoap5
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt5-based applications.
This package is built against Qt5.

%package -n qtsoap5-devel
Summary: Development files for qtsoap5
Group: Development/KDE and QT
Requires: libqtsoap5 = %version-%release

%description -n qtsoap5-devel
Development files for qtsoap5.

%prep
%setup -c -n %name
pushd %name-%version
%patch1 -p1 -b .install-pub-headers
# Fix build for qt5
%patch2 -p1 -b .qt5
popd

sed -i 's:$$DESTDIR:%_libdir:g' qtsoap-%version/buildlib/buildlib.pro

cp -a %name-%version qtsoap5-%version

%build
pushd %name-%version
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri
echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%version" >> common.pri

qmake-qt4 PREFIX=%prefix 'QMAKE_CFLAGS+=%optflags' 'QMAKE_CXXFLAGS+=%optflags'
%make_build
popd

pushd qtsoap5-%version
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri
echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap5)" >> common.pri
echo "VERSION=%{version}" >> common.pri

#qmake_qt5 PREFIX=%_prefix 'QMAKE_CFLAGS+=%optflags' 'QMAKE_CXXFLAGS+=%optflags'
#make_build -fPIC -DQT_DISABLE_DEPRECATED_BEFORE=0x000000"
%qmake_qt5 PREFIX=%_prefix
%make_build CXXFLAGS="%{optflags} -fPIC -DQT_DISABLE_DEPRECATED_BEFORE=0x000000"
popd

%install
pushd %name-%version
make INSTALL_ROOT=%buildroot install
popd

pushd qtsoap5-%version
make INSTALL_ROOT=%buildroot install
popd

%files -n lib%name
%doc %name-%version/README.TXT
%_libdir/libqtsoap.so.*

%files devel
%_libdir/libqtsoap.so
%_includedir/qt4/QtSoap/

%files -n libqtsoap5
%doc %name-%version/README.TXT
%_libdir/libqtsoap5.so.*

%files -n qtsoap5-devel
%_libdir/libqtsoap5.so
%_includedir/qt5/QtSoap/

%changelog
* Fri Jan 05 2017 Anton Midyukov <antohami@altlinux.org> 2.7-alt2%ubt
- build qtsoap5

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.7-alt1
- initial build
