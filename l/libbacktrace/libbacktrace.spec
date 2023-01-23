%def_disable static
%define git ad106d5

Name: libbacktrace
Version: 1.0
Release: alt0.2.g%{git}
Summary: Library of Direct Hardware Access
License: BSD
Group: Development/C
URL: https://github.com/ianlancetaylor/libbacktrace
Source: %name.tar

BuildRequires: gcc zlib-devel liblzma-devel libzstd-devel

%description
%name - A C library that may be linked into a C/C++ program to produce symbolic
backtraces.

The libbacktrace library may be linked into a program or library and used to
produce symbolic backtraces. Sample uses would be to print a detailed backtrace
when an error occurs or to gather detailed profiling information. In general
the functions provided by this library are async-signal-safe, meaning that they
may be safely called from a signal handler.


%package devel
Summary: Headers for library of %name
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %EVR

%description devel
Headers for library of %name


%if_enabled static
%package devel-static
Summary: Static library of %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static library of %name.
%endif


%prep
%setup -n %name

%build
%autoreconf
%configure --enable-shared
%make_build

%install
mkdir -p %buildroot{%_includedir,%_libdir}
install -p -m644 backtrace.h %buildroot%_includedir/
cp -a .libs/*.so* %buildroot%_libdir/
%if_enabled static
install -p -m644 .libs/*.a %buildroot%_libdir/
%endif

%files
%_libdir/*.so.*

%files devel
%doc README.md LICENSE
%_includedir/*
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jan 23 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.2.gad106d5
- Updated to GIT ad106d5.
- Enable zstd support.

* Tue Jun 08 2021 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.1.gd0f5e95
- Initial build for ALTLinux.
