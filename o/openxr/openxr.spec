%define _unpackaged_files_terminate_build 1

Name: openxr
Version: 1.1.60
Release: alt1

Summary: An API for writing VR and AR software

License: Apache-2.0
Url: https://github.com/KhronosGroup/OpenXR-SDK-Source
Group: System/Libraries

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake gcc-c++ ctest
BuildRequires: glslang glslang-devel
BuildRequires: libffi-devel libXau-devel libXdmcp-devel
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-glx)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-dri2)
BuildRequires: pkgconfig(xrandr)

Requires: lib%name = %EVR

%description
OpenXR is an API specification for writing portable, cross-platform,
virtual reality (VR) and augmented reality (AR) software.

%package -n lib%name
Summary: Libraries for writing VR and AR software
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with OpenXR.

%package devel
Summary: Headers and development files of the OpenXR library
Group: Development/Other
Requires: lib%name = %EVR

%description devel
Development files for the OpenXR library. Install this package if you
want to compile applications using the OpenXR library.

%prep
%setup
%ifarch %e2k
# error: "No architecture string known!"
sed -i 's/m68k/e2k/' src/common/platform_utils.hpp
# xr_generated_core_validation.cpp:
# parameter "gen_instance_info" was never referenced
sed -i 's/-Werror/-Wno-error/g' src/CMakeLists.txt
%endif

%build
%cmake \
    -DBUILD_ALL_EXTENSIONS=ON \
    -DBUILD_LOADER=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_TESTS=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebinfo \
    -DDYNAMIC_LOADER=ON \
    -DFILESYSTEM_USE_STD=ON \
    -DGLSLANG_VALIDATOR=%{_bindir}/glslangValidator
%cmake_build
    
%install
%cmake_install

# drop duplicate license
rm -v %buildroot%_docdir/openxr/LICENSE

%check
%ctest

%files
%doc CHANGELOG.SDK.md LICENSE README.md
%_bindir/*
%_datadir/%name
%_man1dir/*.1*

%files -n lib%name
%_libdir/lib%{name}_loader.so.*

%files devel
%_includedir/%name
%_libdir/cmake/%name
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 15 2026 Mikhail Tergoev <fidel@altlinux.org> 1.1.60-alt1
- 1.1.60

* Thu Aug 28 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.1.50-alt2
- e2k build fix

* Mon Aug 25 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.50-alt1
- 1.1.50

* Tue Jun 17 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.49-alt1
- 1.1.49

* Mon May 12 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.47-alt1
- 1.1.47

* Thu Mar 27 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.46-alt1
- 1.1.46

* Tue Feb 25 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.45-alt1
- 1.1.45

* Sat Feb 01 2025 Mikhail Tergoev <fidel@altlinux.org> 1.1.43-alt1
- 1.1.43

* Thu Nov 07 2024 Mikhail Tergoev <fidel@altlinux.org> 1.1.42-alt1
- 1.1.42

* Tue Oct 22 2024 Mikhail Tergoev <fidel@altlinux.org> 1.1.41-alt1
- 1.1.41

* Fri May 03 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.1.36-alt2
- NMU: fixed FTBFS on LoongArch

* Thu May 02 2024 Mikhail Tergoev <fidel@altlinux.org> 1.1.36-alt1
- 1.1.36

* Tue Mar 26 2024 Mikhail Tergoev <fidel@altlinux.org> 1.0.34-alt1
- initial build for ALT Sisyphus

