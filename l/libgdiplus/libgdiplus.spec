%def_disable static
%def_without pango
%define cairo system

Name: libgdiplus
Version: 2.10.8
Release: alt1.1

Summary: An Open Source implementation of the GDI+ API.
License: MPL
Group: System/Libraries
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.mono-project.com/

Source0: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-2.10.8-alt-DSO.patch

BuildPreReq: glib2-devel >= 2.2.3
BuildPreReq: libcairo-devel >= 1.4.0
%{?_with_pango:BuildPreReq: libpango-devel >= 1.10.0}
BuildPreReq: fontconfig-devel libfreetype-devel libXrender-devel libX11-devel
BuildPreReq: libexif-devel libjpeg-devel libtiff-devel libungif-devel libpng-devel zlib-devel
BuildRequires: gcc-c++

%description
An Open Source implementation of the GDI+ API

%package devel
Summary: Development libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries and header files for developing against libgdiplus.

%prep
%setup -q
%patch -p1
%patch1 -p0

%build
#%%remove_optflags -Wall
NOCONFIGURE=1 ./autogen.sh --skip-cairo
%configure  \
%if %cairo == system
	--with-cairo=%cairo \
	%{?_with_pango:--with-pango} \
%endif
	%{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc COPYING NEWS README TODO MPL-1.1.html AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.8-alt1.1
- Fixed build

* Wed Feb 08 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.8-alt1
- 2.10.8

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 2.6.7-alt2
- snapshot of 2.6 branch (20101015)
- fixed CVE-2010-1526 (ALT #24399)

* Sun Aug 22 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.7-alt1
- 2.6.7

* Tue Apr 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Tue Jun 30 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- move libgdiplus.so to devel package

* Tue Jun 23 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1.1
- rebuild with libpng12

* Mon Apr 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Jan 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- removed obsolete pre/post macros

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0 release

* Fri Sep 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.rc1
- 2.0 RC1

* Sat Aug 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre2
- 2.0 preview2

* Mon Aug 11 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1
- add support for build with pango, but build without

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1
- 1.9

* Sun Dec 16 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6
- use a parameter --with-cairo=system for configure instead of patch

* Wed Sep 19 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt2
- move libgdiplus.pc to devel package 
- add post and postun  ldconfig
- mini fix spec

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Feb 23 2007 Ildar Mulyukov <ildar@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Wed Nov 15 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.2-alt1
- 1.2

* Mon Oct 02 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.1.17-alt1
- limited patch for system cairo
- added libexif support

* Tue Sep 26 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.1.13.6-alt2
- BuildRequires list fix

* Thu Mar 30 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.13.6-alt1
- Update to release
- Fix libcairo patch

* Sat Feb 04 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.13.2-alt1
- Update to release
- Fix build patch for using system libcairo

* Mon Nov 14 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release

* Wed Oct 05 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.2-alt1
- Update to 1.1.9.2

* Sat Jun 18 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.8-alt1
- Update to 1.1.8

* Sat May 14 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.7-alt1
- Update to 1.1.7

* Thu Sep 23 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0-alt1
- Initial build.
