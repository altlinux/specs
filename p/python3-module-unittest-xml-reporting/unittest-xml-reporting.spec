%define oname unittest-xml-reporting

Name: python3-module-%oname
Version: 3.0.2
Release: alt1.1

Summary: unittest-based test runner with Ant/JUnit like XML reporting
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/unittest-xml-reporting/
BuildArch: noarch

# https://github.com/xmlrunner/unittest-xml-reporting.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-lxml

Requires: python3-module-django-tests

%py3_provides xmlrunner


%description
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/xmlrunner/tests/

%description tests
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!.*python|&3|' $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

cp -fR tests/ %buildroot%python3_sitelibdir/xmlrunner

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/xmlrunner/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/xmlrunner/tests

%files tests
%python3_sitelibdir/xmlrunner/tests


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 3.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.2-alt1
- Version updated to 3.0.2.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.4-alt2
- Build for python2 disabled.

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

