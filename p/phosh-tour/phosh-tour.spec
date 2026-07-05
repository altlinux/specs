%def_enable snapshot

%define ver_major 0.56
%define beta %nil
%define gmobile_ver v0.1.0
%define rdn_name mobi.phosh.PhoshTour

%def_disable embed_gmobile
%def_enable check

Name: phosh-tour
Version: %ver_major.0
Release: alt1%beta

Summary: Phosh Tour
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phosh-tour

Vcs: https://gitlab.gnome.org/World/Phosh/phosh-tour

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/phosh-tour/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
%{?_enable_embed_gmobile:Source1: gmobile-%gmobile_ver.tar}

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
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
%setup -n %name-%{?_disable_snapshot:v}%version%beta %{?_enable_embed_gmobile:-a1
mv gmobile-%gmobile_ver subprojects/gmobile}

%build
%meson \
    -Dvendor='ALT Linux' \
    -Durl='https://altmobile.org'
%nil
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
%_xdgconfigdir/autostart/%rdn_name-first-login.desktop
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_userunitdir/%rdn_name-first-login.service
%_datadir/icons/hicolor/scalable/apps/%rdn_name.svg
%_datadir/icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS

%changelog
* Sun Jul 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- 0.56.0

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.55.0-alt1
- 0.55.0

* Sun Apr 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- 0.54.0

* Sun Feb 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Sun Jan 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0

* Sun Oct 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.47.0-alt1
- 0.47.0

* Mon Mar 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt1
- 0.45.0

* Tue Dec 31 2024 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Fri Nov 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1
- 0.43.0

* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- 0.41.0.rc1

* Wed May 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0
- build against shared gmobile-0.1.0 library

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- first build for Sisyphus



