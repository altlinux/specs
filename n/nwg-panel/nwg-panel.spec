Name: nwg-panel
Version: 0.10.12
Release: alt1
License: MIT

Summary: GTK3-based panel for sway and Hyprland

Group: Graphical desktop/Other

Url: https://github.com/nwg-piotr/nwg-panel
Vcs: https://github.com/nwg-piotr/nwg-panel.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3

BuildRequires: pkgconfig(gio-2.0)

%description
Nwg-panel is a GTK3-based panel for sway and Hyprland Waylandcompositors.
The panel is equipped with a graphical configuration program that frees
the user from the need to manually edit configuration files.

%prep
%setup
subst "s|/usr/bin/bash|/bin/bash|" nwg_panel/executors/*

%build
%python3_build

%install
%python3_install

install -Dpm0644 %name.svg -t %buildroot%_pixmapsdir/
install -Dpm0644 nwg-shell.svg -t %buildroot%_pixmapsdir/
install -Dpm0644 nwg-processes.svg -t %buildroot%_pixmapsdir/

install -Dpm0755 %name-config.desktop -t %buildroot%_desktopdir/
install -Dpm0755 nwg-processes.desktop -t %buildroot%_desktopdir/

install -Dpm0755 %name.service -t %buildroot%_userunitdir/

%files
%_bindir/nwg-*
%python3_sitelibdir/nwg_panel
%python3_sitelibdir/nwg_panel-*.egg-info
%_pixmapsdir/nwg-*.svg
%_desktopdir/nwg-*.desktop
%_userunitdir/%name.service

%changelog
* Thu Jul 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.12-alt1
- new version 0.10.12 (with rpmrb script)

* Sat Jul 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.10-alt1
- new version 0.10.10 (with rpmrb script)

* Mon Jun 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.8-alt1
- new version 0.10.8 (with rpmrb script)

* Sat Jun 14 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.7-alt1
- new version 0.10.7 (with rpmrb script)

* Fri Jun 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.6-alt1
- new version 0.10.6 (with rpmrb script)

* Wed May 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.4-alt1
- new version 0.10.4 (with rpmrb script)

* Thu Apr 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Sun Apr 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Mar 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.9.62-alt1
- Initial build
