%define _unpackaged_files_terminate_build 1
%define oname sqlquerybuilder

%def_with python3

Name: python-module-%oname
Version: 0.0.13
Release: alt2
Summary: Python SQL Query Builder based on django ORM
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sqlquerybuilder/

# https://github.com/josesanch/sqlquerybuilder.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
SQL Query Builder inspired on django ORM Syntax.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SQL Query Builder inspired on django ORM Syntax.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python SQL Query Builder based on django ORM
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
SQL Query Builder inspired on django ORM Syntax.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
SQL Query Builder inspired on django ORM Syntax.

This package contains tests for %oname.
%endif

%prep
%setup -n %oname-%version

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py build_ext -i
py.test %oname/tests.py
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
py.test3 %oname/tests.py
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
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

