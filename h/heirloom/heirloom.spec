Name: heirloom
Version: 070715
Release: alt2

Summary: Traditional implementations of standard Unix utilities
License: Various, see LICENSE dir
Group: System/Base

Url: http://heirloom.sf.net/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-070715-man-default.patch

BuildPreReq: bc bzlib-devel flex libncurses-devel zlib-devel

Autoreq: yes, noshell

%define basedir %_libexecdir/%name
%define defbin %basedir/bin
%define makeoptions \\\
	DEFBIN=%defbin \\\
	SV3BIN=%defbin \\\
	S42BIN=%defbin/s42 \\\
	SUSBIN=%defbin/posix \\\
	SU3BIN=%defbin/posix2001 \\\
	UCBBIN=%basedir/ucb \\\
	CCSBIN=%basedir/ccs/bin \\\
	DEFLIB=%basedir/lib \\\
	DEFSBIN=%basedir/sbin \\\
	DFLDIR=%_sysconfdir/%name-default \\\
	SULOG=%_logdir/%name-sulog \\\
	SPELLHIST=/dev/null \\\
	ROOT=%buildroot \\\
	LIBZ=-lz \\\
	LIBBZ2=-lbz2 \\\
	USE_BZLIB=1 \\\
	TTYGRP= \\\
	CFLAGS="%optflags" \\\
	CFLAGS2="%optflags" \\\
	CFLAGSS="%optflags" \\\
	CFLAGSU="%optflags"


%description
The Heirloom Toolchest is a collection of standard Unix utilities. Highlights
are:
* Derived from original Unix material released as open source by Caldera.
* Up to four versions of each utility corresponding to SVID3/SVR4,
  SVID4/SVR4.2, POSIX.2/SUSV2, and 4BSD (SVR4 /usr/ucb).
* Support for lines of arbitrary length and in many cases binary input data.
* Support for multibyte character sets, especially UTF-8.
* More than 100 individual utilities including bc, cpio, diff, ed, file,
  find, grep, man, nawk, oawk, pax, ps, sed, sort, spell, and tar.
* The cpio and pax utilities can read and write zip files, GNU tar files,
  and the cpio formats of several commercial Unix systems.
* Extensive documentation including a manual page for any utility.


%prep
%setup
%patch0 -p1
%__subst '/stropts.h/d' shl/shl.c

%build
%make_build %makeoptions
mkdir _doc
find . -depth -name NOTES -print0 | cpio -pdm0 _doc

%install
%makeinstall %makeoptions
rm -f %buildroot%basedir/ucb/{prt,sccs}
rm -f %buildroot/dev/null

%files
%doc CHANGES README LICENSE/ _doc/*
%basedir/
%dir %_sysconfdir/%name-default/
%config(noreplace) %_sysconfdir/%name-default/*
%_logdir/%name-sulog
%_mandir/5man/

%exclude %defbin/shl
%attr(-,root,utmp) %defbin/shl


%changelog
* Wed Apr 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 070715-alt2
- mark /etc/heirloom-default as config(noreplace)
- sync /etc/heirloom-default/man with heirloom-doctools README, to use
  the tools from that package by default

* Mon Mar 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 070715-alt1
- initial build
