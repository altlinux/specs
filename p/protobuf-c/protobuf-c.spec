%define soversion 1

Name: protobuf-c
Version: 1.3.0
Release: alt1
Summary: Google's Protocol Buffers implementation in C

Group: System/Libraries
License: ASL 2.0
Url: https://github.com/protobuf-c/protobuf-c

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel >= 2.5.0 protobuf-compiler

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package compiler
Summary: Protocol Buffers Compiler
Group: Development/Other
Requires: lib%{name}%{soversion} = %version-%release

%description compiler
Compiler for protocol buffer definition files.

%package -n lib%{name}%{soversion}
Summary: Protocol Buffer C library.
Group: System/Libraries
Provides: lib%{name} = %version-%release

%description -n lib%{name}%{soversion}
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%{name}%{soversion} = %version-%release

%description -n lib%{name}-devel
This package contains development files required for packaging
%name.

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

%files compiler
%_bindir/protoc-c
%_bindir/protoc-gen-c

%files -n lib%{name}%{soversion}
%_libdir/*.so.*

%files -n lib%{name}-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%doc TODO ChangeLog README.md LICENSE

%changelog
* Fri Jan 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Updated to upstream version 1.3.0.

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- 1.1.1
- build with protobuf 2.6

* Mon Aug 11 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Thu Jul 31 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt2
- rebuilt for protobuf-2.5.0

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- initial build for ALT Linux Sisyphus
