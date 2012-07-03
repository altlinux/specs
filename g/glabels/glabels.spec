Name: glabels
Version: 3.0.0
Release: alt1.1

Summary: glabels is a GNOME program to create labels and business cards
Summary(ru_RU.UTF-8): glabels для GNOME - программа создания этикеток и визиток

License: GPL
Group: Graphics
Url: http://glabels.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sf.net/%name/%name-%version.tar
Source: http://ftp.gnome.org/pub/GNOME/sources/glabels/3.0/%name-%version.tar
Patch: %name-1.93.3-crop.patch
Patch1: %name-2.2.0-etersoft.patch
Patch2: %name-3.0.0-build.patch

# Automatically added by buildreq on Fri Jun 03 2011
# optimized out: fontconfig fontconfig-devel glib2-devel gnome-doc-utils gtk-update-icon-cache libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libxml2-devel perl-Encode perl-XML-Parser pkg-config python-base python-module-libxml2 python-modules python-modules-compiler python-modules-encodings time
BuildRequires: glibc-devel-static gtk-doc intltool libgtk+3-devel librsvg-devel python-module-paste python-module-peak

BuildPreReq: intltool libxml2-devel

Requires: lib%name = %version-%release

# Typical environment for GNOME program
Requires(post): GConf2
Requires(post,postun): scrollkeeper
Requires(post,postun): desktop-file-utils
BuildPreReq: GConf2
BuildPreReq: desktop-file-utils

%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.

%description -l ru_RU.UTF-8
gLabels -- простая и компактная программа для создания этикеток
и визитных карточек в среде GNOME.
Она позволяет работать с различными видами специальной бумаги
для этикеток и визиток, пригодными для лазерных и струйных
принтеров.

%package -n lib%name
Summary: library for glabels
Group: Graphics

%description -n lib%name
This package contains the library for glabels program.

%package -n lib%name-devel
Summary: header files for glabels library
Group: Graphics
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains headers files for development with glabels library.

%prep
%setup -q
#%patch0 -p0
#%patch1
%patch2 -p2

%build
%autoreconf
%configure --disable-static \
	--disable-schemas-install
%make_build

%install
%makeinstall_std

ln -s %name-3 %buildroot%_bindir/%name

%find_lang %name-3.0 --with-gnome

%files -f %name-3.0.lang
%doc README ChangeLog NEWS AUTHORS
%_bindir/%name
%_bindir/%name-3
%_bindir/%name-3-batch
%_desktopdir/*
%_datadir/%name-3.0
%_datadir/glib-2.0/schemas/*
%_datadir/gnome/help/%name-3.0/
%_iconsdir/hicolor/*/*/*.png
%_datadir/mime/packages/*
%_man1dir/*

%files -n lib%name
%_datadir/lib%name-3.0
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/lib*/
%_pkgconfigdir/*
%_datadir/gtk-doc/html/lib*/

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.1
- Fixed build

* Fri Jun 03 2011 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (ALT bug #25705)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.8-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for glabels

* Sun Jun 27 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2.8-alt1
- new version 2.2.8 (with rpmrb script)
- cleanup spec, update buildreqs

* Sat May 23 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt1
- new version 2.2.5 (with rpmrb script), update buildreqs
- add updated ru.po from Alexandre Prokoudine

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version 2.2.4 (with rpmrb script)
- drop out post/postun sections

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new version 2.2.2 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)
- update buildreqs

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt0.1
- new version 2.1.3 (with rpmrb script)

* Fri Dec 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version

* Sun Apr 10 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version
- drop patch for change crop offset :(

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version

* Sat Jun 26 2004 Vitaly Lipatov <lav@altlinux.ru> 1.93.3-alt3
- add ldconfig in post/postun for lib package
- remove duplicates in labels
- update ru.po
- add patch for change crop offset

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.93.3-alt2
- fix menu entry (move to Publishing)

* Thu Jun 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.93.3-alt1
- new version
- update russian translation
- move libglabels and headers to separate packages
- remove COPYING from doc

* Sat Sep 13 2003 Vitaly Lipatov <lav@altlinux.ru> 1.92.0-alt1
- release
- update russian translation

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.92.0-alt0.2cvs
- cvs build from Dec 29 2002
- add required post and postun sections
- update russian translation
- add genericname in menu
- cleanup spec

* Thu Dec 26 2002 Vitaly Lipatov <lav@altlinux.ru> 1.92.0-alt0.1cvs
- Alexey Lubimov <avl@l14.ru>:
	- cvs build
	- fix input russian letters in text label
	- partial fix freeze font combo in text label when set not listed font. (use arrow keys)
- split in two package (glabels-batch)

* Fri Nov 01 2002 Vitaly Lipatov <lav@altlinux.ru> 1.90.0-alt2
- add patch for ported to libgnomeprint(ui)-2.2 by Alexey Lubimov <avl@l14.ru>
- repeat build for GNOME2 (previous is lost)
- remove unuseful dependencies

* Sun Oct 27 2002 Vitaly Lipatov <lav@altlinux.ru> 1.90.0-alt1
- 1.90.0 for GNOME2
- update russian translation
- update spec

* Fri Sep 06 2002 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- new version

* Fri Jun 28 2002 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- new version
- russian translation
- spec updated

* Mon Dec 10 2001 AEN <aen@logic.ru> 0.3.2-alt1
- new version

* Mon Nov 12 2001 AEN <aen@logic.ru> 0.2.3-alt1
- new version

* Tue Oct 16 2001 AEN <aen@logic.ru> 0.2.0-alt1
- new version
* Tue Oct 2 2001 AEN <aen@logic.ru> 0.1.4-alt1
- build for Sisyphus
* Sat May 19 2001 Jim Evins <evins@snaught.com>
- Created

