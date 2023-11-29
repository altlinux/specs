%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_disable static
%def_enable rust

Name: gd3
Version: 2.3.3
Release: alt2
Summary: A graphics library for drawing image files in various formats
License: BSD-style
Group: Graphics
Url: https://libgd.github.io/

# https://github.com/libgd/libgd.git
Source: %name-%version.tar

BuildRequires: fontconfig-devel libXpm-devel libfreetype-devel libjpeg-devel libpng-devel
BuildRequires: libwebp-devel zlib-devel libtiff-devel
%if_enabled rust
BuildRequires: libheif-devel
%endif

# needed for tests
BuildRequires: fonts-ttf-dejavu

%package -n lib%name
Summary: A graphics library for drawing image files in various formats
Group: System/Libraries

%package -n lib%name-devel
Summary: Development library and header files for lib%name
Group: Development/C
Requires: lib%name = %EVR
Conflicts: libgd-devel < 2.0.4
Provides:  libgd2-devel = %EVR
Conflicts: libgd2-devel < %EVR
Obsoletes: libgd2-devel

%if_enabled static
%package -n lib%name-devel-static
Summary: Development static library for lib%name
Group: Development/C
Requires: lib%name-devel = %EVR
Conflicts: libgd-devel-static < 2.0.4
Provides:  libgd2-devel-static = %EVR
Conflicts: libgd2-devel-static < %EVR
Obsoletes: libgd2-devel-static
%endif

%package utils
Summary: Utilities for drawing image files in various formats
Group: Graphics
Requires: lib%name = %EVR
Conflicts: gd-utils < 2.0.4
Provides:  libgd2-utils = %EVR
Conflicts: libgd2-utils < %EVR
Obsoletes: libgd2-utils

%description
Gd is a graphics library.  It allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and write out the result as a PNG or
JPEG file.  This is particularly useful in World Wide Web applications,
where PNG and JPEG are two of the formats accepted for inline images
by most browsers.

Gd is not a paint program.  If you are looking for a paint program, you
are looking in the wrong place.  If you are not a programmer, you are
looking in the wrong place, unless you are installing a required
library in order to run an application.

Gd does not provide for every possible desirable graphics operation.
It is not necessary or desirable for Gd to become a kitchen-sink
graphics package, but version 2.0 does include most frequently
requested features, including both truecolor and palette images,
resampling (smooth resizing of truecolor images) and so forth.

%description -n lib%name
Gd is a graphics library for drawing image files in various formats.  Gd
allows your code to quickly draw images (lines, arcs, text, multiple colors,
cutting and pasting from other images, flood fills) and write out the result
as a jpeg, png or wbmp file.  Gd is particularly useful in web applications,
where jpeg, png or wbmp files are commonly used as inline images.  Note,
however, that Gd is not a paint program.

%description -n lib%name-devel
Gd is a graphics library for drawing image files in various formats.  Gd
allows your code to quickly draw images (lines, arcs, text, multiple colors,
cutting and pasting from other images, flood fills) and write out the result
as a jpeg, png or wbmp file.  Gd is particularly useful in web applications,
where jpeg, png or wbmp files are commonly used as inline images.  Note,
however, that Gd is not a paint program.

%if_enabled static
%description -n lib%name-devel-static
Gd is a graphics library for drawing image files in various formats.  Gd
allows your code to quickly draw images (lines, arcs, text, multiple colors,
cutting and pasting from other images, flood fills) and write out the result
as a jpeg, png or wbmp file.  Gd is particularly useful in web applications,
where jpeg, png or wbmp files are commonly used as inline images.  Note,
however, that Gd is not a paint program.
%endif

%description utils
Gd is a graphics library.  It allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and write out the result as a PNG or
JPEG file.  This is particularly useful in World Wide Web applications,
where PNG and JPEG are two of the formats accepted for inline images
by most browsers.

Gd is not a paint program.  If you are looking for a paint program, you
are looking in the wrong place.  If you are not a programmer, you are
looking in the wrong place, unless you are installing a required
library in order to run an application.

Gd does not provide for every possible desirable graphics operation.
It is not necessary or desirable for Gd to become a kitchen-sink
graphics package, but version %version does include most frequently
requested features, including both truecolor and palette images,
resampling (smooth resizing of truecolor images) and so forth.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%ifarch %ix86 aarch64 ppc64le riscv64 loongarch64
# Tests are known to be buggy on x86 32bit due to rounding issues. See:
# https://github.com/libgd/libgd/issues/359
# https://github.com/libgd/libgd/issues/242
%make_build -k check ||:
%else
%make_build -k check
%endif

%files -n lib%name
%doc COPYING
%_libdir/*.so.*

%files -n lib%name-devel
%doc README.md
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%files utils
%_bindir/*

%changelog
* Wed Nov 29 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.3.3-alt2
- spec:
  + run tests on LoongArch.
  + support building without rust stuff (to simplify bootstrap).

* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.3-alt1
- Updated to upstream version 2.3.3.

* Tue Mar 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.2-alt1
- Updated to upstream version 2.3.2.
- Enabled HEIF support.

* Tue Apr 21 2020 Nikita Ermakov <arei@altlinux.org> 2.3.0-alt2
- Fix build on riscv64 (gdimagegrayscale/basic and
  gdimagecopyresampled/bug00201 tests are fails because of the
  rounding after fused multiply-add instructions. One possible
  workarround is to add -ffp-contract=off to the CFLAGS but as the
  difference between images in the tests is small it would be better
  to just ignore these tests).

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 2.2.5-alt3
- Fix build on aarch64 (gdimagegrayscale/basic test fails alike to i586).
- Drop %%ubt macro.
- Minor spec cleanup.

* Fri May 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.5-alt2
- Updated provides/conflicts/obsoletes.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.5-alt1
- Updated to upstream version 2.2.5.

* Thu Apr 18 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0.35-alt6
- Fixed gdImageFill stack overflow comparison (libGD #177)

* Thu Sep 27 2012 Dmitry V. Levin <ldv@altlinux.org> 2.0.35-alt5
- Check max colors while loading gd palette image (fixes CVE-2009-3546).

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.35-alt4
- Rebuilt for debuginfo.

* Mon Oct 25 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.35-alt3
- Rebuilt for soname set-versions.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 2.0.35-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Wed Sep 19 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.35-alt1
- Updated to 2.0.35.
- Added pkg-config file.
- Updated default fontpath (shrek@).

* Fri May 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.34-alt3
- gd_png.c (gdPngReadData): Fixed infinite loop bug (CVE-2007-2756).

* Mon Apr 16 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.34-alt2
- Fixed regression introduced by patch from #5088 (#11515).

* Mon Mar 26 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.34-alt1
- Updated to 2.0.34.
- Added gdImageCreate*() return code checks.
- Updated build dependencies.
- Disabled build and packaging of the static library by default.
- Replaced iso8859-2 based fonts with koi8-r based (#5088).
- Imported FC patches:
  gd-2.0.33-AALineThick.patch, gd-2.0.33-BoxBound.patch.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.33-alt2
- Relocated gdlib-config from %name-utils to lib%name-devel (closes #6735).

* Fri Nov 12 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.33-alt1
- Updated to 2.0.33.

* Wed Nov 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.32-alt1
- Updated to 2.0.32.
- Merged upstream patches: alt-gdImageOpenPolygon.

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.28-alt1
- Updated to 2.0.28.

* Sun Jun 27 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt3
- sync'd with current fontpath layout

* Mon Nov 04 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt2
- Fixed shared library linkage.

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt1
- 2.0.4 (named as libgd2).

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.4-alt5
- Removed all mdk patches;
  redone build of shared library and utilities.
- Enforce compile and link without freetype 1.x (rh).
- Relocated Gd utilities to right place (%_bindir).
- Renamed to gd1.
- Added URL.
- Added GIF support from http://www.rhyme.com.au/gd/.
- Added versioning for GIF API.

* Thu Mar 21 2002 AEN <aen@logic.ru> 1.8.4-alt4
- symlinks fixed (#734)

* Thu Feb 06 2002 AEN <aen@logic.ru> 1.8.4-alt3
- really built with ttf support

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.8.4-alt2
- Rebuilt with libpng.so.3.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.8.4-alt1
- 1.8.4
- Built with freetype2.
- Moved static library to devel-static subpackage.

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.8.3-ipl1mdk
- Initial revision (merged specfiles from RH and MDK).
