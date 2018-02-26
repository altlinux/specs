Name: pngcrush
Version: 1.6.4
Release: alt1

Summary: Utility to compress PNG files
License: BSD-like
Group: Graphics
Url: http://pmt.sourceforge.net/pngcrush/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: pngcrush-%version.tar

BuildPreReq: libpng-devel

%description
Pngcrush is an optimizer for PNG (Portable Network Graphics) files.
Its main purpose is to reduce the size of the PNG IDAT data stream by
trying various compression levels and PNG filter methods.  It also can
be used to remove unwanted ancillary chunks, or to add certain chunks
including gAMA, tRNS, and textual chunks.

%prep
%setup -q

%build
%__cc pngcrush.c -lpng -o pngcrush %optflags -I. \
	-DPNG_INTERNAL -DPNG_USE_LOCAL_ARRAYS -DPNG_USE_PNGGCCRD \
	-DGAS_VERSION="\"$(as --version |grep 'GNU assembler' |sed -e 's/GNU assembler //' -e 's/ .*//')\""

%install
install -Dpm755 pngcrush %buildroot%_bindir/pngcrush

%files
%_bindir/*
%doc ChangeLog.txt

%changelog
* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1.6.4-alt1
- Updated to 1.6.4.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1.5.10-alt3
- Fixed build with --as-needed.

* Mon Oct 18 2004 Dmitry V. Levin <ldv@altlinux.org> 1.5.10-alt2
- Fixed build with libpng-devel >= 1.2.6.

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5.10-alt1
- 1.5.10

* Wed Feb 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.5.8-alt2
- Link with system zlib anf libpng (needs testing).
- Corrected license information.

* Fri Dec 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.5.8-alt1
- 1.5.8

* Wed Oct 10 2001 Rider <rider@altlinux.ru> 1.5.7-alt1
- 1.5.7

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 1.5.6-alt1
- 1.5.6

* Fri Jan 26 2001 Dmitry V. Levin <ldv@fandra.org> 1.5.3-ipl2mdk
- RE adaptions.

* Wed Jan 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5.3-2mdk
- rebuild

* Mon Dec 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.5.3-1mdk
- updated to 1.5.3

* Thu Sep 14 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.5.1-1mdk
- v1.5.1
- BM
- macros

* Mon May 15 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.4.3-1mdk
- v1.4.3

* Tue Jan 25 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Dara Hazeghi <dhazegi@pacbell.net>
