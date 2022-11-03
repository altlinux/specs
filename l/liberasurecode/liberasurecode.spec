%define _unpackaged_files_terminate_build 1

Name: liberasurecode
Version: 1.6.3
Release: alt1
Summary: Erasure Code API library written in C with pluggable backends
Group: System/Libraries

License: BSD-2-Clause
Url: https://github.com/openstack/liberasurecode.git
Source: %name-%version.tar
Patch1: liberasurecode-1.6.1-Fix-linking.patch
Patch2: liberasurecode-1.6.0-docs.patch

BuildRequires: doxygen
BuildRequires: zlib-devel

%description
An API library for Erasure Code, written in C. It provides a number
of pluggable backends, such as Intel ISA-L library.

%package doc
Summary: Documentation for %name
Group: System/Libraries

%description doc
The documentation for %name.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%autoreconf
%configure --disable-static --disable-mmi
%make_build

%install
%makeinstall_std

%files
%doc README.md COPYING
%_libdir/*.so.*

%files doc
%_docdir/liberasurecode/html/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Nov 03 2022 Alexey Shabalin <shaba@altlinux.org> 1.6.3-alt1
- Build new version.

* Wed May 13 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- Build new version.
- Add a patch for using strncpy on binary data.

* Fri May 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Build new version.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT

