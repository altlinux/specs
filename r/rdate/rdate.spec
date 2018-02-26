Name: rdate
Version: 1.4
Release: alt5

Summary: Tool for retrieving the date/time from another machine on your network
Summary(ru_RU.KOI8-R): Программа для чтения удалённых часов и установки по ним местных

Packager: Stanislav Yadykin <tosick@altlinux.ru>

License: GPL
Group: System/Servers
Url: http://directory.fsf.org/sysadmin/remote/rdate.html

Source: ftp://people.redhat.com/sopwith/%name-%version.tar.bz2

%description
The %name utility retrieves the date and time from another machine
on your network, using the protocol described in RFC 868.  If you
run %name as root, it will set your machine's local time to the time
of the machine that you queried.  Note that %name isn't scrupulously
accurate.  If you are worried about milliseconds, get the ntp
package instead.
You need install xinetd and run 'chkconfig time-udp on' on time server.

%description -l ru_RU.KOI8-R
Утилита rdate считывает дату и время с другой машины сети,
используя протокол, описанный в RFC 868. Если вы запускаете rdate от
пользователя root, она также может установить время на локальной
машине в соответствии со временем на удалённой машине. Имейте в виду,
что rdate не отличается особенной точностью; если вы заботитесь о
миллисекундах, установите пакет ntp, использующий ntpd.
На сервере времени вам потребуется установить xinetd и
запустить 'chkconfig time-udp on'.

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -D_GNU_SOURCE %name.c -o %name

%install
install -p -m755 -D %name %buildroot%_bindir/%name
install -p -m644 -D %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Sep 22 2006 Stanislav Yadykin <tosick@altlinux.ru> 1.4-alt5
- fixed summary encoding

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt3
- NMU: spec fixes again
- add Packager
- fix name of ntp package in descriptions
- add info about server setup in descriptions

* Thu Jan 26 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt2
- NMU: spec fixes: add Url, change Source, some cleanup
- add russian summary & description (from PLD)

* Wed Aug 18 2004 Stanislav Yadykin <tosick@altlinux.ru> 1.4-alt1
- build with 1.4

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.0-ipl4mdk
- rebuild

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl3mdk
- Merged RH patches.
- RE adaptions.

* Wed Jul 26 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-3mdk
- change copyright to public domain

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-2mdk
- BM
- use new macros
- let spec-helper compress man-pages and strip binaries : i'm getting bored
  to do a mdk7.1 job :-(

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.0-1mdk
- updated 1.0
- changed group to new groups

* Fri Feb 04 2000 Elliot Lee <sopwith@redhat.com>
- Rewrite the stinking thing due to license worries (bug #8619)

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 8)

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed the url to the source

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
