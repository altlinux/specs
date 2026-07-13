Name:    tinygltf
Version: 3.0.0
Release: alt1

Summary: Header only C++11 tiny glTF 2.0 library
License: MIT
Group:   Development/C++
Url:     https://github.com/syoyo/tinygltf

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
%summary

%package devel
Summary: Development files for %name
Group:   Development/C++
Provides: %name = %EVR

%description devel
This package contains development files for %name.

%prep
%setup

%build
%cmake  \
    -DTINYGLTF_HEADER_ONLY=ON

%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE README.md
%_includedir/tiny_gltf.h
%_includedir/tinygltf_json.h
%_includedir/json.hpp
%_includedir/stb_image.h
%_includedir/stb_image_write.h
%_libdir/cmake/tinygltf/

%changelog
* Mon Jul 13 2026 Sergey Palcheh <minergenon@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
