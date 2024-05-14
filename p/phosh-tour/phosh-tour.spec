%def_disable snapshot

%define gmobile_ver v0.1.0
%define rdn_name mobi.phosh.PhoshTour

%def_disable embed_gmobile
%def_enable check

Name: phosh-tour
Version: 0.39.0
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
%{?_enable_embed_gmobile:Source1: gmobile-%gmobile_ver.tar}

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk4) >= 4.12
BuildRequires: pkgconfig(libadwaita-1) >= 1.4
%if_enabled embed_gmobile
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gobject-introspection-devel}
%else
BuildRequires: pkgconfig(gmobile)
%endif

%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Simple introduction to phosh.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version %{?_enable_embed_gmobile:-a1
mv gmobile-%gmobile_ver subprojects/gmobile}

%build
%meson
%meson_build

%install
%meson_install
%if_enabled embed_gmobile
rm %buildroot%_libdir/libgmobile.*
rm %buildroot%_pkgconfigdir/gmobile.pc
%endif

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
* Wed May 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0
- build against shared gmobile-0.1.0 library

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- first build for Sisyphus



