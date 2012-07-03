Name: mailcap
Version: 2.1.23
Release: alt2

Summary: Associates helper applications with particular file types
License: Public domain
Group: System/Configuration/Networking

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.

Mailcap should be installed to allow certain programs to be able to
handle non-text files.

%prep
%setup
%patch -p1

%build

%install
mkdir -p %buildroot{%_sysconfdir,%_man4dir}
install -pm644 mailcap mime.types %buildroot%_sysconfdir
install -pm644 mailcap.4 %buildroot%_man4dir

%files
%_sysconfdir/*
%_man4dir/*

%changelog
* Fri Apr 22 2011 Michael Shigorin <mike@altlinux.org> 2.1.23-alt2
- added text/x-patch to /etc/mime.types (closes: #25498)

* Wed Dec 13 2006 Michael Shigorin <mike@altlinux.org> 2.1.23-alt1
- 2.1.23 (sync with FC6)
- License: s/GPL/Public domain/ according to FC spec
- spec cleanup
- fix macro use in ancient RH changelog

* Fri Nov 22 2002 Kachalov Anton <mouse@altlinux.ru> 2.1.12-alt1
- sync with RH version
- use xine instead gtv & xanim
- use gqview instead eog
- use links instead htmlview
- use url_handler.sh instead netscape

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.3-ipl1
- RE adaptions.

* Thu Jan 18 2001 Bill Nottingham <notting@redhat.com>
- use gpg, not pgp (#13816, others)

* Sat Jan  6 2001 Bill Nottingham <notting@redhat.com>
- fix typo (#23409)

* Thu Dec 28 2000 Bill Nottingham <notting@redhat.com>
- reintegrate stuff into the package so it doesn't get lost 

* Thu Dec 28 2000 Than Ngo <than@redhat.com>
- add ms(TM) word document entry (Bug #17474)
- bzip2 sources

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- add wap entries

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- remove mailcap.vga

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Tue Jan 18 2000 Bill Nottingham <notting@redhat.com>
- add .bz2

* Thu Jan 13 2000 Bill Nottingham <notting@redhat.com>
- add tgz/gz to gzip

* Thu Jun 16 1999 Bill Nottingham <notting@redhat.com>
- rpm files are RPM files. :)

* Sat May 15 1999 Jeff Johnson <jbj@redhat.com>
- fix typo in pdf entry (#2618).

* Mon Mar 29 1999 Bill Nottingham <notting@redhat.com>
- comment out play

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- updated mime type for images from xv to ee
- cleaned up for our new version of the package which is in CVS

* Sat Mar 13 1999 Matt Wilson <msw@redhat.com>
- updated mime.types

* Fri Feb 12 1999 Bill Nottingham <notting@redhat.com>
- comment out backticked %%variables to work around security problems

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- glibc version 2.1

* Mon Sep 21 1998 Bill Nottingham <notting@redhat.com>
- we don't ship tracker, use mikmod instead

* Wed Jul 29 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- added /etc/mime.types from mutt to this package to make it universal

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
