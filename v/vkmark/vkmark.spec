%define _unpackaged_files_terminate_build 1

%ifarch %ix86
# https://github.com/vkmark/vkmark/issues/59
%def_without check
%else
%def_with check
%endif

Name: vkmark
Version: 2017.08
Release: alt3.git.ab6e6f340

Summary: Vulkan benchmark
License: LGPL-2.1-or-later
Group: Graphics
Url: https://github.com/vkmark/vkmark

Source0: %name-%version-%release.tar

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
%setup -n %name-%version-%release

%build
%meson \
    -Dxcb=true \
    -Dwayland=true \
    -Dkms=true
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
%_libdir/%name/kms.so
%_man1dir/%name.1*
%_datadir/%name

%changelog
* Tue Feb 27 2024 Ivan A. Melnikov <iv@altlinux.org> 2017.08-alt3.git.ab6e6f340
- disable tests on %ix86.

* Tue Feb 27 2024 Ivan A. Melnikov <iv@altlinux.org> 2017.08-alt2.git.ab6e6f340
- restore package in Sisyphus;
- update to new git snapshot (fixes FTBFS);
- enable kms window system.

* Mon Feb 27 2023 Sergey Ivanov <zagagyka@altlinux.org> 2017.08-alt1.git.30d2cd37
- Initial build

