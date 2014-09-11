Name: libbson
Version: 1.0.0
Release: alt1.git20140826
Summary: A BSON utility library
License: ASLv2.0
Group: System/Libraries
Url: https://github.com/mongodb/libbson
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mongodb/libbson.git
Source: %name-%version.tar

BuildPreReq: yelp-tools gcc-c++

%description
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

%package devel
Summary: Development files of %name
Group: Development/C++
Requires: %name = %EVR

%description devel
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

This package contains development files of %name.

%package docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description docs
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

This package contains development documentation for %name.

%prep
%setup
ln -s README.md README

%build
%autoreconf
%configure \
	--enable-debug \
	--enable-optimizations \
	--enable-lto \
	--enable-html-docs=yes \
	--enable-yelp=yes
%make_build V=1 ENABLE_HTML_DOCS=1
%make -C doc html

%install
%makeinstall_std V=1 ENABLE_HTML_DOCS=1

%files
%doc NEWS *.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files docs
%doc doc/doc/html examples

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Initial build for Sisyphus

