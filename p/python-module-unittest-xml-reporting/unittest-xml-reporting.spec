%define oname unittest-xml-reporting

%def_with python3

Name: python-module-%oname
Version: 1.9.4
Release: alt1.git20141109.1.1
Summary: unittest-based test runner with Ant/JUnit like XML reporting
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unittest-xml-reporting/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xmlrunner/unittest-xml-reporting.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six
%endif

%py_provides xmlrunner

%description
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: unittest-based test runner with Ant/JUnit like XML reporting
Group: Development/Python3
%py3_provides xmlrunner

%description -n python3-module-%oname
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

This package contains tests for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.4-alt1.git20141109.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.4-alt1.git20141109.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.git20141109
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.git20141104
- Version 1.9.4

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1.git20141020
- Initial build for Sisyphus

