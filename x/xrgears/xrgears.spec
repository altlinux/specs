Name:    xrgears
Version: 1.0.1
Release: alt1

Summary: An OpenXR example using Vulkan for rendering
License: MIT
Group:   Other
URL:     https://gitlab.freedesktop.org/monado/demos/xrgears

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake gcc-c++ meson
BuildRequires: libvulkan-devel openxr-devel libglm-devel glslang xxd libX11-devel

ExclusiveArch: x86_64

%description
xrgears is an OpenXR VR demo using Vulkan for rendering.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Sun Jun 21 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.1-alt1
Initial build for Sisyphus

