Name:    wlmaker
Version: 0.8
Release: alt1

Summary: Wayland Maker - A Wayland compositor inspired by Window Maker
License: Apache-2.0
Group:   Graphical desktop/Window Maker
Url:     https://github.com/phkaeser/wlmaker

Source0: %name-%version.tar

# To get required submodule version open github version tag,
# go to submodules/libbase @ <hash>, Code -> Download ZIP,
# and extract it to .gear/submodules/.
Source1: submodules.tar

BuildRequires(pre): rpm-build-cmake ctest
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots-0.19)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(xwayland)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(libxdg-basedir)
BuildRequires: pkgconfig(libinput)

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
sed -i 's/XkbConfigurationFile/\/\/ XkbConfigurationFile/g' etc/Config.plist

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest \
-E backend_test

%files
%doc *.md LICENSE
%_bindir/%name
%_bindir/wlmtool
%_bindir/wlmclock
%_bindir/wlmeyes
%_bindir/wlmcpugraph
%_bindir/wlmmemgraph
%_bindir/wlmnetgraph
%_bindir/wlmbattery
%_datadir/applications/*.desktop
%_datadir/wayland-sessions/%name.desktop
%_datadir/%name
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/64x64/apps/*.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_sysconfdir/xdg/%name

%changelog
* Thu May 21 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.8-alt1
- 0.7.1 -> 0.8

* Thu Mar 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.7.1-alt2
- Linked last wlroots version (closes: #58162).
- Added another one vendored submodule.
- Avoided keyboard configuration reading.

* Mon Feb 16 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.7.1-alt1
- 0.6.2 -> 0.7.1
- Patched to link with libinih.

* Mon Nov 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Tue Sep 23 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.6.1-alt1
- 0.6 -> 0.6.1

* Thu Aug 28 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.6-alt1
- 0.5 -> 0.6

* Mon Mar 10 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.5-alt1
- 0.4 -> 0.5

* Tue Oct 22 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.4-alt1
- 0.3 -> 0.4

* Fri Oct 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.3-alt1
- initial build for Sisyphus
