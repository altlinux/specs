Name: ardour
Version: 7.1
Release: alt1

Summary: Professional multi-track audio recording application
License: GPLv2+
Group:   Sound
Url:     http://ardour.org/

Source:  %name-%version-%release.tar

BuildRequires: gcc-c++ itstool python3-base boost-devel libqm-dsp-devel readline-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(aubio)
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: pkgconfig(hidapi-hidraw)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(ltc)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(pangomm-1.4)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sord-0)
BuildRequires: pkgconfig(soundtouch)
BuildRequires: pkgconfig(sratom-0)
BuildRequires: pkgconfig(suil-0)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(vamp-sdk)

%description
Ardour is a digital audio workstation. You can use it to record, edit
and mix multi-track audio. You can produce your own CDs, mix video sound
tracks, or just experiment with new ideas about music and sound.

Ardour capabilities include: multi channel recording, non-destructive
editing with unlimited undo/redo, full automation support, a powerful
mixer, unlimited tracks/busses/plugins, time-code synchronization, and
hardware control from surfaces like the Mackie Control Universal.

See the online user manual at https://manual.ardour.org/toc/

%prep
%setup
# Generate revision number
echo '#include "ardour/revision.h"' > libs/ardour/revision.cc
echo 'namespace ARDOUR { const char* revision = "%version"; const char* date = "'$(date --rfc-3339=date)'"; }' >> libs/ardour/revision.cc

egrep -rl '^#!/usr/bin/env python'|xargs sed -ri '/env python$/ s,$,3,'

%ifarch %e2k
# wscript set CXXFLAGS_OSX without checking sys.platform
# GCC silently ignores -Fxxx options, but LCC responds with an error
sed -i "/conf.env.append_value('CXXFLAGS_OSX', '-F/s|conf.env|pass # conf.env|" wscript
%endif

%build
LC_ALL=C.utf8 ./waf configure \
	--prefix=%_prefix \
	--bindir=%_bindir \
	--configdir=%_sysconfdir \
	--datadir=%_datadir \
	--includedir=%_includedir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--optimize \
	--arch="%optflags" \
%ifarch armh
    --dist-target=armhf \
%endif
%ifarch aarch64
    --dist-target=aarch64 \
%endif
%ifarch i586
    --dist-target=i686 \
%endif
	--no-phone-home \
	--freedesktop \
	--use-external-libs \
%ifarch %e2k
    --cxx11 \
    --keepflags \
%endif
	#

./waf build i18n -j%([ %__nprocs -gt 32 ] && echo 32 || echo %__nprocs)

%install
./waf --destdir=%buildroot install
install -pm0644 -D ardour.1 %buildroot%_man1dir/ardour.1
install -pm0644 -D gtk2_ardour/resources/Ardour-icon_16px.png %buildroot%_miconsdir/ardour7.png
install -pm0644 -D gtk2_ardour/resources/Ardour-icon_32px.png %buildroot%_niconsdir/ardour7.png
install -pm0644 -D gtk2_ardour/resources/Ardour-icon_48px.png %buildroot%_liconsdir/ardour7.png
find %buildroot%_bindir -type l |while read l; do
	ln -srvf %buildroot/$(readlink $l) $l
done
%find_lang --output ardour.lang --append ardour7 gtk2_ardour7 gtkmm2ext3

%files -f ardour.lang
%dir %_sysconfdir/ardour7
%config(noreplace) %_sysconfdir/ardour7/*
%_bindir/ardour7*
%_libdir/lib*.so.*
%_libdir/ardour7
%_datadir/ardour7
%_datadir/appdata/ardour7.appdata.xml
%_datadir/mime/packages/ardour.xml
%_desktopdir/ardour7.desktop
%_iconsdir/*/*/*/*.png
%_man1dir/ardour.1*

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.1-alt1
- 7.1 released

* Wed Nov 02 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.0-alt2
- added workaround for broken gtk2 themes (closes: 44184)

* Mon Oct 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.0-alt1
- 7.0 released

* Fri Apr 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.9-alt3
- fix FTBFS by relocating shared libraries to %%_libdir

* Wed Jan 12 2022 Grigory Ustinov <grenka@altlinux.org> 6.9-alt2
- Remove jack-audio-connection-kit from Requires (Closes: #41496).

* Tue Sep 14 2021 Grigory Ustinov <grenka@altlinux.org> 6.9-alt1
- Build new version.

* Mon Jul 05 2021 Grigory Ustinov <grenka@altlinux.org> 6.8-alt2
- Build new version.

* Mon Jun 21 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.7-alt2
- fixed a bug in the build script that appears on Elbrus
- enabled multithreaded build

* Fri May 28 2021 Grigory Ustinov <grenka@altlinux.org> 6.7-alt1
- Build new version.
- Switch to building from git.

* Wed Feb 24 2021 Grigory Ustinov <grenka@altlinux.org> 6.6-alt1
- Build new version (thx to cas@).

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 6.5-alt1
- Build new version.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 6.3-alt1
- Build new version.

* Mon Jul 13 2020 Grigory Ustinov <grenka@altlinux.org> 6.2-alt1
- Build new version (for ppc64le too).
- Fix desktop file (Closes: #38420).

* Thu May 28 2020 Grigory Ustinov <grenka@altlinux.org> 6.0-alt1
- Build new version.

* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 5.12-alt3
- ExcludeArch: ppc64le for now (undefined symbols)

* Sun Sep 01 2019 Michael Shigorin <mike@altlinux.org> 5.12-alt2
- E2K: fix stupid waf build

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 5.12-alt1.1
- NMU: rebuild with libaubio5

* Mon Sep 17 2018 Grigory Ustinov <grenka@altlinux.org> 5.12-alt1
- Build new version.

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

