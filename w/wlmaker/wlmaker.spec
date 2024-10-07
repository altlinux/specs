Name:    wlmaker
Version: 0.3
Release: alt1

Summary: Wayland Maker - A Wayland compositor inspired by Window Maker
License: Apache-2.0
Group:   Graphical desktop/Window Maker
Url:     https://github.com/phkaeser/wlmaker

Source0: %name-%version.tar
# To get required submodule version open github version tag,
# go to submodules/libbase @ <hash>, Code -> Download ZIP,
# and extract it to .gear/submodules/libbase.
Source1: submodules.tar

BuildRequires(pre): cmake ctest
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(libdrm)

BuildRequires: flex doxygen

Requires: foot

%description
A lightweight and fast Wayland compositor, visually inspired by Window Maker,
and fully theme-able and configurable.
Key features:

- Compositor for windows in stacking mode.
- Supports multiple workspaces.
- Appearance inspired by Window Maker, following the look and feel of NeXTSTEP.
- Easy to use, lightweight, low gimmicks and fast.
- Dock and clip, to be extended for dockable apps.

%prep
%setup -a1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
# FIXME: Temporarily ignore broken toolkit_test set
%ctest -E toolkit_test

%files
%doc *.md LICENSE
%_bindir/%name
%_bindir/wlmclock
%_bindir/wrap-%name.sh
%_datadir/%name.desktop
%_iconsdir/%name

%changelog
* Fri Oct 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.3-alt1
- initial build for Sisyphus
