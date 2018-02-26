Name: talk
Version: 0.17
Release: alt3
Serial: 1

Summary: Talk client for one-on-one Internet chatting
License: BSD
Group: Networking/Chat
Summary(ru_RU.KOI8-R): Клиентская программа для частных разговоров
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: ftp://ftp.ibiblio.org/pub/Linux/system/network/chat/netkit-ntalk-%version.tar.bz2
Source1: ntalk.xinetd
Patch1: ntalk-0.17-alt-build.patch
Patch2: ntalk-0.17-alt-defaults.patch
Patch3: ntalk-0.17-slackware-alt-talkd.patch
Patch4: ntalk-0.17-alt-fixes.patch
Patch5: ntalk-0.17-rh-talk-SO_BSDCOMPAT.patch
Patch6: ntalk-0.17-rh-talk-resize.patch
Patch7: ntalk-0.17-rh-i18n.patch

Obsoletes: ntalk
Provides: ntalk
BuildRequires: libncursesw-devel

%package server
Summary: talk server for the talk program
Summary(ru_RU.KOI8-R): Сервер для частных разговоров
Group: System/Servers
PreReq: shadow-utils
Obsoletes: ntalk

%description
This package provides client and daemon programs for the
Internet talk protocol, which allows you to chat with other users
on different systems.  Talk is a communication program which copies
lines from one terminal to the terminal of another user.

%description -l ru_RU.KOI8-R
Этот пакет содержит клиентскую программу для общения через протокол
talk, который позволяет вам общаться с другими пользователями на вашей
или другой системе.  Talk - это коммуникационная программа, копирующая
строки с терминала на терминал другого пользователя.

%description server
This is the talk server.

%description -l ru_RU.KOI8-R server
Этот пакет содержит сервер talk.

%prep
%setup -q -n netkit-ntalk-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%__subst s/ncurses/ncursesw/g configure

%build
%add_optflags -D_GNU_SOURCE -Werror
CFLAGS="%optflags" ./configure
%make_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_mandir/man{1,8}}

%make_install install INSTALLROOT=%buildroot MANDIR=%_mandir
ln -snf in.ntalkd.8 %buildroot%_man8dir/talkd.8
install -pD -m640 %_sourcedir/ntalk.xinetd %buildroot/etc/xinetd.d/ntalk
chmod 711 %buildroot%_sbindir/*

%post server
/usr/sbin/useradd -r -g tty -d / -s /dev/null -n %name >/dev/null 2>&1 ||:

%files
%_bindir/*
%_man1dir/*
%doc README BUGS ChangeLog

%files server
%_sbindir/*
%_man8dir/*
%config(noreplace) %attr(0640,root,wheel) %_sysconfdir/xinetd.d/*
%doc README BUGS ChangeLog

%changelog
* Sun Nov 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.17-alt3
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.
- Fixed a few fd leaks on error path.
- Made xinetd config readable for wheel group.
- Linked talk client with -lncursesw.
- Imported RH patch to avoid using deprecated SO_BSDCOMPAT.
- Imported RH patch to fix spurious 0x9a ("^Z") on window resize.
- Imported RH patch to handle UTF-8 input.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1:0.17-alt2
- talkd: Fixed potential DoS, based on patch from Mauro Persano.

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1:0.17-alt1
- Specfile cleanup.
- Fixed build with -Werror.
- Updated build dependencies.

* Tue Oct 15 2002 Rider <rider@altlinux.ru> 0.17-ipl5mdk
- patch for default hostname on talk client
- russian summary and description

* Fri Sep 27 2002 Rider <rider@altlinux.ru> 0.17-ipl4mdk
- rebuild

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.17-ipl3mdk
- Fixed build with glibc-2.2.2.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl2mdk
- Updated xinet support.

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl1mdk
- 0.17
- Dropped inetd support, rewritten xinetd support.

* Wed Sep 28 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- update to multi-homed 0.11 version.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
