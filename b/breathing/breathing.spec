%def_enable snapshot

%define _name breathing
%define __name Breathing
%define ver_major 0.1
%define rdn_name io.github.seadve.%__name

%def_enable check

Name: %_name
Version: %ver_major.4
Release: alt1

Summary: Relax and meditate
License: GPL-3.0-or-later
Group: Sciences/Medicine
Url: https://github.com/SeaDve/Breathing

Vcs: https://github.com/SeaDve/Breathing.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%name

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Breathing is a simple application that guides your breathing pattern.
This pattern is recommended by experts that will help ease your anxiety.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun Sep 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- v0.1.4-2-g34c6889

* Mon May 19 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- first build for Sisyphus (v0.1.3-57-g486487f)


