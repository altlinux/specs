%define _name protobuf-c

Name: lib%_name
Version: 0.15
Release: alt1
Summary: C bindings for Google's Protocol Buffers

Group: System/Libraries
License: ASL 2.0
Url: http://code.google.com/p/protobuf-c/

Source: http://protobuf-c.googlecode.com/files/protobuf-c-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel protobuf-compiler

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package devel
Summary: Protocol Buffers C headers and libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure --disable-static
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_bindir/protoc-c
%_libdir/libprotobuf-c.so.*
%doc TODO ChangeLog

%files devel
%dir %_includedir/google
%_includedir/google/protobuf-c
%_libdir/libprotobuf-c.so
%_pkgconfigdir/libprotobuf-c.pc

%changelog
* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- initial build for ALT Linux Sisyphus
