Name: libchm
Version: 0.40
Release: alt4

Summary: chmlib is a small library designed for accessing MS ITSS files
License: LGPLv2.1+
Group: System/Libraries

URL: http://www.jedrea.com/chmlib
Source: %url/chmlib-%version.tar.bz2
Patch0: chmlib-0.39-alt-ppc.patch

# Automatically added by buildreq on Wed Feb 14 2007
BuildRequires: gcc-c++

%description
chmlib is a small library designed for accessing MS ITSS files. The ITSS file
format is used for Microsoft Html Help files (.chm), which have been the
predominant medium for software documentation from Microsoft during the past
several years, having superceded the previously used .hlp file format. Note that
this is NOT the same as the OLE structured storage file format used by MS Excel,
Word, and so on. Instead, it is a different file format which fulfills a similar
purpose.

%package devel
Summary: Development files for libchm
License: LGPLv2.1+
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for packaging libchm-based
software.

%package utils
Summary: Utilities that uses libchm
License: LGPLv2.1+
Group: Office
Requires: %name = %version-%release

%description utils
This package contains example utility programs that use chmlib.

%prep
%setup -n chmlib-%version
%patch0 -p1

%build
%configure --enable-examples --disable-static
# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std

%files
%_libdir/libchm.so.*

%files devel
%_includedir/*
%_libdir/*.so

%files utils
%_bindir/*

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.40-alt4
- Fix RPATH issue.

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40-alt3
- Rebuilt for debuginfo

* Mon Nov 01 2010 Victor Forsiuk <force@altlinux.org> 0.40-alt2
- Rebuilt for soname set-versions.

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.40-alt1
- 0.40

* Thu Feb 26 2009 Victor Forsyuk <force@altlinux.org> 0.39-alt4
- Fix powerpc build.

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 0.39-alt3
- Remove obsolete ldconfig calls.

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 0.39-alt2
- Build example utils (needed for chm2pdf).

* Wed Feb 14 2007 Victor Forsyuk <force@altlinux.org> 0.39-alt1
- Security fix: CVE-2007-0619.
- Update URL.

* Sat Jun 17 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.38-alt1
- 0.38

* Mon Oct 31 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.37.4-alt1
- new version

* Fri Oct 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.37.3-alt1
- new version

* Sat Sep 10 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.36-alt1
- 0.36

* Tue May 10 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.35-alt2
- update license

* Sun Jul 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.35-alt1
- new version

* Fri May 14 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.33-alt1
- new version

* Tue May 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.32-alt1
- new version
- Minor portability fixes for Windows CE
- Minor bugfix regarding detecting directory entries versus empty files
- autoconf-based build process
- Simple makefile has been fixed (finally) to use gcc instead of gcc-3.2

* Sat Jan 3 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.31-alt3
- rebuild with gcc-3.3

* Fri Sep 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.31-alt2
- Add build requires

* Tue Aug 5 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.31-alt1
- First version of RPM package.
