%set_automake_version 1.11

Name: fftw
Version: 2.1.5
Release: alt8

Summary: Fast Fourier transform library
License: GPL
Group: System/Libraries
Url: http://www.fftw.org

Source: fftw-%version.tar
Patch0: fftw-2.1.5-pentium.patch
Patch1: fftw-2.1.5-alt-texinfo.patch
Patch2: fftw-2.1.5-alt-link_no_undefined.patch

BuildRequires: gcc-fortran makeinfo

%description
FFTW is a collection of fast C routines for computing the Discrete Fourier
Transform in one or more dimensions.  It includes complex, real, and
parallel transforms, and can handle arbitrary array sizes efficiently.
This RPM package includes both the double- and single-precision FFTW
uniprocessor and threads libraries.  (The single-precision files have
an "s" prefix.)

%package -n lib%name
Summary: Dynamic libraries for FFTW fast fourier transform library
Group: System/Libraries

%description -n lib%name
FFTW is a collection of fast C routines for computing the Discrete Fourier
Transform in one or more dimensions.  It includes complex, real, and
parallel transforms, and can handle arbitrary array sizes efficiently.
This RPM package includes both the double- and single-precision FFTW
uniprocessor and threads libraries.  (The single-precision files have
an "s" prefix.)

%package -n lib%name-devel
Summary: Headers, libraries, & docs for FFTW fast fourier transform library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the additional header files, documentation, and
libraries you need to develop programs using the FFTW fast fourier
transform library.

%package -n lib%name-devel-static
Summary: Static libraries for FFTW fast fourier transform library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries you need to develop programs using
the FFTW fast fourier transform library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# sources came with pre-generated config.h :-(
rm fftw/config.h

# create two separate build directories within main dir
mkdir -p double single

%build
aclocal
automake
autoconf
libtoolize --copy --force

%global _configure_script ../configure

%ifarch %ix86
%define arch_options --enable-i386-hacks
%else
%define arch_options %nil
%endif

pushd double
%configure --enable-shared --enable-threads %arch_options
%make
popd

pushd single
%configure --enable-shared --enable-threads %arch_options \
	--enable-float --enable-type-prefix
%make
popd

%install
# The double-precision version is installed with the normal library names,
# while the single-precision version is installed with an "s" prefix.
%makeinstall -C double
%makeinstall -C single

%files -n lib%name
%doc AUTHORS NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_infodir/*.info*
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt8
- Updated build dependencies.

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt7.qa2
- Fixed build

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.5-alt7.qa1
- NMU: rebuilt for updated dependencies.

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 2.1.5-alt7
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt6
- Rebuilt for soname set-versions

* Tue Nov 24 2009 Denis Smirnov <mithraen@altlinux.ru> 2.1.5-alt5
- cleanup spec

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 2.1.5-alt4
- cleanup spec

* Fri Nov 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.1.5-alt3
- rebuild

* Sun Sep 30 2007 Alexey Morozov <morozov@altlinux.org> 2.1.5-alt2.1
- NMU: fix build:
  + no more unresolved symbols in libraries
    (patch fftw-2.1.5-alt-link_no_undefined.patch, #2)
  + build process slightly re-organized and optimized

* Wed Oct 18 2006 Denis Smirnov <mithraen@altlinux.ru> 2.1.5-alt2
- fix building with last toolchain

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5
- do not package .la files.

* Fri Feb 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt3
- use %%{un}install_info macros in %%post{un}.

* Tue Sep 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- cleanups.

* Fri Nov 23 2001 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- Adaptation and first build for Sisyphus.

* Thu Jun 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-8mdk
- fixed by Mika Korhonen <mikak@ee.oulu.fi> :
	- removed broken ld.so.conf test (/usr/lib is not listed there anyways)
	- made install-info work with RPM macros shipping with newer Mandrakes
	  and actually add an entry to the top dir file

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-7mdk
- rebuild

* Tue Aug 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-6mdk
- add installinfo

* Wed Aug 30 2000 Alexander Skwar <ASkwar@DigitalProjects.com> 2.1.3-5mdk
- Actually used macros
- Added %%doc files
- Shortened %files section of the SPEC file a lot
- Provide libfftw as eXtace requires it
- Obsolote libfftw package
- Optimized for Pentium builds per README.hacks

* Wed Aug 30 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-4mdk
- BM
- macros

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-3mdk
- fix group
- spec helper fixes

* Tue Jan 25 2000 Lenny Cartier <lenny@mandrakesoft.com>
- updated, installs in /usr instead of /usr/local by Dara Hazeghi
  <dara@pacbell.net>

* Thu Dec 16 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- bz2 archive
- add defattr
