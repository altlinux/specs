%define _unpackaged_files_terminate_build 1
%define libname libktx
%define sover 0

Name:    KTX-Software
Version: 4.4.2
Release: alt1

Summary: KTX (Khronos Texture) Library and Tools
License: Apache-2.0
Group:   Other
Url:     https://github.com/khronosgroup/ktx-software
VCS:     https://github.com/khronosgroup/ktx-software.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++

%description
KTX Khronos Texture is a lightweight container for textures for OpenGL, Vulkan
and other GPU APIs. KTX files contain all the parameters needed for texture
loading. A single file can contain anything from a simple base-level 2D texture
through to a cubemap array texture with mipmaps. Contained textures can be in a
Basis Universal format, in any of the block-compressed formats supported by
OpenGL family and Vulkan APIs and extensions or in an uncompressed single-plane
format. Basis Universal currently encompasses two formats that can be quickly
transcoded to any GPU-supported format, LZ/ETC1S, which combines
block-compression and supercompression, and UASTC, a block-compressed format.
Formats other than LZ/ETC1S can be supercompressed with Zstd and ZLIB.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary:     Dev files and headers for %name
Group: Development/C++

%description -n %libname-devel
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%if "%_lib" != "lib"
    mv -v %buildroot%_prefix/lib/cmake %buildroot%_cmakedir
%endif

%files
%doc *.md
%_bindir/*

%files -n %libname%sover
%_libdir/%libname.so.%sover.*
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%changelog
* Tue Oct 06 2026 Artem Semenov <savoptik@altlinux.org> 4.4.2-alt1
- Initial build for Sisyphus.
