%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name gdm-settings
%define pypi_name gdms
%define ver_major 4.4
%define rdn_name io.github.realmazharhussain.GdmSettings

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: GDM Settings
License: AGPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/gdm-settings/gdm-settings
Vcs: https://github.com/gdm-settings/gdm-settings.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.10
%define adw_ver 1.4

Requires: typelib(Adw) = 1 dconf /usr/bin/pkexec

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver typelib(Adw)
BuildRequires: pkgconfig(pygobject-3.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
A settings app for GNOME's Login/Display Manager, GDM. It is written in
Python and uses LibAdwaita for graphical interface.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%python3_sitelibdir_noarch/%pypi_name/
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%{rdn_name}*.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README* NEWS


%changelog
* Thu May 09 2024 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- 4.4

* Thu Feb 29 2024 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Mon Feb 26 2024 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Sat Feb 3 2024 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- first build for Sisyphus (v4.1-18-g38c63db)


