%define _name xmms_ladspa

Name: xmms-ladspa
Version: 0.7
Release: alt1.1

Summary: A LADSPA effect plugin for XMMS
Group: Sound
License: GPL
Url: http://www.ecs.soton.ac.uk/~njl98r/code/ladspa
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %url/%_name-%version.tar.gz

Patch0: xmms_ladspa-0.7-alt-linking.patch

Requires: xmms ladspa-swh-plugins

# Automatically added by buildreq on Thu May 01 2003
BuildRequires: glib-devel gtk+-devel ladspa_sdk libxmms-devel

%description 
XMMS LADSPA is an Effect for XMMS that provides (some of) the power of
the Linux Audio Developer's Simple Plugin API to your everyday MP3 and
all-around media player.

Normally XMMS can only handle a single Effect, such as Echo and it has
to be written specifically for XMMS. With XMMS LADSPA you can use any
number of audio processing plugins written to the LADSPA specification.

%define _xmms_effect_plugin_dir %(xmms-config --effect-plugin-dir)

%prep
%setup -q -n %_name-%version
%patch0 -p1
# use system ladspa_sdk
%__rm -f ladspa.h
find . -type f -print0|xargs -r0 %__subst 's,"ladspa.h",<ladspa.h>,' --

%build
%__subst 's,\(CFLAGS\=\),\1 \$(RPM_OPT_FLAGS),' Makefile
%make_build

%install
%__install -pD ladspa.so %buildroot%_xmms_effect_plugin_dir/ladspa.so

%files
%_xmms_effect_plugin_dir/*.so
%doc ChangeLog PLUGINS README 

%changelog
* Fri Apr 13 2007 Igor Zubkov <icesik@altlinux.org> 0.7-alt1.1
- NMU
- fix linking (#11434)

* Thu May 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Tue Dec 31 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- new version.

* Sun Oct 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt2
- Rebuild with gcc-3.2

* Wed May 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- First build for Sisyphus. 
