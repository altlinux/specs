Name: gd2
Version: 2.0.35
Release: alt4

Summary: A graphics library for drawing image files in various formats
License: BSD-style
Group: Graphics
Url: http://www.libgd.org/Main_Page

%define srcname gd-%version
# http://www.libgd.org/releases/gd-%version.tar.bz2
Source: %srcname.tar

Patch: gd-%version-%release.patch

# Automatically added by buildreq on Mon Mar 26 2007
BuildRequires: fontconfig-devel libXpm-devel libfreetype-devel libjpeg-devel libpng-devel

%def_disable static

%package -n lib%name
Summary: A graphics library for drawing image files in various formats
Group: System/Libraries

%package -n lib%name-devel
Summary: Development library and header files for lib%name
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: libgd-devel < 2.0.4

%package -n lib%name-devel-static
Summary: Development static library for lib%name
Group: Development/C
Requires: lib%name-devel = %version-%release
Conflicts: libgd-devel-static < 2.0.4

%package utils
Summary: Utilities for drawing image files in various formats
Group: Graphics
Requires: lib%name = %version-%release
Conflicts: gd-utils < 2.0.4

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

%description -n lib%name-devel-static
Gd is a graphics library for drawing image files in various formats.  Gd
allows your code to quickly draw images (lines, arcs, text, multiple colors,
cutting and pasting from other images, flood fills) and write out the result
as a jpeg, png or wbmp file.  Gd is particularly useful in web applications,
where jpeg, png or wbmp files are commonly used as inline images.  Note,
however, that Gd is not a paint program.

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
%setup -n %srcname
%patch -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%define docdir %_docdir/%srcname
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
cp -a index.html COPYING %buildroot%docdir/

%check
%make_build -k check

%files -n lib%name
%_libdir/*.so.*
%dir %docdir
%docdir/COPYING

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_bindir/gdlib-config
%dir %docdir
%docdir/index.html

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%files utils
%_bindir/*
%exclude %_bindir/gdlib-config

%changelog
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
