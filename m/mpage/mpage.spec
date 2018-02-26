Name: mpage
Version: 2.5.4
Release: alt2.0

Summary: A tool for printing multiple pages of text on each printed page
License: GPL
Group: System/Configuration/Printing

Source: http://www.mesa.nl/pub/mpage/%name-%version.tar
Patch: mpage252-config.patch
Patch1: %name-2.5.1-newenc.patch
Patch2: %name-2.5.4-alt-tmpfile.patch
Patch3: mpage-2.5.4-alt-no-japanese.patch
Patch4: mpage-2.5.4-rh-gcc4.patch

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper.  Mpage
is very useful for viewing large printouts without using up tons of
paper.  Mpage supports many different layout options for the printed
pages.

Mpage should be installed if you need a useful utility for viewing
long text documents without wasting paper.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build BINDIR=%_bindir LIBDIR=%_datadir MANDIR=%_mandir/man1 PREFIX=%prefix

%install
make PREFIX=$RPM_BUILD_ROOT%prefix MANDIR=$RPM_BUILD_ROOT%_mandir/man1 install

%files
%doc CHANGES Copyright README NEWS TODO
%_bindir/*
%_mandir/man?/*
%_datadir/%name

%changelog
* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.4-alt2.0
- Automated rebuild.

* Tue May 16 2006 Stanislav Ievlev <inger@altlinux.org> 2.5.4-alt2
- fixed build with gcc4
- build from git

* Thu Apr 14 2005 Stanislav Ievlev <inger@altlinux.org> 2.5.4-alt1
- 2.5.4
  japanese fonts turned off, 'cause they was hardcoded

* Wed Oct 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.3-alt1
- 2.5.3
- it's now gpl

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.2-alt2
- rebuild with gcc3

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-ipl14mdk
- Rebuilt
- Added normal tmpdir support

* Thu Nov 16 2000 AEN <aen@logic.ru>
- KOI8-{R,U}, CP1251, PT154 support

* Fri Jul 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.5.1-12mdk
- BM + macroszification
- clean spec

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 2.5.1-11mdk
- relocate to group Networking/File transfer

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build release.

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 2.5.1
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- changed group

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- 6.0 build stuff.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 15 1997 Michael Fulbright <msf@redhat.com>
- (Re)applied patch to correctly print dvips output.

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
