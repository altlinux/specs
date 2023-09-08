#TODO: system wlroots
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: hyprland
Version: 0.29.1
Release: alt1

Summary: Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice on its looks
License: BSD-3-Clause and MIT
Group: Graphical desktop/Other

Url: https://github.com/hyprwm/Hyprland

ExcludeArch: i586 armh
Patch0: hyprland-0.25.0-native-udis86.patch

# Source-url: https://github.com/hyprwm/Hyprland/releases/download/v%version/source-v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: jq
BuildRequires: git

BuildRequires: gcc-c++ >= 11
BuildRequires: glslang-devel
BuildRequires: libudis86-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm) >= 17.1.0
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libdrm) >= 2.4.113
BuildRequires: pkgconfig(libinput) >= 1.14.0
BuildRequires: pkgconfig(libseat) >= 0.2.0
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1) >= 0.42.0
BuildRequires: libpixman
BuildRequires: pkgconfig(vulkan) >= 1.2.182
BuildRequires: pkgconfig(pango)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.26
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server) >= 1.21
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)

BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xwayland)
BuildRequires: libdisplay-info-devel

BuildRequires: pkgconfig(hwdata)

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots
that doesn't sacrifice on its looks.

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

%package devel
Summary: Static library and header files for the %name
Group: Development/C++

%description devel
%summary devel

%prep
%setup
%patch0 -p1

%build
%meson -Dwlroots:xcb-errors=disabled -Dwlroots:examples=false
%meson_build

%install
%meson_install
rm -rf %buildroot%_includedir
rm -rf %buildroot%_libdir/libwlroots.a
rm -rf %buildroot%_pkgconfigdir/wlroots.pc

%files
%doc README.md LICENSE
%_bindir/Hyprland
%_bindir/hyprctl
%_man1dir/Hyprland.1*
%_man1dir/hyprctl.1*
%_datadir/hyprland
%_datadir/wayland-sessions/%name.desktop
%_datadir/xdg-desktop-portal/%name-portals.conf
%files devel
%_datadir/pkgconfig/%name-protocols.pc
%_datadir/pkgconfig/%name.pc
%_datadir/hyprland-protocols/

%changelog
* Fri Sep 08 2023 Roman Alifanov <ximper@altlinux.org> 0.29.1-alt1
- new version 0.29.1 (with rpmrb script)

* Fri Aug 25 2023 Roman Alifanov <ximper@altlinux.org> 0.28.0-alt1
- new version 0.28.0 (with rpmrb script)

* Tue Aug 01 2023 Roman Alifanov <ximper@altlinux.org> 0.27.2-alt1
- new version 0.27.2 (with rpmrb script)

* Thu Jun 29 2023 Roman Alifanov <ximper@altlinux.org> 0.26.0-alt1
- new version 0.26.0 (with rpmrb script)

* Fri May 12 2023 Roman Alifanov <ximper@altlinux.org> 0.25.0-alt1
- Initial build for Sisyphus
