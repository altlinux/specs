%define sover 5.1
Name: racket
Version: 5.1
Release: alt2

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
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-shared \
	--enable-pthread
#sed -i 's|^\(INSTALL_STRIP_PROGRAM.*\)\-s|\1|' $(find ./ -name Makefile)
#sed -i 's|^\(STRIP.*\)|\1 = echo|' $(find ./ -name Makefile)
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

chrpath -d %buildroot%_bindir/%name
chrpath -d %buildroot%_bindir/g%name

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
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- Removed RPATH

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1
- Initial build for Sisyphus

