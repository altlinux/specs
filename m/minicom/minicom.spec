%define my_lockdir /var/lock/serial
%define my_group uucp

Name: minicom
Version: 2.5
Release: alt1.hg

Group: Communications
Summary: A text-menu-driven modem control and terminal emulation program
License: GPL
Url: http://alioth.debian.org/projects/minicom/

# old cvs:
#  git cvsimport -o upstream -v -d :pserver:anonymous@cvs.alioth.debian.org:/cvsroot/minicom minicom
# new hg repo:
#  hg clone https://alioth.debian.org/anonscm/hg/minicom/minicom
Source: %name-%version.tar
Source1: %name.sh
Source2: %name.csh
Source4: %name.admin
Source5: %name.admin.ru
Source6: %name.xpm
Source7: %name-xstart.sh
Source9: %name.FAQ.ru

# Without this dependency it would be difficult to find the package with file-transfer tools
Requires: lrzsz

# added because autopoint requires it. crap.
BuildRequires: cvs

# I add the specialization of the BuildRequires:
BuildRequires: bison libtinfo-devel

# The access to serial ports should be controlled through '%my_group'
# group. It is provided by the new setup pkg.
# We need it before this package (minicom) is installed in order
# to set right permissions on files.
# Also, we need the place to create lockfiles. It should be
# provided by te new FS pkg.
PreReq: %my_lockdir

%description
Minicom is a simple modem control and terminal emulation program 
that resembles MS-DOS Telix somewhat.  It is driven by text-based menus,
has a dialing directory, full ANSI and VT100 emulation, an (external)
scripting language, and other features.

Minicom should be installed if you need a simple modem control program
or terminal emulator. It can be used for remote access (in a terminal)
and to test and configure your modem.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-lock-dir=%my_lockdir \
	--enable-dfl-port=/dev/modem
%make_build

%install
%makeinstall

dest=%buildroot%_sysconfdir/profile.d
mkdir -p $dest
install -p %SOURCE1 $dest/%name.sh
install -p %SOURCE2 $dest/%name.csh
unset dest

for f in minirc.dfl; do
  mv {doc,%buildroot%_sysconfdir}/$f
done
install -p -m644 %SOURCE4 %name.admin
install -p -m644 %SOURCE5 %name.admin.ru
install -p -m644 %SOURCE9 %name.FAQ.ru

%find_lang %name

# Preparing the docs:
find extras doc -name 'Makefile*' -print0 |
	xargs -r0 rm -f --

# The icon (from Caldera)
install -pD -m644 %SOURCE6 %buildroot%_liconsdir/%name.xpm

# The script to start minicom in an X terminal
install -pD -m755 %SOURCE7 %buildroot%_libdir/%name/xstart

# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
Comment=Terminal Emulator (for modem/other serial lines)
Icon=%{name}
Exec=/usr/lib/minicom/xstart
Terminal=true
Categories=Network;Dialup;
EOF

%files -f %name.lang
%attr(640,root,%my_group) %config(noreplace) %_sysconfdir/minirc.dfl
%attr(755,root,root) %config %_sysconfdir/profile.d/%name.sh
%attr(755,root,root) %config %_sysconfdir/profile.d/%name.csh
%_bindir/*
%_mandir/man?/*

%_desktopdir/%{name}.desktop
%_liconsdir/*

%dir %_libdir/%name
%attr(755,root,root) %_libdir/%name/xstart

%doc doc extras
%doc %name.admin
%lang(ru) %doc %name.admin.ru
%lang(ru) %doc %name.FAQ.ru

%changelog
* Tue Apr 26 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.5-alt1.hg
- Update to latest hg HEAD v2.5-23-gecee7eb.

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1.cvs.20091118.qa1
- NMU: converted menu to desktop file.

* Wed Nov 18 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4-alt1.cvs.20091118
- cvs snapshot 20091118.
- Fix buffer overflow in src/dial.c because of too long translated
  message (Closes: #22301).

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt4.cvs.20081130.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for minicom
  * postclean-05-filetriggers for spec file

* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3-alt4.cvs.20081130
- cvs snapshot 20081130
- Remove obsolete %%clean_menus/%%update_menus calls

* Wed Sep 10 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3-alt3.cvs.20080805
- cvs snapshot 20080805

* Thu May 29 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3-alt2.cvs.20080425
- cvs snapshot 20080425

* Mon Feb 04 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3-alt1.cvs.20080202
- cvs snapshot 20080202:
  + russian translation merged by upstream and updated

* Tue Jan 22 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3-alt1.cvs.20080116
- cvs snapshot 20080116:
  + src/config.c: overflow fix in snprintf
- Recode russian docs to utf8

* Tue Jan 15 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3-alt1.cvs.20080110
- Updated to post-2.3-rc1 version, cvs snapshot 20080110
- Add more actual russian translation by Vitaly Lipatov

* Mon Apr 16 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.2.cvs.16042007-alt1
- Updated to post-2.2 version cvs snapshot 16.04.2007

* Fri Oct 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1-alt3
- Fix building with gcc4

* Thu Oct 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- NMU: bug free action
- fix description/summary
- move to Applications/Communications menu group (bug #4405)
- remove minicom -s (root setup) from menu
- add patch from Debian agains unescaped shell exec (#2772)
- update russian translation
- remove old autoconf using (fix some things for it)
- add FAQ translation

* Tue Aug 12 2003 Ivan Zakharyaschev <imz@altlinux.ru> 2.1-alt1
- New upstream version (bug-fix release): 
  + moved URL and source location;
  + redone patch8;
- BuildRequires(build): autoconf = 2.13;

* Sat Oct 20 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt6
- Updated upstream URL and maintainer's email, summary & description.

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.00.0-alt5
- Linked with libtinfo.
- Fixed configure, to allow build with arbitrary lock directory.
- Updated buildrequires.

* Wed Nov 21 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt4
- added another pair of zmodem file transfer methods: they resume an
  interrupted transfer (suggested by goldhead@altlinux.ru).

* Tue Nov 20 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt3
- menu entry for configuration added -- in future it may evolve into
  a consolehelper-assisted utility;
- menu entry fixed: now it should work in all windowing environments
  (added a special script for starting minicom in X);
- small changes in the spec and docs since we are using
  %my_lockdir/ instead of /var/lock/, but not yet
  group serial instead of uucp (actually done in released alt2, ldv).

* Fri Oct  5 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt2
- menu entry changed a bit: to make the terminal not disappear
  immediately (TODO: special error handling and a menu entry for minicom
  configuration)

* Fri Oct  5 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt1
- new version
- try only /dev/modem if no other device specified
  (/dev/modem should be a symbolic link to a real device with modem)
- for packagers:
  + string vulnerability patch merged upstream
  + "config-2" patch repalced by "device-config"
  + "ko" messages thrown away upstream
  + using ./configure (so some patches and environment variables are
    not needed any more)
  + the default configuration files are now taken from the sources
- added translations of the package info (from the original spec)
- icon added (taken from Caldera)

* Thu Aug 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.83.1-ipl10mdk
- Fixed permissions on /etc/minicom* files

* Thu Jun 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.83.1-ipl9mdk
- Added format and permission fixes.

* Thu Mar 09 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl8mdk
- fix SegFault on wide console (> 160)

* Thu Mar 08 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl7mdk
- fix build on glibc 2.2.2
- coment out Russian summary & desrciption

* Thu Feb 01 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl6mdk
- change default serial port setting once more: use /dev/ttyS0 if
  /dev/modem is unavailable

* Thu Feb 01 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl5mdk
- find_lang
- Russian summary and description

* Wed Jan 31 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl4mdk
- security patch from RH (Bill Nottingham <notting@redhat.com>), just in
  case someone will make minicom suid: drop privs on opening of capture file
- config patch changed: the default serial port is /dev/ttyS0
- a stupid doc-file added
- requires: rzsz (to send files)

* Tue Jan 30 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.83.1-ipl3mdk
- Url added
- %_sysconfdir/profile.d/minicom.{csh,sh} -- to enable 8-bit and colour
- empty %_sysconfdir/minirc.dfl
- patch3 to have the "pulse" dialing prefix in newly created
  dial-entries pre-set

* Mon Nov 20 2000 Dmitry V. Levin <ldv@fandra.org> 1.83.1-ipl2mdk
- FHSification.
- Removed suid & sgid bits from %_bindir/%name.

* Wed Jul 05 2000 Dmitry V. Levin <ldv@fandra.org> 1.83.1-ipl1mdk
- RE adaptions.

* Wed Jun 28 2000 Alexandre Dussart <adussart@mandrakesoft.com> 1.83.1-1mdk
- Updated patches(make patch only modify Makefile and install only install.sh)
- 1.83.1

* Mon Mar 27 2000 Daouda Lo <daouda@mandrakesoft.com> 1.82.1-2mdk
- fix group

* Fri Nov 12 1999 Camille Bègnis <camille@mandrakesoft.com>
- restore setgid uucp to permit minicom to lock in /var/lock
- add test for compilation on SMP architectures
- add patch to install.sh to allow installation by non-root users
- modif install section to allow installation by non-root users
- update to 1.82.1

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- fixed bug, changed groups.

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.82 to include i18n fixes

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- Built package for 5.2.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
