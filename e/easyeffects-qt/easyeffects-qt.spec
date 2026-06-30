%def_disable snapshot
%define __isa_bits %(s="%_lib"; s=${s#lib}; echo "${s:-32}")

%define _name easyeffects
%define xdg_name com.github.wwmm.%_name

Name: %_name-qt
Version: 8.2.7
Release: alt1

Summary: Audio effects for Pipewire applications
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/wwmm/easyeffects

Vcs: https://github.com/wwmm/easyeffects.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

ExcludeArch: %ix86

Conflicts: %_name < 8.0.0

%define pw_api_ver 0.3
%define pw_ver 1.6
%define lv2_ver 1.18.2
%define lilv_ver 0.22
%define calf_ver 0.90.1
%define lsp_ver 1.2.10

Requires: qt6-wayland
Requires: pipewire >= %pw_ver dconf
Requires: calf calf-plugins >= %calf_ver
Requires: lv2-lsp-plugins >= %lsp_ver
Requires: lv2-mda-plugins
Requires: lv2-zam-plugins
Requires: lv2-x42-plugins
%ifnarch %ix86
Requires: ladspa-deepfilternet-plugins
%endif
Requires: kf6-kirigami-addons
Requires: xdg-desktop-portal-kde
Requires: libqtgraphs-qt6
# https://bugzilla.altlinux.org/58803
Requires: kf6-qqc2-desktop-style libkf6sonnetui

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: desktop-file-utils /usr/bin/appstreamcli
BuildRequires: pkgconfig(libpipewire-%pw_api_ver) >= %pw_ver
BuildRequires: pkgconfig(libmysofa)
BuildRequires: nlohmann-json-devel
BuildRequires: pkgconfig(gsl)
BuildRequires: lv2-devel >= %lv2_ver
BuildRequires: ladspa_sdk
BuildRequires: libsndfile-devel libsamplerate-devel libfftw3-devel
BuildRequires: libbs2b-devel
BuildRequires: liblilv-devel >= %lilv_ver
BuildRequires: libebur128-devel
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(rnnoise) >= 0.2
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(soundtouch)
BuildRequires: zita-convolver-devel
BuildRequires: libtbb-devel
BuildRequires: libgio-devel
BuildRequires: libwebrtc-audio-processing-2-devel
BuildRequires: libvulkan-devel
# QT
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Graphs)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6QuickControls2)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(libportal-qt6)
# KDE
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kirigami-addons-devel kf6-kirigami-addons
BuildRequires: kf6-qqc2-desktop-style-devel

%description
This application was formerly known as PulseEffects, but it was
renamed to EasyEffects after it started to use GTK4 and GStreamer
usage was replaced by native PipeWire filters. And eventually the whole
application was ported from GTK4 to a combination of Qt, QML and
KDE/Kirigami frameworks.

%prep
%setup -n %_name-%version

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang --with-gnome --output=%name.lang %_name

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* src/contents/docs/community/CHANGELOG.md

%changelog
* Tue Jun 30 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.7-alt1
- 8.2.7

* Sun Jun 28 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.5-alt1
- 8.2.5

* Sun May 24 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.4-alt1
- 8.2.4

* Sun May 10 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.2-alt1
- 8.2.2

* Sun Apr 26 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.1-alt1
- 8.2.1

* Wed Apr 15 2026 Yuri N. Sedunov <aris@altlinux.org> 8.2.0-alt1
- 8.2.0

* Tue Apr 14 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.9-alt1
- 8.1.9

* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.8-alt1
- 8.1.8

* Fri Mar 20 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.6-alt1
- 8.1.6

* Wed Mar 18 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.5-alt1
- 8.1.5

* Wed Mar 11 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.4-alt1
- 8.1.4

* Mon Mar 09 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.3-alt1
- 8.1.3

* Fri Feb 13 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.2-alt1.1
- removed useless since 8.0.7 QtWebEngine from BR

* Tue Feb 03 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.2-alt1
- 8.1.2

* Sat Jan 31 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.1-alt1
- 8.1.1

* Sat Jan 17 2026 Yuri N. Sedunov <aris@altlinux.org> 8.1.0-alt1
- 8.1.0

* Thu Dec 25 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.9-alt1
- 8.0.9

* Sat Dec 13 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.8-alt1
- 8.0.8

* Tue Dec 02 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.6-alt1
- 8.0.6

* Tue Nov 25 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.5-alt1
- 8.0.5

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.3-alt1
- 8.0.3

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.1-alt0.9
- 8.0.1

* Mon Nov 10 2025 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt0.1
- v8.0.0-22-g337f6066d (ported to Qt/KDE)

* Tue Sep 09 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.5-alt1.1
- fixed build for %%e2k by ilyakurdyukov@

* Sat Jul 19 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.5-alt1
- 7.2.5

* Tue Jul 08 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.4-alt1
- 7.2.4

* Wed Jul 02 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.3-alt2
- updated runtime dependencies:
  ladspa-zam-plugins -> lv2-zam-plugins (ALT #55023)
  + ladspa-deepfilternet-plugins (ALT #55024)

* Tue Jan 07 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.3-alt1
- 7.2.3

* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 7.2.2-alt1
- 7.2.2

* Sat Nov 23 2024 Yuri N. Sedunov <aris@altlinux.org> 7.2.1-alt1
- 7.2.1

* Wed Nov 20 2024 Yuri N. Sedunov <aris@altlinux.org> 7.2.0-alt1
- 7.2.0

* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.9-alt1
- 7.1.9

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.8-alt1
- 7.1.8

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.7-alt1
- updated to v7.1.7-6-gc1b678a11

* Sat Mar 30 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.6-alt1
- 7.1.6

* Sat Mar 23 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.5-alt1
- 7.1.5

* Fri Feb 02 2024 Yuri N. Sedunov <aris@altlinux.org> 7.1.4-alt1
- 7.1.4
- added lv2-mda-plugins to runtime dependencies (ALT #4913)

* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 7.1.3-alt1
- 7.1.3

* Tue Oct 31 2023 Yuri N. Sedunov <aris@altlinux.org> 7.1.1-alt1.1
- required lsp-plugins for all default arches

* Sat Oct 28 2023 Yuri N. Sedunov <aris@altlinux.org> 7.1.1-alt1
- 7.1.1

* Thu Sep 07 2023 Yuri N. Sedunov <aris@altlinux.org> 7.1.0-alt1
- 7.1.0

* Tue Aug 29 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.8-alt1
- 7.0.8

* Sat Aug 12 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.7-alt1
- 7.0.7

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.6-alt1
- 7.0.6

* Tue Jun 13 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.5-alt1
- 7.0.5

* Tue May 02 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.4-alt1
- 7.0.4

* Thu Apr 06 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.3-alt1
- 7.0.3

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

