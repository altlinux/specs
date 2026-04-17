Name: waypaper
Version: 2.8
Release: alt1
License: GPL-3.0

Summary: GUI wallpaper manager

Group: Graphical desktop/Other

Url: https://github.com/anufrievroman/waypaper
VCS: https://github.com/anufrievroman/waypaper.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%description
GUI wallpaper setter for Wayland and Xorg window managers.
It works as a frontend for popular wallpaper backends like
swaybg, swww, wallutils, hyprpaper, mpvpaper and feh.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*.dist-info
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/*.1.*

%changelog
* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 2.8-alt1
- new version 2.8

* Tue Sep 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.7-alt1
- new version 2.7 (with rpmrb script)

* Wed May 14 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.6-alt1
- new version 2.6 (with rpmrb script)

* Fri May 02 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.5-alt1
- Initial build
