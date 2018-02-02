%define oname triangle

%def_with python3

Name: python-module-%oname
Version: 2017.04.29
Release: alt1.1
Summary: Python wrapper for libtriangle
License: LGPL
Group: Development/Python
Url: http://dzhelil.info/triangle/

# https://github.com/drufat/triangle.git
Source: %name-%version.tar
Patch1: %oname-alt-docs.patch
Patch2: %oname-alt-reqs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libtriangle-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Cython libnumpy-devel
BuildRequires: python-module-nose
BuildRequires: python-module-matplotlib-sphinxext
BuildRequires: python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-numpy-testing python-module-objects.inv python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-nose
BuildRequires: python3-module-html5lib python3-module-notebook python3-module-numpy-testing
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
%patch1 -p1
%patch2 -p1

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2017.04.29-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.04.29-alt1
- Updated to upstream version 20170429.
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.04.05-alt1.git20141030.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.04.05-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.04.05-alt1.git20141030
- Initial build for Sisyphus

