%define _name tap-plugins

Name: ladspa-%_name
Version: 0.7.0
Release: alt1

Summary: Tom's Audio Processing plugins for LADSPA
License: GPL
Group: Sound
Url: http://%_name.sourceforge.net
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%_name-%version.tar.gz

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver

BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Tue Sep 21 2004
BuildRequires: ladspa_sdk

%description
TAP-plugins is short for Tom's Audio Processing plugins. It is a bunch
of LADSPA plugins for digital audio processing, intended for use in a
professional DAW environment such as Ardour.

Now available plugins: 
TAP AutoPanner,
TAP DeEsser,
TAP Dynamics
TAP Equalizer,
TAP Fractal Doubler
TAP Pink/Fractal Noise
TAP Pitch Shifter,
TAP Reflector
TAP Reverberator,
TAP Rotary Speaker,
TAP Stereo Echo,
TAP Tremolo,
TAP Vibrato,

%prep
%setup -n %_name-%version

# use system ladspa.h
%__rm -f ladspa.h
find . -type f -print0|xargs -r0 %__subst 's,"ladspa\.h",<ladspa.h>,' --
%__subst 's,ladspa\.h,,
	  s,mkdirhier,mkdir -p,' Makefile

%build
%remove_optflags %optflags_optimization
%make_build CC="%__cc $RPM_OPT_FLAGS"

%install
%make_install INSTALL_PLUGINS_DIR=%buildroot%_ladspa_path \
	      INSTALL_LRDF_DIR=%buildroot%_ladspa_datadir/rdf install

%files
%_ladspa_path/*.so
%_ladspa_datadir/rdf/*
%doc README CREDITS

%changelog
* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt1
- new version.

* Wed Jun 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Sat May 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus
