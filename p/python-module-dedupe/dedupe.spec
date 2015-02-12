%define oname dedupe

%def_without python3

Name: python-module-%oname
Version: 0.7.7.0.2
Release: alt1.git20150211
Summary: A python library for accurate and scaleable data deduplication and entity-resolution
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dedupe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/dedupe.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-numpy
BuildPreReq: python-module-hcluster python-module-categorical-distance
BuildPreReq: python-module-rlr python-module-affinegap
BuildPreReq: python-module-haversine python-module-BTrees
BuildPreReq: python-module-zope.interface python-module-zope.index
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-fastcluster
BuildPreReq: python-modules-json python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-numpy
BuildPreReq: python3-module-hcluster python3-module-categorical-distance
BuildPreReq: python3-module-rlr python3-module-affinegap
BuildPreReq: python3-module-haversine python3-module-BTrees
BuildPreReq: python3-module-zope.interface python3-module-zope.index
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-fastcluster
%endif

%py_provides %oname
%py_requires numpy hcluster categorical rlr haversine BTrees json
%py_requires zope.interface zope.index fastcluster

%description
dedupe is a library that uses machine learning to perform de-duplication
and entity resolution quickly on structured data.

dedupe will help you:

* remove duplicate entries from a spreadsheet of names and addresses
* link a list with customer information to another with order history,
  even without unique customer id's
* take a database of campaign contributions and figure out which ones
  were made by the same person, even if the names were entered slightly
  differently for each record

%package -n python3-module-%oname
Summary: A python library for accurate and scaleable data deduplication and entity-resolution
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy hcluster categorical rlr haversine BTrees json
%py3_requires zope.interface zope.index fastcluster

%description -n python3-module-%oname
dedupe is a library that uses machine learning to perform de-duplication
and entity resolution quickly on structured data.

dedupe will help you:

* remove duplicate entries from a spreadsheet of names and addresses
* link a list with customer information to another with order history,
  even without unique customer id's
* take a database of campaign contributions and figure out which ones
  were made by the same person, even if the names were entered slightly
  differently for each record

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
dedupe is a library that uses machine learning to perform de-duplication
and entity resolution quickly on structured data.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
dedupe is a library that uses machine learning to perform de-duplication
and entity resolution quickly on structured data.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
cython src/cpredicates.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 src/cpredicates.pyx
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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.7.0.2-alt1.git20150211
- Version 0.7.7.0.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.7.0.0-alt1.git20150209
- Initial build for Sisyphus

