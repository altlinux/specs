%def_enable snapshot
%define xdg_name com.github.wwmm.easyeffects

Name: easyeffects
Version: 7.0.1
Release: alt1

Summary: Audio effects for Pipewire applications
License: GPL-3.0
Group: Sound
Url: https://github.com/wwmm/%name

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/wwmm/easyeffects.git
Source: %name-%version.tar
%endif

%define sigc_ver 3.0.6
%define gtk_ver 4.2.1
%define adwaita_ver 1.0.0
%define pw_api_ver 0.3
%define pw_ver 0.3.41
%define lv2_ver 1.18.2
%define lilv_ver 0.22
%define calf_ver 0.90.1
%define lsp_ver 1.1.24

Requires: pipewire >= %pw_ver dconf
Requires: ladspa-rubberband
Requires: ladspa-zam-plugins
Requires: calf-plugins >= %calf_ver
%ifarch %ix86 x86_64 aarch64
Requires: lv2-lsp-plugins >= %lsp_ver
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ pkgconfig(sigc++-3.0) >= %sigc_ver libfmt-devel
BuildRequires: yelp-tools desktop-file-utils /usr/bin/appstream-util
BuildRequires: libgtk4-devel >= %gtk_ver pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(libpipewire-%pw_api_ver) >= %pw_ver
BuildRequires: nlohmann-json-devel
BuildRequires: pkgconfig(gsl)
BuildRequires: lv2-devel >= %lv2_ver
BuildRequires: libsndfile-devel libsamplerate-devel libfftw3-devel
BuildRequires: libbs2b-devel
BuildRequires: liblilv-devel >= %lilv_ver
BuildRequires: libebur128-devel
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(rnnoise)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(rubberband)
BuildRequires: zita-convolver-devel
BuildRequires: libdbus-devel
BuildRequires: libtbb-devel

%description
This application used to be called PulseEffects but it was renamed to
EasyEffects after we started to use GTK4 and replaced GStreamer by native
PipeWire filters.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
# system-wide config directory
mkdir -p %buildroot%_sysconfdir/EasyEffects

%find_lang --with-gnome --output=%name.lang %name %name-news

%files -f %name.lang
%_bindir/%name
%dir %_sysconfdir/EasyEffects
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.*gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* CHANGELOG.*

%changelog
* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.1-alt1
- updated to v7.0.1-5-g224b641a

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 6.3.0-alt1
- 6.3.0

* Tue Jul 26 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.8-alt1
- 6.2.8

* Tue Jul 19 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.7-alt1
- 6.2.7

* Thu Jun 23 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.6-alt1
- 6.2.6

* Sun May 01 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.5-alt1
- 6.2.5

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.4-alt1
- 6.2.4

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.3-alt1
- 6.2.3

* Thu Jan 06 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.1-alt1
- updated to v6.2.1-1-gcd8967b5 (ported to GTK4 + LibAdwaita)

* Thu Nov 18 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.5-alt1
- 6.1.5

* Sun Oct 17 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.4-alt1
- 6.1.4

* Mon Oct 04 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.3-alt1
- 6.1.3

* Mon Sep 20 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.2-alt1
- 6.1.2

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- 6.1.1

* Tue Sep 14 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- first build to Sisyphus

