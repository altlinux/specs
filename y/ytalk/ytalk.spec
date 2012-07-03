Name: ytalk
Version: 3.3.0
Release: alt1

Summary: A chat program for multiple users
License: GPL
Group: Networking/Chat

Url: http://www.impul.se/ytalk/
Source: %url/ytalk-%version.tar.bz2
Source1: ytalkrc

# Automatically added by buildreq on Fri Feb 10 2006
BuildRequires: libncurses-devel libtinfo-devel

%description
The YTalk program is essentially a chat program for multiple users. YTalk works
just like the UNIX talk program and even communicates with the same talk
daemon(s), but YTalk allows for multiple connections (unlike UNIX talk). YTalk
also supports redirection of program output to other users as well as an
easy-to-use menu of commands.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog
%config %_sysconfdir/ytalkrc
%_bindir/ytalk
%_man1dir/ytalk*

%changelog
* Mon Oct 03 2005 Victor Forsyuk <force@altlinux.ru> 3.3.0-alt1
- New version.
- License now GPL.

* Sun Oct 13 2002 Rider <rider@altlinux.ru> 3.1.1-ipl8mdk
- specfile cleanup
- gcc 3.2 rebuild

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 3.1.1-ipl7mdk
- rebuild

* Sun Jan 28 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> 3.1.1-ipl6mdk
- IPLabs Linux Team adaptations

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.1.1-6mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.1-5mdk
- use new macros
- BM

* Thu Apr 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1.1-4mdk
- new groups
- added url
- added documentation

* Thu Mar 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.1-3mdk
- build for new environment
- clean up spec file by means of spechelper

* Wed Nov 03 1999 Jerome Martin <jerome@mandrakesoft.com>
- Rebuild for new distribution

* Sun Jul 18 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Updated description/summary (fr/de/tr)
- 3.1.1 :
	    + Now looks a bit harder for the fqdn of the current machine.
	    + Fixed problems with ncurses resizing under Linux, and (again) with
	      Ytalk shells under Solaris.
	    + YTalk now complains (and prints the right hostname) if a
	      connection is answered from an unexpected host.
	    + Fixed the checks to prevent user duplication (getting twice the
	      same user in an n-way talk where n>=4).
	    + More portability fixes for 64-bit machines.
	    + Fixed the "readdress" option somewhat.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Nov 22 1998 Preston Brown <pbrown@redhat.com>
- upgrade to ytalk 3.1

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
