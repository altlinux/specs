%def_disable snapshot

# https://github.com/sass/sass-spec.git requires for tests
%define sass_spec_ver 3.4
%def_disable check

Name: libsass
Version: 3.4.9
Release: alt1

Summary: A C/C++ implementation of a Sass compiler
License: MIT
Group: System/Libraries
Url: http://libsass.org/

%if_disabled snapshot
Source: https://github.com/sass/%name/releases/download/%version/%name-%version.tar.gz
%else
# VCS: https://github.com/sass/libsass.git
Source: %name-%version.tar
%endif

BuildRequires(pre): gcc-c++

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
%configure --enable-static=no
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc *.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.9-alt1
- 3.4.9

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.git20150216
- Initial build for Sisyphus

