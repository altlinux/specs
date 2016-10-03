Name: qtermwidget
Version: 0.7.0
Release: alt1

Summary: unicode-enabled, embeddable QT4 terminal widget
License: GPL
Group: Terminals

Url: http://github.com/qterminal/qtermwidget
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Mar 07 2012
# optimized out: cmake-modules fontconfig libqt4-core libqt4-designer libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel
BuildRequires: cmake gcc-c++ phonon-devel qt5-base-devel git-core

%description
QTermWidget is an opensource project based on KDE4 Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable QT4 widget for using as a built-in
console (or terminal emulation widget).

Of course I`m aware about embedding abilities of original
Konsole, but once I had Qt without KDE, and it was a serious
problem.

0.4.0+ is a friendly fork, the original project is still available
at http://qtermwidget.sourceforge.net/

%package data
Summary: unicode-enabled, embeddable QT4 terminal widget shared data
Group: Terminals
BuildArch: noarch

%description data
QTermWidget is an opensource project based on KDE4 Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable QT4 widget for using as a built-in
console (or terminal emulation widget).

This package contains the shared data.

%package -n lib%name
Summary: unicode-enabled, embeddable QT4 terminal widget library
Group: System/Libraries
Requires: %name-data = %version-%release

%description -n lib%name
QTermWidget is an opensource project based on KDE4 Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable QT4 widget for using as a built-in
console (or terminal emulation widget).

This package contains the shared library.

%package -n lib%name-devel
Summary: unicode-enabled, embeddable QT4 terminal widget library
Group: Development/KDE and QT

%description -n lib%name-devel
QTermWidget is an opensource project based on KDE4 Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable QT4 widget for using as a built-in
console (or terminal emulation widget).

This package contains the development headers for the library.

%prep
%setup

%build
%cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%make_build

%install
%makeinstall_std

%files

%files data
%_datadir/%{name}*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS COPYING README
%_includedir/*
%_libdir/*.so
%_libdir/qt4/plugins/designer/lib%{name}*plugin.so
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (see also #30468)
- updated Url:

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- initial build (loosely based on qterminal.spec and upstream one)

