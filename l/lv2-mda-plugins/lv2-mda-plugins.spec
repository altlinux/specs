%def_disable snapshot
%define _name mda-lv2
%def_disable check

Name: lv2-mda-plugins
Version: 1.2.10
Release: alt1

Summary: A port of the MDA VST plugins to LV2
Group: Sound
License: GPL-2.0-or-later
Url: https://drobilla.net/software/mda-lv2

%if_disabled snapshot
Source: https://download.drobilla.net/%_name-%version.tar.xz
%else
Vcs: https://gitlab.com/drobilla/mda-lv2.git
Source: %_name-%version.tar
%endif

Requires: lv2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ lv2-devel
%{?_enable_check:BuildRequires: /usr/bin/autoship /usr/bin/lv2lint /usr/bin/reuse}

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/lv2/mda.lv2
%doc NEWS README*

%changelog
* Thu Sep 29 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.10-alt1
- 1.2.10 (ported to Meson build system)

* Fri Jan 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4
- fixed License tag

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- updated buildreqs

* Thu Jun 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- first build for Sisyphus

