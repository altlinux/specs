%define _unpackaged_files_terminate_build 1
%define git def2038

Name:    parallel-hashmap
Version: 2.0.0
Release: alt1.g%{git}
Summary: A family of header-only, very fast and memory-friendly hashmap and btree containers
Group:   Development/C++
License: Apache-2.0
URL:     https://greg7mdp.github.io/parallel-hashmap
Vcs:     https://github.com/greg7mdp/parallel-hashmap

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake gcc-c++

BuildArch: noarch

%description
%summary

%package devel
Summary: A family of header-only, very fast and memory-friendly hashmap and btree containers
Group:   Development/C++

%description devel
%summary

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  -DPHMAP_BUILD_TESTS=OFF \
  -DPHMAP_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE CITATION.cff
%doc *.md
%_includedir/parallel_hashmap

%changelog
* Mon Aug 25 2025 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt1.gdef2038
- Initial build for ALTLinux.


