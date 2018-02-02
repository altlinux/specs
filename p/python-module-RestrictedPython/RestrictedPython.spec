%define oname RestrictedPython
# python3 lacks compiler module, disable it
%def_without python3

Name: python-module-%oname
Version: 4.0
Release: alt1.a3.1
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/RestrictedPython/

# https://github.com/zopefoundation/RestrictedPython.git
Source: %name-%version.tar
BuildArch: noarch

%add_findreq_skiplist %python_sitelibdir/%oname/tests/restricted_module.py
%add_findreq_skiplist %python3_sitelibdir/%oname/tests/restricted_module.py
%add_findreq_skiplist %python_sitelibdir/%oname/tests/testRestrictions.py
%add_findreq_skiplist %python3_sitelibdir/%oname/tests/testRestrictions.py
%add_findreq_skiplist %python_sitelibdir/%oname/tests/unpack.py
%add_findreq_skiplist %python3_sitelibdir/%oname/tests/unpack.py

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest python-module-pytest-mock python-module-pytest-runner python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-pytest-mock python3-module-pytest-runner python3-module-mock
%endif

%description
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

%package tests
Summary: Tests for RestrictedPython
Group: Development/Python
Requires: %name = %version-%release

%description tests
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

This package contains tests for RestrictedPython.

%if_with python3
%package -n python3-module-%oname
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
Group: Development/Python

%description -n python3-module-%oname
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

%package -n python3-module-%oname-tests
Summary: Tests for RestrictedPython
Group: Development/Python
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

This package contains tests for RestrictedPython.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
python setup.py test -v
export PYTHONPATH=$PWD/src
py.test -vv

%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD/src
py.test3 -vv
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0-alt1.a3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0-alt1.a3
- Updated to upstream version 4.0a3.
- Enabled build with python-3.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.dev.git20130312
- Added tests

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.dev.git20130312
- Version 3.6.1dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1.1
- Rebuild with Python-2.7

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

