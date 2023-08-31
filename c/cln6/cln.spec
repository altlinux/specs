%global _unpackaged_files_terminate_build 1
%def_disable static
%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif
%define abiversion 6
%define oname cln

Name: %oname%abiversion
Version: 1.3.6
Release: alt2

Summary: CLN - Class Library for Numbers
Group: System/Libraries
License: GPLv2+
Url: http://www.ginac.de/CLN

Source: %oname-%version.tar

# Automatically added by buildreq on Fri Jun 17 2005
BuildRequires: gcc-c++ libgmp-devel libstdc++-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Class Library for Numbers.
Features:
- Rich set of number classes.
- Elementary, logical, transcendental functions.
- Memory efficiency.
- Speed efficiency.
- Interoperability.

%package -n lib%name
Summary: CLN - Class Library for Numbers
Group: System/Libraries

%description -n lib%name
Class Library for Numbers.
Features:
- Rich set of number classes.
- Elementary, logical, transcendental functions.
- Memory efficiency.
- Speed efficiency.
- Interoperability.

%package -n lib%oname-devel
Summary: CLN development package
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%oname-devel
The CLN package contains the header files needed for developing
applications that use CLN library. Install libcln-devel if
you want to develop applications using CLN.

%if_enabled static
%package -n lib%oname-devel-static
Summary: CLN static library
Group: Development/C
Requires: lib%oname-devel = %version-%release

%description -n lib%oname-devel-static
This package contains static version of CLN library. Install
libcln-devel-static if you want to develop applications statically linked
with CLN.
%endif

%package -n lib%oname-doc
Summary: CLN library documentation
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-doc
This package contains documentation on CLN library.

%package -n pi
Summary: Compute decimal Archimedes' constant Pi to arbitrary accuracy
Group: Sciences/Mathematics
Requires: lib%name = %version-%release
Conflicts: puppet

%description -n pi
Compute decimal Archimedes' constant Pi to arbitrary accuracy.

%prep
%setup 
rm -f aclocal.m4

%build
%ifarch %arm
%add_optflags -DNO_ASM
%endif
%autoreconf
%configure %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%check
%make_build check

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files -n lib%name
%_libdir/*.so.*
%_man1dir/*

%files -n lib%oname-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%oname-devel-static
%_libdir/*.a
%endif

%files -n lib%oname-doc
%_infodir/*

%files -n pi
%_bindir/pi

%changelog
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
