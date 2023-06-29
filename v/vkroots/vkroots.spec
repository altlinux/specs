Name: vkroots
Version: 0.0.0.1
Release: alt1.e554d4c

Summary: vkroots is a framework for writing Vulkan layers that takes all the complexity/hastle away from you!
License: MIT AND LGPL-2.1-or-later AND Apache-2.0
Group: Development/C++

Url: https://github.com/Joshua-Ashton/vkroots
# Source0-url: https://github.com/Joshua-Ashton/vkroots
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libvulkan-devel

%description
vkroots is incredibly easy to integrate into your project,
it's a single include, and even supports defining multiple
layers in a single shared library with VKROOTS_NEGOTIATION_INTERFACE.

All you do is just implement the functions you want,
and they are automagically hooked using C++20 concepts magic!

%package devel
Summary: vkroots is a framework for writing Vulkan layers that takes all the complexity/hastle away from you!
Group: Development/C++

%description devel
vkroots is incredibly easy to integrate into your project,
it's a single include, and even supports defining multiple
layers in a single shared library with VKROOTS_NEGOTIATION_INTERFACE.

All you do is just implement the functions you want,
and they are automagically hooked using C++20 concepts magic!

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%files devel
%doc LICENSE README.md
%_includedir/%name.h
%_pkgconfigdir/%name.pc

%changelog
* Mon May 22 2023 Mikhail Tergoev <fidel@altlinux.org> 0.0.0.1-alt1.e554d4c
- Initial build for Sisyphus
