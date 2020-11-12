%define major 5
%define oname libucl

Name: %oname%major
Version: 0.8.1
Release: alt1

Summary: universal configuration language

License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/vstakhov/libucl

# repacked https://github.com/vstakhov/libucl/archive/%version.tar.gz
Source: %oname-%version.tar
Source1: %oname.watch

%description
UCL is heavily infused by nginx configuration as the example of a convenient
configuration system. However, UCL is fully compatible with JSON format and is
able to parse json files.

%package devel
Summary: development files for universal configuration language
Group: Development/C
Requires: %oname%major

%description devel
UCL is heavily infused by nginx configuration as the example of a convenient
configuration system. However, UCL is fully compatible with JSON format and is
able to parse json files.

This package contains the %name development library and header files.

%prep
%setup -n %oname-%version

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog.md COPYING README.md
%_libdir/libucl.so.%major
%_libdir/libucl.so.%major.*

%files devel
%_libdir/libucl.so
%_includedir/*
%_pkgconfigdir/libucl.pc
%_man3dir/libucl.3*

%changelog
* Thu Nov 12 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt1
- Initial build for ALT Sisyphus.

