%def_disable snapshot
%define _libexecdir %_prefix/libexec

Name: evisum
Version: 0.5.9
Release: alt1

Summary: The Enlightenment system and process monitor
Group: Graphical desktop/Enlightenment
License: ISC
Url: https://enlightenment.org

%if_disabled snapshot
Source: https://download.enlightenment.org/rel/apps/%name/%name-%version.tar.xz
%else
# VCS: https://git.enlightenment.org/apps/evisum.git
Source: %name-%version.tar
%endif

%define efl_ver 1.22

BuildRequires(pre): meson
BuildRequires: libelementary-devel >= %efl_ver

%description
System and process monitor for Enlightenment

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_desktopdir/%{name}_cpu.desktop
%_desktopdir/%{name}_mem.desktop
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS NEWS README

%changelog
* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- 0.5.9

* Mon Nov 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Mon Aug 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Fri Aug 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Wed Jul 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (v0.5.0-2-gd71b1a2)


