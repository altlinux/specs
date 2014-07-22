%define oname pyquery

%def_with python3

Name: python-module-%oname
Version: 1.2.8
Release: alt1
Summary: A jquery-like library for python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyquery
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-cssselect
BuildPreReq: python-module-webob
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: A jquery-like library for python
Group: Development/Python3

%description -n python3-module-%oname
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1
- Initial build for Sisyphus

