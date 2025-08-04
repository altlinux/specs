%define repo dde-wayland-config

Name: deepin-wayland-config
Version: 1.0.10
Release: alt1

Summary: Wayland settings for the DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-wayland-config
VCS: https://github.com/linuxdeepin/dde-wayland-config.git

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

Requires: startdde
# prevent hasher_priv error
%filter_from_requires /\/usr\/bin\/kwin_wayland/d

BuildRequires: rpm-build-golang /proc

%description
dde-wayland-config provides the wayland settings for the DDE.

%prep
%setup -n %repo-%version
%patch -p1

%build
export GO111MODULE=off
export GOPATH="%go_path"
%make

%install
export GOPATH="%go_path"
%makeinstall DESTDIR=%buildroot

%files
%_bindir/Xdeepin
%_bindir/dde_update_dbus_env
%_bindir/kwin_wayland-x11_helper
%_bindir/kwin_wayland_helper
%_bindir/runkwin-x11.sh
%_bindir/runkwin.sh
%_bindir/startdde-wayland
%_bindir/startdde-x11
%_datadir/wayland-sessions/DeepinOnXwayland.desktop
%_datadir/wayland-sessions/Wayland.desktop

%changelog
* Mon Aug 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- Initial build for ALT Sisyphus (for deepin-update-ui).
