%define mname coveralls
%define oname z4r-%mname

%def_disable check

Name: python3-module-%oname
Version: 2.9.1
Release: alt4
Summary: Python interface to coveralls.io API
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/python-coveralls/

# https://github.com/z4r/python-coveralls.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-pytest-cov
BuildRequires: python3-module-setuptools python3-module-unittest2 python3-module-yaml python3-tools-pep8
BuildRequires: python3-module-httpretty python3-module-requests

%py3_provides %mname z4r_%mname
Conflicts: python-module-%oname < %EVR
Obsoletes: python-module-%oname < %EVR
Conflicts: python3-module-%mname < %EVR
Conflicts: python3-module-%mname > %EVR
Provides: python3-module-%mname = %EVR
%py3_requires yaml requests coverage six sh

%description
This package provides a module to interface with the https://coveralls.io
API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires pytest_pep8 pytest_cov httpretty

%description tests
This package provides a module to interface with the https://coveralls.io
API.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*

%changelog
* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 2.9.1-alt4
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.9.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt3
- Fixed build.
- Disabled tests.

* Tue Oct 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt2
- Fixed build with new setuptools.

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt1
- Updated to upstream release 2.9.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.4-alt1.git20141111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.4-alt1.git20141111.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.git20141111
- Initial build for Sisyphus

