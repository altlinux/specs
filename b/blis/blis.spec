%define _unpackaged_files_terminate_build 1
%define soname 4
# arm64 build fails with error
# lto1: warning: switch '-mcpu=cortex-a53' conflicts with '-march=armv8-a+sve' switch and resulted in options '+sve+nocrc' being added
# known issue see https://github.com/flame/blis/issues/397
%ifarch x86_64
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%else
%global optflags_lto %nil
%endif

Name: blis
Summary: BLAS-like Library Instantiation Software Framework
Version: 2.0
Release: alt0.1
License: BSD-3-Clause-Clear
Group: Development/C

Url: https://github.com/flame/blis
Vcs: https://github.com/flame/blis

Source: %name-%version.tar

BuildRequires: gcc gcc-c++ gcc-fortran rpm-build-python3

%description
BLIS is an award-winning portable software framework for instantiating
high-performance BLAS-like dense linear algebra libraries. The framework was
designed to isolate essential kernels of computation that, when optimized,
immediately enable optimized implementations of most of its commonly used and
computationally intensive operations.

%package -n lib%{name}%{soname}
Summary: BLIS shared libraries
Group: System/Libraries

%description -n lib%{name}%{soname}
BLIS shared libraries

%package -n lib%{name}-devel
Summary: BLIS development library and headers
Group: Development/C

%description -n lib%{name}-devel
BLIS development library and headers

%package -n lib%{name}-devel-static
Summary: BLIS static library
Group: Development/C
Requires: lib%{name}-devel = %EVR

%description -n lib%{name}-devel-static
BLIS static library

%prep
%setup
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
export CFLAGS="%optflags"
# arm64 doesn't pass the tests due SVE errors
# see https://github.com/flame/blis/issues/904
# no clue what's the issue here
arch=generic
%ifarch x86_64
arch=%_arch
%endif
%ifarch aarch64
arch=cortexa57
%endif
./configure --prefix=%_prefix --libdir=%_libdir $arch
%make_build V=1

# tests take lots of memory and cpu time
# consider disable during local build
%check
%make check

%install
%makeinstall_std
mv %buildroot%_datadir/pkgconfig %buildroot%_libdir/

%files -n lib%{name}%{soname}
%doc README.md CHANGELOG LICENSE
%_libdir/lib%{name}.so.%{soname}*

%files -n lib%{name}-devel
%doc docs
%_libdir/lib%{name}.so
%_includedir/%name
%_includedir/%{name}.h
%_libdir/pkgconfig/*.pc
%_datadir/%name

%files -n lib%{name}-devel-static
%_libdir/lib%{name}.a

%changelog
* Tue Mar 31 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- Initial build for ALTLinux.
