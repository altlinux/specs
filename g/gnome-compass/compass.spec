%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name compass
%define ver_major 0.4
%define rdn_name com.gitlab.lgtrombetta.Compass

Name: gnome-%_name
Version: %ver_major.0
Release: alt1

Summary: A simple GTK3 compass app for Mobile Linux.
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://gitlab.com/lgtrombetta/compass

%if_enabled snapshot
Vcs: https://gitlab.com/lgtrombetta/compass.git
Source: %_name-%version.tar
%else
Source: %url/-/archive/v%version/%_name-%version.tar.gz
%endif

BuildArch: noarch
%add_python3_path %_datadir/%_name

%define handy_ver 1.5.0

Requires: dconf
Requires: typelib(Gtk) = 3.0 typelib(Handy) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson /usr/bin/appstream-util desktop-file-utils
BuildRequires: python3(gi) python3(matplotlib) python3(numpy) python3(pandas)
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver typelib(Handy) = 1

%description
Currently supported devices:

* Pine64 Pinephone v1.0, v1.1, v1.2 (LIS3MDL magnetometer)
* Pine64 Pinephone v1.2b (AF8133J magnetometer)
* Pine64 Pinephone Pro (AF8133J magnetometer, requires Megi's
  kernel>=6.3 for the correct (https://github.com/megous/linux/commit/cf46f43b097bbe5d7a5f96c7c490eae9dee7390b))
* Purism Librem 5 (LSM9DS1 magnetometer)

Known issues:

* AF8133J is not currently recognized in [pmOS](https://gitlab.com/postmarketOS/pmaports/-/issues/1945)

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%_name
%_udevrulesdir/90-magn.rules
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%changelog
* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus

