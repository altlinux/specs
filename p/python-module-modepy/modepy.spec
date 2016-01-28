%define oname modepy

%def_with python3

Name: python-module-%oname
Version: 2013.3
Release: alt1.git20140704.1
Summary: Modes and nodes for high-order discretizations
License: MIT
Group: Development/Python
Url: http://documen.tician.de/modepy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel libnumpy-devel python-module-sphinx-devel
#BuildPreReq: python-module-pytools python-module-decorator
#BuildPreReq: python-module-sphinx-bootstrap-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel libnumpy-py3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-Fabric python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-decorator python-module-ecdsa python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mpi4py python-module-nose python-module-numpy python-module-pycrypto python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-numpy
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-matplotlib python-module-numpy-testing python-module-objects.inv python-module-pytools python-module-sphinx-bootstrap-theme python3-module-setuptools rpm-build-python3 time

%description
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

%package -n python3-module-%oname
Summary: Modes and nodes for high-order discretizations
Group: Development/Python3

%description -n python3-module-%oname
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

%package pickles
Summary: Pickles for modepy
Group: Development/Python

%description pickles
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

This package contains pickles for modepy.

%package doc
Summary: Documentation for modepy
Group: Development/Documentation

%description doc
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

This package contains documentation for modepy.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.3-alt1.git20140704.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.3-alt1.git20140704
- New snapshot
- Added module for Python 3

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.3-alt1.git20140621
- Initial build for Sisyphus

