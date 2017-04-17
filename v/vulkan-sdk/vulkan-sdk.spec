%define sover 1
%define pkgname vulkan

Name: %pkgname-sdk
Version: 1.0.46.0
Release: alt2

Summary: Vulkan SDK
Group: System/Libraries
License: Apache 2.0

Url: https://www.khronos.org/%pkgname/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/archive/sdk-%version/Vulkan-LoaderAndValidationLayers-sdk-%version.tar.gz

Requires: lib%pkgname-devel = %EVR
Requires: %pkgname-utils = %EVR
Requires: %pkgname-validation-layers = %EVR

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glslang
BuildRequires: glslang-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXrandr-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: python3-dev

%description
Vulkan API Software Development Kit

%package -n lib%pkgname%sover
Summary: Vulkan API loader library
Group: System/Libraries
Provides: %pkgname = %version
Obsoletes: %pkgname

%description -n libvulkan%sover
Loader library for Vulkan API drivers.

%package -n lib%pkgname-devel
Summary: Headers files for the Vulkan API
Group: Development/C++
Provides: %pkgname-devel = %version
Obsoletes: %pkgname-devel

%description -n libvulkan-devel
Headers files for the Vulkan API

%package -n %pkgname-utils
Summary: Vulkan utilities
Group: Development/Tools
Provides: %pkgname = %version
Obsoletes: %pkgname

%description -n %pkgname-utils
Vulkan utilities

%package -n %pkgname-validation-layers
Summary: Validation layers for Vulkan
Group: System/Libraries
Requires: lib%pkgname%sover = %EVR
Provides: %pkgname = %version
Obsoletes: %pkgname

%description -n %pkgname-validation-layers
Validation layers for Vulkan

%prep
%setup -n Vulkan-LoaderAndValidationLayers-sdk-%version

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_INSTALL_SYSCONFDIR:PATH=%_datadir \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_WSI_MIR_SUPPORT:BOOL=FALSE

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__mkdir_p %buildroot%_datadir/%pkgname/icd.d

%files

%files -n lib%pkgname%sover
%doc COPYRIGHT.txt LICENSE.txt
%_libdir/lib%pkgname.so.*
%dir %_datadir/%pkgname
%dir %_datadir/%pkgname/explicit_layer.d
%dir %_datadir/%pkgname/icd.d

%files -n lib%pkgname-devel
%_libdir/lib%pkgname.so
%dir %_includedir/%pkgname
%_includedir/%pkgname/*
%_pkgconfigdir/%pkgname.pc

%files -n %pkgname-utils
%_bindir/%{pkgname}info

%files -n %pkgname-validation-layers
%_libdir/libVkLayer_*.so
%_datadir/%pkgname/explicit_layer.d/VkLayer_*.json

%changelog
* Mon Apr 17 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.46.0-alt2
- Fix post-install unowned files
- Add ICD directory for additional layers

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.46.0-alt1
- Version 1.0.46.0
- Separated packages
- SDK meta package
- Use external SPIRV-Tools and GLSLang
