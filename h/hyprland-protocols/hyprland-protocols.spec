Name: hyprland-protocols
Version: 0.8.0
Release: alt1

Summary: Wayland protocol extensions for Hyprland
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/hyprwm/hyprland-protocols
Vcs: https://github.com/hyprwm/hyprland-protocols.git

ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_datadir/%name/
%_datadir/pkgconfig/%name.pc

%changelog
* Thu Oct 29 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.8.0-alt1
- new version 0.8.0

* Tue Oct 06 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.7.1-alt1
- new version 0.7.1

* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.7.0-alt1
- Initial build
