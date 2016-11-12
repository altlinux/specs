%define _name qtermwidget

Name: %_name-qt5
Version: 0.7.0
Release: alt1

Summary: unicode-enabled, embeddable QT5 terminal widget
License: GPLv2+
Group: Terminals

Url: http://github.com/qterminal/%_name
#VCS: https://github.com/lxde/qtermwidget.git
Source: %_name-%version.tar.gz

BuildRequires: cmake gcc-c++ qt5-base-devel

%description
QTermWidget is an opensource project based on KDE Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable QT5 widget for using as a built-in
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
%setup -n %_name-%version

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files

%files data
%_datadir/%{_name}*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS README*
%_includedir/*
%_libdir/*.so
#%_qt5_plugindir/designer/lib%{_name}*plugin.so
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Thu Jul 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- updated to 0.6.0-82-g4b0662d
- built against Qt5 libraries

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (see also #30468)
- updated Url:

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- initial build (loosely based on qterminal.spec and upstream one)

