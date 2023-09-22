%def_enable snapshot

%define ver_major 8
%define pypi_name gsecrets
%define xdg_name org.gnome.World.Secrets

%def_disable check

Name: secrets
Version: %ver_major.0
Release: alt1

Summary: A password manager for GNOME
License: GPL-3.0
Group: Networking/File transfer
Url: https://gitlab.gnome.org/World/secrets

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/secrets.git
Source: %name-%version.tar
%endif

%define glib_ver 2.73.1
%define gtk_ver 4.9
%define adwaita_ver 1.4

Requires: typelib(Adw) = 1
Requires: yelp

BuildArch: noarch
%py3_provides %pypi_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: /usr/bin/appstreamcli
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: python3(pykeepass) python3(pyotp) python3(validators) python3(zxcvbn)
%{?_enable_check:BuildRequires: python3(pytest) python3(gi) typelib(Gtk) = 4.0}

%description
A password manager which integrates perfectly with the GNOME desktop and
provides an easy and uncluttered interface for the management of password
databases.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%__meson_test -v

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/mime/packages/%xdg_name.xml
%python3_sitelibdir_noarch/%pypi_name/
%doc README*

%changelog
* Fri Sep 22 2023 Yuri N. Sedunov <aris@altlinux.org> 8.0-alt1
- 8.0

* Wed Jun 28 2023 Yuri N. Sedunov <aris@altlinux.org> 7.3-alt1
- first build for Sisyphus


