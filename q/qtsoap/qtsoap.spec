Name: qtsoap
Version: 2.7
Release: alt1

Group: System/Libraries
Summary: The Simple Object Access Protocol Qt-based client side library
Url: http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtsoap/
License: LGPLv2 with exceptions or GPLv3

#http://get.qt.nokia.com/qt/solutions/lgpl/
Source: qtsoap-%{version}.tar.gz
# FC
Patch1: qtsoap-2.7_1-opensource-install-pub-headers.patch

# Automatically added by buildreq on Wed Sep 21 2011 (-bi)
# optimized out: elfutils fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-xml libstdc++-devel
#BuildRequires: gcc-c++ glibc-devel-static phonon-devel
BuildRequires: gcc-c++ glibc-devel-static phonon-devel libqt4-devel

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

%prep
%setup -q
%patch1 -p1 -b .install-pub-headers

sed -i 's:$$DESTDIR:%_libdir:g' buildlib/buildlib.pro

%build
echo "SOLUTIONS_LIBRARY = yes" > config.pri
echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%version" >> common.pri

qmake-qt4 PREFIX=%prefix 'QMAKE_CFLAGS+=%optflags' 'QMAKE_CXXFLAGS+=%optflags'
%make_build

%install
%make INSTALL_ROOT=%buildroot install

%files -n lib%name
%doc README.TXT
%_libdir/libqtsoap.so.*

%files devel
%_libdir/libqtsoap.so
%_includedir/qt4/QtSoap/

%changelog
* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.7-alt1
- initial build
