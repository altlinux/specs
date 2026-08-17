# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: stdexec-devel
Version: 0.11.0
Release: alt1.git61fb73d7.1

Summary: Reference implementation of C++26 std::execution for async programming
License: Apache-2.0
Group: Development/C
URL: https://github.com/NVIDIA/stdexec
VCS: https://github.com/NVIDIA/stdexec.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++

%description
stdexec is a header-only C++ library from NVIDIA that implements
std::execution ([exec], WG21 P2300) - the C++26 model for asynchronous
and parallel programming based on composable sender/receiver pipelines.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_includedir/exec
%_includedir/stdexec
%_pkgconfigdir/stdexec.pc

%changelog
* Thu Jun 4 2026 Anatoly Mukosey <mukav@altlinux.org> 0.11.0-alt1.git61fb73d7.1
- Initial build for Sisyphus.
