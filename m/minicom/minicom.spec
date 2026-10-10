%define my_lockdir /var/lock/serial
%define my_group uucp

Name: minicom
Version: 2.11.1
Release: alt1

Group: Communications
Summary: A text-menu-driven modem control and terminal emulation program
# Some files are built from Public Domain files in addition to GPLv2+ files
# (/usr/bin/minicom). Some LGPLv2+ files *may* be used in building of certain
# files (minicom, ascii-xfr, runscript). They are probably not actually used,
# but I wasn't able to exclude them from the build process completely yet.
# The rest is simply GPLv2+.
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Unlicense
URL: http://alioth.debian.org/projects/minicom/
VCS: https://salsa.debian.org/minicom-team/minicom.git

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

# I add the specialization of the BuildRequires:
BuildRequires: bison libtinfo-devel

# The access to serial ports should be controlled through '%my_group'
# group. It is provided by the new setup pkg.
# We need it before this package (minicom) is installed in order
# to set right permissions on files.
# Also, we need the place to create lockfiles. It should be
# provided by te new FS pkg.
Requires(pre): %my_lockdir

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
%autopatch -p1

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

# The script to start minicom in an X terminal
#install -pD -m755 %SOURCE7 %buildroot%_libdir/%name/xstart

%files -f %name.lang
%attr(640,root,%my_group) %config(noreplace) %_sysconfdir/minirc.dfl
%attr(755,root,root) %config %_sysconfdir/profile.d/%name.sh
%attr(755,root,root) %config %_sysconfdir/profile.d/%name.csh
%_bindir/*
%_mandir/man?/*

#dir %_libdir/%name
#attr(755,root,root) %_libdir/%name/xstart

%doc doc extras
%doc %name.admin
%lang(ru) %doc %name.admin.ru
%lang(ru) %doc %name.FAQ.ru

%changelog
* Sat Oct 10 2026 Anton Midyukov <antohami@altlinux.org> 2.11.1-alt1
- New version 2.11.1 (Closes: 60881).
- Cleanup Changelog.

* Wed Sep 16 2026 Anton Midyukov <antohami@altlinux.org> 2.8-alt2
- Remove minicom.desktop (Closes: 60561, 60562).
- Convert License to SPDX format.

* Mon Aug 14 2023 Anton Midyukov <antohami@altlinux.org> 2.8-alt1
- new version 2.8

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.7.1-alt2
- Added upstream patchs
- Fix License Tag

* Sat Sep 02 2017 Anton Midyukov <antohami@altlinux.org> 2.7.1-alt1
- New version 2.7.1
- Fix desktop files.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.hg.qa2
- Fixed build

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.hg.qa1
- NMU: rebuilt for updated dependencies.

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

* Sun Oct 20 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2.00.0-alt6
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
