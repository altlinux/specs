%define _unpackaged_files_terminate_build 1
%define oname sqlquerybuilder

Name: python3-module-%oname
Version: 0.0.13
Release: alt3

Summary: Python SQL Query Builder based on django ORM
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/sqlquerybuilder/
# https://github.com/josesanch/sqlquerybuilder.git

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
SQL Query Builder inspired on django ORM Syntax.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
SQL Query Builder inspired on django ORM Syntax.

This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i
py.test3 %oname/tests.py

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.13-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.13-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.13-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20141129.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1.git20141129.1
- NMU: Use buildreq for BR.

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141129
- Version 0.0.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141125
- Initial build for Sisyphus

