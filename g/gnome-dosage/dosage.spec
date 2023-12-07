%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name dosage
%define __name Dosage
%define ver_major 1.4
%define rdn_name io.github.diegopvlk.Dosage

%def_disable check

Name: gnome-%_name
Version: %ver_major.5
Release: alt1

Summary: GNOME Dosage
License: GPL-3.0-or-later
Group: Sciences/Medicine
Url: https://github.com/diegopvlk/Dosage.git

%if_disabled snapshot
Source: https://github.com/diegopvlk/Dosage/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/diegopvlk/Dosage.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.10

Requires: /usr/bin/gjs dconf
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
%_datadir/appdata/%rdn_name.*.xml
%doc README*

%changelog
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


