%define gmobile_ver v0.0.4
%define rdn_name mobi.phosh.MobileSettings

Name: phosh-mobile-settings
Version: 0.34.0
Release: alt1

Summary: Mobile Settings App for phosh and related components
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/guidog/phosh-mobile-settings

Vcs: https://gitlab.gnome.org/guidog/phosh-mobile-settings.git
Source: https://gitlab.gnome.org/guidog/phosh-mobile-settings/-/archive/v%version/phosh-mobile-settings-v%version.tar.gz
Source1: gmobile-%gmobile_ver.tar

Requires: dconf lm_sensors3

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.68
BuildRequires: pkgconfig(gtk4) >= 4.4
BuildRequires: pkgconfig(gtk4-wayland) >= 4.4
BuildRequires: pkgconfig(libadwaita-1) >= 1.1
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(gsound)
BuildRequires: libsensors3-devel
BuildRequires: pkgconfig(phosh-plugins)

# for gmobile
BuildRequires: pkgconfig(json-glib-1.0)

%description
Mobile Settings App for phosh and related components.

%prep
%setup -n %name-v%version -a1
mv gmobile-%gmobile_ver subprojects/gmobile

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libms-plugin-librem5.so
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/scalable/apps/%rdn_name.svg
%_datadir/icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Wed Nov 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Sun Oct 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.31.0-alt1
- first build for Sisyphus



