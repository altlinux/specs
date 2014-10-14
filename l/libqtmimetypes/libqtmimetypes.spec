Name: libqtmimetypes
Version: 1.0.1
Release: alt1

Summary: MIME type library for Qt4
License: GPLv2
Group: System/Libraries

Url: http://qt.gitorious.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ libqt4-devel

%description
%summary

%package devel
Summary: Development headers for QtMimeTypes library
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for %name.

%prep
%setup
sed -i 's,\(LIBDIR.*\)lib$,\1%_lib,' mimetypes-nolibs.pri

%build
qmake-qt4 PREFIX=%prefix SYSTEMQTSA=True
%make_build

%install
make install INSTALL_ROOT=%buildroot

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc

%changelog
* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- built for ALT Linux (required by libqtxdg-1.0.0)

