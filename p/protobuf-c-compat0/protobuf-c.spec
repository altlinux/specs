
%define soversion 0
%define _name protobuf-c

Name: %{_name}-compat%{soversion}
Version: 0.15
Release: alt3
Summary: C bindings for Google's Protocol Buffers

Group: System/Libraries
License: ASL 2.0
Url: http://code.google.com/p/protobuf-c/

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel protobuf-compiler

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

%package -n lib%{_name}%{soversion}
Summary: Protocol Buffer c++ library.
Group: System/Libraries
Provides: lib%{_name} = %version-%release

%description -n lib%{_name}%{soversion}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

%prep
%setup -q

%build
%autoreconf
%configure --disable-static
%make_build

%check
%make check

%install
%makeinstall_std

%files -n lib%{_name}%{soversion}
%_libdir/*.so.*

%changelog
* Thu Jul 31 2014 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt3
- build only library package for compat

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt2
- rebuilt for protobuf-2.5.0

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- initial build for ALT Linux Sisyphus
