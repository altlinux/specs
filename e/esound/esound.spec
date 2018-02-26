%define ver_major 0.2
%def_enable alsa
%def_enable oss
%def_disable arts
%def_disable static

Name: esound
Version: %ver_major.41
Release: alt7

Summary: The Enlightened Sound Daemon
License: GPL
Group: System/Servers
Url: ftp://ftp.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2
Patch1: %name-0.2.37-alt-config.patch
Patch3: %name-0.2.37-alt-esd_spawn_options.patch
Patch4: esound-0.2.37-alt-esd_no_spawn.patch
Patch7: %name-0.2.39-alt-shut_up.patch
Patch8: %name-0.2.41-link.patch

%define audiofile_ver 0.2.3

BuildPreReq: libaudiofile-devel >= %audiofile_ver
BuildRequires: docbook-utils-print libwrap-devel

%if_enabled alsa
%define alsa_ver 1.0.0
BuildPreReq: libalsa-devel >= %alsa_ver
%endif
%if_enabled arts
BuildPreReq: libarts-devel
%endif
%if_enabled static
BuildPreReq: glibc-static-devel
%endif

%description
EsounD (the Enlightened Sound Daemon) is a server process that allows multiple
applications to share a single sound card. For example, when you're listening
to music from your CD and you receive a sound-related event from ICQ, your
applications won't have to jockey for the attention of your sound card.

EsounD mixes several audio streams for playback by a single audio device.

%package -n esd
Summary: The Enlightened Sound Daemon
Group: System/Servers
Provides: esound = %version
Obsoletes: esound < %version
Provides: esound-daemon
Requires: libesd = %version-%release

%description -n esd
EsounD (the Enlightened Sound Daemon) is a server process that allows multiple
applications to share a single sound card. For example, when you're listening
to music from your CD and you receive a sound-related event from ICQ, your
applications won't have to jockey for the attention of your sound card.

EsounD mixes several audio streams for playback by a single audio device.

%package -n libesd
Summary: Enlightened Sound Daemon shared library
Group: System/Libraries

%description -n libesd
EsounD (the Enlightened Sound Daemon) is a server process that allows multiple
applications to share a single sound card. For example, when you're listening
to music from your CD and you receive a sound-related event from ICQ, your
applications won't have to jockey for the attention of your sound card.
EsounD mixes several audio streams for playback by a single audio device.

This package contains shared library for applications which use Esound.

%package utils
Summary: Enlightened Sound Daemon - clients
Group: Sound
Requires: libesd = %version-%release

%description utils
Utilities that control and interact with the Enlightened Sound Daemon.

%package -n libesd-devel
Summary: Libraries, includes and more to develop EsounD applications
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Requires: libesd = %version-%release

%description -n libesd-devel
Libraries, include files and other resources you can use to develop EsounD
applications.

%package -n libesd-devel-static
Summary: Static libraries to develop EsounD applications
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version
Requires: libesd-devel = %version-%release

%description -n libesd-devel-static
Static libraries you can use to develop statically linked EsounD
applications.

%prep
%setup -q
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch7
%patch8

%build
%autoreconf
%configure \
	--with-libwrap \
	--enable-local-sound \
	%{subst_enable alsa} \
	%{subst_enable oss} \
	%{subst_enable arts} \
	%{subst_enable static}

%make_build

%install
# fix manpage for esd
subst 's,/etc/esound,/etc,g' docs/esd.1

%make DESTDIR=%buildroot install

%files -n esd
%_bindir/esd
%_bindir/esddsp
%_bindir/esdplay
%_man1dir/esd.*
%_man1dir/esddsp.*
%config(noreplace) %_sysconfdir/esd.conf

%files -n libesd
%_libdir/*.so.*
%doc AUTHORS NEWS README TIPS MAINTAINERS

%files utils
%_bindir/*
%exclude %_bindir/esd
%exclude %_bindir/esddsp
%exclude %_bindir/esd-config
%exclude %_bindir/esdplay
%_man1dir/*.1*
%exclude %_man1dir/esd.1*
%exclude %_man1dir/esddsp.1*
%exclude %_man1dir/esd-config.1*

%files -n libesd-devel
%_bindir/esd-config
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/aclocal/*
%_man1dir/esd-config.1*
%doc ChangeLog TODO TIPS docs/html

%if_enabled static
%files -n libesd-devel-static
%_libdir/*.a
%endif

# packaged as %doc
%exclude %_datadir/doc/esound

%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.41-alt7
- linked esound programs against libm explicitly

* Thu Mar 03 2011 Alexey Tourbin <at@altlinux.ru> 0.2.41-alt6
- disabled dependency on libalsa-devel

* Thu Mar 03 2011 Alexey Tourbin <at@altlinux.ru> 0.2.41-alt5
- rebuilt for debuginfo

* Thu Nov 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.41-alt4
- rebuild for soname set-versions

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.2.41-alt3
- libesd obsoletes esound (altbug #18430)

* Fri Nov 21 2008 Yuri N. Sedunov <aris@altlinux.org> 0.2.41-alt2
- rename esound package to esd that provides esound

* Wed Nov 19 2008 Yuri N. Sedunov <aris@altlinux.org> 0.2.41-alt1
- 0.2.41
- remove upstreamed and not used patches
- move libesd* to separate subpackage (altbug #16441)

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.40-alt1
- 0.2.40

* Sun Jun 22 2008 Yuri N. Sedunov <aris@altlinux.org> 0.2.39-alt1
- new version
- ubuntu patches
- enable alsa 
- fix description (altbug #11910)

* Tue Nov 06 2007 Alexey Rusakov <ktirf@altlinux.org> 0.2.38-alt2
- DISABLE alsa over again due to problems with esdlib (see Bug $8349).
- %%exclude installed documentation files, they are packaged along with
  other documentation.

* Fri May 25 2007 Igor Zubkov <icesik@altlinux.org> 0.2.38-alt1
- 0.2.37 -> 0.2.38
- enable alsa

* Mon Apr 30 2007 Igor Zubkov <icesik@altlinux.org> 0.2.37-alt1
- 0.2.36 -> 0.2.37

* Mon Mar 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.2.36-alt5
- fix linking with --as-needed.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.36-alt4.1
- Rebuilt for new pkg-config dependencies.

* Fri Oct 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.2.36-alt4
- Disabled ALSA again due to problems with esdlib (see bug #8349).

* Fri Oct 14 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.2.36-alt3
- Added options for building OSS and aRts backends.

* Tue Sep 13 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.2.36-alt2
- Switched to ALSA (upstream).
- Disabled building static libs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.2.36-alt1
- 0.2.36

* Mon Nov 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.34-alt1.2
- build static libraries (#5582).

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.34-alt1.1
- move esdplay to main package (ZerG).

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.34-alt1
- 0.2.34

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.33-alt1
- 0.2.33

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.32-alt2
- use libtool-1.4
- do not package .la files.
- devel-static subpackage now is optional.

* Fri Sep 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.32-alt1
- 0.2.32

* Fri Aug 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.31-alt2
- disable unwarily enabled alsa support.

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.31-alt1
- new version.

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.29-alt3
- move esddsp to main package.

* Sun Nov 10 2002 AEN <aen@altlinux.ru> 0.2.29-alt2
- rebuilt with new libwrap

* Fri Sep 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.29-alt1
- 0.2.29
- esddsp.patch removed, not needed more.
- post/postun scripts updated.
- patch names fixed.

* Sat Jun 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.28-alt2
- esddsp.in.patch fixed.

* Wed Jun 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.28-alt1
- 0.2.28
- config.patch adopted (new -promiscuous option)

* Mon Jun 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.27-alt1
- 0.2.27
- man.patch removed. (man pages now included in main package)
- config.patch adopted.

* Sat May 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.26-alt1
- 0.2.26
- debian patch removed
- config and man patches applied.
- esddsp.in patch

* Sun Feb 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.23-alt2
- debian.patch (modified esound_0.2.23-3.diff).
- utils, devel-static packages.
- manpages.
- esd.conf highly commented and esound no longer starts in tcp
  mode by default.
- BuildRequires updated.

* Mon Nov 26 2001 AEN <aen@logic.ru> 0.2.23-alt1
- new version

* Sun Mar 11 2001 AEN <aen@logic.ru> 0.2.22-ipl2mdk
- removed BuildReq on stylesheets (thnx to Andrey Brindeew) & ld.so

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 0.2.22-ipl1mdk
- 0.2.22
- Updated esdstart patch.
- RE adaptions.

* Mon Oct  9 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.20-2mdk
- Patch esddsp script to use correct libraries
- binaries are no longer owned by audio group.

* Sat Oct  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2.20-1mdk
- Upgrade to 0.2.20 to have complete security fix.

* Fri Sep 29 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.19-7mdk
- Include security fix from Vincent Danen

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.2.19-6mdk
- automatically added BuildRequires

* Mon Jul 24 2000 dam's <damien@mandrakesoft.com> 0.2.19-5mdk
- added --disable-alsa

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 0.2.19-4mdk
- added %%make

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 0.2.19-3mdk
- BM + macrozification

* Thu Jul 20 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.19-3mdk
- enforce devel dependency on same version of esound

* Wed Jul 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.19-2mdk
- apply again esd launch kill signal
- add BuildRequires for libtool
- add patch  esound-esdstart.patch.bz2

* Wed Jul 19 2000 David BAUDENS <baudens@mandrakesoft.com> 0.2.19-1mdk
- 0.2.19
- Big spec cleanup
- make Pixel happy
- BC

* Tue Jul 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.18-3mdk
- only send signal when esd could not be started by shell

* Tue Jul 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.18-2mdk
- correct check when launching spawning esd

* Fri Jul  7 2000 dam's <damien@mandrakesoft.com> 0.2.18-1mdk
- updated.

* Wed Apr 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.2.17-2mdk
- fixed group.

* Thu Dec 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.2.17

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Sane SMP build

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.2.14

* Wed Sep 22 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- sysconfdir=/etc

* Thu Jul 22 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- set permissions for binarys root:audio 0750 to prevent DoS attacks
- Default System wide esd.conf (for the 3rd time, whys this keep getting lost?)
- Removed Esound.html from docs it hasn't been there for a long time.

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Last CVS version from Mon Jun 28 1999.

* Mon Jun 14 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 0.2.12
- fix URL entry in .spec
- move %prefix/lib/lib*.so files to the main esound package from the devel
  one, as esddsp requires them to function correctly

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adatations.

* Wed Apr 07 1999 Michael Fulbright <drmike@redhat.com>
- bump release to stay 1 ahead of 5.2 packages so upgrades work

* Mon Apr 05 1999 Michael Fulbright <drmike@redhat.com>
- version 0.2.10

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- version 0.2.9

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 0.2.8 with SIGPIPE fixes from Raster

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 0.2.8

* Wed Feb 3 1999 Jonathan Blandford <jrb@redhat.com>
- bug fixes -- new release.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated in preparation of GNOME freeze

* Sat Nov 21 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- added %prefix/share/aclocal/* to %files devel
- added spanish and french translations for rpm

* Thu Oct 1 1998 Ricdude <ericmit@ix.netcom.com>
- make autoconf do the version updating for us.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
