%def_enable snapshot

%define _name password
%define ver_major 1.6
%define rdn_name io.gitlab.elescoute.%_name

# online screenshots
%def_disable check

Name: gnome-%_name
Version: %ver_major.3
Release: alt1

Summary: Password calculator and random generator for Gnome
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.com/elescoute/password

Vcs: https://gitlab.com/elescoute/password.git

%if_disabled snapshot
Source: %url/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(webkitgtk-6.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
This app calculates strong unique passwords for each alias and
passphrase combination.

No need to remember dozens of passwords any longer and no need for a
password manager!

The calculator can use MD5, SHA1, SHA256 and SHA512 hash algorithms in
combination with HMAC.

Compatible with Linux Phone using Phosh (PinePhone, Librem 5).

%prep
%setup -n %_name-%version
sed -i "s/\('appstream\)-util'/\1cli'/" data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name %rdn_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Jun 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Mon Jun 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sun Jun 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- first build for Sisyphus (1.6.0-3-g805f45b)


