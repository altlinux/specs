%define oname requests-unixsocket

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt2.1
Summary: Use requests to talk HTTP via a UNIX domain socket
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-unixsocket/

# https://github.com/msabramo/requests-unixsocket.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: git-core python-module-pbr python-module-pytest-capturelog python-module-pytest-pep8 python-module-setuptools python-module-waitress
BuildRequires: python-module-requests python-module-pytest-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-setuptools python3-module-waitress python3-tools-pep8
BuildRequires: python3-module-requests python3-module-pytest-pep8
%endif

%py_provides requests_unixsocket
%py_requires requests

%description
Use requests to talk HTTP via a UNIX domain socket.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Use requests to talk HTTP via a UNIX domain socket.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Use requests to talk HTTP via a UNIX domain socket
Group: Development/Python3
%py3_provides requests_unixsocket
%py3_requires requests

%description -n python3-module-%oname
Use requests to talk HTTP via a UNIX domain socket.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Use requests to talk HTTP via a UNIX domain socket.

This package contains tests for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
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
touch %buildroot%python_sitelibdir/requests_unixsocket/tests/__init__.py

%if_with python3
pushd ../python3
%python3_install
touch %buildroot%python3_sitelibdir/requests_unixsocket/tests/__init__.py
popd
%endif

%check
PYTHONPATH=$(pwd) py.test
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt2
- Fixed build dependencies.

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 0.1.5-alt1
- (NMU) version update for pylxd module

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150203
- Initial build for Sisyphus

