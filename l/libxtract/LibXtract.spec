%def_with python3

Name: libxtract
Version: 0.7.1
Release: alt1.beta.git20140717.1.1
Summary: Simple, portable, lightweight library of audio feature extraction functions
License: MIT
Group: System/Libraries
Url: https://github.com/jamiebullock/LibXtract
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jamiebullock/LibXtract.git
Source: %name-%version.tar

BuildPreReq: doxygen graphviz python-devel swig gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

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

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%name
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies.

This package contains Python module of %name.

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

touch NEWS README AUTHORS

%if_with python3
cp -fR . ../python3
sed -i 's|\(lpython\${ac_python_version}\)|\1%_python3_abiflags|' \
	../python3/m4/ax_python_devel.m4
sed -i 's|\(\$(SWIG)\)|\1 -py3|' \
	../python3/swig/python/Makefile.am
%endif

%build
%add_optflags -std=gnu++11
%autoreconf
%configure \
	--enable-static=no \
	--enable-simpletest \
	--enable-debug \
	--enable-swig \
	--with-ooura \
	--with-python
%make_build

%if_with python3
pushd ../python3
export PYTHON=python3
%autoreconf
%configure \
	--enable-static=no \
	--enable-simpletest \
	--enable-debug \
	--enable-swig \
	--with-ooura \
	--with-python
%make_build
popd
%endif

%install
%makeinstall_std
rm -f %buildroot%python_sitelibdir/libxtract/*.la
%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/libxtract/* \
	%buildroot%python_sitelibdir/libxtract/
%endif

%if_with python3
pushd ../python3
%make install DESTDIR=$PWD/buildroot
install -d %buildroot%python3_sitelibdir
mv buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir/
rm -f %buildroot%python3_sitelibdir/libxtract/*.la
%ifarch x86_64
mv buildroot%python3_sitelibdir_noarch/libxtract/* \
	%buildroot%python3_sitelibdir/libxtract/
%endif
popd
%endif

%files
%doc ChangeLog *.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n python-module-%name
%python_sitelibdir/*

%files devel-docs
%doc doc/html/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1.beta.git20140717.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.beta.git20140717.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.beta.git20140717
- Initial build for Sisyphus

