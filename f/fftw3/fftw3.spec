Name: fftw3
Version: 3.3.7
Release: alt1

Summary: Library for computing Fast Fourier Transforms
License: GPLv2+
Group: System/Libraries
Url: http://www.fftw.org/

# ftp://ftp.fftw.org/pub/fftw/fftw-%version.tar.gz
Source: fftw-%version.tar
Patch: fftw-alt-link.patch

%def_enable check
%def_disable bigcheck
%def_disable quadcheck
%def_disable static
%def_enable openmp
%def_enable sse
%def_enable sse2
%def_enable avx
%ifarch %ix86 x86_64
%def_enable quad
%else
%def_disable quad
%endif

BuildRequires: gcc-fortran libgomp-devel %{?_enable_quad:libquadmath-devel}
BuildRequires: makeinfo

%description
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

%package -n libfftw3-common
Summary: FFTW runtime libraries, common files
Group: System/Libraries
BuildArch: noarch

%description -n libfftw3-common
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains common files for all FFTW runtime libraries.

%package -n libfftw3
Summary: FFTW runtime libraries, double precision
Group: System/Libraries
Requires: libfftw3-common = %version-%release

%description -n libfftw3
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains FFTW runtime libraries compiled in double precision.

%package -n libfftw3f
Summary: FFTW runtime libraries, single precision
Group: System/Libraries
Requires: libfftw3-common = %version-%release
Conflicts: libfftw3 < %version

%description -n libfftw3f
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains FFTW runtime libraries compiled in sing precision.

%package -n libfftw3l
Summary: FFTW runtime libraries, long double precision
Group: System/Libraries
Requires: libfftw3-common = %version-%release
Conflicts: libfftw3 < %version

%description -n libfftw3l
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains FFTW runtime libraries compiled in long double
precision.

%package -n libfftw3q
Summary: FFTW runtime libraries, quadruple precision
Group: System/Libraries
Requires: libfftw3-common = %version-%release

%description -n libfftw3q
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains FFTW runtime libraries compiled in quadruple
precision.

%package -n lib%name-devel
Summary: FFTW development libraries and header files
Group: Development/C
Requires: libfftw3 = %version-%release
Requires: libfftw3f = %version-%release
Requires: libfftw3l = %version-%release
%{?_enable_quad:Requires: libfftw3q = %version-%release}

%description -n lib%name-devel
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains header files, documentation, and development
libraries required to develop programs using the FFTW.

%package -n lib%name-devel-static
Summary: Static library for computing Fast Fourier Transforms
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains static libraries required to develop statically
linked programs using FFTW.

%package -n lib%name-devel-doc
Summary: FFTW library manual
Group: Development/C
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-doc
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains the manual for the FFTW fast Fourier transform
library in html and pdf formats.

%prep
%setup -n fftw-%version
rm m4/l*.m4
%patch -p1
rm doc/fftw3.info*

%build
sed -n 's/^[^X]*X(\([^[:space:])]\+\)).*/\1/p' threads/*.c |sort -u >threads-r
sed -n 's/^[^X]*X(\([^[:space:])]\+\)).*/\1/p' threads/threads.h |sort -u >threads-p
comm -13 threads-p threads-r >threads-need
while read n; do
	grep -lZ "^[^#[:space:]].*X($n)" -- */*.h |
	xargs -r0 sed -i '/EXTERN/! s/^[^#[:space:]].*X('$n')/__attribute__ ((visibility("default"))) &/' --
done < threads-need

%add_optflags -fvisibility=hidden
%autoreconf
options='--enable-shared %{subst_enable static} --enable-threads %{subst_enable openmp}'
options_single=
options_double=
options_long=
options_quad=
%ifarch %ix86 x86_64
options_single='%{subst_enable sse} %{subst_enable avx}'
options_double='%{subst_enable sse2} %{subst_enable avx}'
%endif
%define _configure_script ../configure

for m in single double long-double %{?_enable_quad:quad-precision}; do
	d=${m%%-*}
	mkdir $d
	pushd $d
	eval extraoptions="\"\$options_$d\""
	%configure $options $extraoptions --enable-$m
	%make_build
	popd
done

%install
for d in single double long %{?_enable_quad:quad}; do
	%makeinstall_std -C $d
done

# remove non-packaged files
rm %buildroot%_libdir/*.la

%define docdir %_docdir/fftw-%version
mkdir -p %buildroot%docdir
install -pm644 AUTHORS CONVENTIONS COPYRIGHT NEWS README \
	doc/fftw3.pdf doc/FAQ/fftw-faq.ascii %buildroot%docdir/
cp -a doc/html doc/FAQ/fftw-faq.html %buildroot%docdir/

%check
rm -f failed
for d in single double long %{?_enable_quadcheck:%{?_enable_quad:quad}}; do
	make %{?_enable_bigcheck:big}check -C $d/tests ||
		echo "$d failed" >> failed &
done
wait
if [ -f failed ]; then
	cat failed
	exit 1
fi

%files -n libfftw3-common
%dir %docdir/
%docdir/[ACNR]*
%docdir/*.ascii

%files -n libfftw3
%_libdir/libfftw3.so.*
%_libdir/libfftw3_*.so.*

%files -n libfftw3f
%_libdir/libfftw3f.so.*
%_libdir/libfftw3f_*.so.*

%files -n libfftw3l
%_libdir/libfftw3l.so.*
%_libdir/libfftw3l_*.so.*

%if_enabled quad
%files -n libfftw3q
%_libdir/libfftw3q.so.*
%_libdir/libfftw3q_*.so.*
%endif # quad

%files -n lib%name-devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_infodir/*.info*
%_man1dir/*
%_libdir/cmake/fftw3/

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-devel-doc
%dir %docdir/
%docdir/*html
%docdir/*.pdf

%changelog
* Sun Dec 10 2017 Dmitry V. Levin <ldv@altlinux.org> 3.3.7-alt1
- 3.3.3 -> 3.3.7.

* Fri Nov 15 2013 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt2
- %%check: disabled quad check by default,
  it takes too much time to complete.

* Mon Jan 21 2013 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt1
- Updated to 3.3.3.

* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.2-alt1
- Updated to 3.3.2.
- Enabled OpenMP support.
- Enabled SSE, SSE2, AVX and quadruple precision support on x86/x86-64.
- Packaged the manual in html in pdf formats into separate subpackage.
- Restricted list of symbols exported by shared libraries.
- Split libfftw3 so that runtime libraries for each precision are
  packaged separately.

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 3.2.2-alt2
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 3.2.2-alt1
- Updated to 3.2.2.

* Wed May 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2.1-alt1.1
- ocaml disabled on ARM

* Thu Jul 02 2009 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Mon Mar 17 2008 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt2
- Fixed build with fresh autotools.

* Fri Feb 09 2007 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt1
- Updated to 3.1.2.
- Cleaned up %%build.
- Fixed threads library linkage.
- Fixed documentation packaging.
- Cleaned up summaries and descriptions.
- Disabled build of static library by default.

* Fri Oct 13 2006 Denis Smirnov <mithraen@altlinux.ru> 3.0.1-alt0.7
- Dixed build.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 3.0.1-alt0.6
- do not package .la files.

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 3.0.1-alt0.5
- new version.

* Tue Jun 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 3.0-alt0.5
- First build for Sisyphus.

