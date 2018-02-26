Name: gkrellm
Version: 2.3.5
Release: alt3
Packager: Roman Savochenko <rom_as at altlinux.ru>

Summary: Multiple stacked system monitors
License: GPLv3+
Group: Monitoring
Url: http://gkrellm.net/

Source0: %name-%version.tar
Source1: gkrellm_16.xpm
Source2: gkrellm_32.xpm
Source3: gkrellm_48.xpm
Source4: gkrellm-2.3.1-alt-init
Source5: gkrellm-2.2.8-alt-sysconfig
Patch0: %name-%version-aticonfig.patch
Patch1: UK_RU_translation.patch
Patch2: gkrellm-2.3.5-build.patch

# for gkrellm >= 2.2.0
Requires: libgtk+2 >= 2.3.1

BuildPreReq: libSM-devel libgtk+2-devel libntlm-devel libsensors3-devel libssl-devel

%description
GKrellM charts SMP CPU, load, Disk, and all active net interfaces
automatically. An on/off button and online timer for the PPP interface
is provided. Monitors for memory and swap usage, file system, internet
connections, APM laptop battery, mbox style mailboxes, and cpu temps.
Also includes an uptime monitor, a hostname label, and a clock/calendar.
Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.

%package devel
Summary: Gkrellm include files
Group: Development/Other
Requires: %name = %version

%description devel
Gkrellm header files for gkrellm development and plugin support.

%package -n gkrellmd
Summary: Gkrellm server
Group: Monitoring

%description -n gkrellmd
Gkrellm server allows connections from Gkrellm clients over network.

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p1

subst 's|^FLAGS = \(.*\)|FLAGS = %optflags \1|' src/Makefile

# gkrellmd tuning
subst 's,^#allow-host\tlocalhost,allow-host	localhost,g' server/gkrellmd.conf
subst 's,^max-clients.*,max-clients 5,g' server/gkrellmd.conf
subst 's,^update-hz.*,update-hz 2,g' server/gkrellmd.conf

# set platform-dependent libdir
subst 's,/usr/lib,%_libdir,g' src/gkrellm.h server/gkrellmd.h

%build
%make_build enable_nls=1 \
	INSTALLROOT=%prefix \
	SMC_LIBS='-L%_x11libdir -lSM -lICE'
#SYS_LIBS=-L%_x11libdir

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/gkrellm2/plugins
mkdir -p %buildroot%_desktopdir

%make_install install enable_nls=1 \
	INSTALLROOT=%buildroot%prefix \
	PKGCONFIGDIR=%buildroot%_pkgconfigdir

mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_miconsdir

install -m 644 %SOURCE2 %buildroot%_niconsdir/gkrellm.xpm
install -m 644 %SOURCE3 %buildroot%_liconsdir/gkrellm.xpm
install -m 644 %SOURCE1 %buildroot%_miconsdir/gkrellm.xpm

install -D -m755 %SOURCE4 %buildroot%_initdir/gkrellmd
install -D -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/gkrellmd
install -D -m644 server/gkrellmd.conf %buildroot%_sysconfdir/gkrellmd.conf

cat > %buildroot%_desktopdir/%name.desktop << __EOF__
[Desktop Entry]
Version=1.0
Type=Application
Name=Gkrellm
Exec=%name
Icon=%name
Categories=System;Monitor;
Comment=A gtk-based monitoring app
__EOF__

%find_lang %name

%pre -n gkrellmd
/usr/sbin/useradd -M -r -d /dev/null -s /dev/null \
	-c "GKrellM server" gkrellmd >/dev/null 2>&1 || :

%post -n gkrellmd
%post_service gkrellmd
%preun -n gkrellmd
%preun_service gkrellmd

%files -f %name.lang
%doc COPYRIGHT Changelog CREDITS README *.html
%_bindir/gkrellm
%_desktopdir/*
%_man1dir/gkrellm.*
%dir %_libdir/gkrellm2
%_libdir/gkrellm2/*
%_niconsdir/gkrellm.xpm
%_liconsdir/gkrellm.xpm
%_miconsdir/gkrellm.xpm

%files devel
%dir %_includedir/gkrellm2
%_includedir/gkrellm2/*
%_libdir/pkgconfig/*

%files -n gkrellmd
%_bindir/gkrellmd
%config(noreplace) %_initdir/gkrellmd
%config(noreplace) %_sysconfdir/sysconfig/gkrellmd
%config(noreplace) %_sysconfdir/gkrellmd.conf
%_man1dir/gkrellmd.*


%changelog
* Wed May 23 2012 Roman Savochenko <rom_as@altlinux.ru> 2.3.5-alt3
- Build fix for direct add -lgmodule-2.0.

* Tue Aug 16 2011 Roman Savochenko <rom_as@altlinux.ru> 2.3.5-alt2
- The patch aticonfig.patch for 2.3.5 is included.

* Wed Jul 27 2011 Roman Savochenko <rom_as@altlinux.ru> 2.3.5-alt1
- 2.3.5
- Update Russian translation
- Added Ukrainian translation
- Remove old patches

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.4-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Mar 10 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.3.4-alt1
- 2.3.4
- build with libntlm
- build with libsensors3
- replace menu file with desktop file

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gkrellm
  * postclean-05-filetriggers for spec file

* Tue Jun 09 2009 Grigory Batalov <bga@altlinux.ru> 2.3.2-alt2
- Include aticonfig support in the cumulative patch.

* Mon May 25 2009 L.A. Kostis <lakostis@altlinux.ru> 2.3.2-alt1.1
- Add experimetal patch for aticonfig support.
- Remove obsoleted macros.
- Fix build with recent glibc.

* Mon Apr 20 2009 Grigory Batalov <bga@altlinux.ru> 2.3.2-alt1
- New upstream release.

* Tue Oct 21 2008 Grigory Batalov <bga@altlinux.ru> 2.3.1-alt3
- Create pidfile while starting gkrellmd from init script.
- Convert package description to UTF-8 charset.

* Mon Sep 08 2008 Grigory Batalov <bga@altlinux.ru> 2.3.1-alt2
- Use %%optflags while compiling (wrar@).
- Fix several memory leaks (wrar@).

* Fri Sep 05 2008 Grigory Batalov <bga@altlinux.ru> 2.3.1-alt1
- New upstream release.

* Fri Sep 05 2008 Grigory Batalov <bga@altlinux.ru> 2.3.0-alt2
- Update build requirements.
- Master 2.4 macro was removed.

* Wed Oct 03 2007 Grigory Batalov <bga@altlinux.ru> 2.3.0-alt1
- New upstream release.

* Tue Dec 26 2006 Grigory Batalov <bga@altlinux.ru> 2.2.10-alt1.1
- Rebuilt by maintainer.

* Mon Dec 25 2006 L.A. Kostis <lakostis@altlinux.ru> 2.2.10-alt1
- NMU.
- add libsensors support.
- update lockdir patch.
- 2.2.10.

* Tue Jun 20 2006 Grigory Batalov <bga@altlinux.ru> 2.2.9-alt1
- 2.2.9

* Fri Mar 31 2006 Grigory Batalov <bga@altlinux.ru> 2.2.8-alt1
- 2.2.8
- Default gkrellmd.conf is included (#8465)
- x86_64 build and install fixes by Damir Shayhutdinov (#8181, #8182)

* Sat Jun 18 2005 Grigory Batalov <bga@altlinux.ru> 2.2.7-alt2
- Vitaly Lipatov has reworked Russian translation.

* Tue May 24 2005 Grigory Batalov <bga@altlinux.ru> 2.2.7-alt1
- 2.2.7

* Mon Apr 04 2005 Grigory Batalov <bga@altlinux.ru> 2.2.5-alt1
- 2.2.5
- split to gkrellm and gkrellmd packages

* Thu Oct 14 2004 Grigory Batalov <bga@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Thu Jul 01 2004 Grigory Batalov <bga@altlinux.ru> 2.2.1-alt1
- 2.2.1 (markup method changed)

* Tue May 25 2004 Grigory Batalov <bga@altlinux.ru> 2.2.0-alt1.2
- text on decals escaped with g_markup_escape_text()

* Thu May 20 2004 Grigory Batalov <bga@altlinux.ru> 2.2.0-alt1.1
- requirement of libgtk+2 >= 2.3.1 added (for gdk_threads_lock)

* Mon May 17 2004 Grigory Batalov <bga@altlinux.ru> 2.2.0-alt1
- 2.2.0
- lockdir changed to /var/lock/serial

* Mon Dec 29 2003 Grigory Batalov <bga@altlinux.ru> 2.1.24-alt1
- 2.1.24

* Tue Nov 11 2003 Grigory Batalov <bga@altlinux.ru> 2.1.21-alt1
- 2.1.21

* Wed Jul 09 2003 Grigory Batalov <bga@altlinux.ru> 2.1.14-alt1
- 2.1.14

* Tue Jun 10 2003 Grigory Batalov <bga@altlinux.ru> 2.1.12a-alt1
- 2.1.12a
- pkgconfig entry added to devel' files section

* Sun May 04 2003 Grigory Batalov <bga@altlinux.ru> 2.1.10-alt1
- 2.1.10

* Tue Mar 18 2003 Grigory Batalov <bga@altlinux.ru> 2.1.8a-alt1
- 2.1.8a
- description of gkrellm-devel translated in specfile

* Sun Dec 29 2002 Grigory Batalov <bga@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Dec 10 2002 Grigory Batalov <bga@altlinux.ru> 2.1.3-alt1
- 2.1.3
- ru.po updated

* Mon Dec 02 2002 Grigory Batalov <bga@altlinux.ru> 2.1.2-alt1
- 2.1.2
- ru.po updated

* Mon Oct 21 2002 Grigory Batalov <bga@altlinux.ru> 2.1.0-alt1
- 2.1.0 (Gtk+2 version)
- ru.po updated

* Fri Aug 23 2002 Grigory Batalov <bga@altlinux.ru> 1.2.13-alt1
- 1.2.13
- specfile translated

* Sat May 11 2002 Grigory Batalov <bga@altlinux.ru> 1.2.11-alt2
- large/mini icons swaped

* Fri Apr 12 2002 Grigory Batalov <bga@altlinux.ru> 1.2.11-alt1
- 1.2.11
- ru.po updated

* Mon Feb 18 2002 Grigory Batalov <bga@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Sat Jan  5 2002 Grigory Batalov <bga@altlinux.ru> 1.2.7-alt1
- 1.2.7
- ru.po updated

* Fri Dec  7 2001 Grigory Batalov <bga@altlinux.ru> 1.2.5-alt1
- 1.2.5
- ru.po updated
- default fonts changed to system "fixed"

* Fri Nov 23 2001 Grigory Batalov <bga@altlinux.ru> 1.2.4-alt2
- NLS enabled and ru.po added

* Sat Nov 03 2001 Rider <rider@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Aug 24 2001 Rider <rider@altlinux.ru>
- 1.2.2

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Mon Jan 08 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.3-1mdk
- 1.0.3

* Wed Nov 15 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2

* Mon Nov  6 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.1-2mdk
- rebuild for new libstdc++

* Thu Oct 20 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Fri Oct 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.0-1mdk
- 1.0.0

* Fri Oct 06 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.10.5-3mdk
- added missing icons

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.10.5-2mdk
- automatically added BuildRequires

* Mon Aug 07 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.10.5-1mdk
- 0.10.5
- more macros
- added requires version for gkrellm-devel
- move include dir from /usr/X11R6/include to /usr/include

* Wed Jul 12 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.10.4-1mdk
- 0.10.4
- macroization
- move plugins to their own RPM
- add devel package

* Wed Jul 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.10.2-1mdk
- v 0.10.2

* Wed May 24 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.9.10-1mdk
- 0.9.10
- bzip2 patches
- comment out all plugins since they refuse to compile

* Tue Apr 25 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.9.8-1mdk
- 0.9.8
- Added gkrellmms plugin by Sander Lebbink <sander@cerberus.demon.nl>

* Mon Apr 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9.7-1mdk
- fix group
- add menu entry

* Fri Mar 24 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.7

* Sun Mar 12 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.6
- Added seti@home plugin by Henry Palonen <henkka@yty.net>
- Added plugin to to display fan speeds by Jarkko Lietolahti <jappe@iki.fi>
- since plugins (currently) need to be in ~/.gkrellm/plugins, you must
  symlink to the plugins in /usr/share/gkrellm/plugins

* Fri Mar 3 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.5

* Mon Feb 28 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.4
- libgtop is no longer required

* Thu Feb 24 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.3

* Wed Feb 23 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.1

* Tue Feb 22 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.9.0
- libgtop-devel is now required but it seems to be broken as the
  glibtop-config.h is in /usr/lib/libgtop/include and not /usr/include/ like
  it should be (you must manually copy before building the RPM)

* Sun Feb 13 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.8.1

* Mon Dec 06 1999 Lenny Cartier <lenny@mandrakesoft.com>
- 0.7.5

* Fri Nov 19 1999 Lenny Cartier <lenny@mandrakesoft.com>
- New in contrib
- Used the SRPMS provided by Vincent Danen
- bz2 archive
- 0.7.4

* Wed Nov 17 1999 Vincent Danen <vdanen@linux-mandrake.com>
- updated specfile for Mandrake contribution

* Thu Nov 11 1999 Vincent Danen <vdanen@softhome.net>
- wrote spec file
- 0.7.3
