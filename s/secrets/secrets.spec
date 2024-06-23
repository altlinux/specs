%def_enable snapshot

%define ver_major 9
%define pypi_name gsecrets
%define xdg_name org.gnome.World.Secrets

%def_disable check

Name: secrets
Version: %ver_major.5
Release: alt1

Summary: A password manager for GNOME
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/secrets

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/secrets.git
Source: %name-%version.tar
%endif

%define glib_ver 2.74
%define gtk_ver 4.9
%define adwaita_ver 1.5

Requires: typelib(Adw) = 1
Requires: yelp

BuildArch: noarch
%py3_provides %pypi_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: python3(pykeepass) python3(pyotp) python3(validators)
BuildRequires: python3(zxcvbn) python3(PyKCS11) python3(yubico)
%{?_enable_check:
BuildRequires: desktop-file-utils /usr/bin/appstreamcli
BuildRequires: python3(pytest) python3(gi) typelib(Gtk) = 4.0 ruff}

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
* Sun Jun 23 2024 Yuri N. Sedunov <aris@altlinux.org> 9.5-alt1
- 9.5

* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 9.4-alt1
- updated to 9.4-1-gf121ced7

* Mon Apr 01 2024 Yuri N. Sedunov <aris@altlinux.org> 9.3-alt1
- updated to 9.3-3-g402a759f

* Tue Mar 26 2024 Yuri N. Sedunov <aris@altlinux.org> 9.2-alt1
- 9.2

* Mon Mar 25 2024 Yuri N. Sedunov <aris@altlinux.org> 9.1-alt1
- updated to 9.1-2-gc1637e02

* Thu Mar 21 2024 Yuri N. Sedunov <aris@altlinux.org> 9.0-alt1
- 9.0

* Fri Sep 22 2023 Yuri N. Sedunov <aris@altlinux.org> 8.0-alt1
- 8.0

* Wed Jun 28 2023 Yuri N. Sedunov <aris@altlinux.org> 7.3-alt1
- first build for Sisyphus


