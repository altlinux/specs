%define _name rev
%define beta %nil

Name: ladspa-%_name-plugins
Version: 0.3.1
Release: alt1%beta

Summary: The reverberation LADSPA plugin
License: GPL
Group: Sound
Url: http://alsamodular.sourceforge.net/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %url/REV-plugins-%version%beta.tar.bz2

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Fri Dec 19 2003
BuildRequires: gcc-c++ ladspa_sdk libstdc++-devel

%description
This reverb is based on gverb by Juhana Sadeharju, but the code
(now C++) is entirely original. A second input was added for stereo
operation, and some code to prevent FP denormalisation.
This is a preliminary release, and this plugin will probably change
a lot in future versions.

%prep
%setup -q -n REV-plugins-%version%beta

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
* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- new version

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.1-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Fri Dec 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- First build for Sisyphus.
