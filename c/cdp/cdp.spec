Name: cdp
Version: 0.33
Release: alt3
Epoch: 1

Summary: An interactive text-mode program for controlling audio CD-ROMs
License: GPLv2+
Group: Sound
Url: https://sourceforge.net/projects/cdp/

Source: ftp://ibiblio.org/pub/Linux/apps/sound/cdrom/curses/cdp-%version.tar

Patch0: cdp-0.33-rh-fsstnd.patch
Patch1: cdp-0.33-rh-cdplay.patch
Patch2: cdp-0.33-rh-ncurses.patch
Patch3: cdp-0.33-rh-glibc.patch
Patch4: cdp-0.33-rh-changer.patch
Patch5: cdp-0.33-rh-keys.patch

BuildRequires: libncurses-devel

%description
The cdp program plays audio CDs in your computer's CD-ROM drive.
Cdp includes a full-screen interface version and a command line
version.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

make clean
sed -i 's/ getline/ get_line/g' getline.* display.c

%build
%make_build COMP_OPT="%optflags" cdp

%install
install -Dpm755 cdp %buildroot%_bindir/cdp
install -Dpm644 cdp.1 %buildroot%_man1dir/cdp.1
ln -s cdp %buildroot%_bindir/cdplay

%files
%_bindir/*
%_mandir/man?/*
%doc ChangeLog README

%changelog
* Thu Jul 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1:0.33-alt3
- Fixed build with fresh toolchain.

* Fri Aug 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1:0.33-alt2
- Resurrected cdplay (#12520).

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.33-alt1
- Package cleanup.

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 0.33-ipl11mdk
- rebuild with gcc3

* Fri Mar 29 2002 Stanislav Ievlev <inger@altlinux.ru> 0.33-ipl10mdk
- removed my buggy patch

* Wed Mar 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.33-ipl9mdk
- Rebuilt

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 0.33-ipl8mdk
- Cleaned up patches.
- Automatically added BuildRequires.

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 0.33-ipl7mdk
- RE adaptions.

* Fri Mar 24 2000 Warly <warly@mandrakesoft.com> 0.33-7mdk
- new group
- spechelper

* Mon Nov 22 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- cdchanger patch, %%patch & Patch sux (rh#2735), segfault of improper keypress

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable sane SMP building

* Sat Oct 16 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix incorrect Path in patch #2 (cdp-0.33-ncurses.patch)

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- changed group, this app will never be updated.

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- not sure if this package will ever be updated.
- rebuilt for 6.0

* Sat Aug 15 1998 Jeff Johnson
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
