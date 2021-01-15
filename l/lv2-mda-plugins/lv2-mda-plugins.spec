%def_disable snapshot
%define _name mda-lv2

Name: lv2-mda-plugins
Version: 1.2.6
Release: alt1

Summary: A port of the MDA VST plugins to LV2
Group: Sound
License: GPL-3.0
Url: https://drobilla.net/software/mda-lv2

%if_disabled snapshot
Source: https://download.drobilla.net/%_name-%version.tar.bz2
%else
#VCS: https://git.drobilla.net/mda.lv2.git
Source: %_name-%version.tar
%endif

Requires: lv2

BuildRequires: python3-devel gcc-c++ lv2-devel libsuil-devel libgtk+2-devel

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%setup -n %_name-%version
sed -i 's|\(#!/usr/bin/\)env \(python\)|\1\23|' waf wscript
#sed -i -e 's|obj.cxxflags = cflags|obj.cxxflags = cflags + "%optflags".split(" ")|' wscript

%build
export CXXFLAGS="$CXXFLAGS %optflags"
%__python3 ./waf configure -v --prefix=%prefix --libdir=%_libdir
%__python3 ./waf -v build %{?_smp_mflags}

%install
%__python3 ./waf install --destdir=%buildroot

%files
%_libdir/lv2/mda.lv2
%doc NEWS README*

%changelog
* Fri Jan 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4
- fixed License tag

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- updated buildreqs

* Thu Jun 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- first build for Sisyphus

