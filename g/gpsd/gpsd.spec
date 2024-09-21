%define _unpackaged_files_terminate_build 1

%def_with libQgpsmm
%define abiversion 30

Name: gpsd
Summary: Service daemon for mediating access to a GPS
Version: 3.25
Release: alt1
License: BSD-2-Clause
Group: System/Servers
Url: https://gpsd.gitlab.io/gpsd/index.html
VCS: https://gitlab.com/gpsd/gpsd
Source: %name-%version.tar

# Add old status names to gps.h for compatibility
Patch0: gpsd-3.25-fedora-apistatus.patch
Requires: libgps%abiversion = %EVR
BuildRequires: asciidoc docbook-dtds docbook-style-xsl asciidoctor gem-rouge

BuildRequires: scons gcc-c++ libXaw-devel libXext-devel libXpm-devel libdbus-glib-devel xorg-cf-files xsltproc libgtk+3-devel pps-tools-devel
BuildRequires: python3-dev python3-module-pycairo python3-module-pygobject3 python3-module-serial python3-module-matplotlib
BuildRequires: python3-module-setuptools
%add_findreq_skiplist */gpsdebuginfo

%if_with libQgpsmm
BuildRequires: qt5-base-devel
%endif

BuildRequires: libbluez-devel
BuildRequires: libusb-devel

%set_verify_elf_method unresolved=relaxed

%description
gpsd is a service daemon that mediates access to a GPS sensor
connected to the host computer by serial or USB interface, making its
data on the location/course/velocity of the sensor available to be
queried on TCP port 2947 of the host computer.  With gpsd, multiple
GPS client applications (such as navigational and wardriving software)
can share access to a GPS without contention or loss of data.  Also,
gpsd responds to queries with a format that is substantially easier to
parse than NMEA 0183.  A client library is provided for applications.

After installing this RPM, gpsd will automatically connect to USB
GPSes when they are plugged in and requires no configuration.  For
serial GPSes, you will need to start gpsd by hand.  Once connected,
the daemon automatically discovers the correct baudrate, stop bits,
and protocol. The daemon will be quiescent when there are no
clients asking for location information, and copes gracefully when the
GPS is unplugged and replugged.

%package -n libgps%abiversion
Summary: Client libraries in C and Python for talking to a running gpsd or GPS
Group: Sciences/Geosciences
%description -n libgps%abiversion
Client libraries in C and Python for talking to a running gpsd or GPS

%if_with libQgpsmm
%package -n libQgpsmm%abiversion
Summary: Qt bindings for gpsd
Group: Sciences/Geosciences
%description -n libQgpsmm%abiversion
This package contains Qt bindings for gpsd
%endif

%package -n libgps-devel
Summary: Development files for libgps
Group: Development/C
Requires: libgps%abiversion = %EVR
%if_with libQgpsmm
Requires: libQgpsmm%abiversion = %EVR
%endif

%description -n libgps-devel
Development files for libgps

%package -n gpsd-clients-console
Summary: Console clients for gpsd
Group: Sciences/Geosciences
Requires: libgps%abiversion = %EVR
Requires: python3-module-gps = %EVR
Conflicts: gpsd-clients < %EVR

%description -n gpsd-clients-console
Console clients pack for the gpsd

cgps resembles xgps, but without the pictorial satellite display.
It can run on a serial terminal or terminal emulator.

%package -n gpsd-clients-gui
Summary: Clients for gpsd with an X interface
Group: Sciences/Geosciences
Requires: libgps%abiversion = %EVR
Requires: python3-module-gps = %EVR
Conflicts: gpsd-clients < %EVR

%description -n gpsd-clients-gui
xgps is a simple sample client for gpsd with an X interface.
xgpsspeed is a speedometer that uses position information from gpsd.

%package -n gpsd-helpers
Summary: Helpers pack for the gpsd
Group: Sciences/Geosciences
Requires: libgps%abiversion = %EVR
Requires: python3-module-gps = %EVR
Conflicts: gpsd-clients < %EVR

%description -n gpsd-helpers
Helpers pack for the gpsd

%package -n python3-module-gps
Summary: Python bindings to libgps
Group: Development/Python

%description -n python3-module-gps
Python bindings to libgps

%prep
%setup
%patch0 -p1

%build
scons \
    prefix=/usr \
    systemd=yes \
    dbus_export=yes \
    libdir=%_libdir \
    docdir=%_defaultdocdir/%name-%version \
    icondir=%_iconsdir \
    python_libdir=%python3_sitelibdir \
    udevdir=$(dirname %{_udevrulesdir}) \
    unitdir=%{_unitdir} \
    target_python=%__python3 \
    python_shebang=%__python3 \
    %if_with libQgpsmm
	qt=yes \
	qt_versioned=5 \
    %else
	 qt=no \
    %endif
    debug=yes

%install
DESTDIR=%buildroot scons install udev-install

install -p -m 0755 gpsinit %buildroot/%_sbindir

mkdir -p %buildroot/%_desktopdir
install -p -m 0644 %name-%version/packaging/X11/xgps.desktop      %buildroot/%_desktopdir
install -p -m 0644 %name-%version/packaging/X11/xgpsspeed.desktop %buildroot/%_desktopdir

mkdir -p %buildroot/%_sysconfdir/sysconfig
install -p -m 0644 %name-%version/packaging/rpm/gpsd.sysconfig %buildroot/%_sysconfdir/sysconfig/gpsd

%files
%doc AUTHORS COPYING NEWS README.adoc INSTALL.adoc SUPPORT.adoc build.adoc www/example1.c.txt
%_sbindir/gpsd
%_man8dir/gpsd.*

%_sbindir/gpsdctl
%_man8dir/gpsdctl*

%_sbindir/gpsinit
%_man8dir/gpsinit*

%_bindir/ppscheck
%_man8dir/ppscheck*

%_unitdir/gpsd.service
%_unitdir/gpsd.socket
%_unitdir/gpsdctl@.service
%_udevrulesdir/*.rules
%config(noreplace) %attr(0644,root,root) %_sysconfdir/sysconfig/gpsd

%_man5dir/*

%_man1dir/gps.*

%_iconsdir/gpsd-logo.png
%_datadir/snmp

%files -n libgps%abiversion
%_libdir/libgps*.so.%abiversion
%_libdir/libgps*.so.%abiversion.*

%if_with libQgpsmm
%files -n libQgpsmm%abiversion
%_libdir/libQgps*.so.%abiversion
%_libdir/libQgps*.so.%abiversion.*
%endif

%files -n libgps-devel
%if_with libQgpsmm
%_libdir/libQgpsmm.so
%_libdir/libQgpsmm.prl
%endif
%_libdir/libgps*.so
%_pkgconfigdir/*.pc
%_includedir/*.h
%_man3dir/*

%files -n gpsd-clients-console
%_bindir/cgps
%_man1dir/cgps*

%_bindir/gegps
%_man1dir/gegps*

%_bindir/gpscsv
%_man1dir/gpscsv*

%_bindir/gpsdecode
%_man1dir/gpsdecode*

%_bindir/gpsmon
%_man1dir/gpsmon*

%_bindir/gpspipe
%_man1dir/gpspipe*

%_bindir/gpsplot
%_man1dir/gpsplot*

%_bindir/gpsprof
%_man1dir/gpsprof*

%_bindir/gpsrinex
%_man1dir/gpsrinex*

%_bindir/gpssubframe
%_man1dir/gpssubframe*

%_bindir/gpxlogger
%_man1dir/gpxlogger*

%_bindir/lcdgps
%_man1dir/lcdgps*

%_bindir/ubxtool
%_man1dir/ubxtool*

%_bindir/zerk
%_man1dir/zerk*

%files -n gpsd-clients-gui
%_bindir/xgps
%_desktopdir/xgps.desktop
%_man1dir/xgps*
%_bindir/xgpsspeed
%_desktopdir/xgpsspeed.desktop

%files -n gpsd-helpers
%_bindir/gps2udp
%_man1dir/gps2udp*

%_bindir/gpscat
%_man1dir/gpscat*

%_bindir/gpsctl
%_man1dir/gpsctl*

%_bindir/gpsdebuginfo
%_man1dir/gpsdebuginfo*

%_bindir/gpsfake
%_man1dir/gpsfake*

%_bindir/gpssnmp
%_man1dir/gpssnmp*

%_bindir/ntpshmmon
%_man1dir/ntpshmmon*

%files -n python3-module-gps
%python3_sitelibdir/gps/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Sep 21 2024 Anton Farygin <rider@altlinux.ru> 3.25-alt1
- 3.23.1 -> 3.25

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.23.1-alt2.1
- NMU: dropped dependency on distutils.

* Sun Oct 24 2021 Sergey Y. Afonin <asy@altlinux.org> 3.23.1-alt2
- added gpsd-apistatus.patch from Fedora Rawhide

* Sat Oct 23 2021 Sergey Y. Afonin <asy@altlinux.org> 3.23.1-alt1
- 3.23.1
- splitted gpsd-clients to gpsd-clients-gui, gpsd-clients-console
  and gpsd-helpers (ALT #41036)

* Sat Oct 23 2021 Sergey Y. Afonin <asy@altlinux.org> 3.23-alt1
- 3.23
- Changed abiversion to 29

* Thu Jul 29 2021 Grigory Ustinov <grenka@altlinux.org> 3.20-alt6.1
- NMU: removed buildrequires on python3-module-anyjson.

* Wed Mar 10 2021 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt6
- updated URL
- added pps-tools-devel to BuildRequires (ALT #39774)

* Wed Jun 24 2020 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt5
- added python3-module-gps to Requires of gpsd-clients subpackage

* Wed Jun 24 2020 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt4
- updated gpsd-3.20-SConstruct.patch: sync all checks
  for target_python for xgps with upstream

* Wed Jun 24 2020 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt3
- fixed check for aiogps for target_python
  (based on upstream's commit e876f4558)

* Sat May 02 2020 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt2
- built with Qt5 (thanks to zerg@altlinux)

* Thu Jan 02 2020 Sergey Y. Afonin <asy@altlinux.org> 3.20-alt1
- 3.20
- added libgtk+3-devel to BuildRequires (is needed for xgps)

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 3.19-alt3
- NMU: Fix license.

* Sun Oct 20 2019 Sergey Y. Afonin <asy@altlinux.org> 3.19-alt2
- switched to python 3
- built with asciidoc

* Tue Oct 15 2019 Sergey Y. Afonin <asy@altlinux.org> 3.19-alt1
- 3.19
- Changed abiversion to 25

* Wed Mar 27 2019 Sergey Y. Afonin <asy@altlinux.ru> 3.18-alt1
- 3.18
- Changed abiversion to 24
- Enabled libQgpsmm
- Packaged systemd's units
- Removed fixes for libm and RPATH

* Tue Jun 09 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.15-alt1
- 3.15
- Removed "Requires: gpsd" from lib* packages

* Wed Jun 03 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.14-alt2
- Built with debuginfo
- Added libusb-devel to BuildRequires
- Installed udev-rules
- Fixed linking with libm
- Removed RPATH without chrpath

* Thu May 28 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.14-alt1
- 3.14
- New URL: http://www.catb.org/gpsd
- changed abiversion to 22
- added libbluez-devel to BuildRequires

* Sun May 24 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt4
- Disabled libQgpsmm temporary
  (undefined symbol _Z17libgps_dump_stateP10gps_data_t)

* Sun May 24 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt3
- Renamed libs for according SharedLibs Policy.

* Sun May 24 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt2
- Built libQgpsmm
- added egg-info file to python-module-gps

* Fri Mar 02 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.4-alt1
- 3.4
- build system changed to scons

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.94-alt2.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 2.94-alt2
- Fixed interpackage dependencies.
- Fixed build dependencies.
- Rebuilt for debuginfo.

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.94-alt1.1
- Rebuilt for soname set-versions

* Tue Jun 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.94-alt1
- build fixed
- 2.94

* Wed Nov 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.37-alt2
- rebuild without pre/post

* Fri Apr 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.37-alt1
- first build for Sisyphus

* Tue Jan 1 2008 Eric S. Raymond <esr@snark.thyrsus.com> - 2.36
- Urgent fix to leap-day calculation affecting dates from today to
  28 Feb on generic NMEA GPSes, Zodiacs, and SirFs emitting message 0x62.
  Integrated Garmin Simple Text Protocol driver from Peter Slansky.
  Minor fixes in error modeling and a better NaN guard stabilize the
  Trimble regression tests.  Remove the wired-in NTP time offset from the
  NMEA driver, this could only have worked by accident and should be
  set in ntpd.conf. Integrated Ashtech driver from Chris Kuethe.

* Mon Dec 10 2007 Eric S. Raymond <esr@snark.thyrsus.com> - 2.35-1
- Navcom driver merged. Removed -d -f and -p options of gpsd; these
  have been undocumented for a while.  Make gpsd play well with pkgconfig.
  Incorrect computation of VDOP when GPSes didn't supply it has been fixed.
  The xgps code has been revamped and now has a much nicer interface.
  Add -b (no-configuration) option as a sadly clumsy workaround for some
  problems with Bluetooth receivers.  Added tests for Haicom-305N and Pharos
  360; separated out the tests for the unstable Trimble drivers.
  32-vs-64-bit problems in the regression tests have been solved.

* Thu Dec 14 2006 Eric S. Raymond <esr@snark.thyrsus.com> - 2.34-1
- Fix for byte-swapping of Zodiac control messages on big-endian hardware.
  Disable iTalk by default and note that it needs to be tested.  Command line
  arguments can now be DGPSIP or NTRIP URLs; -d is deprecated. Added udev
  rules.  Address excessive processor and memory utilization on SBCs; it's
  now possible to configure compile-time limits on the number of devices
  and client sessions.  Eliminate use of fuser(1) in gpsfake.  Get gpsd
  working with EarthMates again, this had been broken since 2.15.  Massive
  string safety audit and OpenBSD port by Chris Kuethe.  J command added.
  The gpsctl and gpscat tools and the gpsd.phps script were added.  Switched
  to lesstif from openmotif.  Better autodetection of DLE-led packet
  protocols (notably TSIP and Garmin binary) and of SiRFStar I and III
  devices.  Fixed buggy parsing and generation of PGRME.

* Fri Jun  9 2006 Eric S. Raymond <esr@snark.thyrsus.com> - 2.33-1
- Fix bad unit conversion in V output.  Clean up some man-page messes.
  Fixed buggy libgps parsing of multiple responses.  It's now possible
  to lock gpsd to a fixed speed at compile time for embedded use.  Added
  NTRIP support, thanks to Ville Nuorvala.  O command now ships an
  explicit mode field.

* Sun Mar 12 2006 Eric S. Raymond <esr@snark.thyrsus.com> - 2.32-1
- Cleanup of the xgps layout, and minor memory-leak fixes for xgps.  Fix
  to cope with Antares uBlox by Andreas Stricker.  Minor fix to libgps
  cgpxlogger.  Merge cgpxlogger and gpxlogger documentation onto
  the xgps(1) manual page and rename it gps(1).

* Fri Feb 17 2006 Eric S. Raymond <esr@snark.thyrsus.com> - 2.31-1
- Now builds and runs under Cygwin.  Correct the speed units in
  synthetic NMEA.  Slightly better time handling under NMEA.  Daemon
  now builds with all but NMEA disabled.  Update the leap-second
  offset. cgpxlogger introduced.  Upgrade gpxlogger to DBUS 0.60
  conformance.  Jason von Nieda's patch may fix the chronic TSIP
  driver problems.

* Wed Sep 14 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.30-1
- Prevent core dump on -d option.  The .log extension is no longer required for
  test loads.  cgps and xgps now have configurable latitude/longitude formats
  via the -l option.  Introduced new 'g' command that allows clients to
  specify whether they want GPS or RTCM104 information.

* Fri Aug 19 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.29-1
- Added Sony CXD2951 support, untested.  All error estimates are
  now nailed to 95%% confidence interval.  Added rtcmdecode and its
  documentation; also, gpsd can now monitor serial devices emitting
  RTCM104 and display differential-GPS data in a readable format.
  Added dangerous alpha version of gpsflash.  Work around a nasty bug
  in SiRFStar III firmware version < 3.1.1.  Added support for True
  North Technologies Revolution 2X Digital compass.  Added the
  gpxlogger client for systems with DBUS support and the gpspipe
  and cgps clients for general use.

* Wed Jul  6 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.28-1
- The 2.27 source tarball somehow got truncated on upload.
  Due to procedural mechanics at berlios.de, shipping a new release
  seems to be the least painful way to recover.  This release is
  identical to 2.27 except the roadmap stuff has been added to TODO.

* Wed Jul 06 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.27
- Arrange for the daemon to remove its pid file on exit.  Fix some
  buffering problems with the Python side of the hotplug interface.
  gpsfake can now run sessions under a monitor like Valgrind.  Most
  of the gpsfake logic now lives in a module that can be used to write
  other test loads; its progress baton is now optional.  Fixed
  some minor bugs found by valgrind audit, including (1) a slow
  memory leak, (2) a possible but unconfirmed file-descriptor leak,
  and (3) a subtle error in the channel-assignment logic that only
  showed up with multiple sessions active.  In fact, the daemon code
  no longer uses dynamic-memory allocation at all.  Also, the code
  no longer relies on FIONREAD working.  The track error field in the
  O response is now computed.  The project website has some new eye candy.
  Client connections now time out when the mode is neither raw nor watcher.
  Fixed a core-dump that could happen if C, B or I commands were issued
  at odd times.

* Wed Jun 22 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.26
- Time DOP and total DOP are now passed on from GPSes that report
  them.  Ensure longitude has a leading zero when <100, for
  compatibility with gpsdrive.  Synchronous and thread hooks are now
  separate in the client library.  Packet-sniffing on a new device no
  longer holds up incoming data on already-connected ones.  There is
  now a super-raw mode (R=2) that dumps a hex-encoding of every binary
  packet received to the client; sirfmon uses it to operate through
  the daemon if one is running.  Support for Trimble TSIP GPSes
  merged. gpsfake now works with SiRF and Zodiac logs.  Python library
  supports thread callbacks.  New -p option of gpsfake supports
  regression testing of the daemon, and there is a test suite included
  with the distribution.  PPS support is turned off, as there is some
  pthreads problem that sometimes kills the daemon on pthreads exit.
  Correct off-by-one error in GPZDA processing.  The code has been
  audited and cleaned with splint (www.splint.org).

* Sat May 21 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.25-1
- Various signedness and scaling fixes and an OpenBSD port patch for the
  Zodiac driver. Command-line arguments to gpsd are now treated as a default
  device list; -f is still supported but deprecated.  sirfmon now tries not
  changing the line speed first, so it syncs up much faster.  Prevent a
  potential buffer overrun in the client library.  PPS-thread support is now
  on by default.  Lots of documentation improvements. D-BUS broadcast support
  by Amaury Jacquot.  Added Alfredo Pironti's thread-callback and C++
  support.  gpsd no longer uses the system clock for anything, so it
  can be used to set that clock.

* Tue May 17 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.24-1
- Crazy-speed bug is finally fixed. Autobauding now starts with the
  current speed of the device, not the stored gpsd speed; this means
  hunting only takes place when device and GPS speed aren't matched.
  xgpsspeed unit-conversion bug introduced in 2.22 is fixed.  Satellite
  display now really shows 12 channels, not just 11. Major improvements
  in ntp notifications.

* Wed May  4 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.23-1
- For better security, the daemon now drops root privileges after startup.
  gpsd-clients is now a separate RPM; this is helpful on lean systems
  that don't run X.  The O command now reports speeds in meters per second
  rather than knots, client code has been adjusted so there is no user-visible
  change.  We now compute the missing components of DOP when using SiRF chips.
  /dev/gps is no longer special; there is no default GPS device unless you
  specify one.  The intermittent processor-hogging problem introduced by the
  control-channel change in 2.21 has been solved.

* Mon Apr 25 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.22-1
- SiRF-binary driver can now get leap-second corrections from subframe data.
  Device add/delete commands now send back OK or ERROR.  Error-modeling
  corrections from the SiRF folks.  Higher precision in position reports.

* Tue Apr 12 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.21-1
- Add tag and timestamp to Y response.  Use computed geoid separation as
  SiRF packet 42 is flaky.  Security fix: hotplug scripts now do device
  add/removes through a separate local control channel.  True multi-device
  support is in place.  When in watcher mode, device switches are announced.

* Thu Mar 31 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.20-1
- Rob Janssen's patches to fix timezone issues and improve cooperation
  with NTP.  License changed to BSD so linking to libgps won't make people
  nervous.  gpsprobe and gpsd.py are obsolete and have been removed, the
  autoprobe and profiling capabilities in the daemon more than replace
  them.  gpsprof now ships self-contained GNUPLOT scripts to stdout,
  so they can be saved and redisplayed.  Zodiac sort of works again, but
  occasionally spins madly during autobauding.

* Sat Mar 26 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.19-1
- Fix brown-paper-bag bug with NMEA parsing. Set SiRF GPSes to use
  SBAS.  sirfmon now displays SBAS parameters, and is included in the
  installed programs.  Add to FAQ a fix for spurious high speeds reported
  in XTrac mode.  We now interpret GPZDA.  We no longer fudge a missing
  ddmmyy in NMEA timestamps from the system clock, so replay will work better.

* Wed Mar 23 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.18-1
- First cut at cooperating with NTP.  Major library restructuring;
  a fix is now a data structure of its own, and per-field timestamps
  are gone. Use new 'o' command for watcher mode.  Compute some estimated
  error bounds.

* Wed Mar 16 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.17
- Fix packet-engine problem that made disconnect/reconnect unreliable
  (important!).  Fix bonehead error in interpretation of PGRME.  We
  don't use O_SYNC (it turned out not to be reliable) so remove it to make
  life easier under Mac OS X.  Allow gpsfake to accept subsecond cycle times.
  Add a FAQ to the HTML documentation.  gps_poll() now handles multi-line
  responses.  Add N command for switching driver modes.

* Fri Mar 11 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.16-1
- New F command allows changing the GPS device after startup time.
  Hotplug scripts to go with it are now installed by the RPM.  The
  Garmin probe is working.  The -T and -s options are gone.  We have
  achieved zero configuration!

* Wed Mar 02 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.15-1
- A new packet engine autobauds much more quickly, and now iterates
  over both 1 and 2 stopbits. Explicit support for FV18 (the -T f
  option) is gone; instead, gpsd syncs with any 7N2 device and always
  ships a suitable init string.  New E command, supporting the Garmin
  position-error sentence or computing these numbers from DOP and an
  error model. New U command reports climb/sink from GPSes that report
  vertical velocity.  There is a prototype driver for SiRF-binary GPses,
  invoked automatically when SiRF packets present themselves on the
  wire after device open.

* Fri Feb 25 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.14-1
- Pass zero magnetic variation in generated NMEA from binary GPSes
  correctly.  Use O_SYNC rather than timeouts to guarantee that
  baud-rate change strings get to the GPS before changing the line
  parameters.  Introduced I command.  Spatial scattergram plotting
  moved from gpsprobe to gpsprof.

* Mon Feb 21 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.13-1
- Correct a bug in binary-protocol dumping (applies to Zodiac and
  Garmin only).  Gary Miller's patch to deal gracefully with GPSes
  like the Magellan EC10X that send only GPRMC and never GPGGA or
  GPGSA, and thus never set mode or status fields.  Fixed buggy
  handling of units options in xgps and xgpsspeed.  Bumped library
  major version, since seen_sentences is now exposed and drivers have
  more capabilities.  Stricter NMEA buffer validation.  Withdrew the
  change that always passed up a timestamp; on SiRF receivers, the year
  part is garbage when the PVT fields are garbage.  Can now recognize
  SiRF GPSes.  Experimental baud-switching support for Zodiac.

* Tue Feb 15 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.12-1
- Fixed core-dump bug in processing of the GLL variant that does not
  include an FAA Mode Indicator. When using the NMEA driver, gpsd now
  hunts for a baud rate rather than requiring a fixed one to be set.
  A new 'B' command returns the RS232 parameters, and a new 'C'
  command returns the update cycle time.  Added gpsfake test harness.
  Alpha driver for Garmin binary protocol added, requires Linux
  garmin_usb kernel driver.  The daemon now always passes up a
  timestamp for every sentence that has one, even if the PVT fields
  aren't valid.

* Thu Feb 10 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.11-1
- Added gpsprof and the capability to generate GPS latency profiles.
  gpsprobe now hunts through plausible baud rates when looking for NMEA
  data from a GPS. The -b (baudrate) option fixes a speed, disabling
  the baud-matching logic.  Also, gpsprobe can now recognize SiRF
  protocol, though not speak it.  Fixed a math domain error in
  gps.EarthDistance due to numeric blowup on points very close together,
  and another in gps.MeterOffset() that was screwing up gpsprobe plots.

* Tue Feb  1 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.10
- Add -N option to explicitly foreground the daemon.  Fixed a bug
  that was causing gpsd to keep reopening the GPS device after
  leaving raw or watcher mode.  Fixed Gary Miller's core-dump bug.

* Thu Jan 27 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.9-1
- Python files restored to RPM.

* Thu Jan 27 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.8-1
- Embarrassing typo fix in gps.py. Avoid buffer overrun in xgps.c.
  Plug Debian security bug 292347, CVE number CAN-2004-1388.
  This version issued on an emergency basis without Python libraries,
  which have packaging problems due to the 2.3/2.4 transition.

* Fri Jan  14 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.7-1
- More compiler-warning cleanups.  gps client name changed to xgps.
  Added --speedunits option to xgpsspeed, --speedunits and --altunits
  options to xgps.  Improved GPGSV parsing so it copes gracefully if
  we start in the middle of a sequence.  Merged Petter Reinholdtsen's
  fix for GPGSA lists with holes.  In xgps, satellites used in the
  last fix are now dotted in the middle.  New -P option to create
  pidfile.  Audited for potential buffer overruns, found and fixed
  two.

* Sat Jan 01 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.6-1
- Petter Reinholdtsen's fix for gps.py buffering.  Fix syntax errors
  in udev scriptlets.  Clean up after GCC warning messages.  Drop use of
  vsprintf, so we get a link-time error on systems that might produce
  buffer overruns (all modern Unixes support vsnsprintf which is safe).

* Thu Dec 23 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.5.1
- Use gmtime instead of localtime when guessing the day or year of a date;
  this avoids jitter in the day after 19:00 GMT.  Added -v option to dump
  version and exit.  Commented out a crash-causing debug line in gps.py.

* Thu Dec  9 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.4-1
- Minor bugs in gpsd.py fixed.  M now returns 0 status if GPGSA not yet
  seen; this change also fixes a bug where gpsd claimed it was confused
  if GPGSA had not been seen and status was set.  RPM will now install
  a udevd rule if the host system uses it.  Don't set the online flag
  on activate.  HP port changes and -Wall cleanup.  James Cameron's
  fixes to clean up gps.c and use X timeouts rather than alarms.

* Mon Oct 25 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.3-1
- Documentation and comment fixes.  Last two globals removed from
  low-level interface; library should now be fully re-entrant. Mac OS X
  port fixes. Q command fix from Robin L Darroch <robin@spade-men.com>.

* Mon Oct 18 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.2-1
- Documentation improvements.  BSD port fixes.  Bug fix: speed timestamp
  wasn't initialized properly in libgps. Device is now an optional
  command-line argument of gpsprobe, in line with the clients.  gpsd.py
  now should handle fvwm devices correctly.  Values in gps data
  panel are now labeled with units.  Attempted fix for 2.1 bug of DTR
  not being pulled low on exit.

* Thu Sep 30 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.1-1
- Various internal cleanups, including fossil removal in the
  configuration machinery.  FV-18, Tripmate, Earthmate and are now
  enabled but can be disable with --disable-$NAME at configure time.
  When you call configure with --disable-shared, libgps is linked
  statically to the binaries (native libs are still linked
  shared). Fixed buggy handling of -p option in gps.c and xgpsspeed.c;
  it's now an optional command-line argument.

* Thu Sep 16 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.0-1
- Packaging fixes for 2.0 release.

* Wed Sep  8 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.98-1
- Only do one getdtablesize() call, otherwise we do several
  getrlimits() each poll cycle.  TripMate is working.  gpsprobe now
  deduces NMEA version.  Zodiac Earthmate seems to work.

* Wed Sep 08 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.97-1
- Removed PRWIZCH support (it still passes through in raw mode).
  Build Motif-dependent programs conditionally.  Added gpsprobe.
  Fixed a brown-paper-bag-bug in 1.96 RPM packaging.

* Tue Aug 31 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.96-1
- Implemented non-blocking writes to clients, so a stalled client
  cannot stall gpsd.  Fixed a nasty array-overrun bug.  Timestamps
  are now in ISO8601 format, with sub-second precision if the GPS
  delivers that.  First cuts at Python interfaces included.  libgps.a
  interface now bundles session fd into an allocated session block.
  Automake-based build machinery from Jens Oberender; RPM now
  installs shared libraries.  FV18 driver added. Offline timer in GPS.

* Wed Aug 25 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.95-1
- Fixed broken 'make dist', missing display.c and Tachometer.c
  are in there now.

* Tue Aug 24 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.94-1
- Fix embarrassing bug -- watcher mode did not work for more than one
  client at a time.  Y command now carries information about which
  satellites were used in the last fix.  New timeout mechanism, no
  longer dependent on FIONREAD.

* Mon Aug 23 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.93-1
- Fourth prerelease. Daemon-side timeouts are gone, they complicated
  the interface without adding anything.  Command responses now
  contain ? to tag invalid data. -D2 feature of 1.92 backed out.

* Sun Aug 22 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.92-1
- Third prerelease.  Clients in watcher mode now get notified when
  the GPS goes online or offline.  Major name changes -- old libgps
  is new libgpsd and vice-versa (so the high-level interface is more
  prominent).  Specfile now includes code to install gpsd so it will
  be started at boot time.  -D2 now causes command error messages
  to be echoed to the client.

* Sat Aug 21 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.91-1
- Second pre-2.0 release.  Features a linkable C library that hides the
  details of communicating with the daemon.  The daemon now recovers
  gracefully from having the GPS unplugged and plugged in at any time;
  one of the bits of status it can report is whether the GPS is online.
  The gps and xgpsspeed clients now query the daemon; their code
  for direct access to the serial port has been deliberately removed.

* Sun Aug 15 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 1.90
- Creation of specfile.

* Sun Mar 21 2004 Remco Treffkorn <remco@rvt.com> - ?
- Without PRWIZCH sentence: sat. colors in gps according to ss, grey==lt20,
  yellow==lt40 else green.
- Added L Q and I to the protocol. Removed G and T.
  Changed the timeout mechanism. Try to not return Lat/Lon/Alt if
  validity is in doubt.

* Thu Jan 29 2004 Remco Treffkorn <remco@rvt.com> - ?
- Make applications null-terminate their resource lists.

* Sat Dec 20 2003 Remco Treffkorn <remco@rvt.com> - ?
- Removed <varargs.h> from netlib. Not needed, and new gcc does not support
  it any more.

* Wed Aug 20 2003 Remco Treffkorn <remco@rvt.com> - 1.10
- Add install target. Fix clean target. Make GPS timeout configurable.
- Make xgpsspeed build with Apple's X11.
- Make sure that we don't segfault if the NMEA is badly formed.

* Mon Aug 18 2003 Remco Treffkorn <remco@rvt.com> - ?
- Use cfset[io]speed() to set speed in serial.h. Glibc is quite insane
  and I am tired to chase it, so I give up. Hope this works for BSD.
  Set status and mode 0 after GPS timeout (5 sec) - Cougar <cougar@random.ee>

* Sun Feb 16 2003 Remco Treffkorn <remco@rvt.com> - 1.09
- Include sys/time.h in gpsd.c for struct timeval.

* Sun Nov 03 2002 Remco Treffkorn <remco@rvt.com> - ?
- G or g command returns six-digit Maidenhead grid square (like FN12fx)

* Thu Oct 03 2002 Remco Treffkorn <remco@rvt.com> - 1.08
- Added sockopt SO_REUSEADDR to netlib.c passive_sock.

* Tue Feb 05 2002 Remco Treffkorn <remco@rvt.com> - 1.07
- em.c uses <time.h> (as it should). Removed some <sys/time.h>
- where they were not needed.
- Russ Nelson: Improved Earthmate support: added state machine for
  EARTHA recognizer, removed alignment problems seen on ARM architecture.
  Added setsockopt to add SO_REUSEADDR, so that
  gpsd can stop and immediately restart.  Added support for bitrates
  higher than 38400, needed for the SIRF chipset.
- Derrick: my patch causes longitude when under 100 degrees to be printed
  zero-padded as needed, the latitude same deal under 10, fixes the GGA
  sentence to not erroneously print fix type (2/3) instead of fix quality,
  and calculates fix type correctly.

* Fri Aug 11 2000 Remco Treffkorn <remco@rvt.com> - 1.06
- Change from C++ (/) to C comments (/* */)for compatibility.
- Added -n (need init) flag.
- Don't init unless lat/lon specified.
- Remove gps.mayko.com as the default hostname.

* Fri May 12 2000 Remco Treffkorn <remco@rvt.com> - 1.05
- (even though version.h says 1.04)
- Added some includes to xgpsspeed.c for portability.
- Fix problem with flags being overwritten, and using the wrong port
- variable also in xgpsspeed.c
- Add a note about Y2K compatibility fix.
- Pass latitude and longitude into em_init().

* Fri Mar 17 2000 Remco Treffkorn <remco@rvt.com> - 1.02
- (even though version.h says 1.01)

* Sun Mar 05 2000 Remco Treffkorn <remco@rvt.com> - 1.01
- Updated to IANA port.
- Fixes to DGPS support.

* Sun Jan 02 2000 Remco Treffkorn <remco@rvt.com> - 1.0
- Added DGPS fixes from Curt Mills. (See README for contact info.)

* Mon Dec 13 1999 Remco Treffkorn <remco@rvt.com> - 0.99dgps
- Added minimal DGPS support by Derrick J Brashear

* Sat Jul 17 1999 Remco Treffkorn <remco@rvt.com> - 0.99
- Rockwell binary is now translated to NMEA format, so that
  clients like gps will work with an EarthMate.
- Added speedometer application. Thanks to Derrick J Brashear
  for his work (see README for contact info).

* Thu Mar 04 1999 Remco Treffkorn <remco@rvt.com> - 0.96
- Changed EarthMate support. Rockwell binary is now almost properly
  supported. Only the minimum required information is extracted.

* Sat Feb 06 1999 Remco Treffkorn <remco@rvt.com> - 0.95
- Added support for EarthMate receivers. Since I do not have one, this is
  untested.
- If it works, it does the following: You start gpsd with a baudrate of 9600
  and give it the -Te option. If gpsd gets the EartMate it will enable the
  receiver and then attempt to switch it into NMEA mode. If the EarthMate id
  is not received, but a binary data header is received, then we will try to
  switch NMEA too.

* Sun Jan 24 1999 Remco Treffkorn <remco@rvt.com> - 0.94
- Y2K compliant ;-)  (... is NOT. Look for "FIXME:" in nmea_parse.c)

* Tue Jan 27 1998 Remco Treffkorn <remco@rvt.com> - 0.93
- using GNU autoconf now.
- combined gpsd + gpsclient. No more init files, command line only.

* Tue May 13 1997 Remco Treffkorn <remco@rvt.com> - 0.9
- some cleanups in the ini code. version 0.9 ...

* Fri Apr 25 1997 Remco Treffkorn <remco@rvt.com> - 0.8
- version 0.8, some bug fixes. New MODE member, STATUS member changed.

* Mon Apr 21 1997 Remco Treffkorn <remco@rvt.com> - 0.7
- released version 0.7

# The following sets edit modes for GNU EMACS
# Local Variables:
# mode:rpm-spec
# End:
