%def_without static
%define abiversion 6
%define oname cln

Name: %oname%abiversion
Version: 1.3.2
Release: alt1.1

Summary: CLN - Class Library for Numbers
Group: System/Libraries
License: GPL
Url: http://www.ginac.de/CLN
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %oname-%version.tar

# Automatically added by buildreq on Fri Jun 17 2005
BuildRequires: gcc-c++ libgmp-devel libstdc++-devel

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

# remove non-packaged files
rm -f %buildroot%_libdir/*.la
%if_without static
rm -f %buildroot%_libdir/*.a
%endif


%files -n lib%name
%_bindir/*
%_libdir/*.so.*
%_man1dir/*

%files -n lib%oname-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_with static
%files -n lib%oname-devel-static
%_libdir/*.a
%endif

%files -n lib%oname-doc
%_infodir/*

%changelog
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
