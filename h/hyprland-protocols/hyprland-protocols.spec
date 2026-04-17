Name: hyprland-protocols
Version: 0.7.0
Release: alt1

Summary: Wayland protocol extensions for Hyprland
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/hyprwm/hyprland-protocols
Vcs: https://github.com/hyprwm/hyprland-protocols.git

ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/%name/
%_datadir/pkgconfig/%name.pc

%changelog
* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.7.0-alt1
- Initial build
