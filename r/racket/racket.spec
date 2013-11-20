%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1
%define debug_package %nil

%define sover 5.3.6
Name: racket
Version: 5.3.6
Release: alt1

Summary: Racket programming language

License: LGPL
Group: Development/Scheme
Url: http://racket-lang.org/

Source: %name-%version.tar
Source1: drscheme.png
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# do not scan collects for requires
%add_findreq_skiplist %_libdir/%name/collects/*/*
%add_findreq_skiplist %_libdir/%name/collects/*/*/*

Provides: plt = %version-%release
Obsoletes: plt < %version-%release

BuildPreReq: gcc-c++ zlib-devel libjpeg-devel libpng-devel
BuildPreReq: libcairo-devel libXaw-devel libXext-devel libXft-devel
BuildPreReq: gcc-fortran libpango-devel /proc chrpath
BuildPreReq: desktop-file-utils libffi-devel libgc-devel
BuildPreReq: libgtk+2-devel libgtkglext-devel libwxGTK2.9-devel
BuildPreReq: libssl-devel zlib-devel 

Requires: lib%name = %version-%release

%description
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

%package doc
Summary: Documentation for Racket
Group: Documentation
#BuildArch: noarch

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
Requires: lib%name = %version-%release
Provides: libmzscheme-devel = %version-%release
Obsoletes: libmzscheme-devel < %version-%release

%description -n lib%name-devel
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains development files of Racket.

%define __arch_install_post %nil

%prep
%setup

cat << __EOF__ > drscheme.desktop
[Desktop Entry]
Type=Application
Name=DrScheme
Comment=The Racket programming environment
Icon=drscheme
Exec=drscheme
Categories=Development;Education;IDE;Science;ComputerScience;
__EOF__

%build
pushd src
#sed -i "s|^\(LIBRACKET_DEP\)=.*|\1=\"$PWD/racket/libmzgc.la -lgc\"|" \
#	configure
%ifarch %ix86
%add_optflags -march=i686 -mtune=i686
%endif
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-shared \
	--enable-pthread \
	--enable-gl \
	--enable-xrender \
	--enable-xft \
	--enable-docs=no
%make_build
popd

%install
NP=%__nprocs
if [ "$NP" = "1" ]; then
	NP=2
fi
%makeinstall_std -C src -j$NP docdir=%_docdir/%name-%version

install -p -m644 README %buildroot%_docdir/%name-%version/
install -pD -m644 %SOURCE1 %buildroot%_niconsdir/drscheme.png
install -pD -m644 drscheme.desktop \
	%buildroot%_desktopdir/drscheme.desktop

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%_bindir/*
%_libdir/%name
%_desktopdir/*
%_niconsdir/*
%_man1dir/*

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

