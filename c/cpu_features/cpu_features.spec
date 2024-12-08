# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: cpu_features
Version: 0.9.0
Release: alt1
Summary: A library to get CPU features at runtime
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/cpu_features

Source: %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
BuildRequires: libgtest-devel
}}

%description
A cross-platform C library to retrieve CPU features (such as available
instructions) at runtime.

%package -n libcpu_features-devel
Summary: A cross platform C99 library to get CPU features at runtime
Group: Development/C
Requires: cpu_features = %EVR

%description -n libcpu_features-devel
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
	-DBUILD_SHARED_LIBS=ON \
%if_disabled check
	-DBUILD_TESTING=OFF \
%endif
	%nil
%cmake_build

%install
%cmake_install

%check
%ctest
export LD_LIBRARY_PATH=%buildroot%_libdir
%buildroot%_bindir/list_cpu_features
# https://github.com/google/cpu_features/issues/373
# %buildroot%_bindir/list_cpu_features --json | jq .

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md
%_bindir/list_cpu_features
%_libdir/libcpu_features.so.0
%_libdir/libcpu_features.so.%version

%files -n libcpu_features-devel
%_libdir/libcpu_features.so
%_includedir/cpu_features
%_cmakedir/CpuFeatures

%changelog
* Sun Dec 08 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.0-alt1
- First import v0.9.0-22-g3db721e (2024-11-12).
