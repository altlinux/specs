%define oname brownie

%def_without python3

Name: python-module-%oname
Version: 0.5.1
Release: alt2.git20110725.1
Summary: Common utilities and datastructures for Python applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Brownie/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/DasIch/brownie.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-attest python-module-tox
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel python-module-sphinxcontrib-ansi
BuildPreReq: sphinx-theme-minimalism
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-attest python3-module-tox
BuildPreReq: python3-module-coverage
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Common utilities and datastructures for Python applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Common utilities and datastructures for Python applications.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Common utilities and datastructures for Python applications
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Common utilities and datastructures for Python applications.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Common utilities and datastructures for Python applications.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Common utilities and datastructures for Python applications.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Common utilities and datastructures for Python applications.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
rm -fR docs/_themes/minimalism
ln -s %_datadir/sphinx-theme-minimalism docs/_themes/minimalism

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt2.git20110725.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.git20110725
- Fixed build

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20110725
- Initial build for Sisyphus

