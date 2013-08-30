Name: qextserialport
Version: 1.2rc
Release: alt1
Summary: Qt interface class for old fashioned serial ports
License: MIT
Group: System/Libraries
Url: http://code.google.com/p/qextserialport/

Packager: Ivan Ovcherenko <asdus@altlinux.org>

Source0: %name-%version.tar
Source1: %name-config.pri

BuildRequires: gcc-c++
BuildRequires: qt4-devel
BuildRequires: libudev-devel

%description
QextSerialPort provides an interface to old fashioned serial ports
for Qt-based applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
#Requires: qt4-devel

%description devel
This package contains the files necessary to develop applications
using Qextserialport.

%prep
%setup
cp -a %SOURCE1 config.pri

%build
%qmake_qt4
#qmake-qt4
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files 
%doc ChangeLog LICENSE
%_libdir/*.so.*

%files devel
%_includedir/qt4/QtExtSerialPort/
%_libdir/*.so
%_datadir/qt4/mkspecs/features/*

%changelog
* Fri Jun 07 2013 Ivan Ovcherenko <asdus@altlinux.org> 1.2rc-alt1
- Initial release
