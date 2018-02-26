# FIXME: (build without libMagick)
#trgt_magickpp.cpp:58: error: 'MagickLib' has not been declared
#trgt_magickpp.cpp:58: error: expected constructor, destructor, or type conversion before '*' token
#trgt_magickpp.cpp: In destructor 'virtual magickpp_trgt::~magickpp_trgt()':

%define oname synfig

Name: libsynfig
Version: 0.63.03
Release: alt1

Summary: Vector-based 2D animation software package

License: free
Group: Development/C++
Url: http://www.synfig.org/

Packager: Yuriy Shirokov <yushi@altlinux.org>

#Source: http://www.bridgetone.com/voria/files/%oname-%version.tar.bz2
#Source: http://prdownloads.sf.net/synfig/%oname-%version.tar.gz
Source: %oname-%version.tar

# Automatically added by buildreq on Wed Jun 03 2009
BuildRequires: ImageMagick-tools cvs fontconfig-devel gcc-c++ libavformat-devel libetl-devel libfreetype-devel libjpeg-devel libltdl7-devel libmng-devel libpng-devel libswscale-devel libxml++2-devel openexr-devel

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
%__libtoolize  --copy --force
autoreconf --install --force
%configure
#%__subst "s|\$(includedir)/synfig|\$(includedir)|g" src/synfig/Makefile
#%__subst "s|%_includedir/synfig-0.0|\$(pkgincludedir)/synfig-0.0|g" src/synfig/Makefile
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
%_includedir/synfig-0.0/
%_pkgconfigdir/*
%_libdir/lib*.so

%changelog
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

