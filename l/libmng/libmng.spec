Name: libmng
Version: 2.0.3
Release: alt3

Summary: A library for handling MNG files
License: Zlib
Group: System/Libraries
Url: https://sourceforge.net/projects/libmng/

# http://downloads.sourceforge.net/libmng/libmng-%version.tar.bz2
Source: libmng-%version.tar
Patch1: libmng-1.0.10-alt-build-fixes.patch
Patch2: libmng-1.0.10-alt-player-build.patch
Patch3: libmng-2.0.3-debian-linux-makefile.patch
BuildRequires: gcc-c++ libjpeg-devel liblcms2-devel zlib-devel

%package devel
Summary: Include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description
The MNG library supports decoding, displaying, encoding, and various
other manipulations of the Multiple-image Network Graphics (MNG) format
image files. It uses the zlib compression library, and optionally the
JPEG library by the Independent JPEG Group (IJG) and/or lcms (little cms),
a color-management library by Marti Maria Saguar.

%description devel
The MNG library supports decoding, displaying, encoding, and various
other manipulations of the Multiple-image Network Graphics (MNG) format
image files. It uses the zlib compression library, and optionally the
JPEG library by the Independent JPEG Group (IJG) and/or lcms (little cms),
a color-management library by Marti Maria Saguar.

This package contains include files required for development %name-based
applications.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp makefiles/Makefile.am .
%autoreconf
%configure --enable-shared --disable-static \
	--with-zlib --with-jpeg --with-lcms
%make_build

%install
mkdir -p %buildroot%_mandir/man{3,5}
%makeinstall

pushd doc/man
	install -pm644 *.3 %buildroot%_man3dir/
	install -pm644 *.5 %buildroot%_man5dir/
popd

%files
%_libdir/*.so.*
%_man5dir/*
%doc CHANGES LICENSE README README.contrib README.examples
%doc doc/*.* contrib/gcc/gtk-mng-view/*.mng

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_mandir/man3/*

%changelog
* Fri Nov 29 2024 Anton Farygin <rider@altlinux.ru> 2.0.3-alt3
- FTBFS: unused utils package was removed
- fixed License

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 2.0.3-alt2
- removed ubt macros

* Thu May 11 2017 Anton Farygin <rider@altlinux.ru> 2.0.3-alt1
- new version

* Thu Oct 20 2016 Anton Farygin <rider@altlinux.ru> 1.0.10-alt3
- Build with lcms2

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt2.2
- Fixed build

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt2.1
- Fixed build

* Mon Apr 18 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.10-alt2
- Dropped libmng-devel-static.
- Updated build dependencies.

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 1.0.10-alt1.4
- Rebuilt for debuginfo

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.3
- Rebuilt for soname set-versions

* Tue Nov 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.10-alt1.2
- rebuilt

* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.10-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmng
  * postun_ldconfig for libmng

* Wed Sep 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.10-alt1
- Updated to 1.0.10.
- Fixed build.

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.9-alt1
- Updated to 1.0.9.
- Updated patches.
- Fixed multilib support (mouse).

* Mon Mar 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.8-alt3
- Reimplemented previous change.

* Thu Mar 17 2005 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- build libmng-mini.a for bootsplash (SuSE).

* Tue Oct 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Dec 17 2003 Stanislav Ievlev <inger@altlinux.org> 1.0.6-alt1
- 1.0.6

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.4-alt3
- rebuild with new XFree86

* Mon Sep 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.4-alt2
- rebuild with gcc3

* Tue Jul 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- 1.0.4.

* Fri Feb 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.3-alt2
- Fixed build on kernel headers which define "linux" macro.

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.3-alt1
- 1.0.3.

* Mon Jul 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.2-alt1
- 1.0.2.

* Mon Apr 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.0-ipl2mdk
- Moved static libraries to devel-static subpackage.
- Rebuilt with libSDL-1.2.0.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.0-ipl1mdk
- 1.0.0

* Tue Feb 06 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.4-ipl1mdk
- 0.9.4
- Build with lcms support.
- Build mng utilities.

* Wed Dec 20 2000 AEN <aen@logic.ru>
- back to old lib name
- adopted for RE

* Fri Nov 24 2000 David BAUDENS <baudens@mandrakesoft.com> 0.9.3-2mdk
- Make compliant to new LMDK lib policy

* Tue Nov 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.9.3-1mdk
- First package for Linux-Mandrake distribution
