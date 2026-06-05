Name: niri
Version: 26.04
Release: alt1
License: GPL-3.0

Summary: A scrollable-tiling Wayland compositor

Group: Graphical desktop/Other

Url: https://github.com/YaLTeR/niri
Vcs: https://github.com/YaLTeR/niri.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel
BuildRequires: /proc

BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(gbm)

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pixman-1)

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)

BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(xkbcommon)

BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libpipewire-0.3)

Requires: libwayland-server

%description
Windows are arranged in columns on an infinite strip going to the right.
Opening a new window never causes existing windows to resize.

Every monitor has its own separate window strip.
Windows can never "overflow" onto an adjacent monitor.

Workspaces are dynamic and arranged vertically.
Every monitor has an independent set of workspaces,
and there's always one empty workspace present all the way down.

The workspace arrangement is preserved across disconnecting and
connecting monitors where it makes sense. When a monitor disconnects,
its workspaces will move to another monitor, but upon reconnection
they will move back to the original monitor.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

install -pD resources/niri-session %buildroot%_bindir/niri-session
install -pD resources/niri.desktop %buildroot%_datadir/wayland-sessions/niri.desktop
install -pD resources/niri-portals.conf %buildroot%_datadir/xdg-desktop-portal/niri-portals.conf
install -pD resources/niri.service %buildroot%_userunitdir/niri.service
install -pD resources/niri-shutdown.target %buildroot%_userunitdir/niri-shutdown.target

%buildroot%_bindir/%name completions bash | \
    install -Dm644 /dev/stdin %buildroot%_datadir/bash-completion/completions/%name

%buildroot%_bindir/%name completions zsh | \
    install -Dm644 /dev/stdin  %buildroot%_datadir/zsh/site-functions/_%name

%buildroot%_bindir/%name completions fish | \
    install -Dm644 /dev/stdin %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc README.md
%doc resources/default-config.kdl
%doc docs/wiki
%_bindir/%name
%_bindir/niri-session
%_datadir/wayland-sessions/niri.desktop
%_datadir/xdg-desktop-portal/niri-portals.conf
%_userunitdir/niri.service
%_userunitdir/niri-shutdown.target
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu May 07 2026 Kirill Unitsaev <fiersik@altlinux.org> 26.04-alt1
- new version 26.04

* Tue Dec 02 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.11-alt1
- new version 25.11 (with rpmrb script)

* Wed Nov 12 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.08-alt2
- add requires to libwayland-server (ALT bug 56830)

* Sun Aug 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.08-alt1
- new version 25.08 (with rpmrb script)

* Wed May 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.05.1-alt1
- new version 25.05.1 (with rpmrb script)

* Sun May 18 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.05-alt1
- new version 25.05 (with rpmrb script)

* Thu Apr 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 25.02-alt1
- Initial build
