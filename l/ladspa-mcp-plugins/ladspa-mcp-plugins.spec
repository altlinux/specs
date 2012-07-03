%define _name mcp
%define beta %nil

Name: ladspa-%_name-plugins
Version: 0.4.0
Release: alt1%beta

Summary: The Moog VCF LADSPA plugins
License: GPL
Group: Sound
Url: http://www.kokkinizita.net/linuxaudio/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %url/downloads/MCP-plugins-%version%beta.tar.bz2

Obsoletes: ladspa-moogvcf-plugins
Provides: ladspa-moogvcf-plugins = %version-%release

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Sat May 08 2004
BuildRequires: gcc-c++ ladspa_sdk libstdc++-devel

%description
This LADSPA plugin contains four versions of a digital implementation of
the voltage controlled lowpass filter as used in vintage Moog synthesizers.
Many software versions of this filter already exist. Most use some limiting
mechanism in order to keep the self-oscillation amplitude under control, but
as far as I know, none of them attempt to accurately emulate the non-linear
circuit elements of the original analog filter. To do this has been the 
main reason for developing this plugin.

Also this package provides some phaser and chorus plugins based on
CSound's modules.

%prep
%setup -q -n MCP-plugins-%version%beta

# use system ladspa.h
%__rm -f ladspa.h
find . -type f -print0|xargs -r0 %__subst 's,"ladspa.h",<ladspa.h>,' --

%build
CPPFLAGS="$CPPFLAGS %optflags"; export CPPFLAGS
%make_build

%install
%__mkdir_p %buildroot%_ladspa_path
%__install -m644 *.so %buildroot%_ladspa_path/

%files
%_ladspa_path/*.so
%doc AUTHORS README

%changelog
* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0
- changed %%Url

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.0-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Sat May 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt0.5
- 0.3.0

* Fri Dec 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5b
- new version.

* Sun Apr 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt0.5
- First build for Sisyphus.
