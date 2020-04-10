%define oname json_patch

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Implementation of the json-patch spec
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/json_patch/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-json_pointer

%description
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
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
* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

