%def_disable snapshot
%define _name mda-lv2

Name: lv2-mda-plugins
Version: 1.2.2
Release: alt1

Summary: A port of the MDA VST plugins to LV2
Group: Sound
License: GPLv3+
Url: https://drobilla.net/software/mda-lv2

%if_disabled snapshot
Source: https://download.drobilla.net/%_name-%version.tar.bz2
%else
#VCS: https://git.drobilla.net/mda.lv2.git
Source: %_name-%version.tar
%endif

Requires: lv2

BuildRequires: gcc-c++ lv2-devel libsuil-devel libgtk+2-devel

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%setup -n %_name-%version
sed -i -e 's|obj.cxxflags = cflags|obj.cxxflags = cflags + "%optflags".split(" ")|' wscript

%build
./waf configure -v --prefix=%prefix --libdir=%_libdir
./waf -v build %{?_smp_mflags}

%install
./waf install --destdir=%buildroot

%files
%_libdir/lv2/mda.lv2
%doc NEWS README

%changelog
* Thu Jun 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- first build for Sisyphus

