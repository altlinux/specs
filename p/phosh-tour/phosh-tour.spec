%def_disable snapshot

%define gmobile_ver v0.0.6
%define rdn_name mobi.phosh.PhoshTour

Name: phosh-tour
Version: 0.37.0
Release: alt1

Summary: Phosh Tour
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phosh-tour

Vcs: https://gitlab.gnome.org/World/Phosh/phosh-tour

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/phosh-tour/-/archive/v%version/%name-v%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: gmobile-%gmobile_ver.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk4) >= 4.12
BuildRequires: pkgconfig(libadwaita-1) >= 1.4
# for gmobile
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Simple introduction to phosh.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version -a1
rm -r subprojects/gmobile
mv gmobile-%gmobile_ver subprojects/gmobile

%build
%meson
%meson_build

%install
%meson_install
rm %buildroot%_libdir/libgmobile.*
rm %buildroot%_pkgconfigdir/gmobile.pc

%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/icons/hicolor/scalable/apps/%rdn_name.svg
%_datadir/icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- first build for Sisyphus



