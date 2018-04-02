%define oname keyring

Name: python-module-%oname
Version: 12.0.0
Release: alt1
Summary: Keyring provides an easy way to access the system keyring service

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/keyring
BuildArch: noarch

Source: %oname-%version.tar
Patch0: fix_deps.patch

BuildRequires: python-module-setuptools python-devel
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-sugar
BuildRequires: python-module-setuptools_scm

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel
BuildPreReq: python-module-pytest
BuildPreReq: python-module-pytest-sugar
BuildPreReq: python-module-setuptools_scm


%description
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

%package -n python3-module-%oname
Summary: Keyring provides an easy way to access the system keyring service
Group: Development/Python3
%py3_requires ctypes entrypoints json logging pluggy

%description -n python3-module-%oname
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

%package -n python3-module-%oname-tests
Summary: Tests for keyring
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

This package contains tests for keyring.

%package tests
Summary: Tests for keyring
Group: Development/Python
Requires: %name = %EVR

%description tests
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

This package contains tests for keyring.

%prep
%setup -n %oname-%version
%patch0 -p0

rm -rf ../python3
cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py3
done
popd

%python_install

%files
%doc *.rst LICENSE
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc *.rst *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests


%changelog
* Mon Apr 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 12.0.0-alt1
- Updated version to 12.0.0
  Fixed deps

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
