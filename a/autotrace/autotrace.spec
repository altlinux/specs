%define soname 3
%def_with pstoedit
%def_disable static
%def_disable magick
%define pstoedit_ver 3.32

Name: autotrace
Version: 0.31.10
Release: alt3

Summary: Bitmap to vector graphics converter
Summary(ru_RU.UTF-8): Программа трассировки растровых изображений.
Group: Graphics
License: GPLv2+ and LGPLv2+
Url: https://github.com/autotrace/autotrace
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
%if_with pstoedit
BuildPreReq: libpstoedit-devel >= %pstoedit_ver
%endif
BuildRequires: libImageMagick-devel libpng-devel
BuildRequires: glib2-devel
BuildRequires: gettext-devel
BuildRequires: libstdc++-devel
BuildRequires: intltool

%description
The aim of the AutoTrace project is the development of a freely
available application with a functionality similar to CorelTrace or
Adobe Streamline. I hope that it will become better than all
commercially available programs. In some aspects it is already better.

Supported formats:
Input BMP, TGA, PNM, PPM, PGM, PBM and those supported by ImageMagick.
Export Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm, mif, p2e and sk

%description -l ru_RU.UTF-8
%name - программа преобразования растровых изображений в векторные.

Поддерживаемые форматы:
Растровые: BMP, TGA, PNM, PPM, PGM, PBM и прочие, поддерживаемые программой ImageMagick.
Векторные: Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm, mif, p2e и sk

%package -n lib%name%soname
Summary: Shared library for %name
Group: System/Libraries
Obsoletes: libautotrace < 0.31.10
Conflicts: libautotrace < 0.31.10

%description -n lib%name%soname
Shared library needed to run %name.

%package -n lib%name-devel
Summary: Development package of %name
Group: Development/C
Requires: lib%name%soname = %EVR
Requires: libImageMagick-devel
%if_with pstoedit
Requires: libpstoedit-devel >= %pstoedit_ver
%endif

%description -n lib%name-devel
Headers files needed to compile programs using lib%name.

%package -n lib%name-devel-static
Summary: Static version of lib%name
Group: System/Libraries
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static library required for packaging statically
linked software using lib%name.

%prep
%setup
%patch0 -p1

%build
autoreconf -fisv
%configure \
	%{subst_enable static} \
	%{subst_enable magick} \
%if_without pstoedit
	--without-pstoedit
%endif
	%nil

%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%doc README* NEWS AUTHORS ChangeLog THANKS
%_bindir/%name
%_man1dir/*

%files -n lib%name%soname
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Jul 02 2024 Anton Farygin <rider@altlinux.ru> 0.31.10-alt3
- added Conflicts and Obsoltes with libautotrace 0.31.1 and earlier

* Fri Jun 28 2024 Anton Farygin <rider@altlinux.ru> 0.31.10-alt2
- fix pkcconfig file

* Fri Jun 28 2024 Anton Farygin <rider@altlinux.ru> 0.31.10-alt1
- returned to ALT with the new upstream

* Fri May 06 2016 Anton Farygin <rider@altlinux.ru> 0.31.1-alt6
- fixed CVE-2013-1953

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.31.1-alt5
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.31.1-alt4
- Rebuild with new libImageMagick

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 0.31.1-alt3
- cleanup spec
- add patch from gentoo for fix build with new libpng

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.4.1
- Rebuild with new libImageMagick

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.4
- rebuild with new libImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.3
- rebuild with new libImageMagick

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.31.1-alt2.2
- Removed obsolete post_ldconfig/postun_ldconfig calls.
- Rebuilt with libMagickCore.so.2.

* Sat Dec 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt2.1
- Automated rebuild with libImageMagick-6.4.x.

* Mon Jan 08 2007 Yury Aliaev <mutabor@altlinux.org> 0.31.1-alt2
- Fixed for modern Sisyphus building environment (much thanks to Debian people :))

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.6.1
- Rebuilt for new pkg-config dependencies.

* Thu Sep 15 2005 Anton Farygin <rider@altlinux.ru> 0.31.1-alt1.6
- rebuild with libMagick.so.9

* Mon Sep 12 2005 Anton Farygin <rider@altlinux.ru> 0.31.1-alt1.5
- rebuild with new libImageMagick

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.4.1.1
- Rebuilt with libstdc++.so.6.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.4.1
- Rebuilt with libtiff.so.4.

* Thu May 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.4
- fixed build.

* Thu Dec 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.3
- do not package .la files.
- devel-static subpackage is optional. 

* Tue Sep 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.2
- rebuild due ImageMagick depends on new libexif.

* Mon Sep 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.1
- updated buildreqs.

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1
- 0.31.1

* Fri Oct 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.31.0-alt1
- 0.31.0

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.30.5-alt0.5cvs20020917
- fix changelog entry

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.30.5-alt0.5
- 0.30.5 from cvs
- built w/o libming (SWF output disabled) and pstoedit support.
- we have shared library now.

* Thu Apr 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.30-alt0.5
- 0.30

* Sat Mar 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.29-alt0.5
- First build for Sisyphus w/o shared library (makefile don't 
  supports it) and w/o swf-output support, it requires libming.
