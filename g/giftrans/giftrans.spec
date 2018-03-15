Name: giftrans
Version: 1.12.2
Release: alt2.1
Epoch: 1

Summary: A program for making transparent GIFs from non-transparent GIFs
License: GPLv2+
Group: Graphics
Url:	ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/
# ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/giftrans-%version.tar.bz2
Source: giftrans-%version.tar
Patch01: 01_relocate_rgb.diff
Patch10: 10_local_colour_tables.diff
Patch11: 11_ignore_comments.diff
Patch12: 12_initialise_gct_size.diff
Patch20: 20_manpage_escape_warning.diff
Patch21: 21_manpage_hyphens.diff
Patch22: 22_manpage_remove_distribution_section.diff
Patch23: 23_manpage_additional_credentials.diff

%description
This packages contains the giftrans utility, which allows for setting
a specific transparent or background color of GIF images as well as
changing colors, adding or removing comments; it also provides the
ability to analyze GIF contents.

%prep
%setup
%patch01 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%build
%__cc %optflags $(getconf LFS_CFLAGS) -o giftrans giftrans.c

%install
mkdir -p %buildroot/{%_bindir,%_man1dir}
install -pm755 giftrans %buildroot%_bindir/
install -pm644 giftrans.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.12.2-alt2.1
- NMU: added URL

* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 1:1.12.2-alt2
- Updated Debian patches.
- Built with LFS support enabled.

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
