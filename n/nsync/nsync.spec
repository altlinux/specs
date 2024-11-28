%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with check

%define soname 1

Name: nsync
Version: 1.29.2
Release: alt1

Summary: A C library that exports various synchronization primitives, such as mutexes
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/nsync
Vcs: https://github.com/google/nsync

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: ctest
%endif

%description
nsync is a C library that exports various synchronization primitives:
    locks
    condition variables
    run-once initialization
    waitable counter (useful for barriers)
    waitable bit (useful for cancellation, or other conditions)

It is not an offical Google product.

%package -n lib%name%soname
Summary: %{summary %name}
Group: System/Libraries

%description -n lib%name%soname
%{description %name}.

%package -n lib%name-devel
Summary: Headers files and library symbolic links for %name
Group: Development/C

%description -n lib%name-devel
%{description %name}.

%prep
%setup
%autopatch -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name%soname
%_libdir/libnsync.so.%{soname}*
%_libdir/libnsync_cpp.so.%{soname}*

%files -n lib%name-devel
%doc README
%_includedir/nsync*.h
%_cmakedir/nsync/
%_cmakedir/nsync_cpp/
%_libdir/libnsync.so
%_libdir/libnsync_cpp.so

%changelog
* Thu Nov 28 2024 Anton Zhukharev <ancieg@altlinux.org> 1.29.2-alt1
- Built for ALT Sisyphus.

