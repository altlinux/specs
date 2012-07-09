%def_disable static

Name: vips
Version: 7.28.9
Release: alt1
%define majorver %(echo %version |cut -d. -f1,2)

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Large image processing library
License: LGPLv2.1
Group: Graphics

Url: http://www.vips.ecs.soton.ac.uk
Source0: %{name}-%{version}.tar.gz
Source100: vips.watch

BuildPreReq: libxml2-devel
# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: fontconfig fontconfig-devel glib2-devel ilmbase-devel libX11-devel libfreetype-devel libstdc++-devel libxml2-devel pkg-config python-base python-modules xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ gtk-doc imake libICE-devel libImageMagick-devel libcfitsio-devel libexif-devel libfftw3-devel libjpeg-devel liblcms-devel libmatio-devel liborc-devel libpango-devel libpng-devel libtiff-devel openexr-devel python-devel xorg-cf-files

%description
VIPS is an image processing library. It is good for very large
images (ie.  larger than the amount of RAM in your machine),
and for working with colour.  It includes a C++ API, complete
man pages, a command-line interface, automatic threading and
an operation database. There are several user interfaces built
on top of VIPS: for example "nip2".

%package -n lib%name
Summary: VIPS development kit
Group: System/Libraries

%package -n lib%name-devel
Summary: VIPS development kit
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 7.16.3-alt3

%package -n lib%name-devel-doc
Summary: VIPS development kit documentation
Group: Development/C
BuildArch: noarch

%if_enabled static
%package -n lib%name-devel-static
Summary: VIPS static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static < 7.16.3-alt3
%endif

%description -n lib%name
Shared libraries for VIPS.

%description -n lib%name-devel
Development libraries and header files for VIPS.

%description -n lib%name-devel-doc
This package contains development documentation for VIPS.

%if_enabled static
%description -n lib%name-devel-static
Static libraries for developing statically linked VIPS applications.
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std
%find_lang vips7

%files -f vips7.lang
%_bindir/*
%_man1dir/*
%_docdir/vips
%exclude %python_sitelibdir

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/vips/*
%_libdir/lib*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
#_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

# TODO:
# - package python bindings

%changelog
* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.9-alt1
- new version (watch file uupdate)

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 7.28.5-alt1.1
- Rebuild with new libImageMagick

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.5-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 7.28.4-alt1
- 7.28.4

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.26.7-alt1.1
- Fixed build

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 7.26.7-alt1
- 7.26.7
- drop RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 7.26.3-alt1
- 7.26.3 (thx fedorawatch)
- drop man3 following upstream
- built with orc, cfitsio

* Mon Apr 04 2011 Michael Shigorin <mike@altlinux.org> 7.24.4-alt1
- 7.24.4

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 7.24.2-alt1
- 7.24.2 (thanks force@)

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.4-alt1
- 7.22.4
- minor spec cleanup

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.3-alt1
- 7.22.3 fixes CVE-2010-3364 (insecure library loading);
  thanks crux@ for heads-up (closes: #24330)

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 7.22.2-alt1.1
- NMU: rebuild with new libImageMagick

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 7.22.2-alt1
- 7.22.2

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 7.20.4-alt1.1
- NMU: rebuild with new libImageMagick

* Thu Dec 03 2009 Victor Forsyuk <force@altlinux.org> 7.20.4-alt1
- 7.20.4
- Build with all libraries vips can make use of (fftw3, openexr etc).

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 7.18.2-alt1
- 7.18.2

* Fri Mar 20 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt1
- 7.16.4
- autoreconf

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt3
- performed libification
- disabled static subpackage by default
- added Packager:
- minor spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt2
- applied repocop patch

* Mon Nov 17 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt1
- 7.16.3

* Tue Oct 07 2008 Michael Shigorin <mike@altlinux.org> 7.16.2-alt1
- 7.16.2
- spec cleanup
- NB: this package seeks proper maintainer

* Tue Jun 21 2005 Anatoly Yakushin <jaa@altlinux.ru> 7.10.10-alt1
- new stable version

* Wed Mar 09 2005 Anatoly Yakushin <jaa@altlinux.ru> 7.10.8-alt1
- new stable version

* Wed Dec 17 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.9.0-alt2
- delete *.la files

* Thu Oct 23 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.9.0-alt1
- new version. spec clean

* Mon Sep 15 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt1
- new version

* Thu May 22 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.8-alt2
- bug fix spec file

* Thu May 08 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.8-alt1
- adapting spec from Sisyphus

* Mon Feb 3 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-2
- hack to change default install prefix to /usr/local

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.7-1
- first stab at an rpm package for vips
