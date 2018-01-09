Name: libbson
Version: 1.9.0
Release: alt1%ubt
Summary: A BSON utility library
License: ASLv2.0
Group: System/Libraries
Url: https://github.com/mongodb/libbson

# https://github.com/mongodb/libbson.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-module-sphinx
BuildRequires: gcc-c++


%description
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

This package contains development files of %name.

%prep
%setup

# Remove pregenerated documentation
rm -rf doc/html/_static doc/html/*.{html,inv,js} doc/man/*.3

%build
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	--disable-lto \
	--disable-maintainer-flags \
	--enable-man-pages \
	--disable-optimizations \
	--disable-silent-rules \
	--enable-tests

%make_build all doc/man

%install
%makeinstall_std

%check
%make_build check

%files
%doc NEWS README.rst
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%changelog
* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1%ubt
- 1.9.0

* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1%ubt
- 1.8.2
- drop docs package

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150310
- Version 1.1.2

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150226
- Version 1.1.1

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Initial build for Sisyphus

