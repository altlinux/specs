%define _name blop

Name: ladspa-%_name-plugins
Version: 0.2.8
Release: alt2

Summary: Bandlimited LADSPA Oscillator Plugins
License: GPL
Group: Sound
Url: http://blop.sourceforge.net/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %_name-%version.tar.gz
Patch: blop-0.2.8-fix-link.patch

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Wed Jun 23 2004
BuildRequires: ladspa_sdk

%description
BLOP comprises a set of LADSPA plugins that generate bandlimited
sawtooth, square, variable pulse and slope-variable triangle waves, for
use in LADSPA hosts, principally for use with one of the many modular
software synthesisers available. They are wavetable based, and are
designed to produce output with harmonic content as high as possible
over a wide pitch range. Additionally, there are a few extra plugins to
assist in building synthesis networks.

%prep
%setup -n %_name-%version
%patch -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot pkgbindir=%_ladspa_path install
%__install -pD -m644 doc/blop.rdf %buildroot%_ladspa_datadir/rdf/blop.rdf

%find_lang %_name

%files -f %_name.lang
%_ladspa_path/*
%_ladspa_datadir/rdf/*
%doc AUTHORS README NEWS ChangeLog THANKS TODO
%doc doc/*.txt

%changelog
* Sun Feb 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.2.8-alt2
- Fix plugin build

* Wed Jun 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Thu Feb 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.7-alt1
- First build for Sisyphus.

