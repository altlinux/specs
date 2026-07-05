%define _unpackaged_files_terminate_build 1
%def_enable snapshot

%define ver_major 0.56
%define beta %nil
%define gmobile_ver 0.4.0
%define rdn_name mobi.phosh.MobileSettings
%define libname libpms
%define namespace Pms
%define api_ver 1.0

%def_disable embed_gmobile
%def_enable introspection
%def_enable man
%def_enable examples
# Linux dmabuf support unavailable
%def_disable check

%define gvc_ver d2442f45

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
# https://gitlab.gnome.org/GNOME/libgnome-volume-control.git
Source10: gvc-%gvc_ver.tar
%{?_enable_embed_gmobile:Source11: gmobile-%gmobile_ver.tar}

%define phoc_ver %ver_major
%define phosh_ver %ver_major
%define phosh_settings_ver 0.40
%define desktop_ver 44

Requires: %libname = %EVR
Requires: dconf feedbackd lm_sensors3
# and ModemManager 1.25.1
Requires: cellbroadcastd
# for sysfs backend
Requires: sysfsutils

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: gcc-c++ meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.84
BuildRequires: pkgconfig(gtk4) >= 4.12.5
BuildRequires: pkgconfig(gtk4-wayland) >= 4.22
BuildRequires: pkgconfig(libadwaita-1) >= 1.9
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(gsound)
BuildRequires: libsensors3-devel
BuildRequires: pkgconfig(phosh-plugins)
BuildRequires: pkgconfig(phosh-settings) >= %phosh_settings_ver
BuildRequires: pkgconfig(gnome-desktop-4) >= %desktop_ver
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(libportal-gtk4)
# since 0.49
BuildRequires: pkgconfig(libcellbroadcast-0.0)
# since 0.50
BuildRequires: pkgconfig(yaml-0.1)
# since 0.55
BuildRequires: pkgconfig(accountsservice) >= 23.13
BuildRequires: pkgconfig(polkit-gobject-1)
# for gvc
BuildRequires: pkgconfig(libpulse)
%if_enabled embed_gmobile
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gobject-introspection-devel}
%else
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
%endif
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Adw) = 1}
%{?_enable_man:BuildRequires: %_bindir/rst2man}
%{?_enable_check:BuildRequires: xvfb-run phoc >= %phoc_ver phosh /usr/bin/Xwayland}

%description
Mobile Settings App for phosh and related components.

%package -n %libname
Summary: Library for %name
License: LGPL-2.1-or-later
Group: System/Libraries

%description -n %libname
The %libname package contains shared library for %name.

%package -n %libname-devel
Summary: Development files for %libname
License: LGPL-2.1-or-later
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
The %name-devel package contains libraries and header files for
developing applications that use %libname.

%package -n %libname-gir
Summary: GObject introspection data for %libname
Group: System/Libraries
Requires: %libname = %EVR

%description -n %libname-gir
GObject introspection data for %libname

%package -n %libname-gir-devel
Summary: GObject introspection devel data for %libname
Group: Development/Other
BuildArch: noarch
Requires: %libname-gir = %EVR
Requires: %libname-devel = %EVR

%description -n %libname-gir-devel
GObject introspection devel data for %libname

%package -n %libname-demo
Summary: %libname demo programs
License: LGPL-3.0-or-later
Group: Graphical desktop/GNOME
Requires: %libname = %EVR
Requires: python3-module-pygobject3

%description -n %libname-demo
This provides example program that uses %libname.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta -a10 %{?_enable_embed_gmobile:-a11
mv gmobile-%gmobile_ver subprojects/gmobile}

mv gvc-%gvc_ver subprojects/gvc
pushd subprojects/gvc
# not needed with latest gvc
#for p in ../packagefiles/gvc/*.patch; do
#    patch -p1 -i $p; done
popd

%build
%meson \
    %{subst_enable_meson_bool man man} \
    %{subst_enable_meson_bool examples examples} \
    -Dpolkit-group=wheel
%nil
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
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/rules.d/phosh-mobile-settings.rules
%_datadir/icons/hicolor/scalable/apps/%rdn_name.svg
%_datadir/icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%{?_enable_man:%_man1dir/%name.1*}
%doc README* NEWS

%files -n %libname
%_libdir/%libname-%api_ver.so.*

%files -n %libname-devel
%_includedir/pms-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/pms-%api_ver.pc
%{?_enable_vala:%_datadir/vala/vapi/pms-%api_ver.*}

%if_enabled introspection
%files -n %libname-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n %libname-gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled examples
%files -n %libname-demo
%endif

%changelog
* Sun Jul 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- updated to v0.56.0-2-g2b98cc7

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.55.0-alt1
- 0.55.0

* Sun Apr 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- 0.54.0
- new libpms* subpackages

* Sun Feb 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- updated to v0.53.0-2-g6f77f42

* Sun Jan 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1
- 0.51.0

* Thu Oct 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt1
- 0.50.1

* Sun Oct 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Fri Aug 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.49.0-alt1
- 0.49.0

* Mon Jun 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48.0-alt1
- 0.48.0

* Thu Jun 26 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48-alt0.9.rc1
- v0.48_rc1-7-g91a52c3

* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.47.0-alt1
- 0.47.0

* Mon Mar 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt1
- 0.45.0

* Mon Dec 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Fri Nov 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1
- updated to v0.43.0-7-g2a4add4

* Tue Oct 01 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1.1
- packaged lost schemas file (ALT #51612)

* Mon Sep 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

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



