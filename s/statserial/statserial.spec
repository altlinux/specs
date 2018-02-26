# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: statserial
Version: 1.1
Release: %branch_release alt2
Epoch: 1

Summary: A tool which displays the status of serial port modem lines.
Summary(ru_RU.KOI8-R): Утилита, отображающая состояние серийных портов
License: %lgpl2plus
Group: Communications

# Source: ftp://ibiblio.org/pub/Linux/system/serial/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-config.patch
Patch1: %name-%version-dev.patch
Patch2: %name-%version--n.patch

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Wed Jan 17 2001
BuildRequires: ncurses-devel

%description
The %name utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines.  Statserial is useful for debugging serial port
and/or modem problems.

Install the %name package if you need a tool to help debug serial
port or modem problems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build

%install
install -p -m755 -D %name %buildroot%_bindir/%name
install -p -m644 -D %name.1 %buildroot%_mandir/man1/%name.1

%files
%doc COPYING
%doc phone_log
%_bindir/*
%_mandir/man?/*

%changelog
* Mon May 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1:1.1-alt2
- Set Epoch: 1

* Thu May 10 2012 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1
- Fixed license
- Ship phone_log script as doc
- Do not specify archaic "-N" anymore for linking
- Fix -n

* Wed Oct 16 2002 Rider <rider@altlinux.ru> 1.1-ipl10mdk
- rebuild (gcc 3.2)
- Russian summary

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.1-ipl9mdk
- rebuild

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 1.1-ipl8mdk
- Changed default device from /dev/cua1 to /dev/ttyS1.
- RE adaptions.

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-8mdk
- BM, spec-helper and macros

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 1.1-7mdk
- added define sections
- fix group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP check/build

* Sun Jul  4 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip manpages

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 13)

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include arch sparc

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
