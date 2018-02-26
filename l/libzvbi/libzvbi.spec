%define static 0
%define oname zvbi

Name: libzvbi
Version: 0.2.33
Release: alt3

Summary: Raw VBI, Teletext and Closed Caption decoding library

License: GPL
Group: Video
Url: http://zapping.sourceforge.net/

Source: http://prdownloads.sf.net/zapping/%oname-%version.tar.bz2
Packager: Konstantin Pavlov <thresh@altlinux.org>

BuildRequires: cvs doxygen libpng-devel libX11-devel

%if %static
BuildPreReq: glibc-devel-static
%endif

Provides: %name
Obsoletes: %name

%description
This library provides routines to

VBI stands for Vertical Blanking Interval, a gap between the image
data transmitted in an analog video signal. This gap is used to
transmit AM modulated data for various data services like Teletext and
Closed Caption.

The zvbi library provides routines to:
* read from raw VBI sampling devices (both V4L and V4L2 API are supported),
* a versatile raw vbi bit slicer,
* decoders for various data services and basic search,
* demodulate raw to sliced VBI data,
* interpret the data of several popular services.
* render and export functions for text pages.

The library is the vbi decoding backbone of the Zapping Gnome TV viewer
and Zapzilla Teletext browser.

%package devel
Summary: Header files for developing apps which will use libzvbi
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files and static library of bzip2 functions, for developing apps which
will use the zvbi library (aka libzvbi)

%if %static
%package devel-static
Summary: Static library for developing apps which will use libzvbi
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static library of bzip2 functions, for developing apps which
will use the zvbi library (aka libzvbi)
%endif

%prep
%setup -q -n %oname-%version

%build
%autoreconf

%configure \
	%{subst_enable static} \
	--with-x \
	--enable-v4l \
	--enable-dvb

%make_build

%install
%makeinstall_std
%find_lang %oname

%files -f %oname.lang
%doc AUTHORS NEWS README
%_bindir/zvbi*
%_sbindir/zvbi*
%_libdir/libzvbi*.so.*
%_man1dir/zvbi*

%files devel
%doc BUGS ChangeLog TODO doc/html
%_libdir/lib*.so
%_includedir/libzvbi.h
%_pkgconfigdir/zvbi*

%if %static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.33-alt3
- Rebuilt for soname set-versions

* Tue Mar 09 2010 Konstantin Pavlov <thresh@altlinux.org> 0.2.33-alt2
- Fix FTBFS on current Sisyphus.
- Spec cleanup.

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.33-alt1
- new version 0.2.33 (with rpmrb script)
- change packager, rename to libzvbi
- rewrote spec, update buildreq

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.24-alt0.1
- new version 0.2.24
- fix static build

* Sun Jul 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.22-alt0.1
- NMU: new version 0.2.22
- remove COPYING from docs

* Thu Jun 09 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.16-alt1
- 0.2.16

* Mon Jan 03 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.11-alt1
- 0.2.11

* Sun Jul 11 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.8-alt1.1
- locale files is moved to libzvbi package (bug #4453)
- libunicode require dropped (it is obsoleted from 2002-06-08)

* Tue Jun 01 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Fri Dec 12 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.5-alt2
- building without *.la

* Wed Nov 05 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.5-alt1
- 0.2.5
- new buildrequires and rebuilding in hasher

* Mon Feb 03 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 0.2.2-alt1
- first build for ALT

* Wed Oct 09 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2-1mdk
- new release

* Mon Jun 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.1-1mdk
- new release
- moves translations to zvbi package

* Wed Jun 05 2002 Stefan van der Eijk <stefan@eijk.nu> 0.1.1-2mdk
- BuildRequires

* Thu Apr 18 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.1-1mdk
- initial release
