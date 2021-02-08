%def_enable snapshot
%define _name tap-plugins

Name: ladspa-%_name
Version: 1.0.1
Release: alt1

Summary: Tom's Audio Processing plugins for LADSPA
License: GPL-2.0
Group: Sound
Url: https://tomscii.sig7.se/tap-plugins

%if_disabled snapshot
Source: https://github.com/tomszilagyi/tap-plugins/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/tomszilagyi/tap-plugins.git
Source: %_name-%version.tar
%endif

%define ladspa_ver 1.12-alt2

Requires(pre): ladspa_sdk >= %ladspa_ver

BuildRequires: ladspa_sdk >= %ladspa_ver

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

%build
%define _optlevel 3
%make_build CC="%__cc $RPM_OPT_FLAGS"

%install
%make_install INSTALL_PLUGINS_DIR=%buildroot%_ladspa_path \
    INSTALL_LRDF_DIR=%buildroot%_ladspa_datadir/rdf install

%files
%_ladspa_path/*.so
%_ladspa_datadir/rdf/*
%doc README CREDITS

%changelog
* Sat Feb 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- updated to v1.0.1-1-g5d88279
- updated Url and License tags

* Tue May 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Build new version (Closes: #21359).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.0-alt1.qa1
- NMU: rebuilt for debuginfo.

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
