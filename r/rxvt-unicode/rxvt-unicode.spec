Name: rxvt-unicode
Version: 9.15
Release: alt1

Summary:  rxvt-unicode is a clone of the well known terminal emulator rxvt
License: GPL
Group: Terminals
Url: http://software.schmorp.de/pkg/rxvt-unicode.html
Packager: Alexey Gladkov <legion@altlinux.ru>

AutoReq: yes, noperl

# due to TERM=rxvt-unicode-256color
Requires: terminfo-extra >= 5.7-alt3.1

Provides: urxvt, xvt

Source: http://dist.schmorp.de/%name/%name-%version.tar.bz2
Source1: %name.alternatives
Source2: %name.desktop

Patch0:	rxvt-unicode-alt-remove-tic.patch
Patch1:	rxvt-unicode-alt-change-cutchars.patch

# Automatically added by buildreq on Mon May 14 2007
BuildRequires: gcc-c++ imake libICE-devel libXft-devel libXpm-devel perl-devel xorg-cf-files
BuildRequires: alternatives

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
	--enable-everything \
	--enable-256-color \
	#
%make_build

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

%__install -pD -m644 %SOURCE1 %buildroot/%_altdir/%name
%__install -pD -m644 %SOURCE2 %buildroot/%_desktopdir/%name.desktop

%files
%doc README.FAQ INSTALL doc/README.xvt doc/etc
%_bindir/*
%_altdir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_man3dir/*
%_man7dir/*
%_libdir/urxvt/

%changelog
* Thu May 31 2012 Alexey Gladkov <legion@altlinux.ru> 9.15-alt1
- New release (9.15).

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 9.10-alt1.1
- rebuilt for perl-5.14

* Mon Dec 20 2010 Alexey Gladkov <legion@altlinux.ru> 9.10-alt1
- New release (9.10).

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 9.09-alt2.20100823.1
- rebuilt with perl 5.12

* Sat Aug 28 2010 Alexey Gladkov <legion@altlinux.ru> 9.09-alt2.20100823
- Fix requires (ALT#23982).
- Add provides (ALT#10488, ALT#23969).

* Mon Aug 23 2010 Alexey Gladkov <legion@altlinux.ru> 9.09-alt1.20100823
- New snapshot (9.09 20100823)
- Add ':' (colon) to default CUTCHARS (ALT#23929).
- Change $TERM to rxvt-unicode-256color in 256-color mode (ALT#23928).

* Sat Jan 02 2010 Alexey Gladkov <legion@altlinux.ru> 9.07-alt1
- New version (9.07).

* Mon May 25 2009 Alexey Gladkov <legion@altlinux.ru> 9.06-alt2
- Fix type conversion.
- Remove obsolete macro.

* Sat Nov 08 2008 Alexey Gladkov <legion@altlinux.ru> 9.06-alt1
- New version (9.06).

* Tue Mar 04 2008 Alexey Gladkov <legion@altlinux.ru> 9.02-alt1
- New version (9.02).

* Mon Jan 28 2008 Alexey Gladkov <legion@altlinux.ru> 9.0-alt1
- New version (9.0).

* Wed Jan 02 2008 Alexey Gladkov <legion@altlinux.ru> 8.9-alt1
- New version (8.9).

* Wed Oct 31 2007 Alexey Gladkov <legion@altlinux.ru> 8.4-alt1
- New version (8.4).

* Wed Sep 05 2007 Alexey Gladkov <legion@altlinux.ru> 8.3-alt1
- New version (8.3).
- Add desktop file.
- Add alternatives.

* Mon May 21 2007 Alexey Gladkov <legion@altlinux.ru> 8.2-alt3
- Remove termutils-devel from Buildrequires.

* Mon May 14 2007 Alexey Gladkov <legion@altlinux.ru> 8.2-alt2
- Update Buildrequires.
- Move terminfo/r/rxvt-unicode to terminfo-5.6-alt3.

* Sat Apr 28 2007 Alexey Gladkov <legion@altlinux.ru> 8.2-alt1
- new version (8.2)

* Sun Dec 10 2006 Alexey Voinov <voins@altlinux.ru> 8.1-alt1
- new version (8.1)

* Sun Nov 12 2006 Alexey Voinov <voins@altlinux.ru> 8.0-alt1
- new version (8.0)
- perl enabled [#10233]
- buildreqs updated

* Sat Sep 16 2006 Alexey Voinov <voins@altlinux.ru> 7.9-alt1
- new version (7.9)
- url updated

* Sun Jan 08 2006 Alexey Voinov <voins@altlinux.ru> 6.3-alt1
- new version (6.3)

* Thu Nov 03 2005 Alexey Voinov <voins@altlinux.ru> 5.8-alt1
- new version (5.8)

* Sun Apr 24 2005 Alexey Voinov <voins@altlinux.ru> 5.5-alt1
- new version (5.5)

* Mon Apr 18 2005 Alexey Voinov <voins@altlinux.ru> 5.4-alt1
- new version (5.4)

* Sun Mar 13 2005 Alexey Voinov <voins@altlinux.ru> 5.3-alt1
- new version (5.3)

* Tue Feb 22 2005 Alexey Voinov <voins@altlinux.ru> 5.2-alt1
- new version (5.2)

* Fri Feb 04 2005 Alexey Voinov <voins@altlinux.ru> 4.9-alt1
- new version (4.9)

* Tue Jan 18 2005 Alexey Voinov <voins@altlinux.ru> 4.8-alt1
- new version (4.8)

* Thu Dec 30 2004 Alexey Voinov <voins@altlinux.ru> 4.7-alt1
- new version (4.7)

* Thu Dec 16 2004 Alexey Voinov <voins@altlinux.ru> 4.6-alt1
- new version (4.6)

* Tue Dec 14 2004 Alexey Voinov <voins@altlinux.ru> 4.5-alt1
- new version (4.5)

* Mon Oct 11 2004 Alexey Voinov <voins@altlinux.ru> 4.0-alt1
- initial build
