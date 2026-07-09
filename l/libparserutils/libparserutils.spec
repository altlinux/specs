%define soname 0
%define oname parserutils
%define netsurf %_datadir/netsurf-buildsystem

Name: libparserutils
Version: 0.2.5
Release: alt1

Summary: Library for building efficient parsers, written in C
License: MIT
Group: System/Libraries

Url: https://www.netsurf-browser.org/projects/libparserutils

# https://download.netsurf-browser.org/libs/releases/
Source: %name-%version.tar

BuildRequires: gcc-c++ netsurf-buildsystem

%description
LibParserUtils is a library for building efficient parsers, written
in C. It was developed as part of the NetSurf project and is available
for use by other software under the MIT licence.

Features:
No mandatory dependencies (iconv() implementation optional for enhanced charset support)
A number of built-in character set converters
Mapping of character set names to/from MIB enum values
UTF-8 and UTF-16 (host endian) support functions
Various simple data structures (resizeable buffer, stack, vector)
A UTF-8 input stream
Simple C API
Portable
Shared library

Charset support:
LibParserUtils has the following built-in charset converters.
- UTF-8
- UTF-16 (platform-native endian)
- ISO-8859-n
- Windows-125n
- US-ASCII

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
%_includedir/%oname
%_libdir/pkgconfig/%name.pc
%_libdir/%name.so

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%changelog
* Thu Jul 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.5-alt1
- Initial build for ALT Linux.

