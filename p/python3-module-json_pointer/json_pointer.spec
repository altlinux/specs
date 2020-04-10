%define oname json_pointer

Name: python3-module-%oname
Version: 0.1.2
Release: alt2

Summary: Simple implementation of the json-pointer spec
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/json_pointer/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-pytest

%description
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3 %oname/test.py

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*

%changelog
* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

