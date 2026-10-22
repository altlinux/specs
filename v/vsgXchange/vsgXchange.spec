%define _unpackaged_files_terminate_build 1
%define libname libvsgXchange
%define sover 3

Name:    vsgXchange
Version: 1.1.14
Release: alt1

Summary: Utility library for converting data+materials to/from VulkanSceneGraph
License: MIT
Group:   Other
Url:     https://github.com/vsg-dev/vsgXchange
VCS:     https://github.com/vsg-dev/vsgXchange.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: KTX-Software
BuildRequires: libassimp-devel
BuildRequires: libcurl-devel
BuildRequires: libdraco-devel
BuildRequires: libfreetype-devel 
BuildRequires: libgdal-devel
BuildRequires: libktx-devel
BuildRequires: libosg2vsg-devel
BuildRequires: libminizip-devel
BuildRequires: libvsg-devel
BuildRequires: osg2vsg-plugins
BuildRequires: libpoly2tri-devel
BuildRequires: libpugixml-devel
BuildRequires: vulkan-devel

%description
vsgXchange contains source code that can directly read a range of
shader and image formats.
reading KTX, DDS, JPEG, PNG, GIF, BMP, TGA and PSD image formats
as vsg::Data objects.
reading GLSL shader files as vsg::ShaderStage objects.
reading and writing SPIRV shader files as vsg::ShaderModule.
writing vsg::Object of all types to .cpp source files that can be
directly compiled into applications.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Def files and headers fore %name
Group: Development/C++

%description -n %libname-devel
%summary.

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc *.md
%_bindir/*

%files -n %libname%sover
%_libdir/%libname.so.%version
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%changelog
* Fri Oct 16 2026 Artem Semenov <savoptik@altlinux.org> 1.1.14-alt1
- New version 1.1.14.

* Wed Oct 07 2026 Artem Semenov <savoptik@altlinux.org> 1.1.9-alt1
- Initial build for Sisyphus.
