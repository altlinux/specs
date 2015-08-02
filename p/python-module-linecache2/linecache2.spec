%define oname linecache2

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150306
Summary: Backports of the linecache module
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/linecache2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/testing-cabal/linecache2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-fixtures python-module-unittest2
BuildPreReq: python-module-mimeparse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fixtures python3-module-unittest2
BuildPreReq: python3-module-mimeparse
%endif

%py_provides %oname

%add_findreq_skiplist %python_sitelibdir/%oname/tests/inspect_fodder2.py

%description
A backport of linecache to older supported Pythons.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A backport of linecache to older supported Pythons.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Backports of the linecache module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A backport of linecache to older supported Pythons.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A backport of linecache to older supported Pythons.

This package contains tests for %oname.
%endif

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150306
- Initial build for Sisyphus

