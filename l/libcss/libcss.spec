%define soname 0
%define netsurf %_datadir/netsurf-buildsystem

Name: libcss
Version: 0.9.2
Release: alt1

Summary: LibCSS is a CSS (Cascading Style Sheet) parser and selection engine
License: MIT
Group: System/Libraries

Url: https://www.netsurf-browser.org/projects/libcss

# https://download.netsurf-browser.org/libs/releases/
Source: %name-%version.tar

Patch: fix-calloc-args.patch
Patch1: dump-test-build.patch

BuildRequires: gcc-c++ netsurf-buildsystem
BuildRequires: libparserutils-devel
BuildRequires: libwapcaplet-devel

%description
LibCSS is a CSS (Cascading Style Sheet) parser and selection engine, written in
C. It was developed as part of the NetSurf project and is available for use by
other software under the MIT licence.

Features
Parses CSS, good and bad
Simple C API
Low memory usage
Fast selection engine
Portable
Shared library

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
%description -n %name%soname
%name library.

%prep
%setup
subst 's|-std=c99|-std=gnu99|' Makefile
%autopatch -p1

%build
%install
install -d %buildroot
make install PREFIX=%buildroot NSSHARED=%netsurf COMPONENT_TYPE=lib-shared INCLUDEDIR=%_includedir LIBDIR=%_libdir
#fixed prefix in .pc file
subst 's|%buildroot|/usr|' %buildroot%_libdir/pkgconfig/%name.pc
sed -i 's/\/\/usr\//\//g' %buildroot%_libdir/pkgconfig/%name.pc

%check
%make_build NSSHARED=%netsurf test

%files devel
%doc COPYING README
%_includedir/%name
%_libdir/pkgconfig/%name.pc
%_libdir/%name.so

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%changelog
* Fri Jul 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux.

