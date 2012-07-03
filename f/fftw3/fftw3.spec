Name: fftw3
Version: 3.2.2
Release: alt2

Summary: Library for computing Fast Fourier Transforms
License: GPLv2+
Group: System/Libraries
Url: http://www.fftw.org/

# ftp://ftp.fftw.org/pub/fftw/fftw-%version.tar.gz
Source: fftw-%version.tar
Patch: fftw-3.2.2-alt-makefile.patch

# Automatically added by buildreq on Fri Feb 09 2007
BuildRequires: gcc-fortran ghostscript-classic glibc-devel-static transfig
%ifnarch %arm
BuildRequires: ocaml
%endif

%def_disable static
%def_disable sse
%def_disable sse2

%description
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

%package -n lib%name
Summary: Dynamic libraries for computing Fast Fourier Transforms
Group: System/Libraries

%description -n lib%name
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains the shared library versions of the fftw libraries
in single, double and long double precisions.
 
%package -n lib%name-devel
Summary: Development library for computing Fast Fourier Transforms
Group: Development/C
Requires: lib%name = %version-%release

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

This package contains static libraries required to develop programs
using FFTW.

%prep
%setup -n fftw-%version
%patch -p1
%define _configure_script ../configure
mkdir single double long-double

%build
%autoreconf
%define options --enable-shared %{subst_enable static} --enable-threads --enable-portable-binary

pushd single
%configure %options --enable-float \
%ifarch %ix86
	%{subst_enable sse} \
%endif
	#
%make_build
%make_build -C doc html
popd

pushd double
%configure %options \
%ifarch %ix86
	%{subst_enable sse2} \
%endif
	#
%make_build
popd

pushd long-double
%configure %options --enable-long-double
%make_build
popd

%install
%makeinstall_std -C single
%makeinstall_std -C double
%makeinstall_std -C long-double

# remove non-packaged files
rm %buildroot%_libdir/*.la

%check
%make_build -k check -C single
%make_build -k check -C double
%make_build -k check -C long-double

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_infodir/*.info*
%_man1dir/*
%doc single/doc/html/ doc/FAQ/fftw-faq.ascii
%doc AUTHORS CONVENTIONS NEWS README TODO

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
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

