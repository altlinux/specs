%def_disable qt4

%define commit0 ad9bc4600ce769a8b3ad10910803cd555811b70c

%define upstreamver 2.6_1-opensource
%define upname qtsingleapplication

Name: lib%upname
Version: 2.6.1
Release: alt4
Url: http://doc.qt.digia.com/solutions/4/qtsingleapplication/qtsingleapplication.html
Group: System/Libraries
License: LGPLv2.1 GPLv3
Summary: The QtSingleApplication component provides support for applications that can be only started once per user
# Source-url: https://github.com/qtproject/qt-solutions/archive/%commit0.tar.gz#/%name-%commit0.tar.gz
Source: %upname-%version.tar
# Proposed upstream in https://codereview.qt-project.org/#/c/92417/
Source1: qtsingleapplication.prf
# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Source2: qtsinglecoreapplication.prf
# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Patch2: qtsingleapplication-build-qtsinglecoreapplication.patch
# Features for unbundling in Qupzilla, https://github.com/QupZilla/qupzilla/issues/1503
Patch3: qtsingleapplication-qupzilla.patch

BuildRequires: gcc-c++
%if_enabled qt4
BuildRequires: libqt4-devel
%endif
BuildRequires: qt5-base-devel

%description
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.
For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

%package devel
Group: Development/C++
Summary: The QtSingleApplication component provides support for applications that can be only started once per user
Requires: %name

%description devel
This package contains libraries and header files for developing applications
that use QtSingleApplication with Qt4.

%package qt5
Group: Development/C++
Summary: The QtSingleApplication component provides support for applications that can be only started once per user

%description qt5
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.
For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

This is a special build against Qt5.

%package qt5-devel
Group: Development/C++
Summary: The QtSingleApplication component provides support for applications that can be only started once per user
Requires: %name-qt5

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtSingleApplication with Qt5.

%prep
%setup -n %upname-%version/%upname
%patch2 -p0
%patch3 -p1

# use versioned soname
sed -i "s,head,%(echo '%version' |sed -r 's,(.*)\..*,\1,'),g" common.pri

mkdir qt5
cp -p %SOURCE1 %SOURCE2 qt5
sed -i -r 's,-lQt,\05,' qt5/qtsingleapplication.prf
sed -i -r 's,-lQt,\05,' qt5/qtsinglecoreapplication.prf

# additional header needed for Qt5.5
sed -i -r 's,.include,\0 <QtCore/QDataStream>\n\0,' src/qtlocalpeer.h

%build
echo yes | ./configure -library
%if_enabled qt4
qmake-qt4
%make_build
%endif

pushd qt5
%qmake_qt5 ..
%make_build
popd

%install
# libraries
mkdir -p %buildroot%_libdir
cp -a lib/* %buildroot%_libdir
# headers
mkdir -p %buildroot%_includedir/QtSolutions
cp -a \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %buildroot%_includedir/QtSolutions
mkdir -p %buildroot%_qt5_headerdir
# symlink is not possible due to split into individual subpackages
cp -ap %buildroot%_includedir/QtSolutions %buildroot%_qt5_headerdir

# features
%if_enabled qt4
mkdir -p %buildroot%_datadir/qt4/mkspecs/features
install -p -m644 %SOURCE1 %SOURCE2 %buildroot%_datadir/qt4/mkspecs/features
%endif
mkdir -p %buildroot%_qt5_archdatadir/mkspecs/features
install -p -m644 qt5/*.prf %buildroot%_qt5_archdatadir/mkspecs/features

%if_enabled qt4
%files
%_libdir/libQtSolutions*.so.*
%files devel
%doc doc/html README.TXT
%_libdir/libQtSolutions*.so
%_includedir/QtSolutions/
%_datadir/qt4/mkspecs/features/*.prf
%endif

%files qt5
%_libdir/libQt5*.so.*

%files qt5-devel
%doc doc/html README.TXT
%_libdir/libQt5*.so
%_qt5_headerdir/QtSolutions/
%_qt5_archdatadir/mkspecs/features/*.prf

%changelog
* Fri Nov 12 2021 Sergey V Turchin <zerg@altlinux.org> 2.6.1-alt4
- build without qt4

* Sat Nov 17 2018 Anton Midyukov <antohami@altlinux.org> 2.6.1-alt3
- new snapshot
- initial build libqtsingleapplication-qt5

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 2.6.1-alt2
- fix build for Sisyphus

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 2.6.1-alt1
- initial build for ALT Linux from OpenSUSE package
