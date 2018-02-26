%define _name moogvcf

Name: ladspa-%_name-plugins
Version: 1.1
Release: alt1

Summary: The Moog VCF LADSPA plugin
License: GPL
Group: Sound
Url: http://alsamodular.sourceforge.net/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: %url/%_name-%version.tar.bz2
Patch: moogvcf-1.1-fix-makefile.patch

%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Sun Apr 27 2003
BuildRequires: gcc-c++ ladspa_sdk libstdc++-devel

%description
This LADSPA plugin contains three versions of a digital implementation of
the voltage controlled lowpass filter as used in vintage Moog synthesizers.
Many software versions of this filter already exist. Most use some limiting
mechanism in order to keep the self-oscillation amplitude under control, but
as far as I know, none of them attempt to accurately emulate the non-linear
circuit elements of the original analog filter. To do this has been the 
main reason for developing this plugin.

%prep
%setup -n %_name
%patch0 -p1
# use system ladspa.h
%__rm -f ladspa.h
find . -type f -print0|xargs -r0 %__subst 's,"ladspa.h",<ladspa.h>,' --

%build
CXXFLAGS="%optflags"; export CXXFLAGS
%make_build

%install
%__install -pD %_name.so %buildroot%_ladspa_path/%_name.so

%files
%_ladspa_path/*.so
%doc AUTHORS README ams/

%changelog
* Sun Feb 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.1-alt1
- Fix build on modern Sisyphus

* Sun Apr 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt0.5
- First build for Sisyphus.
