Name: nwg-displays
Version: 0.3.25
Release: alt1
License: MIT

Summary: Output management utility for sway and Hyprland

Group: System/Configuration/Other

Url: https://github.com/nwg-piotr/nwg-displays
Vcs: https://github.com/nwg-piotr/nwg-displays.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3

%description
Nwg-displays is an output management utility for sway and
Hyprland Wayland compositor, inspired by wdisplays and wlay.
The program is expected to:

%prep
%setup

%build
%python3_build

%install
%python3_install

install -Dpm0644 %name.svg -t %buildroot%_pixmapsdir/
install -Dpm0755 %name.desktop -t %buildroot%_desktopdir/

%files
%_bindir/%name
%python3_sitelibdir/nwg_displays
%python3_sitelibdir/nwg_displays-*.egg-info
%_pixmapsdir/%name.svg
%_desktopdir/%name.desktop

%changelog
* Sun Mar 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.3.25-alt1
- Initial build
