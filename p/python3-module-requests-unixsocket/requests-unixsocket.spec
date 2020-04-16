%define oname requests-unixsocket

Name: python3-module-%oname
Version: 0.1.5
Release: alt3

Summary: Use requests to talk HTTP via a UNIX domain socket
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-unixsocket/

BuildArch: noarch

# https://github.com/msabramo/requests-unixsocket.git
Source: %name-%version.tar

BuildRequires: git-core
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-waitress
BuildRequires: python3-tools-pep8
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest-pep8

%description
Use requests to talk HTTP via a UNIX domain socket.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
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

find ./ -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
%python3_build_debug

%install
%python3_install
touch %buildroot%python3_sitelibdir/requests_unixsocket/tests/__init__.py

%check
PYTHONPATH=$(pwd) py.test3

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%changelog
* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt3
- Build for python2 disabled.

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

