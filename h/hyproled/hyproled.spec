Name: hyproled
Version: 0.1.0
Release: alt1
License: BSD-3-Clause

Summary: Hyprland shader to prevent OLED burn in

Group: Graphical desktop/Other

Url: https://github.com/mklan/hyproled

Source: %name-%version.tar

ExcludeArch: %ix86

%description
Hyprland shader utility to prevent OLED burn in. Disables every other pixel.

%prep
%setup

%install
install -d %buildroot%_bindir
install %name %buildroot%_bindir/

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
