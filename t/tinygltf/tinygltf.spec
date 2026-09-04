Name:    tinygltf
Version: 3.0.1
Release: alt1

Summary: Header only C11 tiny glTF 2.0 library
License: MIT
Group:   Development/C
URL:     https://github.com/syoyo/tinygltf

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc

BuildArch: noarch

%description
%summary

%package devel
Summary: Development files for %name
Group:   Development/C
Provides: %name = %EVR

%description devel
This package contains development files for %name.

%prep
%setup

%build
%cmake

%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE README.md
%_includedir/tiny_gltf_v3.h
%_includedir/tiny_gltf_v3.c
%_includedir/tinygltf_json_c.h

%changelog
* Fri Sep 04 2026 Sergey Palcheh <minergenon@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Mon Jul 13 2026 Sergey Palcheh <minergenon@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
