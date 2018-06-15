Name:		capnproto
Version:	0.6.1
Release:	alt1
Summary:	A data interchange format and capability-based RPC system
License:	MIT
Url:		https://capnproto.org
Source:		%name-%version.tar
Group:		Development/C

BuildRequires:	cmake >= 3.1.0 rpm-macros-cmake ctest
BuildRequires:	gcc-c++

%description
Cap'n Proto is data interchange format and capability-based RPC system.
Think JSON, except binary. Or think Protocol Buffers, except faster.

This package contains the schema compiler and command-line encoder and
decoder tools.

%package libs
Summary:	Libraries for %{name}
Group:		System/Libraries

%description libs
The %{name}-libs package contains the libraries for using %{name}
in applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Group:		Development/C

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
cd c++
%autoreconf -i
%configure
%make_build

%install
cd c++
%makeinstall_std

%check
cd c++
# disable networking test
subst '/TEST(AsyncIo, SimpleNetwork)/,/^}/s/^/\/\//' src/kj/async-io-test.c++
%make_build check

%files
%_bindir/cap*

%files libs
%doc LICENSE CONTRIBUTORS README.md
%_libdir/*.so*

%files devel
%_includedir/*
%_libdir/*.a
%_libdir/pkgconfig/*.pc
# not created if cmake is not used
#%_libdir/cmake/CapnProto/

%changelog
* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 0.6.1-alt1
- Initial build of capnproto for ALT.

