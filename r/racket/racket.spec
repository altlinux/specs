%define _unpackaged_files_terminate_build 1

%define sover 6.12
Name: racket
Version: 6.12
Release: alt1

Summary: Racket programming language

License: LGPL
Group: Development/Scheme
Url: https://racket-lang.org/

Source: %name-%version.tar
Patch1: %name-alt-debuginfo.patch

# do not scan collects for requires and provides
%add_findreq_skiplist  %_libdir/%name/collects/*/*
%add_findreq_skiplist  %_libdir/%name/collects/*/*/*
%add_findprov_skiplist %_libdir/%name/collects/*/*
%add_findprov_skiplist %_libdir/%name/collects/*/*/*

Provides: plt = %EVR
Obsoletes: plt < %EVR

BuildRequires: /proc
BuildRequires: gcc-c++ zlib-devel libjpeg-devel libpng-devel
BuildRequires: libcairo-devel libXaw-devel libXext-devel libXft-devel
BuildRequires: gcc-fortran libpango-devel
BuildRequires: desktop-file-utils libffi-devel libgc-devel
BuildRequires: libgtk+3-devel libgtkglext-devel libwxGTK3.1-devel
BuildRequires: libssl-devel zlib-devel

Requires: lib%name = %EVR
Requires: %name-data = %EVR

%description
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

%package data
Summary: Data for Racket
Group: Development/Scheme

%description data
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains data for Racket.

%package doc
Summary: Documentation for Racket
Group: Documentation
BuildArch: noarch

%description doc
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains documentation for Racket.

%package -n lib%name
Summary: Shared libraries of Racket
Group: System/Libraries

%description -n lib%name
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains shared libraries of Racket.

%package -n lib%name-devel
Summary: Development files of Racket
Group: Development/Scheme
Requires: lib%name = %EVR
Provides: libmzscheme-devel = %EVR
Obsoletes: libmzscheme-devel < %EVR

%description -n lib%name-devel
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains development files of Racket.

%prep
%setup
%patch1 -p2

%build
pushd src
%ifarch %ix86
%add_optflags -march=i686 -mtune=i686
%endif
%add_optflags %optflags_shared
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-shared \
	--enable-pthread \
	--enable-gl \
	--enable-xrender \
	--enable-xft \
	--enable-docs=yes \
	--disable-strip
%make_build
popd

%install
NP=%__nprocs
if [ "$NP" = "1" ]; then
	NP=2
fi
%makeinstall_std -C src -j$NP docdir=%_docdir/%name-%version

install -p -m644 README %buildroot%_docdir/%name-%version/
sed -i 's|%buildroot||g' %buildroot%_desktopdir/*.desktop

# remove static libraries
rm -f %buildroot%_libdir/*.a

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%_bindir/*
%_libdir/%name
%_desktopdir/*
%_man1dir/*
%_sysconfdir/*

%files data
%_datadir/%name

%files doc
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/README

%files -n lib%name
%_libdir/*-%sover.so

%files -n lib%name-devel
%doc src/README
%_libdir/*.so
%exclude %_libdir/*-%sover.so
%_includedir/*

%changelog
* Mon Dec 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12-alt1
- Updated to upstream version 6.12 (Closes: #35721)

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.10.1-alt1
- Updated to upstream version 6.10.1.

* Wed Jun 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt2
- Removed %%buildroot from desktop files

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1
- Version 6.0.1

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.6-alt1
- Version 5.3.6

* Tue Jul 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.5-alt1
- Version 5.3.5

* Mon Feb 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.3-alt1
- Version 5.3.3

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1
- Version 5.3

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt3
- Fixed build with new glibc

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- Removed RPATH

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1
- Initial build for Sisyphus

