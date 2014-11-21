%define oname sqlalchemy_mptt

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141118
Summary: SQLAlchemy MPTT mixins (Nested Sets)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy_mptt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/sqlalchemy_mptt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-SQLAlchemy
BuildPreReq: python-module-sphinx-devel itcase_sphinx_theme
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-SQLAlchemy
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3

%description
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

%package -n python3-module-%oname
Summary: SQLAlchemy MPTT mixins (Nested Sets)
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3

%description -n python3-module-%oname
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

cp -fR %_datadir/itcase_sphinx_theme docs/_themes
%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

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
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141118
- Version 0.1.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20141031
- Initial build for Sisyphus

