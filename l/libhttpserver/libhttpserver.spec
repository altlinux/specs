%define _unpackaged_files_terminate_build 1

%define pkgname httpserver
%define sover 2

%def_disable static
%def_disable check

Name: libhttpserver
Version: 2.0.1
Release: alt1

Summary: libhttpserver is a C++ library for building high performance RESTful web servers
License: LGPL-2.1-only
Group: System/Libraries
Url: https://github.com/etr/libhttpserver

# Source-url: https://github.com/etr/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libmicrohttpd)
%if_enabled check
BuildRequires: pkgconfig(libcurl)
%endif

%description
%name is built upon libmicrohttpd to provide a simple API for
developers to create HTTP services in C++.

%package -n %name%sover
Summary: %summary
Group: System/Libraries

%description -n %name%sover
%name is built upon libmicrohttpd to provide a simple API for
developers to create HTTP services in C++.

%package devel
Summary: Development files for the %name
Group: Development/C++
Requires: %name%sover = %EVR

%description devel
%name is a small C++ library for embedding RESTful HTTP server
functionality into applications. This package contains development
files and headers.

%prep
%setup

%build
./bootstrap
%__mkdir %_host
cd %_host
ln -sf ../configure .
%configure \
%if_disabled check
    --disable-valgrind-memcheck \
    --disable-valgrind-helgrind \
    --disable-valgrind-sgcheck \
%endif
    --disable-valgrind-drd \
    %{subst_enable static} \
    --disable-examples \
    --srcdir=../
%make_build

%install
%makeinstall_std -C %_host

%check
%make_build check -C %_host

%files -n %name%sover
%doc README.md ChangeLog
%_libdir/%name.so.%{sover}*

%files devel
%_includedir/%{pkgname}*
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_datadir/cmake/Modules/*.cmake
%_man3dir/%name.3*

%changelog
* Thu Nov 05 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0.1-alt1
- new version

* Mon May 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.19.0-alt1
- Initial build for ALT Linux
