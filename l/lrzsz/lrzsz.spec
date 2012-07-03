Name: lrzsz
Version: 0.12.20
Release: alt1
Epoch: 1

Summary: Programs for communicating over Z-, Y- & X-modem protocols.
License: GPL
Group: Communications

Url: http://www.ohse.de/uwe/software/%name.html
Source: http://www.ohse.de/uwe/releases/%name-%version.tar.bz2
Patch: %name-%version-glibc21.patch.bz2
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Программы для передачи данных по протоколам Z-, Y- & X- modem.

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of the
rzsz package.  Lrzsz was created to provide a working GNU copylefted
Zmodem solution for Linux systems.

Under certain circumstances, Zmodem is the main protocol that is used to 
transfer files.

You should install %name if you're also installing a Zmodem communications
program that uses it. Minicom is an example of such a program.

%description -l ru_RU.KOI8-R
Пакет %name (состоящий из lrz и lsz) вносит косметические улучшения в пакет 
zmodem/ymodem/xmodem, построенный на основе public-domain версии пакета 
rzsz. 

В некоторых условиях Zmodem становится основным протоколом, который 
используется для передачи файлов.

Стоит поставить %name, если Вы устанавливаете программу, которая его 
использует. Minicom -- пример такой программы.

%prep
%setup
%patch -p1 -b .glibc21

%build
%configure \
	--disable-pubdir \
	--enable-syslog \
	--program-transform-name=s/l//
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*

%changelog
* Mon May 26 2008 Michael Shigorin <mike@altlinux.org> 1:0.12.20-alt1
- adopt/cleanup/rebuild

* Wed Apr 18 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.12.20-ipl12mdk.0
- Automated rebuild.

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 0.12.20-ipl12mdk
- rebuild

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 0.12.20-ipl11mdk
- rebuild

* Wed Jan 31 2001 Ivan Z. <vanyaz@mccme.ru> 0.12.20-ipl10mdk
- no LDFLAGS for stripping (stripping is done automatically)
- Russian translations

* Wed Jan 31 2001 Ivan Z. <vanyaz@mccme.ru> 0.12.20-ipl9mdk
- new homepage & source locations
- more macros, spec clean up
- provides: rzsz

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Nov 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.12.20-7mdk
- more macros
- build for gcc-2.96

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.12.20-6mdk
- BM

* Mon Apr 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.12.20-5mdk
- spechelper fixes
- group fix

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 0.12.20, i18n translations included.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- Upgraded to 0.12.14 and changed makefiles so gettext isnt built.
