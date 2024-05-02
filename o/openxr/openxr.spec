%define _unpackaged_files_terminate_build 1

Name: openxr
Version: 1.1.36
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

%build
%cmake \
    -DBUILD_ALL_EXTENSIONS=ON \
    -DBUILD_LOADER=ON \
    -DBUILD_WITH_STD_FILESYSTEM=OFF \
    -DBUILD_WITH_WAYLAND_HEADERS=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebinfo \
    -DBUILD_TESTS=ON \
    -DDYNAMIC_LOADER=ON
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
* Thu May 02 2024 Mikhail Tergoev <fidel@altlinux.org> 1.1.36-alt1
- 1.1.36

* Tue Mar 26 2024 Mikhail Tergoev <fidel@altlinux.org> 1.0.34-alt1
- initial build for ALT Sisyphus

