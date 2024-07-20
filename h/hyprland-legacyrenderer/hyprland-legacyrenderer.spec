#TODO: system wlroots
%global optflags_lto %optflags_lto -ffat-lto-objects
%define upstream hyprland

Name: hyprland-legacyrenderer
Version: 0.41.2
Release: alt2

Summary: Hyprland is a dynamic tiling Wayland compositor (legacy renderer)
License: BSD-3-Clause and MIT
Group: Graphical desktop/Other

Url: https://github.com/hyprwm/Hyprland

ExcludeArch: i586 armh
Patch0: hyprland-0.40.0-native-udis86.patch

# Source-url: https://github.com/hyprwm/Hyprland/releases/download/v%version/source-v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: jq

BuildRequires: pkgconfig(hyprcursor)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(hyprutils)

BuildRequires: gcc-c++ >= 11
BuildRequires: glslang-devel
BuildRequires: libudis86-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm) >= 17.1.0
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libdrm) >= 2.4.118
BuildRequires: pkgconfig(libinput) >= 1.14.0
BuildRequires: pkgconfig(libseat) >= 0.2.0
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1) >= 0.42.0
BuildRequires: libpixman
BuildRequires: pkgconfig(vulkan) >= 1.2.182
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(uuid)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.26
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server) >= 1.22
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)

BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-errors)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xwayland)
BuildRequires: libdisplay-info-devel
BuildRequires: libtomlplusplus-devel

BuildRequires: pkgconfig(hwdata)

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots
that doesn't sacrifice on its looks. (With legacy renderer support.)

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

%prep
%setup
%patch0 -p1

subst '/^version_h = run_command/d' meson.build

%build
%meson \
    -Dwlroots:xcb-errors=enabled \
    -Dwlroots:examples=false \
    -Dlegacy_renderer=enabled
%meson_build

%install
%meson_install
rm -rf %buildroot%_includedir/%upstream
rm -rf %buildroot%_libdir/libwlroots.a
rm -rf %buildroot%_datadir/pkgconfig/wlroots.pc

rm -rf %buildroot%_datadir/hyprland-protocols
rm -rf %buildroot%_datadir/pkgconfig/hyprland-protocols.pc
rm -rf %buildroot%_datadir/pkgconfig/hyprland.pc

%files
%doc README.md LICENSE
%_bindir/Hyprland
%_bindir/hyprctl
%_bindir/hyprpm

%_man1dir/Hyprland.1*
%_man1dir/hyprctl.1*

%_datadir/hyprland
%_datadir/wayland-sessions/%upstream.desktop
%_datadir/xdg-desktop-portal/%upstream-portals.conf

%_datadir/bash-completion/completions/hyprctl
%_datadir/bash-completion/completions/hyprpm

%_datadir/fish/vendor_completions.d/hyprctl.fish
%_datadir/fish/vendor_completions.d/hyprpm.fish

%_datadir/zsh/site-functions/_hyprctl
%_datadir/zsh/site-functions/_hyprpm

%changelog
* Sat Jul 20 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.41.2-alt2
- Initial build of hyprland with legacy renderer

* Thu Jul 04 2024 Roman Alifanov <ximper@altlinux.org> 0.41.2-alt1
- new version 0.41.2 (with rpmrb script)

* Wed Jun 12 2024 Roman Alifanov <ximper@altlinux.org> 0.41.0-alt1
- new version 0.41.0 (with rpmrb script) (ALT bug 50618)

* Mon May 20 2024 Roman Alifanov <ximper@altlinux.org> 0.40.0-alt1
- new version 0.40.0 (with rpmrb script)
- patch updated

* Thu Apr 04 2024 Roman Alifanov <ximper@altlinux.org> 0.38.0-alt1
- new version 0.38.0 (with rpmrb script)

* Fri Mar 22 2024 Roman Alifanov <ximper@altlinux.org> 0.37.1-alt1
- new version 0.37.1 (with rpmrb script)

* Wed Jan 24 2024 Roman Alifanov <ximper@altlinux.org> 0.34.0-alt1
- new version 0.34.0 (with rpmrb script)

* Sat Dec 16 2023 Roman Alifanov <ximper@altlinux.org> 0.33.1-alt1
- new version 0.33.1 (with rpmrb script)

* Tue Nov 14 2023 Roman Alifanov <ximper@altlinux.org> 0.32.3-alt1
- new version 0.32.3 (with rpmrb script)

* Sat Nov 04 2023 Roman Alifanov <ximper@altlinux.org> 0.31.0-alt1
- new version 0.31.0 (with rpmrb script)

* Mon Oct 02 2023 Roman Alifanov <ximper@altlinux.org> 0.30.0-alt1
- new version 0.30.0 (with rpmrb script)

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
