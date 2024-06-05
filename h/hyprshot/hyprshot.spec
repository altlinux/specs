Name: hyprshot
Version: 1.3.0
Release: alt1

Summary: Utility to easily take screenshots in Hyprland
License: GPL-3.0
Group: Graphics

ExcludeArch: i586 armh

Url: https://github.com/Gustash/Hyprshot

Source0: %name-%version.tar

%description
Utility to easily take screenshots in Hyprland using your mouse.

%description -l ru_RU.UTF-8
Утилита, позволяющая легко делать скриншоты в Hyprland с помощью мыши.

%prep
%setup

%install
install -pD -m0755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md LICENSE

%changelog
* Wed Jun 05 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.3.0-alt1
- Initial build
