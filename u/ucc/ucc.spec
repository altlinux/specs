%define _unpackaged_files_terminate_build 1
%define soversion 1

Name: ucc
Version: 1.8.0
Release: alt1
Summary: Unified Collective Communication Library

Group: Development/Tools
License: BSD

Url: https://openucx.github.io/ucc/
Vcs: https://github.com/openucx/ucc.git

Source: %name-%version.tar

Patch0: %name-1.8.0-alt1-add-include-cstdint-to-gtest.patch

# Unsupported architecture by UCX
ExcludeArch: i586

BuildPreReq: gcc-c++ doxygen
BuildRequires: libucx-devel

%description
UCC is a collective communication operations API and library that is flexible,
complete, and feature-rich for current and emerging programming models and
runtimes.

%package -n %name-devel
Summary: Development files for Unified Collective Communication Library
Group: System/Libraries

%description -n %name-devel
Development files for Unified Collective Communication Library.

%package -n libucc%soversion
Summary: Unified Collective Communication Library
Group: System/Libraries

%description -n libucc%soversion
Unified Collective Communication Library.

%prep
%setup

%patch0 -p1

%build
./autogen.sh
%configure \
    --disable-optimizations \
    --disable-static \
    --with-sysroot=%prefix \
    --localstatedir=%_runtimedir \
    --enable-doxygen-chm \
    --enable-gtest

%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la
rm %buildroot%_libdir/ucc/*.la
rm %buildroot%_bindir/gtest

%check
make gtest GTEST_FILTER='*:-test_*host/*:test_reduce*:test_allreduce*/*:test_barrier*:test_bcast*:test_gather*:test_allgather*:test_scatter*:*test_alltoall*:test_mem_map*:test_team*:test_context*:test_active_set*:test_scoll_*'

%files
%doc AUTHORS NEWS README.md
%_bindir/ucc_info

%files -n %name-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/ucc/lib*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/ucc

%files -n libucc%soversion
%_libdir/libucc.so.%soversion
%_libdir/libucc.so.%soversion.*
%dir %_libdir/ucc
%_libdir/ucc/lib*.so.%soversion
%_libdir/ucc/lib*.so.%soversion.*

%changelog
* Thu Jun 23 2026 Alexey Romanyuta <r9odt@altlinux.org> 1.8.0-alt1
- New version 1.8.0.
- Add check section to spec file.

* Sat Aug 16 2025 Alexey Romanyuta <r9odt@altlinux.org> 1.5.0-alt1
- Initial build 1.5.0.
