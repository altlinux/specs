# FIXME: (build without libMagick)
#trgt_magickpp.cpp:58: error: 'MagickLib' has not been declared
#trgt_magickpp.cpp:58: error: expected constructor, destructor, or type conversion before '*' token
#trgt_magickpp.cpp: In destructor 'virtual magickpp_trgt::~magickpp_trgt()':

%define oname synfig

Name:    libsynfig
Version: 1.1.9
Release: alt1

Summary: Vector-based 2D animation software package

License: free
Group:   Development/C++
Url:     http://www.synfig.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %oname-%version.tar

BuildRequires: ImageMagick-tools cvs fontconfig-devel gcc-c++ libavformat-devel
BuildRequires: libetl-devel libfreetype-devel libjpeg-devel libltdl7-devel
BuildRequires: libmng-devel libpng-devel libswscale-devel libxml++2-devel openexr-devel 
BuildRequires: libtiff-devel libImageMagick-devel libsigc++2-devel
BuildRequires: libcairo-devel libpango-devel boost-devel boost-program_options-devel
BuildRequires: libmlt++-devel boost-filesystem-devel
BuildRequires: libfftw3-devel

%description
Synfig is a powerful, industrial-strength vector-based 2D animation
software package, designed from the ground-up for producing
feature-film quality animation with fewer people and resources.
While there are many other programs currently on the market to aid
with the efficient production of 2D animation, we are currently
unaware of any other software that can do what our software can.

%package devel
Summary: Header files for Synfig
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for Synfig.

%prep
%setup -q -n %oname-%version

%build
%autoreconf
%add_optflags -fpermissive -std=c++11
%configure
%make_build

%install
%makeinstall_std
%find_lang %oname

%files -f %oname.lang
%_bindir/%oname
%_sysconfdir/synfig_modules.cfg
%_libdir/lib*.so.*
%_libdir/%oname/

%files devel
%_bindir/%oname-config
%_includedir/synfig-1.0/
%_pkgconfigdir/*
%_libdir/lib*.so

%changelog
* Sat Jun 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version
- Spec cleanup

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version

* Tue Feb 17 2015 Anton Farygin <rider@altlinux.ru> 0.64.3-alt2
- rebuild with new libImageMagick

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.64.3-alt1.1
- rebuild with boost 1.57.0

* Fri Dec 26 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.3-alt1
- New version

* Mon Nov 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.2-alt1
- New version

* Thu Oct 23 2014 Anton Farygin <rider@altlinux.ru> 0.64.1-alt3
- rebuild with new ImageMagick

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.64.1-alt2
- rebuild with new ImageMagick

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.1-alt1
- New version

* Tue Jul 30 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.0-alt1
- New version

* Mon Feb 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.63.05-alt1
- New version 0.63.05

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.63.03-alt1.1
- Fixed build with gcc 4.7

* Thu Jan 12 2012 Yuriy Shirokov <yushi@altlinux.org> 0.63.03-alt1
- new version 0.63.03

* Mon Oct 10 2011 Yuriy Shirokov <yushi@altlinux.org> 0.63.02-alt1
- new version 0.62.02

* Sun Jun 19 2011 Yuriy Shirokov <yushi@altlinux.org> 0.63.00-alt1
- new version 0.63.00

* Sat Dec 18 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.02-alt1
- new version 0.62.02

* Sun Nov 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt2
- patch for gcc-4.5

* Sat Jun 5 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt1
- new version 0.62.01

* Wed Apr 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt2
- spec cleanup

* Tue Mar 23 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt1
- new version 0.62.00

* Tue Mar 23 2010 Yuriy Shirokov <yuriy.shirokov@gmail.com> 0.61.09-uri1
- bug with PixelFormat convertion fixed

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 0.61.09-alt3
- fix build with new toolchain
- update buildreqs

* Wed Dec 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.09-alt2
- rebuild without ImageMagick

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.09-alt1
- new version 0.61.09 (with rpmrb script)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.08-alt2
- pack lang files
- update buildreqs, add autoreconf
- build with external ltdl (AC_LIBLTDL_INSTALLABLE)

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.08-alt1
- new version 0.61.08 (with rpmrb script)

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.07-alt3
- pack .so in devel package

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.07-alt2
- fix compiling with libavcodec-devel

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.07-alt1
- new version 0.61.07 (with rpmrb script)

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.06-alt1
- new version 0.61.06 (with rpmrb script)

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.05-alt1
- initial build for ALT Linux Sisyphus

