%define xdg_name org.alt.Tweaks

Name: alt-tweaks
Version: 0.2.1
Release: alt5

Summary: A tool to customize advanced phosh options of ALT Mobile OS
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://gitlab.com/postmarketOS/postmarketos-tweaks

Source: %name-%version.tar.xz

BuildArch: noarch

%define gsds_ver 45
%define handy_ver 1.5.0

Requires: phosh lm_sensors3

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: gcc-c++ meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.62
BuildRequires: pkgconfig(gtk4) >= 4.4
BuildRequires: pkgconfig(gtk4-wayland) >= 4.4
BuildRequires: pkgconfig(libadwaita-1) >= 1.1
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(gsound)
BuildRequires: libsensors3-devel
BuildRequires: pkgconfig(phosh-plugins)
BuildRequires: libhandy1-devel 

%description
Mobile Advanced Settings App for phosh and related components of ALT Mobile OS.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
rm -f %buildroot%_datadir/postmarketos-tweaks/postmarketos-tweakd.initd.in

# for locale in ru_RU en_US; do
# install -D -m 0644 data/about-$locale.txt %buildroot%_datadir/%name/$locale/about.txt
# done


%find_lang %name

%files -f %name.lang
%_bindir/pk-tweaks-action
%_bindir/alt-tweakd
%_bindir/alt-tweaks
%_desktopdir/%xdg_name.desktop
%_datadir/alt-tweaks/
%_datadir/polkit-1/actions/
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*

%changelog
* Fri Nov 17 2023 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt5
- Replaced info about device in separate config in en_US locale;
- Updated version in "about" files.

* Thu Nov 16 2023 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt4
- Optimized getting locale variable (thanks to bircoph@)

* Wed Nov 08 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.1-alt3
- Fix getting locale (next iteration).

* Sun Nov  5 2023 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt2
- Fix back getting locale value

* Fri Nov  3 2023 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt1
- Fix locale value

* Fri Oct 27 2023 Artyom Bystrov <arbars@altlinux.org> 0.2-alt1
- Add simply (dumb, bout working) l10n support (UTF-8-only)
- Add Pinephone Pro battery charging level settings
- Add description of program

* Fri Oct  6 2023 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit as fork of PostmarketOS tweaks

* Thu Oct  5 2023 Artyom Bystrov <arbars@altlinux.org> 0.13.1-alt2
- Add Pinephone Pro battery support

* Thu Oct  5 2023 Artyom Bystrov <arbars@altlinux.org> 0.13.1-alt1
- Initial commit
