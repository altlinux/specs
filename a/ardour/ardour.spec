%set_verify_elf_method unresolved=relaxed

%define name2 ardour3

Name:    ardour
Version: 3.2
Release: alt2.1

Summary: Professional multi-track audio recording application
License: GPLv2+
Group:   Sound
Url:     http://ardour.org

Packager: Alex Karpov <karpov@altlinux.ru>

Source:  %name-%version.tar
Source1: ardour3.desktop
Source2: ardour3-3.2-ru.po

BuildRequires: boost-devel
BuildRequires: cppunit-devel >= 1.12.0
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libalsa-devel
BuildRequires: libaubio-devel >= 0.3.2
BuildRequires: libcurl-devel >= 7.0.0
BuildRequires: libcwiid-devel
BuildRequires: libfftw3-devel
BuildRequires: libflac-devel >= 1.2.1
BuildRequires: libgnomecanvasmm-devel
BuildRequires: libgtk+2-devel
BuildRequires: libjack-devel
BuildRequires: liblilv-devel >= 0.14
BuildRequires: liblo-devel >= 0.26
BuildRequires: liblrdf-devel >= 0.4.0
# FIXME BuildRequires: libltc-devel >= 1.1.0
BuildRequires: libogg-devel >= 1.1.2
BuildRequires: libredland-devel
BuildRequires: librubberband-devel
BuildRequires: libsamplerate-devel
BuildRequires: libserd-devel >= 0.14.0
BuildRequires: libsndfile-devel >= 1.0.18
BuildRequires: libsord-devel >= 0.8.0
BuildRequires: libsratom-devel >= 0.4.0
BuildRequires: libsuil-devel >= 0.6.0
BuildRequires: libsqlite3-devel
BuildRequires: libuuid-devel
BuildRequires: libusb-devel
BuildRequires: libvamp-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: lv2-devel >= 1.0.15
BuildRequires: /proc
BuildRequires: python-devel
BuildRequires: raptor2-devel

# FIXME
#Requires:      jackit
#Requires:      gtk-engines2
# For video import
#Requires:      harvid
#Requires:      xjadeo

Requires:       jack-audio-connection-kit

%description
Ardour is a digital audio workstation. You can use it to record, edit
and mix multi-track audio. You can produce your own CDs, mix video sound
tracks, or just experiment with new ideas about music and sound.

Ardour capabilities include: multi channel recording, non-destructive
editing with unlimited undo/redo, full automation support, a powerful
mixer, unlimited tracks/busses/plugins, time-code synchronization, and
hardware control from surfaces like the Mackie Control Universal.

You must have jackd running and an ALSA sound driver to use Ardour.
If you are new to jackd, try qjackctl.

See the online user manual at http://en.flossmanuals.net/ardour/index/

%prep
%setup -q
cp %SOURCE2 gtk2_ardour/po/ru.po

# Generate revision number
echo '#include "ardour/revision.h"' > libs/ardour/revision.cc
echo 'namespace ARDOUR { const char* revision = "%version"; }' >> libs/ardour/revision.cc

%build
./waf configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --configdir=%_sysconfdir \
    --program-name=Ardour \
    --nls \
    --docs

./waf build \
    --nls \
    --docs

./waf i18n_mo

%install
./waf install --destdir=%buildroot

install -d -m 0755 %buildroot%_desktopdir
install -m 644 %SOURCE1 %buildroot%_desktopdir/

install -d -m 0755 %buildroot%_iconsdir
cp -f %buildroot%_datadir/%name2/icons/application-x-ardour_48px.png %buildroot%_iconsdir/ardour3.png

%add_findprov_lib_path %_libdir/%name2
%find_lang --output=%name.lang %name2 gtk2_ardour3 gtkmm2ext3

%files -f %name.lang
%doc README
%_bindir/*
%dir %_datadir/%name2
%_libdir/%name2/*.so
%_libdir/%name2/sanityCheck
%_libdir/%name2/ardour-%{version}
%_libdir/%name2/*.so.*
%_libdir/%name2/panners/*.so
%_libdir/%name2/panners/*.so.*
%_libdir/%name2/surfaces/*.so
%_libdir/%name2/surfaces/*.so.*
%_libdir/%name2/engines/*.so
%_libdir/%name2/vamp/*.so
%_libdir/%name2/vamp/*.so.*
%_datadir/%name2
%_desktopdir/*.desktop
%dir %_sysconfdir/%name2
%config(noreplace) %_sysconfdir/%name2/%{name2}_ui_default.conf
%config(noreplace) %_sysconfdir/%name2/%{name2}_ui_light.rc
%config(noreplace) %_sysconfdir/%name2/%{name2}_ui_dark.rc
%config(noreplace) %_sysconfdir/%name2/ardour.menus
%config(noreplace) %_sysconfdir/%name2/ardour_system.rc
%config(noreplace) %_sysconfdir/%name2/step_editing.bindings
%config(noreplace) %_sysconfdir/%name2/mnemonic-us.bindings
%config(noreplace) %_sysconfdir/%name2/mixer.bindings
%dir %_sysconfdir/%name2/export
%config(noreplace) %_sysconfdir/%name2/export/CD.format
%_iconsdir/ardour3.png

%changelog
* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 3.2-alt2
- Beautify desktop file
- Add Jack server connector to requires

* Wed Jun 19 2013 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version 3.2 (ALT #29087)

* Thu Oct 18 2012 Alex Karpov <karpov@altlinux.ru> 2.8.14-alt1.1
- build fixed

* Sun Sep 02 2012 Alex Karpov <karpov@altlinux.ru> 2.8.14-alt1
- new version

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

