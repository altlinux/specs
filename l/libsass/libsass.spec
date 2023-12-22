%def_disable snapshot

# https://github.com/sass/sass-spec.git requires for tests
%define sass_spec_ver 3.6.0
%def_disable check

Name: libsass
Version: 3.6.6
Release: alt1

Summary: A C/C++ implementation of a Sass compiler
License: MIT
Group: System/Libraries
Url: https://sass-lang.com

%if_disabled snapshot
Source: https://github.com/sass/%name/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/sass/libsass.git
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
export LIBSASS_VERSION=%version
%add_optflags %(getconf LFS_CFLAGS)
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
* Fri Dec 22 2023 Yuri N. Sedunov <aris@altlinux.org> 3.6.6-alt1
- 3.6.6

* Mon Jun 07 2021 Yuri N. Sedunov <aris@altlinux.org> 3.6.5-alt1
- 3.6.5

* Wed Dec 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- updated to 3.6.4-17-gd4d74ef5

* Wed Apr 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon May 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.5.4-alt1
- 3.5.4

* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.9-alt1
- 3.4.9

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.git20150216
- Initial build for Sisyphus

