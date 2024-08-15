%def_enable snapshot

%define ver_major 0.41
%define beta %nil
%define gmobile_ver 0.2.0
%define rdn_name mobi.phosh.MobileSettings

%def_disable embed_gmobile
# Linux dmabuf support unavailable
%def_disable check

Name: phosh-mobile-settings
Version: %ver_major.0
Release: alt1%beta

Summary: Mobile Settings App for phosh and related components
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings

Vcs: https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
%{?_enable_embed_gmobile:Source1: gmobile-%gmobile_ver.tar}

%define phoc_ver %ver_major

Requires: dconf lm_sensors3

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.74
BuildRequires: pkgconfig(gtk4) >= 4.12.5
BuildRequires: pkgconfig(gtk4-wayland) >= 4.4
BuildRequires: pkgconfig(libadwaita-1) >= 1.1
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(gsound)
BuildRequires: libsensors3-devel
BuildRequires: pkgconfig(phosh-plugins)
#BuildRequires: pkgconfig(phosh-settings-schemas)
%if_enabled embed_gmobile
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gobject-introspection-devel}
%else
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
%endif
%{?_enable_check:BuildRequires: xvfb-run phoc >= %phoc_ver phosh /usr/bin/Xwayland}

# for gmobile
BuildRequires: pkgconfig(json-glib-1.0)

%description
Mobile Settings App for phosh and related components.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta %{?_enable_embed_gmobile:-a1
mv gmobile-%gmobile_ver subprojects/gmobile}

%build
%meson
%meson_build

%install
%meson_install
%{?_enable_embed_gmobile:rm %buildroot%_libdir/libgmobile.*
rm %buildroot%_pkgconfigdir/gmobile.pc}

%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libms-plugin-librem5.so
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/icons/hicolor/scalable/apps/%rdn_name.svg
%_datadir/icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- 0.41.0.rc1

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Wed Jun 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt0.9.rc1
- 0.40.0.rc1

* Wed May 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- 0.37.0

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- updated to v0.36.0-5-g794fa6e

* Tue Jan 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.35.1-alt1
- 0.35.1

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.35.0-alt1
- 0.35.0

* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Wed Nov 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Sun Oct 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.31.0-alt1
- first build for Sisyphus



