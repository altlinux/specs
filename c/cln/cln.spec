%def_without static

Name: cln
Version: 1.2.2
Release: alt1.2

Summary: CLN - Class Library for Numbers
Group: System/Libraries
License: GPL
Url: http://www.ginac.de/CLN
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Fri Jun 17 2005
BuildRequires: gcc4.3-c++ libgmp-devel libstdc++-devel

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
Group: System/Legacy libraries

%description -n lib%name
Class Library for Numbers.
Features:
- Rich set of number classes.
- Elementary, logical, transcendental functions.
- Memory efficiency.
- Speed efficiency.
- Interoperability.

%package -n lib%name-devel
Summary: CLN development package
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The CLN package contains the header files needed for developing
applications that use CLN library. Install libcln-devel if
you want to develop applications using CLN.

%if_enabled static
%package -n lib%name-devel-static
Summary: CLN static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static version of CLN library. Install
libcln-devel-static if you want to develop applications statically linked
with CLN.
%endif

%package -n lib%name-doc
Summary: CLN library documentation
Group: Development/Documentation

%description -n lib%name-doc
This package contains documentation on CLN library.

%prep
%setup -q -n %name-%version

%build
%configure %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

# remove non-packaged files
rm -f %buildroot%_libdir/*.la
%if_without static
rm -f %buildroot%_libdir/*.a
%endif

mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/dvi/ %buildroot%_datadir/doc/%name-%version/
mv %buildroot%_datadir/html/ %buildroot%_datadir/doc/%name-%version/

%files -n lib%name
%_libdir/*.so.*

#files -n lib%name-devel
#_includedir/*
#_libdir/*.so
#_libdir/pkgconfig/*

#if_with static
#files -n lib%name-devel-static
#_libdir/*.a
#endif

#files -n lib%name-doc
#_infodir/*
#doc %_datadir/doc/*

%changelog
* Thu Dec 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.2
- Moved this version in System/Legacy libraries

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
