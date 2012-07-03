Name: scmxx
Version: 0.9.0
Release: alt2

Epoch: 20030703

Summary: Exchange data with Siemens mobile phones
License: GPL
Group: Communications

Url: http://www.hendrik-sattler.de/scmxx
Source0: %name-%version.tar.bz2
Source1: scm2tex.pl.txt

Patch0: scmxx-0.9.0-alt-scmxx_tty.patch

Autoreq: yes, noperl

%description
SCMxx is a console program that allows you to exchange certain types of
data with mobile phones made by Siemens. Some of the data types that can
be exchanged are logos, ring tones, vCalendars, phonebook entries, and
SMS messages.

It works with the following models:
 S25,
 S35i, M35i and C35i,
 SL4x, S45, ME45 and C45
and probably others.

It basically uses the AT command set published by Siemens
(with some other, additional resources).

%prep
%setup -q

%patch0 -p1

%build
%configure \
	--with-device=/dev/ircomm1
%make_build

%install
%make DESTDIR=%buildroot install
%__install -pD -m755 %SOURCE1 contrib/scm2tex.pl

iconv -futf-8 -tkoi8-r docs/scmxx.ru.1 > %buildroot%_mandir/ru/man1/scmxx.1

%find_lang %name

%files -f %name.lang
%doc contrib/ BUGS README TODO AUTHORS CHANGELOG examples docs/*.txt
%_bindir/*
%_man1dir/*
%_mandir/ru/man1/*

%changelog
* Wed Jun 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 20030703:0.9.0-alt2
- fixed #9676

* Thu Mar 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 20030703:0.9.0-alt1
- 0.9.0

* Mon Aug 09 2004 Gor <vg@altlinux.ru> 20030703:0.7.3-alt1
- New version

* Mon Jun 14 2004 Gor <vg@altlinux.ru> 20030703:0.7.1-alt1
- New version

* Mon Apr 19 2004 Gor <vg@altlinux.ru> 20030703:0.7.0-alt1
- New version

* Thu Dec 18 2003 Gor <vg@altlinux.ru> 20030703:0.6.4-alt1
- build new version

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 20030703:0.6.3.8-alt1
- 0.6.3.8 appears to be 'newer and better' than 0.6.4rc
- added retval patch and Russian manpage from ASPLinux
  (thanks to Andy Shevchenko)
- scm2tex.pl put to doc/contrib.  Hmm... may be controversial :)

* Wed Mar 26 2003 Michael Shigorin <mike@altlinux.ru> 0.6.4-alt0.4
- 0.6.4-rc4

* Sat Mar 01 2003 Michael Shigorin <mike@altlinux.ru> 0.6.3.3-alt0.1
- built for ALT Linux

* Mon Nov 18 2002 Hendrik Sattler <post@hendrik-sattler.de>
- added manpage to package

* Sat Jul 1 2002 Hendrik Sattler <post@hendrik-sattler.de>
- changed defattr, so dirs get their x-flag

* Sat May 14 2002 Hendrik Sattler <post@hendrik-sattler.de>
- extensive usage of environment variables in the spec file
- moved/renamed files in docdir

* Sat Feb 9 2002 Petr Kri¹tof <Petr@Kristof.cz>
- RPM spec update

* Sat Nov 17 2001 Hendrik Sattler <post@hendrik-sattler.de>
- Initial RPM release
