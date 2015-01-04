%define oname elpy

%def_with python3

Name: python-module-%oname
Version: 1.6.1
Release: alt1.git20141129
Summary: The Emacs Lisp Python Environment
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/elpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jorgenschaefer/elpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8 python-module-bumpversion
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-nose python-module-tox
BuildPreReq: python-module-twine python-module-virtualenv
BuildPreReq: python-module-wheel python-module-jedi
BuildPreReq: python-module-rope
BuildPreReq: python-module-sphinx-devel
# for py3:
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8 python3-module-bumpversion
BuildPreReq: python3-module-coverage python3-module-mock
BuildPreReq: python3-module-nose python3-module-tox
BuildPreReq: python3-module-twine python3-module-virtualenv
BuildPreReq: python3-module-wheel python3-module-jedi
BuildPreReq: python3-module-rope_py3k
%endif

%py_provides %oname
%py_requires jedi rope

%description
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: The Emacs Lisp Python Environment
Group: Development/Python3
%py3_provides %oname
%py3_requires jedi rope

%description -n python3-module-%oname
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Elpy is a mode for Emacs to support writing Python code. This package
provides the backend within Python to support auto-completion,
documentation extraction, and navigation.

This package contains documentation for %oname.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141129
- Initial build for Sisyphus

