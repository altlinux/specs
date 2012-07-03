Name: pulseaudio
Version: 2.0
Release: alt2

Summary: PulseAudio is a networked sound server
Group: System/Servers
License: LGPL
Url: http://pulseaudio.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: doxygen intltool jackit-devel libalsa-devel libasyncns-devel
BuildRequires: libatomic_ops-devel-static libavahi-devel libbluez-devel
BuildRequires: libcap-devel libdbus-devel libgdbm-devel libudev-devel
BuildRequires: liblirc-devel libltdl7-devel libsamplerate-devel
BuildRequires: libsndfile-devel libspeex-devel libssl-devel libwrap-devel
BuildRequires: libSM-devel libX11-devel libXtst-devel libxcbutil-devel
BuildRequires: libjson-devel libgtk+2-devel libGConf-devel
BuildRequires: libfftw3-devel liborc-devel orc xmltoman

Requires: %name-utils = %version-%release
Requires: %name-daemon = %version-%release
Requires: %name-gconf = %version-%release

Provides: polypaudio = %version
Obsoletes: polypaudio < %version

%description
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

A sound server can serve many functions:

* Software mixing of multiple audio streams, bypassing any restrictions the
hardware has.

* Network transparency, allowing an application to play back or record audio
on a different machine than the one it is running on.

* Sound API abstraction, alleviating the need for multiple backends in
applications to handle the wide diversity of sound systems out there.

* Generic hardware abstraction, giving the possibility of doing things like
individual volumes per application.

Features:

* Library licensed under LGPL and server daemon under GPL
* Extensible plugin architecture (by loading dynamic loadable modules with dlopen())
* Support for static linking of modules, allowing a single binary for all your needs
* Module autoloading
* Support for more than one sink/source
* Good low latency behaviour
* Very accurate latency measurement for playback and recording.
* Client side latency interpolation
* Embedabble into other software (the core is available as C library)
* Completely asynchronous C API, complemented by two synchronous variants for
  simple use in synchronous applications
* Simple command line interface for reconfiguring the daemon while running
* Flexible, implicit sample type conversion and resampling
* "Zero-Copy" architecture
* May be used to combine multiple sound cards to one (with sample rate adjustment)
* Ability to fully synchronize multiple playback streams 

This virtual package contains pulseaudio daemon and utilities.

%package utils
Summary: PulseAudio client side utilities
Group: Sound
Requires: lib%name = %version-%release
Conflicts: %name-daemon < 0.9.16-alt0.2

%package qpaeq
Summary: PulseAudio equalizer interface
Group: Sound
Requires: lib%name = %version-%release

%package daemon
Summary: PulseAudio daemon
Group: Sound
PreReq: shadow-utils
Requires: lib%name = %version-%release
Requires: udev-extras >= 0.20090516-alt2
Conflicts: %name-utils < 0.9.16-alt0.2

Provides: esound
Obsoletes: esound
Conflicts: esd

%package system
Summary: Pulseaudio system daemon
Group: Sound
Requires: pulseaudio-daemon = %version-%release

%package bluez
Summary: PulseAudio -- bluetooth-related part
Group: Sound
Requires: %name-daemon = %version-%release

%package gconf
Summary: PulseAudio -- gnome-related part
Group: Sound
Requires: %name-daemon = %version-%release

%package jack
Summary: PulseAudio -- JACK part
Group: Sound
Requires: %name-daemon = %version-%release

%package -n lib%name
Summary: PulseAudio shared libraries
Group: System/Libraries
Provides: libpolypaudio = %version
Obsoletes: libpolypaudio < %version

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: libpolypaudio-devel = %version
Obsoletes: libpolypaudio-devel < %version

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
Provides: libpolypaudio-devel-doc = %version
Obsoletes: libpolypaudio-devel-doc < %version
BuildArch: noarch

%description daemon
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains PulseAudio daemon.

%description system
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains things needed to run PulseAudio system-wide.
See http://www.pulseaudio.org/wiki/SystemWideInstance
and especially http://www.pulseaudio.org/wiki/WhatIsWrongWithSystemMode

%description utils
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains PulseAudio client-side utilities.

%description qpaeq
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains PulseAudio equalizer interface.

%description bluez
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains bluetooth-related part of PulseAudio.

%description gconf
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains gnome-related part of PulseAudio.

%description jack
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains JACK modules of PulseAudio.

%description -n lib%name
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains the pulseaudio shared libraries.

%description -n lib%name-devel
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains development files for pulseaudio.

%description -n lib%name-devel-doc
PulseAudio is a networked sound server, similar in theory to the Enlightened
Sound Daemon (EsounD). PulseAudio is however much more advanced and has
numerous features.

This package contains doxygen documentation for pulseaudio.

%prep
%setup
touch config.rpath

%build
%autoreconf
%configure \
    --localstatedir=/var \
    --with-access-group=audio \
    --enable-per-user-esound-socket \
    --disable-static \
    #

%make_build all doxygen

%install
%make_install DESTDIR=%buildroot install
install -pm0644 -D pulseaudio.sysconfig %buildroot%_sysconfdir/sysconfig/pulseaudio
install -pm0755 -D pulseaudio.init %buildroot%_initdir/pulseaudio
ln -s esdcompat %buildroot%_bindir/esd
mkdir -p %buildroot%_localstatedir/pulse %buildroot%_runtimedir/pulse

find %buildroot%_libdir -name \*.la -delete

%find_lang %name

%define pulselibdir %_libdir/pulse-2.0
%define pulsemoduledir %pulselibdir/modules

%pre system
%_sbindir/groupadd -r -f pulse &> /dev/null
%_sbindir/useradd -r -g pulse -G audio -d %_runtimedir/pulse -s /dev/null \
	-c "Pulseaudio daemon" -M -n pulse &>/dev/null ||:

%files

%files daemon
%_sysconfdir/xdg/autostart/pulseaudio.desktop
%_sysconfdir/xdg/autostart/pulseaudio-kde.desktop

%dir %_sysconfdir/pulse
%config(noreplace) %_sysconfdir/pulse/daemon.conf
%config(noreplace) %_sysconfdir/pulse/default.pa

/lib/udev/rules.d/90-pulseaudio.rules

%_bindir/start-pulseaudio-kde
%_bindir/start-pulseaudio-x11
%_bindir/pulseaudio
%_bindir/esdcompat
%_bindir/esd
%_bindir/pactl

%_datadir/pulseaudio

%_libdir/libpulsecore-2.0.so

%dir %pulselibdir
%dir %pulsemoduledir

%pulsemoduledir/*.so

%exclude %pulsemoduledir/libbluetooth-ipc.so
%exclude %pulsemoduledir/libbluetooth-sbc.so
%exclude %pulsemoduledir/libbluetooth-util.so
%exclude %pulsemoduledir/module-bluetooth-device.so
%exclude %pulsemoduledir/module-bluetooth-discover.so
%exclude %pulsemoduledir/module-bluetooth-proximity.so

%exclude %pulsemoduledir/module-gconf.so

%exclude %pulsemoduledir/module-jack-sink.so
%exclude %pulsemoduledir/module-jack-source.so

%_man1dir/pactl.1*
%_man1dir/esdcompat.1*
%_man1dir/pulseaudio.1*
%_man1dir/start-pulseaudio-kde.1*
%_man1dir/start-pulseaudio-x11.1*
%_man5dir/default.pa.5*
%_man5dir/pulse-cli-syntax.5*
%_man5dir/pulse-daemon.conf.5*

%files system
%_initdir/pulseaudio

%config(noreplace) %_sysconfdir/sysconfig/pulseaudio
%config(noreplace) %_sysconfdir/dbus-1/system.d/pulseaudio-system.conf
%config(noreplace) %_sysconfdir/pulse/system.pa

%attr(0770,root,pulse) %dir %_localstatedir/pulse
%attr(0771,root,pulse) %dir %_runtimedir/pulse

%files utils
%_bindir/pacat
%_bindir/pacmd
%_bindir/padsp
%_bindir/pamon
%_bindir/paplay
%_bindir/parec
%_bindir/parecord
%_bindir/pasuspender
%_bindir/pax11publish

%_libdir/pulseaudio/libpulsedsp.so

%_man1dir/pacat.1*
%_man1dir/pacmd.1*
%_man1dir/padsp.1*
%_man1dir/paplay.1*
%_man1dir/pasuspender.1*
%_man1dir/pax11publish.1*

%files qpaeq
%_bindir/qpaeq

%files bluez
%dir %pulselibdir
%dir %pulsemoduledir
%_libexecdir/pulse/proximity-helper
%pulsemoduledir/libbluetooth-ipc.so
%pulsemoduledir/libbluetooth-sbc.so
%pulsemoduledir/libbluetooth-util.so
%pulsemoduledir/module-bluetooth-device.so
%pulsemoduledir/module-bluetooth-discover.so
%pulsemoduledir/module-bluetooth-proximity.so

%files gconf
%dir %pulselibdir
%dir %pulsemoduledir
%_libexecdir/pulse/gconf-helper
%pulsemoduledir/module-gconf.so

%files jack
%dir %pulselibdir
%dir %pulsemoduledir
%pulsemoduledir/module-jack-sink.so
%pulsemoduledir/module-jack-source.so

%files -n lib%name -f %name.lang
%doc LICENSE README todo

%dir %_sysconfdir/pulse
%config(noreplace) %_sysconfdir/pulse/client.conf

%_libdir/libpulse.so.*
%_libdir/libpulse-simple.so.*
%_libdir/libpulse-mainloop-glib.so.*

%dir %_libdir/pulseaudio
%_libdir/pulseaudio/libpulsecommon-2.0.so
%_man5dir/pulse-client.conf.5*

%files -n lib%name-devel
%_libdir/lib*.so
%_libdir/cmake/PulseAudio
%_includedir/pulse
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*
%exclude %_libdir/libpulsecore-2.0.so

%files -n lib%name-devel-doc
%doc doxygen/html

%changelog
* Thu Jun 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt2
- fixed build after libudev soname bump

* Sat May 12 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0 released

* Tue Feb 07 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt2
-  system-wide daemon mode fixed (closes: 26902)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt1
- 1.1 released

* Tue Sep 27 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- 1.0 released

* Thu Sep 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.99.4-alt1
- 0.99.4 released

* Mon Aug 29 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.99.3-alt1
- 0.99.3 released

* Tue Aug 16 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.99.2-alt1
- 0.99.2 released

* Wed Aug 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.99.1-alt2
- fix crash in path subset elimination

* Fri Aug 05 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.99.1-alt1
- 0.99.1 released

* Fri Jun 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.23-alt1
- 0.9.23 released

* Mon Apr 04 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.22-alt3
- updated to stable-queue git.93e7a19e

* Thu Mar 03 2011 Alexey Tourbin <at@altlinux.ru> 0.9.22-alt2
- rebuilt for debuginfo
- reverted to upstream symbol versioning
- made lib%name-devel-doc noarch

* Fri Nov 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.22-alt1
- 0.9.22 released

* Wed Oct 27 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.21-alt5
- updated to stable-queue git.a8d76e9

* Sat Oct 02 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.21-alt4
- updated to stable-queue git.a21b8328
- be more specific in desktop files (#24058)

* Wed Aug 25 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.21-alt3
- updated to stable-queue git.93750199

* Sat Dec 12 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.21-alt2
- 0.9.21 released

* Sat Nov 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.20-alt1
- 0.9.20 released

* Sun Nov  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.19-alt2
- system-wide stuff packaged separately

* Wed Sep 30 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.19-alt1
- 0.9.19 released

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.18-alt1
- 0.9.18 released

* Mon Sep 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.17-alt2
- 0.9.17 released

* Thu Sep 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.16-alt1
- 0.9.16 released

* Thu Sep  3 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.16-alt0.7
- 0.9.16-test7

* Mon Apr 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.15-alt2
- fixed build with recent libtool package

* Sun Apr 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.15-alt1
- 0.9.15 released

* Tue Mar 24 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.14-alt1
- 0.9.14 released

* Fri Mar 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt4
- align conflicts/obsoletes with esound maintainer's idea (#17998)

* Fri Dec 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt3
- use HAL by default (#17684)

* Fri Nov 21 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt2
- introduced esound compatibility mode via /usr/bin/esdcompat

* Mon Oct  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt1
- 0.9.13 released
- enabled per-user esound sockets

* Sat Jul 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt1
- 0.9.11 released
- redundant req on daemon in devel subpackage suppressed (#16713)

* Mon Mar 31 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.10-alt1
- 0.9.10 released

* Thu Jan 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 released

* Wed Dec 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt3
- fixed build with automake >= 1.10

* Mon Aug 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt2
- jack sink modified to be realtime-aware (svn rev.1680)

* Sat Jul  7 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt1
- 0.9.6 released
- system-wide service added, off by default

* Tue May 29 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.5-alt7
- CVE-2007-1804 fixed, really. thanx to icesik@ for barfing
- use alsa defaults instead of relying on hal

* Thu May 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.5-alt6
- CVE-2007-1804 fixed, (#11335)
- control facility added

* Sat Jan 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.5-alt5
- subpackages rearranged: daemon, utils & gconf subpackages
  appeared instead of all-in-one pulseaudio (#10218)

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt4
- rebuild with new dbus

* Tue Oct 31 2006 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt3
- mv /etc/pulse/client.conf from pulseaudio to libpulseaudio (#10219)

* Tue Oct 10 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.5-alt2
- add Obsoletes
  + polypaudio to pulseaudio subpackage
  + libpolypaudio to libpulseaudio subpackage
  + libpolypaudio-devel to libpulseaudio-devel subpackage
  + libpolypaudio-devel-doc to libpulseaudio-devel-doc subpackage
- add Provides
  + polypaudio = %%version to pulseaudio subpackage
  + libpolypaudio = %%version to libpulseaudio subpackage
  + libpolypaudio-devel = %%version to libpulseaudio-devel subpackage
  + libpolypaudio-devel-doc = %%version to libpulseaudio-devel-doc subpackage

* Fri Sep 01 2006 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- 0.9.3 -> 0.9.5
- buildreq

* Fri Jul 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.3-alt1
- 0.9.3
- rename polypaudio to pulseaudio (without obsoletes, will be added later)
- buildreq

* Sun Jun 25 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.1-alt1
- 0.9.1
- patch2 removed (merged in upstream)
- no API or ABI changes were made
- exclude %%_libdir/polypaudio-0.9/modules/*.la

* Mon May 29 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.0-alt1
- 0.9.0
- build with libhowl
- buildreq

* Fri Apr 28 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.1-alt1
- 0.8.1
- patch1 removed (merged in upstream)
- buildreq
- build with libasyncns

* Wed Apr 26 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt3
- move back .la files

* Sat Apr 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt2
- fix unresolved symbols (patch1)

* Fri Apr 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt1
- 0.8
- #9358
- buildreq

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.7-alt2.1
- Rebuilt for new pkg-config dependencies.

* Fri Dec 16 2005 Igor Zubkov <icesik@altlinux.ru> 0.7-alt2
- fix provides/requires

* Tue Nov 15 2005 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
