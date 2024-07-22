Name: mpvpaper
Version: 1.6
Release: alt1
License: GPL-3.0

Summary: A video wallpaper program for wlroots based wayland compositors

Group: Graphical desktop/Other

Url: https://github.com/GhostNaN/mpvpaper

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: libwlroots-devel
BuildRequires: meson libmpv-devel
BuildRequires: libwayland-egl-devel libglvnd-devel
BuildRequires: wayland-protocols libwayland-client-devel

Requires: mpv

%description
mpvpaper is a wallpaper program for wlroots based wayland compositors,
such as sway. That allows you to play videos with mpv as your wallpaper.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 %name.man %buildroot%_man1dir/%name.1

%files
%doc README.md
%_bindir/%name
%_bindir/%name-holder
%_man1dir/*.1.*

%changelog
* Mon Jul 22 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.6-alt1
- Initial build
