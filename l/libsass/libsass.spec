Name: libsass
Version: 3.0.3
Release: alt1.git20150216
Summary: A C/C++ implementation of a Sass compiler
License: MIT
Group: System/Libraries
Url: http://libsass.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sass/libsass.git
Source: %name-%version.tar

BuildPreReq: gcc-c++

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original
version was written in Ruby, but this version is meant for efficiency
and portability.

This library strives to be light, simple, and easy to build and
integrate with a variety of platforms and languages.

%package devel
Summary: Development files of Sass compiler
Group: Development/C++
Requires: %name = %EVR

%description devel
Libsass is a C/C++ port of the Sass CSS precompiler. The original
version was written in Ruby, but this version is meant for efficiency
and portability.

This package contains development files of Sass compiler.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no
%make_build

%install
%makeinstall_std

%files
%doc *.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.git20150216
- Initial build for Sisyphus

