Name:    wlmaker
Version: 0.4
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

BuildRequires(pre): rpm-build-cmake ctest
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
Requires: seatd

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

# Install default config files
install -d %buildroot%_sysconfdir
install -m644 -v ./etc/{style-default.plist,wlmaker.plist,wlmaker-state.plist} \
%buildroot%_sysconfdir
install -m644 -v ./etc/wlmaker-home.plist %buildroot%_sysconfdir

%check
%ctest

%files
%doc *.md LICENSE
%_bindir/%name
%_bindir/wlmclock
%_bindir/example_toplevel
%_bindir/wrap-%name.sh
%_datadir/%name.desktop
%_datadir/wlmclock.desktop
%_iconsdir/%name
%config(noreplace)%_sysconfdir/*.plist

%changelog
* Tue Oct 22 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.4-alt1
- 0.3 -> 0.4

* Fri Oct 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.3-alt1
- initial build for Sisyphus
