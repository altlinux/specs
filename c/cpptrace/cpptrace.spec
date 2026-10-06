%def_with check
%define abiversion 1

Name: cpptrace
Version: 1.0.4
Release: alt1

Summary: Portable stack trace library for C++

License: MIT
Group: System/Libraries
URL: https://github.com/jeremy-rifkin/cpptrace
# Source-url: https://github.com/jeremy-rifkin/cpptrace/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: cpptrace-shared-config.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++
BuildRequires: pkgconfig(libdwarf)
%if_with check
BuildRequires: /proc
BuildRequires: /usr/bin/ctest libgtest-devel libgmock-devel
%endif

%description
Cpptrace captures stack traces and resolves source locations for C++
applications, with support for exceptions and DWARF debug information.

%package -n libcpptrace%abiversion
Summary: Portable C++ stack trace library
Group: System/Libraries

%description -n libcpptrace%abiversion
Shared library for capturing and resolving C++ stack traces.

%package -n libcpptrace-devel
Summary: Development files for cpptrace
Group: Development/C++

%description -n libcpptrace-devel
Headers and CMake configuration for developing applications with cpptrace.

%prep
%setup
%patch0 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED_LIBS=ON \
    -DCPPTRACE_USE_EXTERNAL_LIBDWARF=ON \
    -DCPPTRACE_FIND_LIBDWARF_WITH_PKGCONFIG=ON \
%if_with check
    -DCPPTRACE_BUILD_TESTING=ON \
%else
    -DCPPTRACE_BUILD_TESTING=OFF \
%endif
    -DCPPTRACE_USE_EXTERNAL_GTEST=ON \
    -DCPPTRACE_BUILD_TOOLS=OFF \
    -DCPPTRACE_DISABLE_CXX_20_MODULES=ON \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libcpptrace%abiversion
%doc LICENSE
%_libdir/libcpptrace.so.%abiversion
%_libdir/libcpptrace.so.%version

%files -n libcpptrace-devel
%_includedir/cpptrace/
%_includedir/ctrace/
%_libdir/libcpptrace.so
%_libdir/cmake/cpptrace/

%changelog
* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- Initial build for ALT Sisyphus.
