Name: polychromatic
Version: 0.8.2
Release: alt1

Summary: RGB lighting interface utilites
License: GPL-3.0
Group: System/Kernel and hardware
URL: https://github.com/polychromatic/polychromatic

ExclusiveArch: %qt5_qtwebengine_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires: sassc
BuildRequires: intltool
BuildRequires: meson

%description
RGB lighting management front-end application for OpenRazer via a
graphical, command line or tray applet interface.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_bindir/%name-cli
%_bindir/%name-controller
%_bindir/%name-helper
%_bindir/%name-tray-applet
%_datadir/applications/%name.desktop
%_datadir/%name/
%python3_sitelibdir_noarch/%name/
%_man1dir/%name-*

%changelog
* Mon Oct 09 2023 Anton Kurachenko <srebrov@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Sat Jul 1 2023 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
