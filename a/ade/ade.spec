%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: ade
Version: 0.1.1
Release: alt1.f.git.bf96bf0
Summary: Graph construction, manipulation, and processing framework
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/opencv/ade

# https://github.com/opencv/ade.git
Source: %name-%version.tar

Patch1: ade-alt-installation.patch

BuildRequires: gcc-c++ cmake

%description
ADE Framework is a graph construction, manipulation, and processing framework.
ADE Framework is suitable for organizing data flow processing and execution.

%package -n lib%name-devel
Group: Development/C++
Summary: Graph construction, manipulation, and processing framework

%description -n lib%name-devel
ADE Framework is a graph construction, manipulation, and processing framework.
ADE Framework is suitable for organizing data flow processing and execution.

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name-devel
%doc LICENSE
%doc README.md
%_includedir/%name
%_libdir/lib%name.a
%_datadir/%name

%changelog
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1.f.git.bf96bf0
- Initial build for ALT.
