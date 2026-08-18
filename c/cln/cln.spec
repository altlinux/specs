%global _unpackaged_files_terminate_build 1
%def_disable static
%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif
# libtool current - age; SONAME libcln.so.6
%define sover 6
%define libname libcln%sover

Name: cln
Version: 1.3.7
Release: alt1

Summary: CLN - Class Library for Numbers
Group: System/Libraries
License: GPLv2+
Url: https://www.ginac.de/CLN
VCS: https://codeberg.org/ginac/cln

Source: cln-%version.tar

BuildRequires: gcc-c++ libgmp-devel libstdc++-devel
BuildRequires: texinfo
# gnulib havelib macros (AC_LIB_LINKFLAGS_FROM_LIBS) and config.rpath;
# not shipped in the git checkout, and since gettext 0.22 not in aclocal/
BuildRequires: gettext-tools
# AX_CXX_COMPILE_STDCXX: dropped from git in 1.3.7, autogen.sh fetches it
BuildRequires: autoconf-archive

%description
Class Library for Numbers.
Features:
- Rich set of number classes.
- Elementary, logical, transcendental functions.
- Memory efficiency.
- Speed efficiency.
- Interoperability.

%package -n %libname
Summary: CLN - Class Library for Numbers
Group: System/Libraries

%description -n %libname
Class Library for Numbers.
Features:
- Rich set of number classes.
- Elementary, logical, transcendental functions.
- Memory efficiency.
- Speed efficiency.
- Interoperability.

%package -n libcln-devel
Summary: CLN development package
Group: Development/C
Requires: %libname = %EVR

%description -n libcln-devel
The CLN package contains the header files needed for developing
applications that use CLN library. Install libcln-devel if
you want to develop applications using CLN.

%if_enabled static
%package -n libcln-devel-static
Summary: CLN static library
Group: Development/C
Requires: libcln-devel = %EVR

%description -n libcln-devel-static
This package contains static version of CLN library. Install
libcln-devel-static if you want to develop applications statically linked
with CLN.
%endif

%package -n libcln-doc
Summary: CLN library documentation
Group: Development/Documentation
BuildArch: noarch

%description -n libcln-doc
This package contains documentation on CLN library.

%package -n cln-pi
Summary: Compute decimal Archimedes' constant Pi to arbitrary accuracy
Group: Sciences/Mathematics
Requires: %libname = %EVR

%description -n cln-pi
Compute decimal Archimedes' constant Pi to arbitrary accuracy.

%prep
%setup
rm -f aclocal.m4
# Provide macros that upstream's autogen.sh downloads from gnulib/gettext.
cp %_datadir/gettext/m4/lib-ld.m4 \
   %_datadir/gettext/m4/lib-link.m4 \
   %_datadir/gettext/m4/lib-prefix.m4 \
   %_datadir/gettext/m4/host-cpu-c-abi.m4 \
   %_datadir/aclocal/ax_cxx_compile_stdcxx.m4 \
   m4/
mkdir -p build-aux
cp %_datadir/gettext/config.rpath build-aux/

%build
%ifarch %arm
%add_optflags -DNO_ASM
%endif
%autoreconf
%configure %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_bindir/pi %buildroot%_bindir/cln-pi
mv %buildroot%_man1dir/pi.1 %buildroot%_man1dir/cln-pi.1

%check
%make_build check

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files -n %libname
%_libdir/*.so.*

%files -n libcln-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n libcln-devel-static
%_libdir/*.a
%endif

%files -n libcln-doc
%_infodir/*

%files -n cln-pi
%_bindir/cln-pi
%_man1dir/cln-pi.1*

%changelog
* Tue Aug 18 2026 Anton Farygin <rider@altlinux.org> 1.3.7-alt1
- 1.3.6 -> 1.3.7
- renamed source package cln6 -> cln (runtime stays libcln6)
- renamed pi -> cln-pi

* Sat Jul 08 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3.6-alt2
- Added upstream patch for LoongArch architecture (lp64d ABI) support
- spec:
  + disabled static libraries by default for real
  + correctly build static libraries (if enabled)
  + do run the test suite in %%check
  + ensure the build fails if there are unpackaged files
- gear: removed unused tags

* Sun Feb 27 2022 Ilya Mashkin <oddity@altlinux.ru> 1.3.6-alt1
- 1.3.6
- Update License tag

* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 1.3.3-alt3
- fixed build on e2k (patch sent upstream)
  + NB: there's official aarch64/riscv64 support in current version

* Thu Apr 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt2
- fixed build on AArch64

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1.1
- NMU: added BR: texinfo

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1
- Version 1.3.3

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt3
- Moved %_bindir/pi into separate package (ALT #27724)

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Rebuilt with gmp 5.0.5

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1.1
- rebuild on arm

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.2
- Rebuilt for debuginfo

* Thu Dec 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.1
- Built for Sisyphus (ALT #24786)

* Thu Oct 08 2009 Alexey Morsov <swi@altlinux.ru> 1.3.1-alt1
- new version

* Wed Jul 15 2009 Alexey Morsov <swi@altlinux.ru> 1.3.0-alt1
- new version
- remove ubsoluted macros
- remove dvi and doc dirs from lib%name-doc
- add bindir to lib%name package

* Tue Nov 18 2008 Alexey Morsov <swi@altlinux.ru> 1.2.2-alt1.1
- fix spec (repocop)

* Fri Nov 07 2008 Alexey Morsov <swi@altlinux.ru> 1.2.2-alt1
- new version

* Fri Aug 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.1.13-alt1
- 1.1.13 release.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.11-alt1
- 1.1.11 release.

* Sun Oct 02 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.9-alt3
- Fixed %post and %postun mis-use in specfile.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.9-alt2
- Fixed package name due to policy.

* Sat Aug 27 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.9-alt1
- Initial build for Sisyphus.
