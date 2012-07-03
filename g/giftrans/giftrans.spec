Name: giftrans
Version: 1.12.2
Release: alt1
Epoch: 1
Packager: Dmitry V. Levin <ldv@altlinux.org>

Summary: A program for making transparent GIFs from non-transparent GIFs
License: GPLv2+
Group: Graphics
# ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/giftrans-%version.tar.bz2
Source: giftrans-%version.tar
Patch: giftrans-1.12.2-deb-alt.patch

%description
This packages contains the giftrans utility, which allows for setting
the transparent or background color, changing colors, adding or removing
comments.

%prep
%setup
%patch -p1

%build
%__cc %optflags -o giftrans giftrans.c

%install
mkdir -p %buildroot/{%_bindir,%_man1dir}
install -pm755 giftrans %buildroot%_bindir/
install -pm644 giftrans.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.12.2-alt1
- Merged fixes from Debian giftrans package.
- Updated release numbering.

* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.12.2-ipl12mdk
- rebuild

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1.12.2-ipl11mdk
- fix bug #0000301

* Tue Dec 19 2000 AEN <aen@logic.ru>
- adopted for RE

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.12.2-9mdk
- use new macros
- BM

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.12.2-8mdk

- Rebuilt on kenobi

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com> 1.2.12-7mdk

- Spec file cleanup
- Changed group to match those of 7.1
- Let spec-helper do its job

* Thu Nov 04 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release
- Fixed defattrs

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>

- udpated version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>

- built against glibc
