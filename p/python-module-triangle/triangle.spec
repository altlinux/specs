%define oname triangle

%def_with python3

Name: python-module-%oname
Version: 2013.04.05
Release: alt1.git20141030
Summary: Python wrapper for libtriangle
License: LGPL
Group: Development/Python
Url: http://dzhelil.info/triangle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/drufat/triangle.git
Source: %name-%version.tar

BuildPreReq: libtriangle-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-matplotlib python-module-nose
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-matplotlib-sphinxext
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-matplotlib python3-module-nose
%endif

%py_provides %oname
%py_requires numpy matplotlib

%description
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper for libtriangle
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy matplotlib

%description -n python3-module-%oname
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

This package contains documentation for %oname.

%prep
%setup

rm -fR c

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
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
pushd doc
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.04.05-alt1.git20141030
- Initial build for Sisyphus

