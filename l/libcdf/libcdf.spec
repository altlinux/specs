%define oversion 33_0
Name: libcdf
Version: 3.3.0
Release: alt4

Summary: Common Data Format (CDF)

License: BSD-like
Group: System/Libraries
Url: http://cdf.gsfc.nasa.gov

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://cdaweb.gsfc.nasa.gov/pub/cdf/dist/latest-release/linux/cdf%oversion-dist-all.tar
Source1: http://cdf.gsfc.nasa.gov/html/FAQ.html

Patch: %name-autotools.patch

# Automatically added by buildreq on Fri Oct 29 2010
BuildRequires: glibc-devel libncurses-devel

%package devel
Summary: Development tools for the CDF library
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Development tools for the CDF library
Group: Development/C
Requires: %name-devel = %version-%release

%description
CDF is the Common Data Format.  It is a conceptual data abstraction for
storing, manipulating, and accessing multidimensional data sets.  The basic
component of CDF is a software programming interface that is a device-
independent view of the CDF data model.  The application developer is
insulated from the actual physical file format for reasons of conceptual
simplicity, device independence, and future expandability.  CDF files
created on any given platform can be transported to any other platform onto
which CDF is ported and used with any CDF tools or layered applications.

The CDF software, documentation, and user support services are provided
by NASA and available to the public free of charge. There are no license
agreements or costs involved in obtaining or using CDF.

%description devel
The static libraries, header files and documentation for using the
CDF library in applications.

If you want to develop applications which will use the CDF library,
you'll need to install the %name-devel package.  You'll also need to
install the %name package.

%description devel-static
This package contains static libraries for developing with CDF library.

%prep
%setup -n cdf%oversion-dist-all
%patch -p2
cp %SOURCE1 FAQ.html
cp CDF_copyright.txt COPYING
cp CHANGES.txt ChangeLog
touch NEWS README AUTHORS
rm -rf cdfjava/lib

%build
%ifarch %e2k armh aarch64 loongarch64
%add_optflags -DIBMPC
%endif

%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%_bindir/*
%_datadir/cdf/
%_libdir/*.so.*
%doc CHANGES.txt Release.notes FAQ.html README.* CDF_copyright.txt Help.*

%files devel
%_includedir/cdf.h
%_libdir/*.so
%doc samples cdfjava

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sun Oct 29 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.3.0-alt4
- NMU: fixed FTBFS (use pkg-config to ask for ncurses libs/cflags)

* Mon Sep 20 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.3.0-alt3
- fixed build for Elbrus and ARM

* Tue Aug 28 2012 Repocop Q. A. Robot <repocop@altlinux.org> 3.3.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * macos-resource-fork-file-in-package for libcdf-devel

* Mon Feb 28 2011 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt2
- rebuild with debuginfo

* Thu Oct 28 2010 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- new version (3.3.0) import in git (ALT bug #24424)
- create patch with autotools

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 3.2.3-alt2
- enable build test and run it

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 3.2.3-alt1
- new version 3.2.3
- use autotools instead distributed Makefiles

* Mon Dec 01 2003 Yury A. Zotov <yz@altlinux.ru> 2.7-alt3
- Do not package .la files.
- Do not package devel-static by default.

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt2
- rebuild with gcc3

* Mon Jun 18 2001 Yury A. Zotov <yz@altlinux.ru> 2.7-alt1
- Initial revision.

