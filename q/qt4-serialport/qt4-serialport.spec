Name: qt4-serialport
Version: 5.3.3
Release: alt1

Summary: Qt4 interface class for serial ports

License: MIT
Group: System/Libraries
Url: http://qt-project.org/wiki/QtSerialPort

# Source-git: git clone git://gitorious.org/qt/qtserialport.git
Source: %name-%version.tar

# Automatically added by buildreq on Mon Nov 17 2014
# optimized out: fontconfig libcloog-isl4 libqt4-core libqt4-gui libqt4-test libstdc++-devel phonon-devel pkg-config python3-base
BuildRequires: gcc-c++ glibc-devel libdb4-devel libqt4-devel libudev-devel

%description
The QtSerialPort module is an add-on module for the Qt4 library,
providing a single interface for both hardware and virtual serial ports.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
#Requires: qt4-devel

%description devel
This package contains the files necessary to develop applications
using %name.

%prep
%setup
#__subst "s|examples tests||g" qtserialport.pro

%build
%qmake_qt4
%make_build
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%doc LICENSE*
%_libdir/*.so.*

%files devel
%_includedir/qt4/QtSerialPort/
%_libdir/*.so
%_libdir/libQtSerialPort.prl
%_datadir/qt4/mkspecs/features/serialport.prf


%changelog
* Mon Nov 17 2014 Vitaly Lipatov <lav@altlinux.ru> 5.3.3-alt1
- initial build for ALT Linux Sisyphus
