Name: libmpfr1
Version: 2.4.2
Release: alt4

Summary: Multiple Precision Floating-Point library
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.mpfr.org/

Provides: libmpfr = %version-%release
Obsoletes: libmpfr
BuildRequires: libgmp-devel

# http://www.mpfr.org/mpfr-%version/mpfr-%version.tar.bz2
Source: mpfr-%version.tar

Patch: mpfr-%version-%release.patch

%description
MPFR provides a library for multiple-precision floating-point computation
with correct rounding.  The computation is both efficient and has a
well-defined semantics.  It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit mantissa).

%prep
%setup -n mpfr-%version
rm m4/l*.m4
%patch -p1
awk '/__MPFR_DECLSPEC/{decl=1}decl&&/_MPFR_PROTO/{decl=0;print}' mpfr.h |
	sed -n 's/^.*[[:space:]*]\+\([^[:space:]*]\+\)[[:space:]]\+_MPFR_PROTO.*/\1/p' \
	>>libmpfr.sym
sort -u -o libmpfr.sym{,}

%build
%autoreconf
%define docdir %_docdir/mpfr-%version
%configure --enable-shared --disable-static --docdir=%docdir
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[ABN]*
%exclude %docdir/COPYING*

%changelog
* Wed Jun 06 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt4
- Packaged libmpfr1 compatibility library.

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
