Name: mpfr
Version: 3.1.0
Release: alt2

Summary: Multiple Precision Floating-Point library
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.mpfr.org/

# Don't build static library by default
%def_disable static

BuildRequires: libgmp-devel

# http://www.mpfr.org/mpfr-current/mpfr-%version.tar.bz2
Source0: mpfr-%version.tar
Source1: mpfrxx.h

Patch: mpfr-%version-%release.patch

%define libmpfr libmpfr4

%package -n %libmpfr
Summary: Multiple Precision Floating-Point library
License: LGPLv2.1+
Group: System/Libraries
Provides: libmpfr = %version
Obsoletes: libmpfr

%package -n libmpfr-devel
Summary: Development MPFR library, header files and documentation
License: LGPLv2.1+, FDLv1.1+
Group: Development/C
Requires: %libmpfr = %version-%release
Requires: libgmp-devel
Conflicts: libgmp-devel = 0:4.1.4-alt3

%package -n libmpfr-devel-static
Summary: Static MPFR library
License: LGPLv2.1+
Group: Development/C
Requires: libmpfr-devel = %version-%release

%description
MPFR provides a library for multiple-precision floating-point
computation with correct rounding.  The computation is both efficient
and has a well-defined semantics.  It copies the good ideas from the
ANSI/IEEE-754 standard for double-precision floating-point arithmetic
(53-bit mantissa).

%description -n %libmpfr
MPFR provides a library for multiple-precision floating-point
computation with correct rounding.  The computation is both efficient
and has a well-defined semantics.  It copies the good ideas from the
ANSI/IEEE-754 standard for double-precision floating-point arithmetic
(53-bit mantissa).

%description -n libmpfr-devel
This package provides the header files and the symbolic links necessary
to allow compilation and linking of programs that use the libraries
provided by %libmpfr package.

%description -n libmpfr-devel-static
This package provides static library necessary to allow static linking
of MPFR-based programs.

%prep
%setup
rm m4/l*.m4
%patch -p1
awk '/__MPFR_DECLSPEC/{decl=1}decl&&/_MPFR_PROTO/{decl=0;print}' src/mpfr.h |
	sed -n 's/^.*[[:space:]*]\+\([^[:space:]*]\+\)[[:space:]]\+_MPFR_PROTO.*/\1/p' \
	>>src/libmpfr.sym
sort -u -o src/libmpfr.sym{,}

%build
%autoreconf
%define docdir %_docdir/mpfr-%version
%configure --enable-shared %{subst_enable static} --docdir=%docdir
%make_build

%install
%makeinstall_std
install -pm644 %_sourcedir/mpfrxx.h %buildroot%_includedir/

%check
%make_build -k check

%files -n %libmpfr
%_libdir/*.so.*
%dir %docdir
%docdir/[ABN]*
%exclude %docdir/COPYING*

%files -n libmpfr-devel
%_libdir/*.so
%_includedir/*
%_infodir/*
%dir %docdir
%docdir/[FTe]*

%if_enabled static
%files -n libmpfr-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jun 06 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.0-alt2
- Updated to v3.1.0-p10.
- Renamed libmpfr to libmpfr4.

* Fri Feb 18 2011 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt3
- Rebuilt for debuginfo.

* Wed Oct 13 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt2
- Rebuilt for soname set-versions.

* Thu Jun 17 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt1
- Updated to 2.4.2-p3.

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 2.4.1-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.
- Moved "make check" to %%check section.

* Fri Apr 17 2009 Dmitry V. Levin <ldv@altlinux.org> 2.4.1-alt1
- Updated to 2.4.1-p5.

* Thu Jan 08 2009 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt2
- mpfr.texi: Recoded from ISO-8859-1 to UTF-8.
- Packaged %%docdir.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt1
- Updated to 2.3.2.
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Mon Mar 17 2008 Dmitry V. Levin <ldv@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1.
- Restricted list of global symbols exported by the library to only those
  which are either declared in mpfr.h file or required by test suit.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1-p5.

* Sat Apr 22 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt1
- Packaged for Sisyphus.
