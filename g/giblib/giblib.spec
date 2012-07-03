Name: giblib
Version: 1.2.4
Release: alt0.4

Summary: Simple library and a wrapper for imlib2.
License: BSD
Group: System/Libraries
Url: http://linuxbrit.co.uk/%name/
Source: %name-%version.tar.gz
Patch: giblib-alt-configure-use_pkgconfig.patch
Packager: Alex Murygin <murygin@altlinux.ru>

BuildRequires: freetype2-devel gcc-c++ hostinfo imlib2-devel libstdc++-devel zlib-devel

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}


%description
giblib is a simple library which wraps imlib2. It provides a wrapper to
imlib2's context API, avoiding all the context_get/set calls, adds fontstyles
to the truetype renderer and supplies a generic doubly-linked list and some
string functions.

%package -n lib%name
Summary: Enlightened backgrounds manipulating library
Group: System/Libraries

%description -n lib%name
giblib is a simple library which wraps imlib2. It provides a wrapper to
imlib2's context API, avoiding all the context_get/set calls, adds fontstyles
to the truetype renderer and supplies a generic doubly-linked list and some
string functions.

This package contains shared giblib library.

%package -n lib%name-devel
Summary: giblib headers and development libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains giblib headers and development libraries

%package -n lib%name-devel-static
Summary: giblib static libraries.
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains giblib static libraries.

%prep
%setup
%patch -p2
%autoreconf

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static}

%build
%make_build

%install
%makeinstall

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS ChangeLog README

%files -n lib%name-devel
%_bindir/*-config
%_includedir/*
%_libdir/*.so
%exclude %_libdir/*.so.1
#_libdir/*.la

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Mar 30 2011 Slava Semushin <php-coder@altlinux.ru> 1.2.4-alt0.4
- NMU
- Updated BuildRequires to get rid of xorg-x11-devel (fixed build)

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt0.3
- Rebuilt for soname set-versions

* Sat Aug 22 2009 Slava Semushin <php-coder@altlinux.ru> 1.2.4-alt0.2
- NMU
- Fixed build (use pkg-config instead of imlib2-config)

* Thu Dec 16 2004 Alex Murygin <murygin@altlinux.ru> 1.2.4-alt0.1
- new version

* Fri Dec 26 2003 Alex Murygin <murygin@altlinux.ru> 1.2.3-alt0.1
- First build for AltLinux

