Name: pngcrush
Version: 1.8.13
Release: alt2

Summary: Optimizer for PNG (Portable Network Graphics) files
License: zlib
Group: Graphics
Url: https://pmt.sourceforge.net/pngcrush/

# http://download.sourceforge.net/pmt/%name-%version.tar.xz

Source: %name-%version.tar

BuildPreReq: libpng-devel libcrc32c-devel

%description
Pngcrush is a commandline optimizer for PNG (Portable Network Graphics)
files.  Its main purpose is to reduce the size of the PNG IDAT data
stream by trying various compression levels and PNG filter methods.
It also can be used to remove unwanted ancillary chunks, or to add
certain chunks including gAMA, tRNS, and textual chunks.

%prep
%setup

%build
make

sed '1,/^<pre>$/d;/<\/pre>/,$d' < ChangeLog.html > ChangeLog
zstd ChangeLog

%install
install -Dpm755 pngcrush %buildroot%_bindir/pngcrush

%files
%_bindir/*
%doc ChangeLog.zst LICENSE

%changelog
* Wed Dec 07 2022 Artyom Bystrov <arbars@altlinux.org> 1.8.13-alt2
- Fix FTBFS https://git.altlinux.org/beehive/logs/Sisyphus-x86_64/latest/error/pngcrush-1.8.13-alt1

* Fri Nov 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1.8.13-alt1
- 1.7.35 -> 1.8.13.

* Mon Sep 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.35-alt1
- Updated to 1.7.35.

* Wed Jul 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.31-alt1
- Updated to 1.7.31.

* Wed Jul 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.13-alt1
- Updated to 1.7.13.

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
