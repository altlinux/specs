Name: psutils
Version: p17
Release: alt2
Epoch: 1

Summary: PostScript utilities
License: freeware
Group: Publishing

Source0: http://www.ctan.org/tex-archive/support/psutils/%name-%version.tar.gz
Patch0: psutils-make.patch
Patch1: psutils-maketext.patch
Patch2: psutils-p17-paper.patch
Patch3: psutils-manpage.patch
Patch4: psutils-flip.patch
Packager: Fr. Br. George <george@altlinux.ru>

%description
psutils contains some utilities for manipulating PostScript documents.
Page selections and rearrangement are supported, including arrengement
into signatures for booklet printing, and page merging for n-up printing.

%prep
%setup -n psutils
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make -f Makefile.unix RPM_OPT_FLAGS="%optflags" \
	BUILDROOT="%buildroot" PERL=/usr/bin/perl

%install
mkdir -p %buildroot/usr/{bin,share/{man,psutils}}
make -f Makefile.unix install BUILDROOT="%buildroot"

%files
%doc LICENSE README
%_bindir/*
%_datadir/psutils
%_man1dir/*

%changelog
* Wed Feb 27 2008 Fr. Br. George <george@altlinux.ru> 1:p17-alt2
- Pageflip patch

* Tue Feb 19 2008 Victor Forsyuk <force@altlinux.org> 1:p17-alt1
- Rebuild with 'alt' release prefix due to deprecation of ipl* releases.

* Wed Mar 02 2005 Victor Forsyuk <force@altlinux.ru> p17-ipl10mdk
- Manpage correction for psresize (Fedora).
- Support getting paper size from current locale (Fedora).

* Sat Oct 05 2002 Rider <rider@altlinux.ru> p17-ipl9mdk
- rebuild (gcc 3.2)
- specfile cleanup

* Mon Apr 15 2002 Rider <rider@altlinux.ru> p17-ipl8mdk
- rebuild

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Aug 30 2000 Etienne Faure <etienne@mandrakesoft.com> p17-6mdk
- rebuilt with new %%doc and _mandir macro

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> p17-5mdk
- Fix bad tag value.
- Fix ownership.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> p17-4mdk
- Fix group.

* Fri Nov 12 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- Rebuilt for Oxygen.

* Fri Aug 27 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- Ajusted perl path in scripts.

* Fri Aug 13 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
