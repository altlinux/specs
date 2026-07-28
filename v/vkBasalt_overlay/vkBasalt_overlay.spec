%define _unpackaged_files_terminate_build 1

Name:    vkBasalt_overlay
Version: 0.1.2
Release: alt1

Summary: A vulkan post processing layer for linux with an in-game overlay GUI
License: Zlib
Group:   System/Configuration/Hardware
URL:     https://github.com/Boux/vkBasalt_overlay

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ cmake meson
BuildRequires: glslang-devel libX11-devel libXi-devel spirv-headers vulkan-headers
Requires: vulkan-filesystem

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libdir/libvkbasalt-overlay.so
%_datadir/vulkan/implicit_layer.d/vkBasalt-overlay.json

%changelog
* Tue Jul 28 2026 Sergey Palcheh <minergenon@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
