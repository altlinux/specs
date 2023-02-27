%define _unpackaged_files_terminate_build 1

%def_with check

Name: vkmark
Version: 2017.08
Release: alt1.git.30d2cd37

Summary: Vulkan benchmark
License: LGPL-2.1-or-later
Group: Graphics
Url: https://github.com/vkmark/vkmark

Source0: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: cmake gcc-c++
BuildRequires: libvulkan-devel
BuildRequires: libglm-devel
BuildRequires: libassimp-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libwayland-egl-devel
BuildRequires: wayland-protocols
BuildRequires: libdrm-devel
BuildRequires: libgbm-devel

%description
vkmark is an extensible Vulkan benchmarking suite with targeted, configurable
scenes.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%check
%meson_test

%files
%_bindir/vkmark
%dir %_libdir/%name
%_libdir/%name/wayland.so
%_libdir/%name/xcb.so
%_man1dir/%name.1*
%_datadir/%name

%changelog
* Mon Feb 27 2023 Sergey Ivanov <zagagyka@altlinux.org> 2017.08-alt1.git.30d2cd37
- Initial build

