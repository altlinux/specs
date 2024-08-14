%define soversion 2

Name: libaquamarine
Version: 0.3.1
Release: alt1
License: BSD-3-Clause

Summary: Is a very light linux rendering backend library

Group: System/Libraries

Url: https://github.com/hyprwm/aquamarine

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(hwdata)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(hyprwayland-scanner)

%description
Aquamarine is a very light linux rendering backend library.
It provides basic abstractions for an application to render
on a Wayland session (in a window) or a native DRM session.

It is agnostic of the rendering API (Vulkan/OpenGL)
and designed to be lightweight, performant, and minimal.

Aquamarine provides no bindings for other languages. It is C++-only.

%package -n %name%soversion
Summary: Is a very light linux rendering backend library
Group: System/Libraries

%description -n %name%soversion
%summary.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name%soversion = %EVR

%description -n %name-devel
This package provides development files for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %name%soversion
%doc README.md
%_libdir/%name.so.%soversion
%_libdir/%name.so.%version

%files -n %name-devel
%_includedir/aquamarine/
%_libdir/%name.so
%_pkgconfigdir/aquamarine.pc

%changelog
* Tue Aug 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.1-alt1
- Initial build
