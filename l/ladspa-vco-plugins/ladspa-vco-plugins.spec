%define _name vco
%define beta %nil

Name: ladspa-%_name-plugins
Version: 0.3.0
Release: alt0.5%beta.1

Summary: The oscillators LADSPA plugins
License: GPL
Group: Sound
Url: http://alsamodular.sourceforge.net/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %url/VCO-plugins-%version%beta.tar.bz2

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Sat May 08 2004
BuildRequires: gcc-c++ ladspa_sdk libstdc++-devel

%description
This package provides oscillator LADSPA plugins  based on the same
principle of using a precomputed interpolated dirac pulse.

%prep
%setup -q -n VCO-plugins-%version%beta

# use system ladspa.h
%__rm -f ladspa.h
%__subst 's, ladspa\.h,,' Makefile
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
* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.0-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Sat May 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt0.5
- 0.3.0

* Fri Dec 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- First build for Sisyphus.
