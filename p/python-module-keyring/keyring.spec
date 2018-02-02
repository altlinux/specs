%define oname keyring

%def_with python3

Name: python-module-%oname
Version: 5.4
Release: alt2.1

Summary: Store and access your passwords safely
License: PSF
Group: Development/Python

Url: https://pypi.python.org/pypi/keyring

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-fs python-module-pycrypto
BuildPreReq: python-module-mock python-module-nose
BuildPreReq: python-module-keyczar python-module-gdata
BuildPreReq: python-module-pytest
BuildPreReq: python-module-pytest-runner
BuildPreReq: python-modules-logging python-modules-json
BuildRequires: python-module-appdirs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-fs python3-module-pycrypto
BuildPreReq: python3-module-mock python3-module-nose
BuildPreReq: python3-module-keyczar
BuildPreReq: python3-module-pytest
BuildPreReq: python3-module-pytest-runner
BuildRequires: python3-module-appdirs
%endif

%setup_python_module %oname

%py_requires fs Crypto logging json keyczar gdata

%description
Store and access your passwords safely.

%package -n python3-module-%oname
Summary: Store and access your passwords safely
Group: Development/Python3
%py3_requires fs Crypto logging json keyczar

%description -n python3-module-%oname
Store and access your passwords safely.

%package -n python3-module-%oname-tests
Summary: Tests for keyring
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Store and access your passwords safely.

This package contains tests for keyring.

%package tests
Summary: Tests for keyring
Group: Development/Python
Requires: %name = %EVR

%description tests
Store and access your passwords safely.

This package contains tests for keyring.

%prep
%setup

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv
popd
%endif

%files
%doc *.rst *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt2
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt1.2
- Updated build spec

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4-alt1
- Version 5.4

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.1-alt1
- Version 5.2.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

