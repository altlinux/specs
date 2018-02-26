Name: lush
Version: 2.0.1
Release: alt2
Summary: Object-oriented programming language for large-scale numerical and graphic applications
License: LGPL v2.0+
Group: Development/Lisp
Url: http://lush.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: binutils-devel gcc-c++ gcc-fortran
BuildPreReq: liblapack-devel libreadline-devel
BuildPreReq: libgsl-devel libGL-devel libGLU-devel libGLUT-devel
BuildPreReq: libSDL-devel libopencv-devel libv4l-devel libalsa-devel
BuildPreReq: libXft-devel libncurses-devel fontconfig-devel

%description
Lush is an object-oriented programming language designed for
researchers, experimenters, and engineers interested in large-scale
numerical and graphic applications. Lush is designed to be used in
situations where one would want to combine the flexibility of a
high-level, weakly-typed interpreted language, with the efficiency of a
strongly-typed, natively-compiled language, and with the easy
integration of code written in C, C++, or other languages.

%prep
%setup

%build
%autoreconf
export CPPFLAGS="%optflags"
%configure \
	--bindir=%_libdir/%name/bin \
	--datadir=%_libdir/%name/share \
	--with-x
%make_build

%install
%makeinstall_std

install -d %buildroot%_bindir

ln -s %_libdir/%name/bin/lush2 %buildroot%_bindir/lush2
ln -s lush2 %buildroot%_bindir/lush

%files
%doc README COPYRIGHT
%_libdir/%name
%_bindir/*
%_man1dir/*

%changelog
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2
- Fixed build

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.beta2.1
- Rebuilt for debuginfo

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.beta2
- Initial build for Sisyphus

