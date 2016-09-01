Name: libmikmod
Version: 3.3.10
Release: alt1

Summary: A portable sound library for Unix
License: GPLv2 and LGPLv2+
Group: System/Libraries

Url: http://mikmod.raphnet.net
# http://download.sourceforge.net/mikmod/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: 0014-playercode-mdreg-Register-the-NULL-driver-before-the.patch
Patch1: use-gnu-install-directories.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Mar 03 2011
BuildRequires: libalsa-devel libesd-devel libpulseaudio-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write wav files.

Supported file formats include mod, stm, s3m, mtm, xm, and it.
Full source included, use of this library for music/sound effects in
your own programs is encouraged!

%package devel
Summary: Header files and libraries for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release
Requires: libpulseaudio-devel

%description devel
Install the %name-devel package if you want to develop applications that
will use the %name library.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README TODO

%files devel
%_bindir/*
%_libdir/*.so
%_includedir/*
%_man1dir/*
%_infodir/*.info*
%_datadir/aclocal/*
%_pkgconfigdir/*.pc

# TODO:
# - consider --enable-simd (marked unstable as of 3.3.7)

%changelog
* Thu Sep 01 2016 Michael Shigorin <mike@altlinux.org> 3.3.10-alt1
- 3.3.10

* Wed Aug 17 2016 Michael Shigorin <mike@altlinux.org> 3.3.9-alt1
- 3.3.9

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.3.8-alt1.1
- NMU: added BR: texinfo

* Sun Nov 15 2015 Michael Shigorin <mike@altlinux.org> 3.3.8-alt1
- 3.3.8

* Wed Sep 10 2014 Michael Shigorin <mike@altlinux.org> 3.3.7-alt1
- 3.3.7
- dropped 3.1.12 patches
- added debian patches

* Wed Dec 28 2011 Michael Shigorin <mike@altlinux.org> 3.1.12-alt4
- applied libmikmod-3.1.12-64bit-fix.patch from SDL_mixer distribution;
  thanks viy@ (closes: #26760)

* Thu Mar 03 2011 Alexey Tourbin <at@altlinux.ru> 3.1.12-alt3
- rebuilt for debuginfo
- removed dependency on libaudiofile-devel

* Fri Nov 26 2010 Michael Shigorin <mike@altlinux.org> 3.1.12-alt2
- rebuilt for set versions

* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 3.1.12-alt1
- Updated to 3.1.12.

* Thu Aug 26 2010 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.8
- imported security fixes from openSUSE 3.1.11a-84.5 package:
  + CVE-2007-6720:
    denial of service (crash) by loading multiple MOD files
    with different numbers of channels
  + CVE-2009-0179:
    denial of service (crash) by loading an XM file
  + CVE-2009-3995:
    arbitrary code execution via (1) crafted samples
    or (2) crafted instrument definitions in an Impulse Tracker file
  + CVE-2009-3996:
    arbitrary code execution via an Ultratracker file

* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.7
- applied repocop patch
- added an Url:
- minor spec cleanup

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.6
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.5
- added libmikmod-3.1.11-a.diff
- applied repocop patch

* Fri Sep 28 2007 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.4
- added Requires: libaudiofile-devel to devel subpackage
  (mikmod configure test fails to link due to missing -laudiofile)

* Mon Sep 17 2007 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.3
- added patch to fix underquoted aclocal macro in libmikmod.m4,
  thanks to Vitaly Lipatov for (shamefully trivial) patch
  (fixes #8776)
- spec macro abuse cleanup

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.2
- s/ru-Ru/ru_RU/g

* Mon Apr 03 2006 Michael Shigorin <mike@altlinux.org> 3.1.11-alt0.1
- NMU: 3.1.11 (tarball updated from Gentoo distfiles)
- added Gentoo makefile patch
- fix build with --as-needed
- removed --disable-alsa
- removed stale Url
- s/ru-Ru/ru_RU/

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 3.1.10-alt3
- do not package .la files.
- devel-static subpackage is optional.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.1.10-alt2
- Rebuild with gcc-3.2. 

* Sat Feb 2 2002  Yuri N. Sedunov <aris@altlinux.ru> 3.1.10-alt1
- new version

* Fri Dec 21 2001 Yuri N. Sedunov <aris@altlinux.ru> 3.1.9-alt1
- Rebuilt with EsounD support, it works.
- URLs changed.
- Russian summary and description added.
- devel-static package

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 3.1.9-ipl5mdk
- Added and applied official "a" patch.

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.9-ipl4mdk
- RE adaptions.

* Wed Nov 08 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.1.9-4mdk
- build for gcc-2.96
- capitalized summary
- fix requires

* Tue Sep 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.1.9-3mdk
- disable alsa, from :
	Goetz Waschk <waschk@linux-mandrake.com>
	- removed alsa support, it caused segfaults

* Sun Jul 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.1.9-2mdk
- macroszifications
- fix hte filelist (*.so goes to devel not main)
- rebuild for BM

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.1.9-1mdk
- v 3.1.9
- fix group
- add doc
- spechelper fix

* Sat Feb 05 2000 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added .so in %files section (reported by David Mihm
  <dmihm@rchitecture.com>).

* Fri Nov 12 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- updated to version 3.1.8.

* Sat Sep 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added .la file.

* Sat Jul 17 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- downgraded to version 3.1.6 for xmms compatibilty.

* Fri Jul 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First version for Mandrake distribution.
