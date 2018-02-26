%define dversion	6.7.7
%define drelease	7
%define qlev		Q16
%define mgkdir		ImageMagick
%define soname		4

%def_enable librsvg
%def_enable x
Name: ImageMagick
Version: %dversion.%drelease
Release: alt1

Summary: An X application for displaying and manipulating images
License: OpenSource
Group: Graphics
Url: http://www.imagemagick.org/

Packager: Anton Farygin <rider@altlinux.ru>

Source0: ftp://ftp.imagemagick.org/pub/ImageMagick/%name-%dversion-%drelease.tar

Source1: %name.desktop
Source2: imagemagick16.png
Source3: imagemagick32.png
Source4: imagemagick48.png
Patch1: ImageMagick-depends.patch


Requires: ghostscript-classic fonts-type1-urw lib%name = %version-%release

# Automatically added by buildreq on Wed Nov 03 2010
BuildRequires: ImageMagick-tools bzlib-devel curl gcc-c++ glibc-devel-static graphviz groff-base imake libXext-devel libXt-devel libdjvu-devel libjasper-devel libjbig-devel liblcms-devel liblqr-devel librsvg-devel libtiff-devel libwmf-devel libxml2-devel openexr-devel perl-devel transfig xdg-utils xorg-cf-files 

BuildRequires: libjasper-devel libjbig-devel liblcms-devel libtiff-devel libwmf-devel libxml2-devel perl-devel chrpath openexr-devel liblqr-devel libdjvu-devel
%if_enabled librsvg
BuildRequires: librsvg-devel libpixman-devel
%endif

Requires: %name-tools %name-doc

%description
%name is a powerful image display, conversion and manipulation tool.
It runs in an X session.  With this tool, you can view, edit and display
a variety of image formats.

This package installs the necessary files to run %name.

%package -n lib%name
Summary: %name shared libraries
Group: System/Libraries
Provides: %name-lib = %version
Obsoletes: %name-lib < %version

%description -n lib%name
%name is a powerful image display, conversion and manipulation libraries.

%package -n lib%name-devel
Summary: Header files for %name app development
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
If you want to create applications that will use %name code or APIs,
you'll need to install these packages as well as %name.  These additional
packages aren't necessary if you simply want to use %name, however.

%package -n lib%name-devel-static
Summary: Static libraries for %name app development
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
If you want to create applications that will use %name code or APIs,
you'll need to install these packages as well as %name.  These additional
packages aren't necessary if you simply want to use %name, however.

lib%name-devel is an addition to %name which includes static libraries files
necessary to develop applications.

%package -n perl-Magick
Summary: Libraries and modules for access to %name from perl
Group: Development/Perl
Requires: lib%name = %version-%release

%description -n perl-Magick
This is the %name perl support package.  It includes perl modules
and support files for access to %name library from perl.

%package tools
Summary: Console tools from %name
Group: Graphics
Requires: lib%name = %version-%release
Conflicts: GraphicsMagick-ImageMagick-compat
Provides: convert

%description tools
%name is a powerful image conversion and manipulation tools.
This package installs the necessary files to run %name-tools.

%package doc
Summary: Documentation for %name
Group: Graphics
Requires: %name-tools
BuildArch: noarch

%description doc
Documentation for %name 

%def_disable static

%prep
%setup -q -n %name-%dversion-%drelease
%patch1 -p2
touch config.rpath

# XXX tests fail
rm PerlMagick/t/composite.t
rm PerlMagick/t/filter.t
rm PerlMagick/t/montage.t

%build
%autoreconf
%configure \
	--with-modules \
	--with-fontpath=%_datadir/fonts/type1/urw \
	--with-gs-font-dir=%_datadir/fonts/type1/urw \
	--with-gvc=yes \
	--with-lqr=yes \
	--enable-hdri \
	--with-perl \
	%{subst_enable x} \
	--with-perl-options="PREFIX=%_prefix INSTALLDIRS=vendor" \
	%{subst_enable static}
subst 's|^\(hardcode_into_libs\)=.*$|\1=no|' libtool
%make_build

pushd PerlMagick
perl Makefile.PL
make
popd

%install
%make transform='' DESTDIR=%buildroot INSTALLDIRS=vendor install


%__subst "s,%_libdir/libMagickCore.la,-L%_libdir -lMagickCore," %buildroot%_libdir/%mgkdir-%dversion/modules-%qlev/*/*.la

%__install -pD -m644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%__install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png

chrpath -d %buildroot%perl_vendor_archlib/auto/Image/Magick/Magick.so

%files

%files tools
%_bindir/[a-z]*
%_man1dir/%name.1*
%_man1dir/[a-z]*.1*
# display, menu and icons to be moved into subpackage
%_bindir/display
%_datadir/applications/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_man1dir/display*.1*

%files doc
%dir %_docdir/%name-%dversion
%dir %_docdir/%name-%dversion/www
%_docdir/%name-%dversion/LICENSE
%_docdir/%name-%dversion/images
%_docdir/%name-%dversion/index.html
%_docdir/%name-%dversion/www/*
%exclude %_docdir/%name-%dversion/www/api
%exclude %_docdir/%name-%dversion/www/Magick++

%files -n lib%name
%dir %_libdir/%mgkdir-%dversion
%dir %_libdir/%mgkdir-%dversion/modules-%qlev
%dir %_libdir/%mgkdir-%dversion/modules-%qlev/coders
%dir %_libdir/%mgkdir-%dversion/modules-%qlev/filters
%_libdir/%mgkdir-%dversion/modules-%qlev/*/*
%dir %_datadir/%mgkdir-%dversion
%dir %_sysconfdir/%name
%_datadir/%mgkdir-%dversion/*
%config %_sysconfdir/%name/*
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_docdir/%name-%dversion
%dir %_docdir/%name-%dversion/www
%_docdir/%name-%dversion/www/api
%_docdir/%name-%dversion/www/Magick++
%_bindir/*-config
%_includedir/*
%_libdir/*.so
%_libdir/%mgkdir-%dversion/config
%_pkgconfigdir/*.pc
%_man1dir/*-config.1*

%files -n perl-Magick
%doc www/perl-magick.html images/examples.jpg PerlMagick/demo
%perl_vendor_archlib/Image
%perl_vendor_autolib/Image

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Jun 15 2012 Anton Farygin <rider@altlinux.ru> 6.7.7.7-alt1
- new version

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 6.7.7.6-alt1
- new version

* Thu Nov 24 2011 Anton Farygin <rider@altlinux.ru> 6.7.3.7-alt1
- new version

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 6.7.2.3-alt1.1
- rebuilt for perl-5.14

* Tue Sep 13 2011 Anton Farygin <rider@altlinux.ru> 6.7.2.5-alt1
- new version with new soname


* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 6.7.2.3-alt1
- new version

* Tue Apr 26 2011 Anton Farygin <rider@altlinux.ru> 6.6.9.6-alt1
- new version
- removed extra dependencies in magick-config (closes: #20725)

* Wed Apr 13 2011 Anton Farygin <rider@altlinux.ru> 6.6.9.4-alt1
- new version

* Tue Apr 05 2011 Anton Farygin <rider@altlinux.ru> 6.6.9.3-alt1
- new version

* Tue Apr 05 2011 Anton Farygin <rider@altlinux.ru> 6.6.8.10-alt1
- new version

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6.8.1-alt1
- new version

* Thu Nov 25 2010 Anton Farygin <rider@altlinux.ru> 6.6.5.10-alt1
- new version

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 6.6.3.10-alt1.1
- rebuilt with perl 5.12

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 6.6.3.10-alt1
- new version

* Fri Jul 02 2010 Anton Farygin <rider@altlinux.ru> 6.6.2.10-alt1
- new version

* Thu Apr 15 2010 Anton Farygin <rider@altlinux.ru> 6.6.1.3-alt1
- new version

* Tue Feb 23 2010 Anton Farygin <rider@altlinux.ru> 6.5.9.10-alt1
- new version

* Fri Jan 15 2010 Anton Farygin <rider@altlinux.ru> 6.5.8.10-alt1
- new version

* Mon Nov 23 2009 Anton Farygin <rider@altlinux.ru> 6.5.7.10-alt1
- new version

* Sat Nov 07 2009 Anton Farygin <rider@altlinux.ru> 6.5.7.5-alt1
- new version

* Tue Oct 13 2009 Anton Farygin <rider@altlinux.ru> 6.5.6.10-alt1
- new version
- patches ImageMagick-6.4.5-Magick-config.patch and ImageMagick-6.5.3-2-perlMagick.patch 
  included to mainstream

* Thu Sep 24 2009 Anton Farygin <rider@altlinux.ru> 6.5.6.4-alt1
- new version

* Sun Sep 13 2009 Anton Farygin <rider@altlinux.ru> 6.5.5.10-alt1
- new version

* Tue Sep 08 2009 Anton Farygin <rider@altlinux.ru> 6.5.5.8-alt1
- new version

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 6.5.5.6-alt1
- new version

* Wed Aug 26 2009 Anton Farygin <rider@altlinux.ru> 6.5.5.2-alt1
- new version

* Sat Aug 08 2009 Anton Farygin <rider@altlinux.ru> 6.5.4.9-alt1
- new version

* Thu Jun 25 2009 Anton Farygin <rider@altlinux.ru> 6.5.3.10-alt1
- new version

* Wed Jun 03 2009 Anton Farygin <rider@altlinux.ru> 6.5.3.2-alt1
- new version

* Thu May 28 2009 Anton Farygin <rider@altlinux.ru> 6.5.2.9-alt1
- new version with fix for Secunia Advisory SA35216 (Closes #20203)

* Tue May 26 2009 Anton Farygin <rider@altlinux.ru> 6.5.2.8-alt1
- new version

* Thu May 14 2009 Anton Farygin <rider@altlinux.ru> 6.5.2.4-alt1
- new version

* Wed May 06 2009 Anton Farygin <rider@altlinux.ru> 6.5.2.1-alt1
- new version

* Mon May 04 2009 Anton Farygin <rider@altlinux.ru> 6.5.2.0-alt1
- new version

* Thu Apr 30 2009 Anton Farygin <rider@altlinux.ru> 6.5.1.9-alt1
- new version

* Mon Apr 27 2009 Anton Farygin <rider@altlinux.ru> 6.5.1.7-alt1
- new version

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 6.5.1.2-alt1
- new version

* Tue Apr 07 2009 Anton Farygin <rider@altlinux.ru> 6.5.1.0-alt1
- new version

* Thu Mar 26 2009 Anton Farygin <rider@altlinux.ru> 6.5.0.8-alt1
- new version

* Fri Mar 20 2009 Anton Farygin <rider@altlinux.ru> 6.5.0.2-alt1
- new version

* Fri Mar 13 2009 Anton Farygin <rider@altlinux.ru> 6.5.0.0-alt1
- new version

* Thu Dec 25 2008 Anton Farygin <rider@altlinux.ru> 6.4.8.1-alt1
- new version

* Wed Dec 24 2008 Anton Farygin <rider@altlinux.ru> 6.4.8.0-alt1
- new version

* Wed Dec 24 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.10-alt0.M50.1
- new version

* Wed Dec 17 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.9-alt1
- new version

* Sat Dec 13 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.7-alt1
- new version

* Wed Dec 10 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.5-alt1
- new version

* Tue Dec 09 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.3-alt1
- new version

* Sun Dec 07 2008 Anton Farygin <rider@altlinux.ru> 6.4.7.2-alt1
- new version
- build with liblqr
- build with libdjvu

* Thu Dec 04 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.9-alt1
- new version

* Sun Nov 30 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.6-alt1
- new version

* Fri Nov 28 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.4-alt1
- new version

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.3-alt1
- new version

* Sun Nov 23 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.1-alt1
- new version

* Sat Nov 22 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.0-alt2
- revert display to %name-tools

* Fri Nov 21 2008 Anton Farygin <rider@altlinux.ru> 6.4.6.0-alt1
- new version
- %name package splitted to %name-tools and %name-doc
- enabled hdri support

* Tue Nov 18 2008 Anton Farygin <rider@altlinux.ru> 6.4.5.8-alt1
- new version

* Mon Nov 17 2008 Anton Farygin <rider@altlinux.ru> 6.4.5.7-alt1
- new version

* Fri Nov 14 2008 Anton Farygin <rider@altlinux.ru> 6.4.5.5-alt3
- post-scripts removed 

* Wed Nov 12 2008 Anton Farygin <rider@altlinux.ru> 6.4.5.5-alt2
- fixed Build

* Tue Nov 11 2008 Anton Farygin <rider@altlinux.ru> 6.4.5.5-alt1
- new version with soname change

* Mon Sep 15 2008 Anton Farygin <rider@altlinux.ru> 6.3.7.2-alt2
- fixed subdirectories packaging violation (Led)
- fixed post scripts (Led)
- use %%autoreconf instead of %%__autoreconf

* Fri Nov 30 2007 Anton Farygin <rider@altlinux.ru> 6.3.7.2-alt1
- new version
- move plugins to libImageMagick package
- perlMagick now required libImageMagick instead of ImageMagick

* Mon Nov 26 2007 Anton Farygin <rider@altlinux.ru> 6.3.7.1-alt1
- new version

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 6.3.6.8-alt1
- new version

* Wed Oct 03 2007 Anton Farygin <rider@altlinux.ru> 6.3.6.0-alt1
- new version

* Mon Sep 17 2007 Anton Farygin <rider@altlinux.ru> 6.3.5.9-alt1
- new version

* Wed Sep 05 2007 Anton Farygin <rider@altlinux.ru> 6.3.5.8-alt1
- new version

* Sun Sep 02 2007 Anton Farygin <rider@altlinux.ru> 6.3.5.7-alt1
- new version

* Thu Aug 16 2007 Anton Farygin <rider@altlinux.ru> 6.3.5.6-alt1
- new version

* Tue Jun 19 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.10-alt1
- new version

* Tue Jun 05 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.6-alt1
- new version

* Tue May 29 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.4-alt1
- new version

* Tue May 22 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.2-alt2
- disabled HDRI for compatibility

* Mon May 21 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.2-alt1
- new version

* Mon May 14 2007 Anton Farygin <rider@altlinux.ru> 6.3.4.1-alt1
- new version
- enabled experimental hdri support
- enabled openexr support

* Tue Apr 24 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.10-alt1
- new version

* Mon Apr 16 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.8-alt1
- new version

* Thu Apr 12 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.7-alt2
- fixed perl-Magick package (added lost Magick.pm)

* Thu Apr 12 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.7-alt1
- new version

* Fri Apr 06 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.6-alt1
- new version

* Tue Apr 03 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.5-alt1
- new version
- fixed bug 11322, by mainstream

* Mon Mar 26 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.4-alt1
- new version

* Fri Mar 23 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.3-alt1
- new version

* Tue Mar 13 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.1-alt1
- new version

* Tue Mar 06 2007 Anton Farygin <rider@altlinux.ru> 6.3.3.0-alt1
- new version

* Wed Feb 21 2007 Anton Farygin <rider@altlinux.ru> 6.3.2.8-alt1
- new version

* Wed Feb 14 2007 Anton Farygin <rider@altlinux.ru> 6.3.2.5-alt1
- new version
- lib%name-devel: removed Requires to devel packages

* Sat Feb 10 2007 Anton Farygin <rider@altlinux.ru> 6.3.2.4-alt1
- new version

* Thu Feb 08 2007 Anton Farygin <rider@altlinux.ru> 6.3.2.3-alt1
- new version
- added requires %name->lib%name
- api documentation moved to lib%name-devel package

* Mon Feb 05 2007 Anton Farygin <rider@altlinux.ru> 6.3.2-alt2
- 6.3.2-2
- lib%name-devel: added Requires to devel packages (#10766)

* Wed Jan 31 2007 Anton Farygin <rider@altlinux.ru> 6.3.2-alt1
- 6.3.2-1

* Sun Jan 14 2007 Anton Farygin <rider@altlinux.ru> 6.3.1-alt7
- 6.3.1-7

* Sun Jan 07 2007 Anton Farygin <rider@altlinux.ru> 6.3.1-alt6
- build with librsvg
- merge with specfile from Valery Inozemtsev

* Tue Jan 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 6.3.1-alt5
- set default font search path to %_datadir/fonts/type1/urw
- fixed directory containing Ghostscript fonts
- relocated architecture dependent configuration files to lib%name subpackage

* Tue Jan 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 6.3.1-alt4
- drop ImageMagick-6.2.9-perlmagick.patch
- fixed unresolved symbols in Magick.so

* Mon Jan 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 6.3.1-alt3
- 6.3.1-5
- build with fontconfig, libtiff
- updated icons
- fixed #10166, #9640, #9074, #8367

* Sun Dec 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 6.3.1-alt2
- updated build dependencies
- clenup spec file
- removed old menu
- added freedesktop menu
- build without librsvg

* Tue Dec 26 2006 Anton Farygin <rider@altlinux.ru> 6.3.1-alt1
- new version

* Tue Oct 10 2006 Anton Farygin <rider@altlinux.ru> 6.2.9-alt1
- updated to 6.2.9-8

* Wed May 31 2006 Anton Farygin <rider@altlinux.ru> 6.2.7-alt2
- updated version (6.2.7-8)
- fixed ghostscript requires
- updated BuildRequires

* Mon May 22 2006 Anton Farygin <rider@altlinux.ru> 6.2.7-alt1
- new version

* Fri Oct 21 2005 Anton Farygin <rider@altlinux.ru> 6.2.5-alt1
- new version

* Fri Sep 30 2005 Anton Farygin <rider@altlinux.ru> 6.2.4-alt3
- 6.2.4-6

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 6.2.4-alt2
- 6.2.4-5

* Thu Sep 08 2005 Anton Farygin <rider@altlinux.ru> 6.2.4-alt1
- new version

* Mon Jun 20 2005 Anton Farygin <rider@altlinux.ru> 6.2.3-alt1
- new version
- icon name fix for menu file (#4383)
- documentation location fixed (#5447,#7860)
- BuildRequires cleanup (#7587)
- pdf documentation removed

* Wed May 25 2005 Anton Farygin <rider@altlinux.ru> 6.2.2-alt1
- new version

* Tue Apr 12 2005 Anton Farygin <rider@altlinux.ru> 6.2.1-alt1
- new version

* Thu Feb 10 2005 Anton Farygin <rider@altlinux.ru> 6.1.9-alt1
- new version
- enabled JPEG2000 support

* Tue Jan 25 2005 Anton Farygin <rider@altlinux.ru> 6.1.8-alt2
- perl-Magick fixed (#5950)

* Tue Jan 18 2005 Anton Farygin <rider@altlinux.ru> 6.1.8-alt1
- new version (6.1.8)

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 6.0.4-alt3.1
- Rebuilt with libtiff.so.4.

* Wed Sep 01 2004 Dmitry V. Levin <ldv@altlinux.org> 6.0.4-alt3
- More potential heap overflow bugfixes from upstream.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 6.0.4-alt2
- Fixed few potential heap overflow bugs (SuSE).
- Do not build and package static libraries by default.
- Cleaned up specfile and build dependencies.

* Fri Aug 13 2004 Anton Farygin <rider@altlinux.ru> 6.0.4-alt1
- new version (6.0.4-3)

* Tue Jun 29 2004 Anton Farygin <rider@altlinux.ru> 6.0.2-alt1
- new version (6.0.2-7)
- icons added (#4383)

* Wed May 12 2004 Anton Farygin <rider@altlinux.ru> 6.0.1-alt2
- new version (6.0.1-2)

* Mon Apr 26 2004 Anton Farygin <rider@altlinux.ru> 6.0.0-alt4
- new version (6.0.0-4)
- added dotty support

* Tue Apr 13 2004 Anton Farygin <rider@altlinux.ru> 6.0.0-alt1
- new version (6.0.0)

* Tue Dec 02 2003 Rider <rider@altlinux.ru> 5.5.7-alt4
- update to 5.5.7-13
- removed .la files from devel package

* Mon Sep 22 2003 Rider <rider@altlinux.ru> 5.5.7-alt3
- icons added for menu item (display), bug #1627
- removed wrong buildrequires (libexif-devel >= exif_ver)

* Tue Sep 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 5.5.7-alt2
- rebuild with new libexif-0.5.12

* Thu Aug 07 2003 Rider <rider@altlinux.ru> 5.5.7-alt1
- new version

* Wed Jan 15 2003 Rider <rider@altlinux.ru> 5.4.9-alt8
- requires fix (bug #0001819)

* Mon Dec 23 2002 Rider <rider@altlinux.ru> 5.4.9-alt7
- bugfix rebuild

* Fri Dec 20 2002 Rider <rider@altlinux.ru> 5.4.9-alt6
- BuildReq fix
- rebuild with new libwmf

* Mon Dec 09 2002 Rider <rider@altlinux.ru> 5.4.9-alt5
- fix for previos bugfix

* Tue Nov 19 2002 Rider <rider@altlinux.ru> 5.4.9-alt4
- PostScript generation bugfix (LC_MONETARY set to POSIX)

* Mon Nov 18 2002 Rider <rider@altlinux.ru> 5.4.9-alt3
- rebuild (new perl)

* Tue Oct 08 2002 Rider <rider@altlinux.ru> 5.4.9-alt2
- 5.4.9-1
- fixed bug #0001341

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 5.4.9-alt1
- 5.4.9
- fixed bug #0001341

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 5.4.8-alt2.1
- rebuild with new XFree86

* Fri Sep 06 2002 Rider <rider@altlinux.ru> 5.4.8-alt2
- 5.4.8-3

* Fri Aug 23 2002 Rider <rider@altlinux.ru> 5.4.8-alt1
- 5.4.8

* Thu Jun 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 5.4.6-alt1
- 5.4.6
- Some spec cleanup

* Sat Jun 01 2002 Rider <rider@altlinux.ru> 5.4.5.1-alt1
- 5.4.5.1

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 5.4.4.5-alt1
- 5.4.4-5

* Mon Apr 08 2002 Rider <rider@altlinux.ru> 5.4.4.4-alt1
- 5.4.4-4

* Sun Mar 10 2002 Rider <rider@altlinux.ru> 5.4.3.11-alt1
- 5.4.3-11

* Sun Feb 24 2002 Rider <rider@altlinux.ru> 5.4.3-alt2
- 5.4.3-5

* Tue Feb 19 2002 Rider <rider@altlinux.ru> 5.4.3-alt1
- 5.4.3-1
- buildreq fix
- remove lcms patch(#4)

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 5.4.2-alt1
- 5.4.2-3

* Thu Oct 11 2001 AEN <aen@logic.ru> 5.3.9-alt2
- Rebuilt with libpng.so.3

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 5.3.9-alt1
- 5.3.9

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.3.3-alt4
- Rebuild with new perl.
- Corrected libification.

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 5.3.3-alt3
- Rebuilt with perl-5.6.1

* Fri May 11 2001 Rider <rider@altlinux.ru> 5.3.3-alt2
- libifications

* Mon May 07 2001 Rider <rider@altlinux.ru> 5.3.3-alt1
- 5.3.3

* Tue Mar 03 2001 Rider <rider@altlinux.ru> 5.3.1-alt1
- 5.3.1

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 5.2.9-ipl1mdk
- 5.2.9
- Fixed bz2 support.
- RE adaptions.

* Mon Jan 30 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 5.2.8-1mdk
- release 5.2.8.
- removed ImageMagick-5.2.7-ps.patch (now merged), and ltdl patch.
- removed option --enable-16bit-pixel in configure, now default.

* Wed Jan 24 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 5.2.7-5mdk
- added liblcms.

* Tue Jan 24 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 5.2.7-4mdk
- added Imagemagick-5.2.7-ps.patch from ImageMagick CVS to fix the
  Camille's problems.
- added patch11 for perl-magick linking.

* Fri Jan 19 2001 David BAUDENS <baudens@mandrakesoft.com> 5.2.7-3mdk
- Fix (once again) build on PPC
- Don't "BuildRequires: " things which are not designed for PPC
- Spec clean up

* Tue Jan 16 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 5.2.7-2mdk
- fixed problems with EPS delegates.

* Sun Jan 14 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 5.2.7-1mdk
- new release.
- added support for HDF5, lcms, jbig formats.
- more BuildRequires.

* Sun Dec 17 2000 David BAUDENS <baudens@mandrakesoft.com> 5.2.6-2mdk
- Fix again build for PPC
- bzip2 patches
- Really use optimizations

* Tue Dec 05 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 5.2.6-1mdk
- new and shiny version bumped into cooker.
- remove the self compile patch.
- build with freetype2.

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 5.2.5-3mdk
- Fix URL

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 5.2.5-2mdk
- Fix build for PPC

* Tue Oct 31 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.2.5-1mdk
- s/5.2.4/5.2.5/

* Sun Oct 15 2000 Geoffrey Lee <snailtlak@mandrakesoft.com> 5.2.4-1mdk
- s/5.2.3/5.2.4/ aka new shiny ImageMagick.

* Mon Oct  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.2.3-3mdk
- don't BuildRequires on ImageMagick-devel.

* Wed Sep 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.3-2mdk
- build release

* Mon Aug 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.2.3-1mdk
- s|5.2.2|5.2.3|.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.2.2-6mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Pixel <pixel@mandrakesoft.com> 5.2.2-5mdk
- put *.la back to main package (otherwise doesn't work!)
- use %%perl_sitearch
- /usr/lib/ImageMagick and subdirs now belongs to main package

* Fri Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.2.2-4mdk
- put module *.so files in the main package while *.la and *.a go to devel

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.2-3mdk
- split out modules in -lib packages for lord rpmlint (gl scks)

* Mon Jul 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.2.2-2mdk
- build withmodules (titiscks)
- license is opensource
- should be ./configure --prefix=_prefix not /usr (titiscks)

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.2-1mdk
- new release

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.1-1mdk
- new release
- BM (this one give me an hard time :-( thanks for the gift)

* Thu Jul 06 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.0-6mdk
- since Lord Chmou've upload my test rpm without asking me before whereas it
  was bogus, i make a new release.
  Language lab, lesson 6, repeat after me : chmou sucks :-)

* Wed Jul 05 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.2.0-5mdk
- built against new libbz2

* Wed Jun 28 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 5.2.0-4mdk
- Changed i386 into %_arch in filelist

* Fri Jun 23 2000 Vincent Saugey <vince@mandrakesoft.com> 5.2.0-3mdk
- Correct %%file of perl-Magick no more empty pod.

* Thu Jun 22 2000 Vincent Saugey <vince@mandrakesoft.com> 5.2.0-2mdk
- Correct local file owner in perl-Magick.

* Wed Jun  7 2000 Vincent Saugey <vince@mandrakesoft.com> 5.2.0-1mdk
- Up to 5.2.0

* Wed May 10 2000 Stefan Siegel <siegel@linux-mandrake.com>
- Split ImageMagick-devel in ImageMagick-devel and perl-Magick.
- moved Magick-config to ImageMagick-devel.

* Wed Apr 26 2000 Vincent Saugey <vince@mandrakesoft.com> 5.1.1-7mdk
- Change prefix to /usr.
- Update to second version 5.1.1 of wizard.dupont.
- Move include files in %_includedir/magick.
- Remove entry menu for display (needs a terminaux stdin)
- Now, compile alone (with good librairie in rpm build dir)

* Wed Apr 19 2000 Vincent Saugey <vince@mandrakesoft.com> 5.1.1-6mdk
- Doc file slipt into the two package.

* Mon Apr 17 2000 Vincent Saugey <vince@mandrakesoft.com> 5.1.1-5mdk
- Patch ltconfig to remove rpath.

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.1.1-4mdk
- Really apply patch.

* Thu Apr  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.1.1-3mdk
- Prereq: /sbin/ldconfig.
- Add menu.
- Adjust groups.
- No need to do Ctrl-q to quit (just q or c-q if you really want).

* Wed Feb 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.1.1-2mdk
- Recompile ImageMagick-devel with the right 5.1.1 devel.

* Thu Jan 13 2000 Vincent Saugey <vince@mandrakesoft.com>
- update to 5.1.0
- Add documentation ImageMagick.pdf

* Mon Nov 01 1999 Vincent Saugey <vincent@mandrakesoft.com>
- 4.2.9
- ImageMagick now supports native blob support for most of the image formats.
- Enable accented letters in text for Postscript fonts
- Broke up some of the large source modules into smaller more managable modules.
- Added methods CreateImage and GetPixels to make using float arrays of pixels easier.
- Fixed GS delegate to get around a Ghostscript bug for device pnmraw (bug report by Thomas Baker).
- Added ImageMagick User's Guide to the distribution. See ImageMagick/docs directory.
- Drawing primitives are antialiased now
- Several API changes were made to accomodate Magick++, the C++ ImageMagick API wrapper
- Several API changes were made to make the ImageMagick API thread safe.
- Many others changes

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Handle SMP compilation.
- 4.2.7.
- Remove unused patch.

* Tue May 04 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 4.2.3
- Mandrake adaptions
- add de locale

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- include the perl man pages as well

* Tue Apr 06 1999 Michael K. Johnson <johnsonm@redhat.com>
- remove --enable-16bit because it damages interoperability

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- update to 4.2.2
- change ChangeLog to refer to actual dates.
- strip binaries

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- add more files. Oops.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Wed Mar 10 1999 Bill Nottingham <notting@redhat.com>
- version 4.2.1

* Tue Jan 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed group

* Tue Jan 19 1999 Cristian Gafton <gafton@redhat.com>
- hacks to make it work with the new perl
- version 4.1.0 (actually installs the sonames as 4.0.10... doh!)
- make sure the libraries have the x bit on

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.5

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.4
- added BuildRoot

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 3.8.3 to 3.9.1
- removed PNG patch (appears to be fixed)

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- updated to version 3.8.3.
- updated source and url tags.
