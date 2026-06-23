%def_disable snapshot

%define _name dosage
%define __name Dosage
%define ver_major 2.1
%define rdn_name io.github.diegopvlk.Dosage

%def_enable check

Name: gnome-%_name
Version: %ver_major.8
Release: alt1

Summary: GNOME Dosage
License: GPL-3.0-or-later
Group: Sciences/Medicine
Url: https://github.com/diegopvlk/Dosage

Vcs: https://github.com/diegopvlk/Dosage.git

%if_disabled snapshot
Source: https://github.com/diegopvlk/Dosage/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.14
%define adw_ver 1.8

Requires: /usr/bin/gjs dconf
Requires: libadwaita >= %adw_ver
Requires: typelib(Adw) = 1
Requires: typelib(Xdp) = 1.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/gjs
BuildRequires: blueprint-compiler >= %bp_ver typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Keep track of your treatments.

Features:
- Notifications - Get reminders at the right time
- History - See which medications you took or skipped
- Dosage management - Multiple doses with different times
- Frequency modes - Every day, selected days, cycle or just when needed
- Color and icon - Give a shape for your treatment
- Inventory tracking - Monitor your stock and get reminded when it's low
- Duration - Define the start and end dates

%prep
%setup -n %__name-%version
sed -i "s|no-net --explain|no-net', '--explain|" data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*

%changelog
* Tue Jun 23 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt1
- 2.1.8

* Sun Apr 19 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Wed Apr 01 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Wed Mar 04 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Sat Feb 07 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Mon Jan 12 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Dec 09 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri Dec 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Mon Sep 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.11-alt1
- 1.9.11

* Sat Aug 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.10-alt1
- 1.9.10

* Sat May 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.9-alt1
- 1.9.9

* Mon Apr 21 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.7-alt1
- 1.9.7

* Tue Apr 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.6-alt1
- 1.9.6

* Sat Mar 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5

* Sun Mar 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Thu Feb 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.3-alt1
- 1.9.3

* Tue Feb 25 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Tue Feb 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Mon Feb 03 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Sat Jan 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sun Jan 12 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Fri Jan 03 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Dec 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Fri Nov 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Tue Nov 12 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sun Nov 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Wed Oct 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Fri Sep 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sun Aug 04 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Sat Jul 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Fri Jul 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Thu Jul 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat May 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Thu Mar 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Feb 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Mon Feb 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 24 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.8-alt1
- 1.4.8

* Wed Dec 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt1
- 1.4.7

* Sat Dec 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Sun Dec 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sat Dec 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Tue Nov 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Nov 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Nov 10 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Wed Nov 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Thu Nov 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Wed Nov 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Oct 30 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus


