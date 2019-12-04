%define oname oauth2_provider

%def_disable check

Name: python3-module-%oname
Version: 0.0
Release: alt2

Summary: Python implementation of the server side of OAUTH2 spec
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/oauth2_provider/
BuildArch: noarch

# https://github.com/eventray/oauth2_provider.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-unittest2
BuildRequires: python3-module-webtest
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Python implementation of the server side of OAUTH2 spec.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python implementation of the server side of OAUTH2 spec.

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

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0-alt1.git20120909.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0-alt1.git20120909.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0-alt1.git20120909.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.git20120909
- Initial build for Sisyphus

