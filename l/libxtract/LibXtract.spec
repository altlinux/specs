%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libxtract
Version: 0.7.1
Release: alt2.beta.git20140717
Summary: Simple, portable, lightweight library of audio feature extraction functions
License: MIT
Group: System/Libraries
Url: https://github.com/jamiebullock/LibXtract

# https://github.com/jamiebullock/LibXtract.git
Source: %name-%version.tar

Patch1: libxtract-alt-python3-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: doxygen graphviz
BuildRequires: python3-devel
BuildRequires: swig

%description
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies.

%package devel
Summary: Development files of %name
Group: Development/C++
Requires: %name = %EVR

%description devel
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies.

This package contains development files of %name.

%package devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies.

This package contains development documentation for %name.

%package -n python3-module-%name
Summary: Python module of %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies.

This package contains Python module of %name.

%prep
%setup
%patch1 -p1

touch NEWS README AUTHORS

%build
%add_optflags -std=gnu++11
export PYTHON=python3
%autoreconf
%configure \
	--enable-static=no \
	--enable-simpletest \
	--enable-debug \
	--enable-swig \
	--with-ooura \
	--with-python \
	%nil

%make_build

%install
%makeinstall_std
rm -f %buildroot%python3_sitelibdir/libxtract/*.la

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mv %buildroot%python3_sitelibdir_noarch/libxtract/* \
	%buildroot%python3_sitelibdir/libxtract/
%endif

%files
%doc ChangeLog *.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-docs
%doc doc/html/*

%files -n python3-module-%name
%python3_sitelibdir/%name

%changelog
* Fri Jan 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt2.beta.git20140717
- Rebuilt without python-2.

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1.beta.git20140717.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.beta.git20140717.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.beta.git20140717
- Initial build for Sisyphus

