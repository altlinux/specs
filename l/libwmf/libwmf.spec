Name: libwmf
Version: 0.2.8.4
Release: alt9

Summary: A library to convert wmf files
License: GPL
Group: Text tools
Url: http://sourceforge.net/projects/wvware

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: fonts-type1-urw
Obsoletes: wmf-fonts < %version-%release

Source: %name-%version.tar.bz2

Patch0: %name-0.2.6-cflags.patch
Patch1: libwmf-0.2.8.4-intoverflow.patch
Patch2: libwmf-0.2.8.3-CAN-2004-0941.patch
Patch3: libwmf-0.2.8.3-CAN-2004-0990.patch
Patch4: libwmf-0.2.8.4-CVE2007-2756.patch
Patch5: libwmf-0.2.8.4-CVE-2007-3473.patch
Patch6: libwmf-0.2.8.4-CVE-2009-1364.patch

# Automatically added by buildreq on Thu Jan 04 2007
BuildRequires: ghostscript-common glib2-devel libICE-devel libX11-devel libexpat-devel
BuildRequires: libfreetype-devel libgtk+2-devel libjpeg-devel libpng-devel

%description
%name is a library for unix like machines that can convert wmf
files into other formats, currently it supports a gd binding
to convert to gif, and an X one to draw direct to an X window
or pixmap.

%package -n wmf-utils
Summary: Utilities to convert wmf files
Group: Text tools
Requires: %name = %version-%release

%description -n wmf-utils
This package contains various programs for manipulating files in
the WMF format.

%package -n wmf-gtk-loader
Summary: GDK-pixbuf loader for WMF files
Group: System/Libraries

%description -n wmf-gtk-loader
WMF file loader for the GTK+ image manipulation library, GDK-pixbuf.

%package devel
Summary: A library to convert wmf files - development environment
Group: Development/C
Requires: %name = %version-%release
Requires: libexpat-devel libfreetype-devel libX11-devel
Requires: libjpeg-devel libpng-devel zlib-devel

%description devel
%name is a library for unix like machines that can convert wmf
files into other formats, currently it supports a gd binding
to convert to gif, and an X one to draw direct to an X window
or pixmap.

Install %name-devel if you need to compile an application with %name
support.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

rm -f configure.in

%build
%autoreconf
%configure \
	--disable-static \
	--with-fontdir=%_datadir/fonts/type1/urw \
	--with-xtrafontmap=%_datadir/%name/fontmap \
	--with-docdir=%_docdir/%name-%version
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 fonts/fontmap %buildroot%_datadir/%name/fontmap
install -p -m644 ChangeLog CREDITS README TODO %buildroot%_docdir/%name-%version

%files
%_libdir/*.so.*
%_datadir/%name

%files -n wmf-utils
%_bindir/wmf2*

%files -n wmf-gtk-loader
%_libdir/gtk-*/*/loaders/*.so

%files devel
%_libdir/*.so
%_bindir/%name-config
%_includedir/%name
%_docdir/%name-%version

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8.4-alt9
- Rebuilt for debuginfo

* Tue Nov 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt8
- rebuild

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt7
- rebuild with libpng12 1.2.37-alt2

* Mon May 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt6
- fixed CAN-2004-0941, CAN-2004-0990, CVE-2007-2756, CVE-2007-3473

* Fri May 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt5
- fixed CVE-2009-1364

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Jan 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.8.4-alt3
- fixed #10589
- added libwmf-0.2.8.4-intoverflow.patch
- drop subpackage wmf-fonts, add requires fonts-type1-urw
- updated build dependencies
- clenup spec file

* Sun Jun 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.4-alt2
- Added dependencies for libwmf-devel to cover libwmf-config --libs output
  (bug 9708)

* Fri Oct 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.4-alt1
- 0.2.8.4

* Sat Dec 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.3-alt3
- Added /usr/share/libwmf to the file list of the fonts package

* Fri Dec 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.3-alt2
- Spec cleanup, buildreq
- Run autoreconf to avoid /lib/cpp error

* Fri Dec 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.3-alt1
- New upstream release

* Wed Nov 26 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8.2-alt1
- New upstream release
- Added gtk-loader subpackage for the gdk-pixbuf loader

* Tue Dec 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Wed Oct 09 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.6-alt2
- listed docs properly

* Tue Sep 24 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.6-alt1
- 0.2.6
- disabled static build by default
- docs to the devel package
- cflags fixes

* Wed Jun 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.5-alt1
- 0.2.5
- postun_ldconfig

* Thu Nov 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.1-alt1
- Rebuilt with libpng.so.3
- 0.2.1

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.2.0-alt2
- More spec cleanup.
- Renamed %name subpackage to %name-utils.

* Mon Aug 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus
- Added devel-static package
- Some spec cleanup

* Mon Jul 02 2001 François Pons <fpons@mandrakesoft.com> 0.2.0-3mdk
- clean up and split to create libwmf0.2_0 and libwmf-fonts,
  renamed libwmf-devel to libwmf0.2_0-devel.

* Sun Jul 01 2001 Stefan van der Eijk <stefan@eijk.nu> 0.2.0-2mdk
- BuildRequires:	libpng-devel
- BuildRequires:	libxml2-devel
- BuildRequires:	freetype2-devel
- Removed BuildRequires:	freetype-devel

* Mon Jun 18 2001  Daouda Lo <daouda@mandrakesoft.com> 0.2.0-1mdk
- release 0.2.0
- spec cleanups

* Tue Dec 19 2000 François Pons <fpons@mandrakesoft.com> 0.1.21-1mdk
- update files and requires.
- 0.1.21.

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.19-4mdk
- fix summary

* Fri Oct 20 2000 François Pons <fpons@mandrakesoft.com> 0.1.19-3mdk
- avoid updating gd with older version here, newer does not run with.

* Fri Oct 20 2000 François Pons <fpons@mandrakesoft.com> 0.1.19-2mdk
- reverted back include files where they are expected.

* Fri Oct 20 2000 François Pons <fpons@mandrakesoft.com> 0.1.19-1mdk
- macroszifications.
- moved include files to a specific directory.
- updated URL and download page to latest modified version.
- 0.1.19.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.1.8-4mdk
- automatically added BuildRequires

* Tue May 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1.8-3mdk
- fix group

* Wed Apr 21 1999 Sean P. Kane <kane@ca.metsci.com>
- Upgraded to version 0.1.8

* Tue Apr 13 1999 Ryan Weaver <ryanw@infohwy.com>
  [libwmf-0.1.7-1]
- Initial RPM Build
- 0.1.7
- added ability to gd to read xbm's from data, rather than file,
  changed source accordingly, dont need to carry xbm's around
  anymore.
- changed configure script to agressively find the xpm header file,
- tested to work under aix (of all things :-))
- tested to work under solaris.
- checked that it reports lack of xpm lib, and fails to go any
  further.
- fiddled a bit more, and libwmf now works cleanly with mswordview,
  all cheer.
