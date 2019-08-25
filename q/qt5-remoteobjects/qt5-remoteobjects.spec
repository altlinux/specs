%define qt_module qtremoteobjects
%define kf5_bindir %prefix/lib/kf5/bin

Name:    qt5-remoteobjects
Summary: Qt5 - Qt Remote Objects
Group: System/Libraries
Version: 5.12.4
Release: alt1

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
Source: %name-%version.tar

BuildRequires: qt5-base-devel >= %version
BuildRequires: qt5-declarative-devel

Requires: %name-common = %EVR

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
module developed for Qt.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %EVR
Requires: qt5-base-devel

%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# fix verify-elf: ERROR
mkdir -p %buildroot%kf5_bindir
mv %buildroot%_qt5_bindir/repc %buildroot%kf5_bindir
ln -s %kf5_bindir/repc %buildroot%_qt5_bindir/repc

# removes static library
rm -fr %buildroot%_qt5_libdir/*.la

%files
%doc LICENSE.*
%_qt5_libdir/libQt5RemoteObjects.so.5*
%_qt5_bindir/repc
%kf5_bindir/repc
## split out? -- rex
%_qt5_qmldir/QtQml/RemoteObjects/
%_qt5_qmldir/QtRemoteObjects/

%files common

%files devel
%_qt5_headerdir/QtRemoteObjects/
%_qt5_headerdir/QtRepParser/
%_qt5_libdir/libQt5RemoteObjects.so
%_qt5_libdir/libQt5RemoteObjects.prl
%_qt5_libdir/cmake/Qt5RemoteObjects/
%_qt5_libdir/cmake/Qt5RepParser
%_qt5_libdir/pkgconfig/Qt5RemoteObjects.pc
%_qt5_archdatadir/mkspecs/features/*
%_qt5_archdatadir/mkspecs/modules/*

%files doc
%_qt5_examplesdir/*

%changelog
* Sun Aug 25 2019 Anton Midyukov <antohami@altlinux.org> 5.12.4-alt1
- Initial build for ALT
