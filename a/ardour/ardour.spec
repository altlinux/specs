%define beta beta11
%define subbeta .1
%define name2 ardour2

Name: ardour
Version: 2.8.12
Release: alt1

Summary: Ardour is a multichannel hard disk recorder and digital audio workstation
License: GPL
Group: Sound
Url: http://ardour.org

Packager: Alex Karpov <karpov@altlinux.ru>

Source: http://releases.ardour.org/%name-%version.tar.bz2

Patch0: %name-2.7.1-alt.patch
Patch1: %name-2.0rc1-x86_64-alt.patch

#BuildPreReq: tetex-dvips
#BuildPreReq: jackit-devel >= 0.116.1
#BuildRequires: boost-devel cvs flex gcc-c++ ghostscript-utils jackit-devel ladspa_sdk
#BuildRequires: libalsa-devel libaubio-devel libfftw3-devel libflac-devel
#BuildRequires: libgnomecanvasmm-devel liblo-devel liblrdf-devel libsamplerate-devel
#BuildRequires: libsoundtouch-devel libusb-devel libxslt-devel rcs scons swig tetex-latex

# Automatically added by buildreq on Wed Oct 14 2009
BuildRequires: boost-devel cvs flex gcc-c++ ghostscript-utils jackit-devel libalsa-devel libaubio-devel libfftw3-devel libgnomecanvasmm-devel liblo-devel liblrdf-devel libsamplerate-devel libsndfile-devel libxslt-devel rcs scons swig texlive-latex-base libsoundtouch-devel

%description
Ardour is a multichannel hard disk recorder (HDR) and digital audio 
workstation (DAW). It is capable of simultaneous recording of 24 or more
channels of 32 bit audio at 48kHz. Ardour is intended to function as a
"professional" HDR system, replacing dedicated hardware solutions such
as the Mackie HDR and provide the same or better functionality as 
proprietary software DAWs such as ProTools, Samplitude, Logic Audio,
Nuendo and Cubase VST/SX.

%prep
%setup -qn %name-%version
%patch0
%patch1
sed -i s,@libdir@,%_libdir, SConstruct

%build
scons PREFIX=/usr DIST_TARGET=none SYSLIBS=yes \
%ifarch x86_64
DIST_TARGET=x86_64
%endif

%install
mkdir %buildroot
scons DESTDIR=%buildroot install \
%ifarch x86_64
DIST_TARGET=x86_64
%endif

%add_findprov_lib_path %_libdir/%name2
%find_lang --output=%name.lang lib%name2 libgtkmm2ext gtk2_ardour

%files -f %name.lang
%_sysconfdir/%name2/
%_bindir/*
%_libdir/%name2/
%_datadir/%name2/

%ifnarch %ix86 x86_64
%set_verify_elf_method textrel=relaxed
%endif

%changelog
* Wed Oct 12 2011 Alex Karpov <karpov@altlinux.ru> 2.8.12-alt1
- new version

* Thu Feb 10 2011 Alex Karpov <karpov@altlinux.ru> 2.8.11-alt1.1
- path bug fixed (to close #24324)
    + minor spec cleanup
    + patch 2 dropped out

* Fri Jul 09 2010 Alex Karpov <karpov@altlinux.ru> 2.8.11-alt1
- new version

* Fri Jun 18 2010 Alex Karpov <karpov@altlinux.ru> 2.8.10-alt1
- new version

* Tue Mar 30 2010 Alex Karpov <karpov@altlinux.ru> 2.8.7-alt1
- new version

* Fri Mar 19 2010 Alex Karpov <karpov@altlinux.ru> 2.8.6-alt1
- new version

* Mon Nov 23 2009 Alex Karpov <karpov@altlinux.ru> 2.8.4-alt1
- new version

* Wed Oct 14 2009 Alex Karpov <karpov@altlinux.ru> 2.8.3-alt1
- new version
    + updated build requirements
    
* Mon Sep 14 2009 Alex Karpov <karpov@altlinux.ru> 2.8.2-alt1
- new version
    + updated russian translation from upstream bugzilla 
	(by Alexandre Prokoudine)

* Wed Jun 03 2009 Alex Karpov <karpov@altlinux.ru> 2.8-alt1.1
- fixed build with new gcc

* Mon Apr 20 2009 Alex Karpov <karpov@altlinux.ru> 2.8-alt1
- new version

* Wed Feb 25 2009 Alex Karpov <karpov@altlinux.ru> 2.7.1-alt1.1
- added verification crutch for PowerPC build

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- new version
- droped upstreamed patch for flac support
- updated buildreqs

* Fri May 30 2008 Alex Karpov <karpov@altlinux.ru> 2.4.1-alt1
- new version

* Wed Mar 19 2008 Alex Karpov <karpov@altlinux.ru> 2.3.1-alt1.2
- more build requirements

* Wed Mar 19 2008 Alex Karpov <karpov@altlinux.ru> 2.3.1-alt1.1
- updated build requirements

* Thu Mar 06 2008 Alex Karpov <karpov@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Jan 22 2008 Alex Karpov <karpov@altlinux.ru> 2.2-alt1
- 2.2

* Mon Oct 01 2007 Alex Karpov <karpov@altlinux.ru> 2.1-alt1
- 2.1 

* Mon Aug 27 2007 Alex Karpov <karpov@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Wed Jul 11 2007 Alex Karpov <karpov@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Thu May 10 2007 Alex Karpov <karpov@altlinux.ru> 2.0.2-alt1
- 2.0.2 upstream bugfix release

* Fri May 04 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt7
- a wrong release number fix

* Thu May 03 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt1
- 2.0 upstream release

* Tue Feb 20 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt6beta11.1
- patch for flac-1.1.3 support by Led <led@> (#10876 fixed)

* Mon Feb 12 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt5beta11.1
- spec update and patch for x86_64 by Damir Shayhutdinov <damir@>

* Fri Feb 09 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt4beta11.1
- arrgh.. who change name of clearlooks's rpm? fixed

* Fri Feb 09 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt3beta11.1
- fixed unmets for x86_64

* Thu Feb 08 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt2beta11.1
- fixed build for x86_64

* Tue Jan 23 2007 Alex Karpov <karpov@altlinux.ru> 2.0-alt1beta11.1
- picked from orphaned

