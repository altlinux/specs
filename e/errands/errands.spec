%def_enable snapshot

%define ver_major 45
%define rdn_name io.github.mrvladus.List

%def_disable check

Name: errands
Version: %ver_major.0.4
Release: alt1

Summary: Todo application for GNOME
License: MIT
Group: Office
Url: https://github.com/mrvladus/Errands.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/mrvladus/Errands.git
Source: %name-%version.tar
%endif

%define adwaita_ver 1.2

Requires: typelib(Adw) = 1
Requires: yelp

BuildArch: noarch

%add_python3_path %_datadir/%name

Requires: python3-module-icalendar >= 5.0.9

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: /usr/bin/appstreamcli
%{?_enable_check:BuildRequires: python3(pytest)}

%description
Todo application for those who prefer simplicity.

%prep
%setup

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
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0.4-alt1
- updated to 45.0.4-27-g01e9d07

* Tue Oct 03 2023 Yuri N. Sedunov <aris@altlinux.org> 44.7.6-alt1
- first build for Sisyphus (44.7.6-7-ge26c812)


