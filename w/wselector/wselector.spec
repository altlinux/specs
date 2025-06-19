%define xdg_name io.github.Cookiiieee.WSelector

Name: wselector
Version: 0.2.1
Release: alt1
License: GPL-3.0

Summary: A modern Adwaita app for browsing, downloading, and setting wallpapers

Group: Graphical desktop/Other

Url: https://github.com/Cookiiieee/WSelector
VCS: https://github.com/Cookiiieee/WSelector.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%description
WSelector - A modern GTK4/Adwaita application for browsing, downloading,
and setting wallpapers from Wallhaven.cc website.

%prep
%setup
subst 's|/app/bin/||' files/%xdg_name.desktop
subst '/Flatpak/d' files/%xdg_name.desktop

%build
%python3_build

%install
%python3_install
./install-icons.sh %buildroot%_exec_prefix

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*.egg-info
%_datadir/metainfo/%xdg_name.metainfo.xml
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/%xdg_name.desktop
%_pixmapsdir/%xdg_name.png

%changelog
* Thu Jun 19 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- Initial build
