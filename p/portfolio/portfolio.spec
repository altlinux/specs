%def_disable snapshot

%define _name Portfolio
%define ver_major 1.0
%define rdn_name dev.tchx84.Portfolio

%ifarch armh
%def_disable check
%else
%def_enable check
%endif

Name: portfolio
Version: %ver_major.0
Release: alt1

Summary: File manager for Linux mobile devices
License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/tchx84/Portfolio

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/tchx84/Portfolio.git
Source: %name-%version.tar
%endif

BuildArch: noarch

%define adwaita_ver 1.0

Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: typelib(Adw)
%{?_enable_check:BuildRequires: xvfb-run python3(pyflakes) python3(pytest)
BuildRequires: python3(black) python3(gi)}

%description
A minimalist file manager for those who want to use Linux mobile devices.

%prep
%setup -n %_name-%version
sed -i "s|'pytest'|'py.test-3'|
        s|'pyflakes'|'pyflakes-py3'|" tests/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%rdn_name
%python3_sitelibdir_noarch/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/polkit-1/rules.d/%rdn_name.rules
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* CHANGELOG*


%changelog
* Sat Sep 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


