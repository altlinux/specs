%define upstreamver 2.6_1-opensource
%define upname qtsingleapplication

Name: lib%upname
Version: 2.6.1
Release: alt2
Url: http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtsingleapplication/
Group: System/Libraries
License: LGPLv2.1 GPLv3
Summary: The QtSingleApplication component provides support for applications that can be only started once per user
Source0: http://get.qt.nokia.com/qt/solutions/lgpl/qtsingleapplication-%upstreamver.tar.gz
Source1: %upname.prf
Patch0: %upname.diff
Patch1: %upname-getuid.diff

BuildRequires: gcc-c++ libqt4-devel

%description
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.
For console (non-GUI) applications, the QtSingleCoreApplication variant is provided, which avoids dependency on QtGui.

Authors:
--------
    Nokia

%package devel
Group: Development/C++
Summary: The QtSingleApplication component provides support for applications that can be only started once per user
Requires: %name = %version

%description devel
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.
For console (non-GUI) applications, the QtSingleCoreApplication variant is provided, which avoids dependency on QtGui.

Authors:
--------
    Nokia

%prep
%setup -n %upname-%upstreamver
%patch0 -p1
%patch1 -p1


%build
echo yes | ./configure -library
qmake-qt4
%make_build

%install
# libraries
mkdir -p $RPM_BUILD_ROOT%_libdir
cp -a lib/* $RPM_BUILD_ROOT%_libdir
# headers
mkdir -p $RPM_BUILD_ROOT%_includedir/QtSolutions
cp -a \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    $RPM_BUILD_ROOT%_includedir/QtSolutions
# features
mkdir -p $RPM_BUILD_ROOT%_datadir/qt4/mkspecs/features
cp -a %SOURCE1 $RPM_BUILD_ROOT%_datadir/qt4/mkspecs/features

%files
%_libdir/lib*.so.*

%files devel
%doc doc examples INSTALL.TXT LGPL_EXCEPTION.txt LICENSE.* README.TXT
%_libdir/lib*.so
%_includedir/QtSolutions
%_datadir/qt4/mkspecs/features/%upname.prf

%changelog
* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 2.6.1-alt2
- fix build for Sisyphus

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 2.6.1-alt1
- initial build for ALT Linux from OpenSUSE package
