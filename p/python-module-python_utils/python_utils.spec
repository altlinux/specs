%define oname python_utils

%def_with python3

Name: python-module-%oname
Version: 2.2.0
Release: alt1
Summary: A module with some convenient utilities not included with the standard Python install
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/python-utils/

# https://github.com/WoLpH/python-utils.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-nose python-module-pytest-runner python-module-pytest-cov python-module-pytest-pep8 python-module-pytest-flakes
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-nose python3-module-pytest-runner python3-module-pytest-cov python3-module-pytest-pep8 python3-module-pytest-flakes
%endif

%py_provides %oname

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

%if_with python3
%package -n python3-module-%oname
Summary: A module with some convenient utilities not included with the standard Python install
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.
%endif

%prep
%setup
%patch1 -p1

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

%make -C docs html

%check
python setup.py test
py.test -vv %oname tests
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv %oname tests
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled build for python-3.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150209
- Version 1.6.2

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141015
- Initial build for Sisyphus

