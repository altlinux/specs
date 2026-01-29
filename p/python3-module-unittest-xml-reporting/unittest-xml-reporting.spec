%define oname unittest-xml-reporting

%def_with check

Name: python3-module-%oname
Version: 4.0.0
Release: alt1

Summary: unittest-based test runner with Ant/JUnit like XML reporting

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/unittest-xml-reporting
Vcs: https://github.com/xmlrunner/unittest-xml-reporting

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-coverage
BuildRequires: python3-module-lxml
%endif

Requires: python3-module-django-tests

BuildArch: noarch

%py3_provides xmlrunner

%description
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools, such
as build systems, IDEs and continuous integration servers.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/xmlrunner/
%python3_sitelibdir/unittest_xml_reporting-%version.dist-info

%changelog
* Thu Jan 29 2026 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.
- Built with check.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt2
- Build without check.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.

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

